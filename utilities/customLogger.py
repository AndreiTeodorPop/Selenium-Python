import logging
import os

log_path = "C:\\Users\\andre\\PycharmProjects\\Selenium-Python\\Logs\\automation.log"


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%d/%m/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
