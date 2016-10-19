#!/usr/bin/env python

import logging
import argparse
import os
import json
import getpass
import subprocess
import socket

# TODO use container name to issue docker inspect command -- results are in json format, no?
#
# TODO web buttons should have a badge alerting the user as to whether or not the service is online
#
# TODO clean up arg parsing (create constants file and/or pull val(args) into a helper function?)
#
# TODO add method to parse dockerfile metadata into json


DOCKERFILE_NAME = "Dockerfile"
DEFAULT_DASH_NAME_PREFIX = "dockerdash for "
DOCKERFILE_PATH_ARG = "dockerfile_path"
DASH_NAME_ARG = "dashboard_name"
CONTAINER_NAME_ARG = "container_name"

def testme():
    print("foop")

def main():
    setup_logging()
    parser = get_parser()
    parsedArgsDict = parse_args(parser)
    print(get_container_names(parsedArgsDict))



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




def arg_check(arg, clazz):
    """

    """
    return isinstance(arg, clazz)



if __name__ == "__main__": main()
