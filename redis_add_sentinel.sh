sentinel=$1
master_ip=$2
port=$3
password=$4
echo "adding:" ${port}_master $master_ip $port

/usr/local/bin/redis-cli -h $sentinel -p 26379 -c sentinel monitor ${port}_master $master_ip $port 2
/usr/local/bin/redis-cli -h $sentinel -p 26379 -c sentinel set ${port}_master down-after-milliseconds 10000 
/usr/local/bin/redis-cli -h $sentinel -p 26379 -c sentinel set ${port}_master auth-pass $password
/usr/local/bin/redis-cli -h $sentinel -p 26379 -c sentinel set ${port}_master failover-timeout 180000
/usr/local/bin/redis-cli -h $sentinel -p 26379 -c sentinel reset ${port}_master