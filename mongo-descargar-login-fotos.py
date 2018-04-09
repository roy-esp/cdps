#!/usr/bin/python
import sys
import os

# Configurar MongoDB
os.system('sudo lxc-attach -n s1 -- sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10')
os.system('sudo lxc-attach -n s1 -- echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list')
os.system('sudo lxc-attach -n s1 -- sudo apt-get update')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install mongodb-org')
os.system('echo Debe aceptar manualmente lo que pidan con y')
os.system('sudo lxc-attach -n s1 -- sudo service mongod start')

# Descargar proyecto CDPSgram y correrlo
os.system('sudo lxc-attach -n s1 -- git clone https://github.com/afrivero/CDPSgram')
os.system('sudo lxc-attach -n s1 -- cd CDPSgram/')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install -y nodejs')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install npm')
os.system('sudo lxc-attach -n s1 -- npm install')
os.system('sudo lxc-attach -n s1 -- npm start &')


# Descargar proyecto login y correrlo
os.system('sudo lxc-attach -n s1 -- git clone https://github.com/jacorralupm/mongodb')
os.system('sudo lxc-attach -n s1 -- cd mondodb/')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install -y nodejs')
os.system('sudo lxc-attach -n s1 -- sudo apt-get install npm')
os.system('sudo lxc-attach -n s1 -- npm install')
os.system('sudo lxc-attach -n s1 -- nodejs server.js')
 
 

 

 

 


