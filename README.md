# redis-7.4.1-ansible

generic install for redis 7.4.1 instance on rhel 8 servers, including software unpacking and creation of service and conf files

**HOW TO**

1. downloads:
   
download latest redis 7.4 from:

https://github.com/redis-stack/redis-stack/releases/tag/v7.4.0-v6

also download this repo

also download ansible rhel 8 install from:

https://github.com/avi-azar-1/rhel8.8-ansible

2. install ansible:
   
unzip ansible install and run on target server

3.ready redis install:

unzip this repo in target server

put unzipped redis software directory in playbook folder

4. edit playbook:
   
change target server and parameters inside redis_inventory.yaml

6. run playbook:
   
from playbook folder:

ansible-playbook -i redis_inventory.yaml redis7.yaml

for local install (without ssh) run with '-c local' flag

for remote ssh create id_rsa.pub in ansible server and copy to known_hosts un target server




