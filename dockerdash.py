#!/usr/bin/env python

import logging
import os
import subprocess


# !! use python logging

# !! arg that tells dockerdash to open a particular dash instance

def main():
    setup_logging()
    logging.info("foo")

    # parse the dash name and filter values

    # parse the output from docker ps

    # parse and update the template file, including the canary port if listed  (unknown if no canary port is the default)

    # serialize the template file

    # open default browser instance with dash instance


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )


if __name__ == "__main__": main()
