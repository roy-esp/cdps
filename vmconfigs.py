#!/usr/bin/python
import sys
import os

# Conectar nas1 con nas2 y nas3
os.system('sudo lxc-attach -n nas1 -- gluster peer probe 10.1.4.22')
os.system('sudo lxc-attach -n nas1 -- gluster peer probe 10.1.4.23')
# Sistema de ficheros distribuidos (replican la info) con la misma configuracion y nombre en todos los servers nas
os.system('sudo lxc-attach -n nas1 -- gluster volume create nas replica 3 10.1.4.21:/nas 10.1.4.22:/nas 10.1.4.23:/nas force')
os.system('sudo lxc-attach -n nas1 -- gluster volume start nas')
# Configuracion timeout servidores
os.system('sudo lxc-attach -n nas1 -- gluster volume set nas network.ping-timeout 5')
os.system('sudo lxc-attach -n nas2 -- gluster volume set nas network.ping-timeout 5')
os.system('sudo lxc-attach -n nas3 -- gluster volume set nas network.ping-timeout 5')

# Configuracion acceso sistema de ficheros de los nas desde los servidores web
os.system('sudo lxc-attach -n s1 -- mkdir /mnt/nas')
os.system('sudo lxc-attach -n s1 -- mount -t glusterfs 10.1.4.21:/nas /mnt/nas')
os.system('sudo lxc-attach -n s2 -- mkdir /mnt/nas')
os.system('sudo lxc-attach -n s2 -- mount -t glusterfs 10.1.4.21:/nas /mnt/nas')
os.system('sudo lxc-attach -n s3 -- mkdir /mnt/nas')
os.system('sudo lxc-attach -n s3 -- mount -t glusterfs 10.1.4.21:/nas /mnt/nas')
os.system('sudo lxc-attach -n s4 -- mkdir /mnt/nas')
os.system('sudo lxc-attach -n s4 -- mount -t glusterfs 10.1.4.21:/nas /mnt/nas')

