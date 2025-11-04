# redis-7.4.1-ansible

generic install for redis 7.4.1 instance on rhel 8 servers, including software unpacking and creation of service and conf files

**HOW TO**

1. **downloads**:  
- download latest redis 7.4 from:  
https://github.com/redis-stack/redis-stack/releases
- also download this repo  
- also download ansible rhel 8 install from:  
https://github.com/avi-azar-1/rhel8.8-ansible

2. **install ansible**:  
look at instructions in ansible repo

3. **ready redis install**:  
unzip this repo in target server  
unzip redis software tarball in target server
```bash
tar -xzf redis-stack-server-7.4.0-v6.rhel8.x86_64.tar.gz
```

4. **edit playbook**:  
change target server and parameters inside redis_inventory.yaml

5. **run playbook**:  
from playbook folder:
```bash
ansible-playbook -i redis_inventory.yaml redis7.yaml
```
for local install (without ssh) run with '-c local' flag  
for remote ssh create id_rsa.pub in ansible server and copy to known_hosts un target server  

6. **replication, sentinels or cluster**:  
   **sentinels**: set up as normal redis then change to sentinel.conf file  
   **replication**: set replicaof manually than use redis_add_sentinel.sh  
   **cluster**: use cluster create:  
```bash
   ps -ef | grep redis | grep -v grep | grep -v export | awk '{print $9}' | tr '\n' ' '
```  
(get node list on each server, combine and run:)  
```bash
redis-cli --cluster create -a <password> --cluster-replicas 1 <redis_list>
```



