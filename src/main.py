
from lib import do
from lib import eval
from lib import actions
from lib import processor
import config
import time
import sys
import argparse
from lib import exceptions


def main(configfile):
    """
    do all the things
    :return:
    """
    # get config
    global c
    c = config.load_config(configfile)

    try:
        while True:
            processor.go(c)
            time.sleep(60)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        raise exceptions.CoastguardException


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Coastguard')
    parser.add_argument("--config", help="Path to config file", required=True)
    args = parser.parse_args()

    main(args.config)