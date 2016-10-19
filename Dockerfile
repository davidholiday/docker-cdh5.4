FROM centos:centos6 
#was6
MAINTAINER David Holiday

ADD docker_files/cdh_centos_startup_script.sh /usr/bin/cdh_centos_startup_script.sh
ADD docker_files/cdh_centos_installer.sh /tmp/cdh_centos_installer.sh

RUN \
    chmod +x /tmp/cdh_centos_installer.sh && \
    chmod +x /usr/bin/cdh_centos_startup_script.sh && \
    bash /tmp/cdh_centos_installer.sh

ENV JAVA_HOME="/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.111.x86_64"
ENV PATH="/usr/lib/anaconda2/bin:$PATH"
ENV SPARK_HOME="/usr/lib/spark"
ENV PYTHONPATH="$SPARK_HOME/python/lib/py4j-0.9-src.zip:$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH"

##
# PORT MAPPINGS
##



##
# @dockerdash:start
##

  ##
  # @new-category:jupyter
  ##

    # @name:notebook
    # @web
    EXPOSE 6666


  ##
  # @new-category:HDFS
  ##

    # @name:NameNode
    EXPOSE 8020

    # @name=NameNode HTTPS UI
    # @web
    EXPOSE 50470

    # @name=DataNode UI
    # @web
    EXPOSE 50075


  ##
  # @new-category:YARN
  ##

    # @name:RESOURCE Manager UI
    # @web
    EXPOSE 8088

    # @name:NodeManager UI
    # @web
    EXPOSE 8042

    # @name:NodeManager localizer
    EXPOSE 8040


  ##
  # @new-categoryHadoop
  ##

    # @name:MapReduce JobHistory UI
    # @web
    EXPOSE 19888


  ##
  # @new-category:Spark
  ##

    # @name:Local Client Driver HTTP UI
    # @web
    EXPOSE 4040


  ##
  # @new-category:ZooKeeper
  ##

    # @name:Zookeeper Client
    EXPOSE 2181


  ##
  # @new-category:Hue
  ##

    # @name: Server
    EXPOSE 8888


  ##
  # @new-category: Oozie
  ##

    # @name:Server HTTP interface
    EXPOSE 11000


  ##
  # @new-category: Other
  ##

    # @name:Linux Cockpit (todo)
    EXPOSE 9090

    # @name:Dogtag Port
    EXPOSE 11443

    # @name:ssh
    EXPOSE 22


##
# @dockerdash:end
##


# Define default command.
CMD ["cdh_centos_startup_script.sh"]
