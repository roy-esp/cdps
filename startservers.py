#!/usr/bin/python
import sys
import os

os.system('sudo lxc-attach -n s1 -- npm start --prefix /CDPSgram-server &')
os.system('sudo lxc-attach -n s2 -- npm start --prefix /CDPSgram-photos &')
os.system('sudo lxc-attach -n s3 -- npm start --prefix /CDPSgram-photos &')
os.system('sudo lxc-attach -n s4 -- npm start --prefix /CDPSgram-photos &')
os.system('sudo lxc-attach -n lb -- xr --verbose --server tcp:0:8000 --backend  10.1.3.12:8000 --backend 10.1.3.13:8000 --backend 10.1.3.14:8000 &')
os.system('sudo lxc-attach -n lb -- xr --verbose --server tcp:0:8080 --backend  10.1.3.11:8080 &')

