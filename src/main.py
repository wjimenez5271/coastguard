
from lib import do
from lib import eval
from lib import actions
from lib import processor
import config
import time
import sys
import argparse
import logging
from lib.util import *



def main(configfile):
    """
    do all the things
    :return:
    """
    # get config
    global c
    c = config.load_config(configfile)

    # setup logging
    log = logging.getLogger('coastguard')
    log.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log.addHandler(ch)

    try:
        log.info('Starting up')
        while True:
            processor.go(c)
            time.sleep(60)
    except KeyboardInterrupt:
        log.info('Exiting on user interrupt')
        sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Coastguard')
    parser.add_argument("--config", help="Path to config file", required=True)
    args = parser.parse_args()

    main(args.config)