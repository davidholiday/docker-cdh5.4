#!/usr/bin/env python

import logging
import argparse
import os
import json

import subprocess


# TODO use container name to issue docker inspect command -- results are in json format, no?
#
# TODO web buttons should have a badge alerting the user as to whether or not the service is online
#
# TODO clean up arg parsing (create constants file and/or pull val(args) into a helper function?)
#
# TODO add method to parse dockerfile metadata into json


_dashName = ""
_containerName = ""

DOCKERFILE_NAME = "Dockerfile"
DEFAULT_DASH_NAME_PREFIX = "dockerdash for container@"
DOCKERFILE_PATH_ARG = "dockerfile_path"
DASH_NAME_ARG = "dashboard_name"
CONTAINER_NAME_ARG = "CONTAINER_NAME"

def testme():
    print("foop")

def main():
    setup_logging()

    parser = get_parser()
    parse_args(parser)



    # parse the dash name and filter values



    # parse the output from docker ps

    # parse and update the template file, including the canary port if listed  (unknown if no canary port is the default)

    # serialize the template file

    # open default browser instance with dash instance


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )



def get_parser():
    parser = argparse.ArgumentParser(description="creates a dashboard that lists port resolutions for a given docker container.")
    parser.add_argument("-d", "--%s" % (DASH_NAME_ARG,), help="the display name for this dashboard instance.")
    parser.add_argument("-c", "--%s" % (CONTAINER_NAME_ARG,), help="the name of the container you wish to create a dock for.")
    return parser



def parse_args(parser):
    isArgKosher = arg_check(parser, argparse.ArgumentParser)
    if (isArgKosher != True):
        raise ValueError("this method only accepts instances of argparse.ArgumentParser!")

    args = parser.parse_args()
    argsDict = vars(args)

    if (argsDict.get(CONTAINER_NAME_ARG)):
        _containerName = argsDict.get(CONTAINER_NAME_ARG);
    else:
        _containerName = ""

    if (argsDict.get(DASH_NAME_ARG)):
        _dashName = "%s@%s" % (argsDict.get(DASH_NAME_ARG), _containerName)
    else:
        _dashName = "%s@%s" % (DEFAULT_DASH_NAME_PREFIX, _containerName)

    print(_dashName)


def arg_check(arg, clazz):
    return isinstance(arg, clazz)



if __name__ == "__main__": main()
