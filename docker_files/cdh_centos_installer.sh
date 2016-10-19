#!/bin/bash

yum -y update;
yum -y clean all; 

# Installing necessary tools
yum -y clean all; yum install -y java-1.7.0-openjdk wget dialog curl sudo lsof vim axel telnet java-1.7.0-openjdk java-1.7.0-openjdk-devel

# Adding cloudera repos
wget http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/cloudera-cdh5.repo
mv cloudera-cdh5.repo /etc/yum.repos.d/cloudera-cdh5.repo
rpm --import http://archive.cloudera.com/cdh5/redhat/6/x86_64/cdh/RPM-GPG-KEY-cloudera

# Installing hadoop
yum -y clean all; yum install -y hadoop-yarn-resourcemanager hadoop-hdfs-namenode hadoop-hdfs-secondarynamenode hadoop-yarn-nodemanager hadoop-hdfs-datanode hadoop-mapreduce hadoop-mapreduce-historyserver hadoop-yarn-proxyserver hadoop-client

# Installing Impala
yum -y clean all; yum install -y hadoop-conf-pseudo impala impala-server impala-state-store impala-catalog impala-shell

# Moving Security file to perform action as hdfs user /etc/security/limits.d/hdfs.conf 
mv /etc/security/limits.d/hdfs.conf ~/
mv /etc/security/limits.d/mapreduce.conf ~/
mv /etc/security/limits.d/yarn.conf ~/

#CDH5-Installation-Guide Step 1 - Format the NameNode
echo "Step 1 - Format the NameNode"
su - hdfs -c 'hdfs namenode -format'

#CDH5-Installation-Guide Step 2 - Start HDFS
echo "Step 2 - Start HDFS"
bash -c 'for x in `cd /etc/init.d ; ls hadoop-hdfs-*` ; do service $x start ; done'

#CDH5-Installation-Guide Step 3 - Create the directories needed for Hadoop processes
echo "Step 3 - Create the directories needed for Hadoop processes"
/usr/lib/hadoop/libexec/init-hdfs.sh

#CDH5-Installation-Guide Step 4: Verify the HDFS File Structure
echo "Step 4: Verify the HDFS File Structure"
su - hdfs -c 'hadoop fs -ls -R /'

#CDH5-Installation-Guide Step 5 - Start Yarn
echo "Step 5 - Start Yarn"
service hadoop-yarn-resourcemanager start
service hadoop-yarn-nodemanager start
service hadoop-mapreduce-historyserver start

#CDH5-Installation-Guide Step 6 - Create User Directories
echo "Step 6 - Create User Directories"

su - hdfs -c 'hadoop fs -chmod a+w /'
su - hdfs -c 'hadoop fs -mkdir -p /user/hadoop'
su - hdfs -c 'hadoop fs -chmod a+w /user'
su - hdfs -c 'hadoop fs -chown hadoop /user/hadoop'

hadoop fs -chmod g+w   /tmp
hadoop fs -mkdir -p /user/hive/warehouse
hadoop fs -chmod g+w   /user/hive/warehouse

#Satish: Changing warehouse permissions
hadoop fs -chmod -R a+w /user/hive/warehouse
hadoop fs -chmod -R a+w /user/hive/warehouse/*

# Adding Hbase dir
su - hdfs -c 'hadoop fs -mkdir /hbase'
su - hdfs -c 'hadoop fs -chown hbase /hbase'
su - hdfs -c 'hadoop fs -chmod a+w /hbase'

# Moving security file back to its location
mv ~/hdfs.conf /etc/security/limits.d/
mv ~/mapreduce.conf /etc/security/limits.d/
mv ~/yarn.conf /etc/security/limits.d/

#CDH5-Installation-Guide Install HBase
echo "Install Cloudera Components"
#Satish: Added zookeeper
yum install -y zookeeper zookeeper-server hive hbase hbase-thrift hbase-master pig oozie oozie-client spark-core spark-master spark-worker spark-history-server spark-python hue hue-server


# from https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4
# for setting up python 2.7, pip, and virtual env so we can install conda
#
echo "Installing python2.7, pip, and virtualenv"
export $WORK_DIR="/usr/lib/"
yum groupinstall -y development
yum install -y zlib-dev openssl-devel sqlite-devel bzip2-devel xz-libs

cd $WORK_DIR 
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
xz -d Python-2.7.12.tar.xz 
tar -xvf Python-2.7.12.tar
cd Python-2.7.12
./configure
make && make altinstall

cd $WORK_DIR 
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz
tar -xvf setuptools-1.4.2.tar.gz
cd setuptools-1.4.2
python2.7 setup.py install
curl https://bootstrap.pypa.io/get-pip.py | python2.7 -
pip install virtualenv

# setup anaconda
#
echo "install and set up anaconda2"
cd $WORK_DIR
wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
chmod +x Anaconda2-4.2.0-Linux-x86_64.sh 
./Anaconda2-4.2.0-Linux-x86_64.sh  -b -p /usr/lib/anaconda2
export PATH="/usr/lib/anaconda2/bin:$PATH"
export SPARK_HOME="/usr/lib/spark"
export PYTHONPATH="$SPARK_HOME/python/lib/py4j-0.9-src.zip:$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH"
mkdir ~/notebooks

#Initiate Oozie Database
oozie-setup db create -run

#Create HUE Secret Key
sed -i 's/secret_key=/secret_key=_S@s+D=h;B,s$C%k#H!dMjPmEsSaJR/g' /etc/hue/conf/hue.ini
