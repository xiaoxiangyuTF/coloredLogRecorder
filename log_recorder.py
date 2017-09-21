# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
# ------------------------------------------------------------

"""
This module provide functions.

Author:     xiaoxiangyutf
Data:       2017/9/13
"""

import logging
import os
import coloredlogs


class ColoredLogger(logging.Logger):
    '''
    colored logging
    '''
    def __init__(self, name, level, log_path='.\log\log.log'):
        try:
            log_dir = os.path.split(log_path)[0]
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
        except IsADirectoryError as e:
            log_path = './log.log'

        logging.Logger.__init__(self, name=name, level=level)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(filename=log_path, mode='a', encoding='utf-8')

        format_str = "[%(asctime)s] [%(name)s:%(levelname)s] [%(threadName)s:%(thread)d] " \
                     "[%(filename)s:%(module)s:%(funcName)s:%(lineno)d]: %(message)s"
        formatter = logging.Formatter(fmt=format_str)

        console_handler.setFormatter(fmt=formatter)
        file_handler.setFormatter(fmt=formatter)

        console_handler.setLevel(level=level)
        file_handler.setLevel(level=level)

        self.addHandler(console_handler)
        self.addHandler(file_handler)

        coloredlogs.install(logger=self,
                            level=level,
                            fmt=format_str,
                            milliseconds=True,
                            field_styles=
                            {
                                'hostname': {'color': 'magenta'},
                                'programname': {'color': 'cyan'},
                                'name': {'color': {}},
                                'levelname': {'color': 'black'},
                                'asctime': {'color': {}}
                            },
                            level_styles=
                            {
                                'info': {'color': 'green', 'bold': True},
                                'notice': {'color': 'magenta'},
                                'verbose': {'color': 'blue'},
                                'success': {'color': 'green', 'bold': True},
                                'spam': {'color': 'green'},
                                'critical': {'color': 'red', 'bold': True},
                                'error': {'color': 'red', 'bold': True},
                                'debug': {'color': 'white', 'bold': True},
                                'warning': {'color': 'yellow', 'bold': True}
                            })
        return

if __name__ == '__main__':
    # Create a logger object.
    logger = ColoredLogger(__name__, logging.DEBUG, '.\log\log.log')
    # Some examples.
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")

