#!/bin/bash

#export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.75.x86_64"
#export JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.111.x86_64"
#export PATH="/usr/lib/anaconda2/bin:$PATH"
#export SPARK_HOME="/usr/lib/spark"
#export PYTHONPATH="$SPARK_HOME/python/lib/py4j-0.9-src.zip:$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH"

echo "Start HDFS"
bash -c 'for x in `cd /etc/init.d ; ls hadoop-hdfs-*` ; do service $x start ; done'

echo "Start Yarn"
service hadoop-yarn-resourcemanager start
service hadoop-yarn-nodemanager start
service hadoop-mapreduce-historyserver start
#Satish: Don't start oozie 
#service oozie start

echo "Start Components"
service hue start

service zookeeper-server init

nohup hiveserver2 &

bash -c 'for x in `cd /etc/init.d ; ls impala-*` ; do service $x start ; done'

rm -rf /tmp/hbase-hbase*

service hbase-master start
service hbase-thrift start

# Start spark
service spark-master start
service spark-worker start
service spark-history-server start

echo "Press Ctrl+P and Ctrl+Q to background this process."
echo 'Use exec command to open a new bash instance for this instance (Eg. "docker exec -i -t CONTAINER_ID bash"). Container ID can be obtained using "docker ps" command.'
#echo "Start Terminal"
#bash
echo "Starting jupyter notebook."
echo "Press Ctrl+C to stop instance."
/usr/lib/anaconda2/bin/jupyter notebook --port 6666 --ip 0.0.0.0 --no-browser --notebook-dir=~/notebooks &
sleep infinity
