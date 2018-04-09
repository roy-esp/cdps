#!/usr/bin/python
import sys
import os


os.system('sudo lxc-attach -n s1 -- sudo apt-get update')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install nodejs -y')

os.system('sudo lxc-attach -n s2 -- sudo apt-get update')
os.system('sudo lxc-attach -n s2 -- sudo apt-get install nodejs -y')

os.system('sudo lxc-attach -n s3 -- sudo apt-get update')
os.system('sudo lxc-attach -n s3 -- sudo apt-get install nodejs -y')

os.system('sudo lxc-attach -n s4 -- sudo apt-get update')
os.system('sudo lxc-attach -n s4 -- sudo apt-get install nodejs -y')

os.system('sudo lxc-attach -n s1 -- git clone https://github.com/roy-esp/CDPSgram-server.git')
os.system('sudo lxc-attach -n s1 -- cd CDPSgram-server')
os.system('sudo lxc-attach -n s1 -- npm install --prefix /CDPSgram-server')

os.system('sudo lxc-attach -n s2 -- git clone https://github.com/roy-esp/CDPSgram-photos.git')
os.system('sudo lxc-attach -n s2 -- cd CDPSgram-photos')
os.system('sudo lxc-attach -n s2 -- npm install --prefix /CDPSgram-photos')

os.system('sudo lxc-attach -n s3 -- git clone https://github.com/roy-esp/CDPSgram-photos.git')
os.system('sudo lxc-attach -n s3 -- cd CDPSgram-photos')
os.system('sudo lxc-attach -n s3 -- npm install --prefix /CDPSgram-photos')

os.system('sudo lxc-attach -n s4 -- git clone https://github.com/roy-esp/CDPSgram-photos.git')
os.system('sudo lxc-attach -n s4 -- cd CDPSgram-photos')
os.system('sudo lxc-attach -n s4 -- npm install --prefix /CDPSgram-photos')

