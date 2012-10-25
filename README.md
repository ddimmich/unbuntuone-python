Ubuntu One Python
-----------------

Library for downloading files from Ubuntu One (cross platform) but written for OSX as ubuntu one has no native support.

Currently only supports downloading/updating.

Installing:

Check it out of the github account:

```
git clone https://github.com/ddimmich/unbuntuone-python.git
cd ubuntuone-python
virtualenv .
./bin python setup.py install
```

If you just want to sync you can run the file sync.py:

./bin/python sync.py --username=username@bla --password=asdf

Once you have logged in once, you do not need to supply your username and password again.



Brief library usage instructions are:

On the python command line you can log in and then iterate over directory tree at given starting point (this 
example will download music purchased at the ubuntu one music store):

```
data =  acquire_token('username@bla', 'password' )
consumer, token = make_tokens(data)
fetch_children(consumer, token, '/~/.ubuntuone/Purchased from Ubuntu One')
```



Copyright Tauri-Tec Ltd. http://www.tauri-tec.com 

Licensed under the BSD license.
