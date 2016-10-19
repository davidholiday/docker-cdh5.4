FROM ubuntu

# LABEL dockerdash.dashname="test_dash_1" \
#      dockerdash.category1="test_category_1" \
#      dockerdash.category1.name="foo" \
#      dockerdash.category1.port="22" \
#      dockerdash.category1.attribute="web" \
#      dockerdash.category2="test_category_2" \
#      dockerdash.category2.name="moo" \
#      dockerdash.category2.port="666"


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




RUN apt-get update && apt-get install -y iputils-ping traceroute
CMD bash
