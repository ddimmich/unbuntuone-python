import base64
import json
import urllib
import urllib2
import os, hashlib
import oauth2
import platform

"""
Brief instructions are:
#log in     
consumer, token =  acquire_token('username@bla', 'password' )
#iterate over tree starting here:
fetch_children(consumer, token, '/~/.ubuntuone/Purchased from Ubuntu One')
"""

base_url = 'https://one.ubuntu.com/api/file_storage/v1'

class Unauthorized(Exception):
    """The provided email address and password were incorrect."""


def acquire_token(email_address, password):
    #get hostname
    description = 'Ubuntu One @ %s' % platform.node()
    """Aquire an OAuth access token for the given user."""
    # Issue a new access token for the user.
    request = urllib2.Request(
        'https://login.ubuntu.com/api/1.0/authentications?' +
        urllib.urlencode({'ws.op': 'authenticate', 'token_name': description}))
    request.add_header('Accept', 'application/json')
    request.add_header('Authorization', 'Basic %s' % base64.b64encode(
        '%s:%s' % (email_address, password)))
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, exc:
        if exc.code == 401: # Unauthorized
            raise Unauthorized("Bad email address or password")
        else:
            raise
    data = json.load(response)
    print data
    consumer = oauth2.Consumer(data['consumer_key'], data['consumer_secret'])
    token = oauth2.Token(data['token'], data['token_secret'])

    # Tell Ubuntu One about the new token.
    get_tokens_url = (
        'https://one.ubuntu.com/oauth/sso-finished-so-get-tokens/')
    request = sign_request(consumer, token, get_tokens_url)
    response = urllib2.urlopen(request)
    print response.headers
    print response.read()
    return consumer, token

def sign_request(consumer, token, url):
    oauth_request = oauth2.Request.from_consumer_and_token(
        consumer, token, 'GET', url)
    oauth_request.sign_request(
        oauth2.SignatureMethod_PLAINTEXT(), consumer, token)
    request = urllib2.Request(url)
    for header, value in oauth_request.to_header().items():
        request.add_header(header, value) 
    return request

def fetch_children(consumer, token, path):
    url = base_url + urllib2.quote(path) +'?include_children=true'
    request = sign_request(consumer, token, url)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError:
        print "Error finding: %s" % url
        return
    basepaths = json.loads(response.read())
    print 'reading %s' % path
    for child in basepaths['children']:
        if child['kind'] == 'directory':
            fetch_children(consumer, token, child['resource_path'])
        elif child['kind'] == 'file':
            fetch_file(consumer, token, child)

def fetch_file(consumer, token, child):
    url = 'https://files.one.ubuntu.com/' + child['key']#+ urllib2.quote(child['content_path'])
    r = sign_request(consumer, token, url)
    try:
        response = urllib2.urlopen(r)
    except urllib2.HTTPError:
        print "Error finding: %s" % url
        return
    filename=child['content_path'].split('/')[-1]
    print 'downloading %s' % filename
    if os.path.isfile(filename):
        file = open(filename, 'rb')
        sha1 = hashlib.sha1()
        try:
            sha1.update(file.read())
        finally:
            file.close()
        if child['hash'] == 'sha1:%s'%sha1.hexdigest():
            print 'sha1 matches for %s, skipping.' % filename
            return
    #otherwise download.
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()
