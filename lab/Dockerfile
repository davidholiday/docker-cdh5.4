FROM ubuntu

# LABEL dockerdash.dashname="test_dash_1" \
#      dockerdash.c1="test_category_1" \
#      dockerdash.c1.name="foo" \
#      dockerdash.c1.port="22" \
#      dockerdash.c1.attribute="web" \
#      dockerdash.c2="test_category_2" \
#      dockerdash.c2.name="moo" \
#      dockerdash.c2.port="666"


# CREATE DOCKERDASH PORT META DATA & EXPOSE PORTS 
LABEL dockerdash.dashname="roots_derriere" \
      #
          dockerdash.c.0="jupyter" \
              dockerdash.c.0.e.0="notebook" \
                  dockerdash.c.0.e.0.port="6666" \
                  dockerdash.c.0.e.0.attribute="web" \
                  #
          dockerdash.c.1="HDFS" \
              dockerdash.c.1.e.0="NameNode" \
                  dockerdash.c.1.e.0.port="8020" \
              dockerdash.c.1.e.1="NameNode HTTPS UI" \
                  dockerdash.c.1.e.1.port="50470" \
                  dockerdash.c.1.e.1.attribute="web" \
              dockerdash.c.1.e.2="DataNode UI" \ 
                  dockerdash.c.1.e.2.port="50075" \
                  dockerdash.c.1.e.2.attribute="web" \
                  #
          dockerdash.c.2="Yarn" \
              dockerdash.c.2.e.0="Resource Manager UI" \
                  dockerdash.c.2.e.0.port="8088" \
                  dockerdash.c.2.e.0.attribute="web" \
              dockerdash.c.2.e.1="Node Manager" \
                  dockerdash.c.2.e.1.port="8042" \
                  dockerdash.c.2.e.1.attribute="web" \
              dockerdash.c.2.e.2="Node Manager Localizer" \
                  dockerdash.c.2.e.2.port="8040" \
                  #
          dockerdash.c.3="Spark" \
              dockerdash.c.3.e.0="Local Client Driver HTTP UI" \
                  dockerdash.c.3.e.0.port="4040" \
                  dockerdash.c.3.e.0.attribute="web" \
                  #
          dockerdash.c.4="Hadoop" \
              dockerdash.c.4.e.0="MapReduce JobHistory UI" \
                  dockerdash.c.4.e.0.port="19888" \
                  dockerdash.c.4.e.0.attribute="web" \
                  #
          dockerdash.c.5="ZooKeeper" \
              dockerdash.c.5.e.0="ZooKeeper Client" \
                  dockerdash.c.5.e.0.port="2181" \
                  #
          dockerdash.c.6="Hue" \
              dockerdash.c.6.e.0="Server" \
                  dockerdash.c.6.e.0.port="8888" \
                  #
          dockerdash.c.7="Oozie" \
              dockerdash.c.7.e.0="Server HTTP interface" \
                  dockerdash.c.7.e.0.port="11000" \
                  #
          dockerdash.c.8="Other" \
              dockerdash.c.8.e.0="Linux Cockpit (todo)" \
                  dockerdash.c.8.e.0.port="9090" \
              dockerdash.c.8.e.1="Dogtag Port" \
                  dockerdash.c.8.e.1.port="11443" \
              dockerdash.c.8.e.2="ssh" \ 
                  dockerdash.c.8.e.2.port="22" 




RUN apt-get update && apt-get install -y iputils-ping traceroute
CMD bash
