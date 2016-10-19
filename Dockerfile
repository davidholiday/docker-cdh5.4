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

# CREATE DOCKERDASH PORT META DATA & EXPOSE PORTS 
LABEL dockerdash.dashname="roots_derriere" \
      #
          dockerdash.category1="jupyter" \
              dockerdash.category1.e1="notebook" \
                  dockerdash.category1.e1.port="6666" \
                  dockerdash.category1.e1.attribute="web" \
                  #
          dockerdash.category2="HDFS" \
              dockerdash.category2.e1="NameNode" \
                  dockerdash.category2.e1.port="8020" \
              dockerdash.category2.e2="NameNode HTTPS UI" \
                  dockerdash.category2.e2.port="50470" \
                  dockerdash.category2.e2.attribute="web" \
              dockerdash.category2.e3="DataNode UI" \ 
                  dockerdash.category2.e3.port="50075" \
                  dockerdash.category2.e3.attribute="web" \
                  #
          dockerdash.category3="Yarn" \
              dockerdash.category3.e1="Resource Manager UI" \
                  dockerdash.category3.e1.port="8088" \
                  dockerdash.category3.e1.attribute="web" \
              dockerdash.category3.e2="Node Manager" \
                  dockerdash.category3.e2.port="8042" \
                  dockerdash.category3.e2.attribute="web" \
              dockerdash.category3.e3="Node Manager Localizer" \
                  dockerdash.category3.e3.port="8040" \
                  #
          dockerdash.category4="Spark" \
              dockerdash.category4.e1="Local Client Driver HTTP UI" \
                  dockerdash.category4.e1.port="4040" \
                  dockerdash.category4.e1.attribute="web" \
                  #
          dockerdash.category5="Hadoop" \
              dockerdash.category5.e1="MapReduce JobHistory UI" \
                  dockerdash.category5.e1.port="19888" \
                  dockerdash.category5.e1.attribute="web" \
                  #
          dockerdash.category6="ZooKeeper" \
              dockerdash.category6.e1="ZooKeeper Client" \
                  dockerdash.category6.e1.port="2181" \
                  #
          dockerdash.category7="Hue" \
              dockerdash.category7.e1="Server" \
                  dockerdash.category7.e1.port="8888" \
                  #
          dockerdash.category8="Oozie" \
              dockerdash.category8.e1="Server HTTP interface" \
                  dockerdash.category8.e1.port="11000" \
                  #
          dockerdash.category9="Other" \
              dockerdash.category9.e1="Linux Cockpit (todo)" \
                  dockerdash.category9.e1.port="9090" \
              dockerdash.category9.e2="Dogtag Port" \
                  dockerdash.category9.e2.port="11443" \
              dockerdash.category9.e3="ssh" \ 
                  dockerdash.category9.e3.port="22" 


EXPOSE 6666
EXPOSE 8020
EXPOSE 50470
EXPOSE 50075
EXPOSE 8088
EXPOSE 8042
EXPOSE 8040
EXPOSE 19888
EXPOSE 4040
EXPOSE 2181
EXPOSE 8888
EXPOSE 11000
EXPOSE 9090
EXPOSE 11443
EXPOSE 22


# Define default command.
CMD ["cdh_centos_startup_script.sh"]
