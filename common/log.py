import logging
import time
import os

project_path = os.path.dirname(os.path.dirname(__file__))
log_path = project_path.split('common')[0] + '/log'
log_name = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y%m%d-%H%M%S')))


class myLog:
    def __printlog(self, level, message):
        """create logger"""
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        """create a handler for writing log"""
        file_hanlder = logging.FileHandler(log_name, 'a', encoding='utf-8')
        file_hanlder.setLevel(logging.DEBUG)

        """create a handler for output in console"""
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        """define the formatter of handler's output"""
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_hanlder.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        """add handler into logger"""
        logger.addHandler(file_hanlder)
        logger.addHandler(console_handler)

        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(console_handler)
        logger.removeHandler(file_hanlder)

        """close file handler"""
        file_hanlder.close()

    def debug(self, message):
        self.__printlog('debug', message)

    def info(self, message):
        self.__printlog('info', message)

    def warning(self, message):
        self.__printlog('warning', message)

    def error(self, message):
        self.__printlog('error', message)

logger = myLog()
# logger.info('test')