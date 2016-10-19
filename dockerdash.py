#!/usr/bin/env python

import logging
import argparse

import os
import subprocess


# TODO use container name to issue docker inspect command -- results are in json format, no?
#
# TODO web buttons should have a badge alerting the user as to whether or not the service is online


_defaultDashNamePrefix = "dockerdash for container: "
_callerSuppliedDashName = ""

def testme():
    print("foop")

def main():
    setup_logging()
    parser = get_parser()
    print(isinstance(parser, argparse.ArgumentParser))


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
    parser.add_argument("-dn", "--dashname", help="the display name for this dashboard instance.")
    parser.add_argument("{DOCKER_CONTAINER_NAME}", help="the name of the container you wish to create a dock for.")
    return parser



def parse_args(parser):
    isArgKosher = arg_check(parser, argparse.ArgumentParser)

    if (!isArgKosher):
        raise ValueError("this method only accepts instances of argparse.ArgumentParser!")




def arg_check(arg, clazz):
    return isinstance(arg, clazz)



if __name__ == "__main__": main()
