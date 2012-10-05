from one import *
import json, argparse
import logging

log = logging.getLogger(__name__)

tokenfile = '.ubuntuonetokens'

def load_tokens(username, password):
    try:
        with open(tokenfile) as f:
            data = json.loads(f.read())
    except IOError as e:
        try:
            data =  acquire_token(username, password )
        except Unauthorized, e:
            print(e)
            raise SystemExit
        jsondata = json.dumps(data)
        with open(tokenfile, 'wb') as f:
            f.write(jsondata)

    consumer, token = make_tokens(data)
    return consumer, token

def main():
    parser = argparse.ArgumentParser(description='Sync files from ubuntu, you only need to provide your username and password once.',
    epilog="Copyright 2012 Tauri-Tec Ltd http://www.tauri-tec.com")
    parser.add_argument('--username', type=str, action='store', dest='username',
        help='Ubuntu One username')
    parser.add_argument('--password', type=str, action='store', dest='password',
        help='Ubuntu One password')

    args = parser.parse_args()
    consumer, token = load_tokens(args.username, args.password)

    #iterate over tree starting here:
    fetch_children(consumer, token, '/~/.ubuntuone/Purchased from Ubuntu One')


if __name__ == "__main__":
    main()