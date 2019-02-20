from __future__ import absolute_import, division, print_function, unicode_literals

import logging

#from a_package import a_module
#from a_package.logging_sqlite import SQLiteHandler
from logging_sqlite import SQLiteHandler


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # sqlite handler
    sh = SQLiteHandler(db="test.db")
    sh.setLevel(logging.INFO)
    logging.getLogger().addHandler(sh)

    # test
    logging.info('Start')
    #a_module.test()
    logging.info('End')

if __name__ == '__main__':
    main()
