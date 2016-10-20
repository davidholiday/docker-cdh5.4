#!/usr/bin/env python

import logging
import argparse
import json
import getpass
import subprocess
import socket
import dpath.util

# TODO use container name to issue docker inspect command -- results are in json format, no?
#
# TODO web buttons should have a badge alerting the user as to whether or not the service is online
#
# TODO clean up arg parsing (create constants file and/or pull val(args) into a helper function?)
#
# TODO add method to parse dockerfile metadata into json


DEFAULT_DASH_NAME_PREFIX = "dockerdash for "
DASH_NAME_ARG = "dashboard_name"
CONTAINER_NAME_ARG = "container_name"


def main():
    setup_logging()
    parser = get_parser()
    parsedArgsDict = parse_args(parser)
    containerNames = get_container_names(parsedArgsDict)
    containerMetadataDict = get_container_metadata_dict(containerNames)


    pretty_print_metadata(containerMetadataDict)



#    for key, value in containerMetadataDict.iteritems():
#        print(key)
#        parsedJSON = json.loads(value)
#        print(json.dumps(parsedJSON, indent=4, sort_keys=True))



    # parse the dash name and filter values



    # parse the output from docker ps

    # parse and update the template file, including the canary port if listed  (unknown if no canary port is the default)

    # serialize the template file

    # open default browser instance with dash instance


def setup_logging():
    """

    """
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )



def get_parser():
    """

    """
    parser = argparse.ArgumentParser(description="creates a dashboard that lists port resolutions for a given docker container.")
    parser.add_argument("-d", "--%s" % (DASH_NAME_ARG,), help="the display name for this dashboard instance.")
    parser.add_argument("-c", "--%s" % (CONTAINER_NAME_ARG,), help="the name of the container you wish to create a dock for (default is to list all running containers in the dash).")
    return parser



def parse_args(parser):
    """

    """
    isArgKosher = arg_check(parser, argparse.ArgumentParser)
    if (isArgKosher != True):
        raise ValueError("this method only accepts instances of argparse.ArgumentParser!")

    args = parser.parse_args()
    parsedArgsDict = vars(args)

    if (parsedArgsDict.get(DASH_NAME_ARG)):
        parsedArgsDict[DASH_NAME_ARG] = "%s %s@%s" % (parsedArgsDict.get(DASH_NAME_ARG), getpass.getuser(), socket.gethostname())
    else:
        parsedArgsDict[DASH_NAME_ARG] = "%s %s@%s" % (DEFAULT_DASH_NAME_PREFIX, getpass.getuser(), socket.gethostname())

    return parsedArgsDict




def get_container_names(parsedArgsDict):
    """

    """
    isArgKosher = arg_check(parsedArgsDict, dict)
    if (isArgKosher != True):
        raise ValueError("this method only accepts instances of dict")

    containerNames = list()

    if (parsedArgsDict[CONTAINER_NAME_ARG]):
        containerNames.append(parsedArgsDict[CONTAINER_NAME_ARG])
    else:
        output = subprocess.Popen(["docker", "ps", "--format", 'table {{.Names}}'],stdout=subprocess.PIPE).communicate()[0]
        outputList = output.split()
        del outputList[0]
        containerNames = containerNames + outputList

    return containerNames


def get_container_metadata_dict(containerNames):
    """

    """
    containerDict = dict()

    for containerName in containerNames:
        output = subprocess.Popen(["docker", "inspect", "--format='{{json .Config}}'", containerName],stdout=subprocess.PIPE).communicate()[0]
        containerDict[containerName]= output

    return containerDict



def pretty_print_metadata(containerMetadataDict):
    for key, value in containerMetadataDict.iteritems():
        print ("container is: " + key)

        dockerdashDict = dict()
        valueDict = json.loads(value)

        # first filter by category
        firstFilterValue = "dockerdash.c."
        dockerdashLabelSet = { k[ len(firstFilterValue): ]  for k in valueDict['Labels'] if k.startswith(firstFilterValue) }

        # figure out how many categories there are
        categoryCount = get_toplevel_highest_index(dockerdashLabelSet)

        # figure out how many elements there are per category
        categoryElementDict = dict()
        # TODO this is farty -- consider changing the metadata to start at '0' and not '1'
        for i in range(1, categoryCount + 1):
            categoryFilterValue = str(i) + ".e."
            categoryLabelSubset = { k[ len(categoryFilterValue): ]  for k in dockerdashLabelSet if k.startswith(categoryFilterValue) }
            elementCount = get_toplevel_highest_index(categoryLabelSubset)
            categoryElementDict[i] = elementCount

        print("there are %d categories" % (categoryCount))
        for k, v in categoryElementDict.iteritems():
            print("category %d has %d elements" % (k, v))


def get_toplevel_highest_index(dockerdashLabelSet):
    """
    does not return a number, bru
    """
    count = 0
    for k in dockerdashLabelSet:
        if k.split('.')[0] > count:
            count = k.split('.')[0]

    return int(count)





def arg_check(arg, clazz):
    """

    """
    return isinstance(arg, clazz)



if __name__ == "__main__": main()
