FROM ubuntu

# CREATE FOXY PORT META DATA & EXPOSE PORTS 
LABEL \
      #
      # group jupyter
          foxy.6666.name="notebook" \
          foxy.6666.group="jupyter" \
          foxy.6666.attribute="web" \
      #
      # group HDFS
          foxy.8020.name="NameNode" \
          foxy.8020.group="HDFS" \
      
          foxy.50470.name="NameNode HTTPS UI" \
          foxy.50470.group="HDFS" \
          foxy.50470.attribute="web" \
      
          foxy.50075.name="DataNode UI" \
          foxy.50075.group="HDFS" \
          foxy.50075.attribute="web" \
      #
      # group Yarn
          foxy.8088.name="Resource Manager UI" \
          foxy.8088.group="Yarn" \
          foxy.8088.attribute="web" \
      
          foxy.8042.name="Node Manager" \
          foxy.8042.group="Yarn" \
          foxy.8042.attribute="web" \
      
          foxy.8040.name="Node Manager Localizer" \
          foxy.8040.group="Yarn" \
      #    
      # group Spark
          foxy.4040.name="Local Client Driver HTTP UI" \
          foxy.4040.group="Spark" \
          foxy.4040.attribute="web" \
      #
      # group Hadoop
          foxy.19888.name="MapReduce JobHistory UI" \
          foxy.19888.group="Hadoop" \
          foxy.19888.attribute="web" \
      #
      # group ZooKeeper
          foxy.2181.name="ZooKeeper Client" \
          foxy.2181.group="ZooKeeper" \
          foxy.2181.attribute="web" \
      #
      # group Hue
          foxy.8888.name="Server" \
          foxy.8888.group="Hue" \
      #      
      # group Oozie
          foxy.11000.name="Server HTTP interface" \
          foxy.11000.group="Oozie" \
      #   
      # group Other
          foxy.9090.name="Linux Cockpit (todo)" \
          foxy.9090.group="Other" \
       
          foxy.11443.name="Dogtag Port" \
          foxy.11443.group="Other" \
       
          foxy.22.name="ssh" \
          foxy.22.group="Other" 


EXPOSE 22
EXPOSE 11443
EXPOSE 9090
EXPOSE 11000
EXPOSE 8888
EXPOSE 2181
EXPOSE 19888
EXPOSE 4040
EXPOSE 8040
EXPOSE 8042
EXPOSE 8088
EXPOSE 50075
EXPOSE 50470
EXPOSE 8020
EXPOSE 6666


RUN apt-get update && apt-get install -y iputils-ping traceroute
CMD bash
