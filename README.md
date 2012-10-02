
Library for downloading files from Ubuntu One (cross platform) but written for OSX as ubuntu one has no native support.

Currently only supports downloading/updating.

Installing:

Check it out of the github account:

git clone https://github.com/ddimmich/unbuntuone-python.git

cd ubuntuone-python

virtualenv .

./bin python setup.py

Brief library usage instructions are:

On the python command line you can log in:

consumer, token =  acquire_token('username@bla', 'password' )

And then iterate over directory tree at given starting point (this example will download music purchased at the ubuntu one music store):

fetch_children(consumer, token, '/~/.ubuntuone/Purchased from Ubuntu One')



Copyright Tauri-Tec Ltd. http://www.tauri-tec.com 

Licensed under the BSD license.
