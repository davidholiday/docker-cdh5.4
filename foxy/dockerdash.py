#!/usr/bin/env python

import logging
import argparse
import json
import getpass
import subprocess
import socket


import constants


# TODO ** start/stop containers from foxy
#      ** have foxy periodically wake up and check for changes as part of the refresh cycle
#      ** collapsable panels
#      ** indicator on container to start/stop

#import dpath.util

# TODO use container name to issue docker inspect command -- results are in json format, no?
#
# TODO web buttons should have a badge alerting the user as to whether or not the service is online
#
# TODO clean up arg parsing (create constants file and/or pull val(args) into a helper function?)
#
# TODO add method to parse dockerfile metadata into json



# TODO make the web app run from within its own container?
# TODO alias docker command to docker blah blah ... & dockerdash.py method to detect changes
# ----- one way to do this might be hashing the results of docker ps

# TODO json -> html table jqGrid??
# ------ this to facillitate conversion of the docker inspect command into data on the running container

# TODO canary -- tag certain services so that you get an alert when it goes offline






def main():
    setup_logging()
    parser = get_parser()
    parsedArgsDict = parse_args(parser)
    containerNames = get_container_names(parsedArgsDict)
    containerInfoDict = get_container_info_dict(containerNames)
    foxyDataDict = get_foxydata_dict(containerInfoDict)
    foxydata_to_html(foxydataDict)
    serialize_foxydata(foxydataDict)



def setup_logging():
    """

    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )


def get_parser():
    """

    """
    parser = argparse.ArgumentParser(\
        description="creates a dashboard that lists port resolutions for a given docker container.")

    parser.add_argument("-d", \
                        "--%s" % (constants.DASH_NAME_ARG,), \
                        help="the display name for this dashboard instance.")

    parser.add_argument("-c", 
                        "--%s" % (constants.CONTAINER_NAME_ARG,), 
                        help="the name of the container you wish to create a dock for \
                              (default is to list all running containers in the dash).")
    return parser



def parse_args(parser):
    """

    """
    isArgKosher = arg_check(parser, argparse.ArgumentParser)
    if (isArgKosher != True):
        raise ValueError("this method only accepts instances of argparse.ArgumentParser!")

    args = parser.parse_args()
    parsedArgsDict = vars(args)

    if (parsedArgsDict.get(constants.DASH_NAME_ARG)):

        parsedArgsDict[constants.DASH_NAME_ARG] = \
            "%s %s@%s" % (parsedArgsDict.get(constants.DASH_NAME_ARG), getpass.getuser(), socket.gethostname())

    else:
        parsedArgsDict[constants.DASH_NAME_ARG] = \
            "%s %s@%s" % (constants.DEFAULT_DASH_NAME_PREFIX, getpass.getuser(), socket.gethostname())

    return parsedArgsDict




def get_container_names(parsedArgsDict):
    """

    """
    isArgKosher = arg_check(parsedArgsDict, dict)
    if (isArgKosher != True):
        raise ValueError("this method only accepts instances of dict")

    containerNames = list()

    if (parsedArgsDict[constants.CONTAINER_NAME_ARG]):
        containerNames.append(parsedArgsDict[constants.CONTAINER_NAME_ARG])
    else:

        output = subprocess.Popen(["docker", "ps", "-a", "--format", 'table {{.Names}}'], \
                    stdout=subprocess.PIPE).communicate()[0]

        outputList = output.split()
        del outputList[0]
        containerNames = containerNames + outputList

    return containerNames


def get_container_info_dict(containerNames):
    """

    """
    containerInfoDict = dict()
    for containerName in containerNames:
        output = subprocess.Popen(["docker", "inspect", "--format='{{json .}}'", containerName],
            stdout=subprocess.PIPE).communicate()[0]
        containerInfoDict[containerName]= output

    return containerInfoDict




def get_foxydata_dict(containerInfoDict):
    """
    """    
    foxyDataDict = dict()
    for key, value in containerInfoDict.iteritems():

        logging.info("container is: %s"  % (key) )
        valueDict = json.loads(value)
        metaDataDict = valueDict['Config']['Labels']
        
        portsDict = dict()
        if valueDict['State']['Running'] == True:
            portsDict = valueDict['NetworkSettings']['Ports']
            
        foxyFilter = constants.TOP_LEVEL_METATDATA_FILTER
        foxyDataDict = filter_by_namespace(metaDataDict, foxyFilter)
        foxyDataDict[constants.DOCKER_PORT_KEY] = portsDict
        print(foxyDataDict)
    return foxyDataDict 




def filter_by_namespace(valueDict, filterValue):
    """
    filters foxy metadata by namespace, returns set of <k,v>'s that DO NOT contain the 
    filtered portion of the namespace. 
    """
    return { k[ len(filterValue): ] : v \
                for k, v in valueDict.iteritems() \
                    if k.startswith(filterValue) }




def foxydata_to_html(foxydataDict):
    """
    """
    print()

    


def serialize_foxydata(foxydataDict):
    """
    """
    print()




def arg_check(arg, clazz):
    """

    """
    return isinstance(arg, clazz)



if __name__ == "__main__": main()
