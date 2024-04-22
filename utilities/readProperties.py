from pathlib import Path
import configparser
import os

config_path = "C:\\Users\\andre\\PycharmProjects\\Selenium-Python\\Configurations\\config.ini"
config = configparser.ConfigParser()
config.read(config_path)


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config.get("common info", "baseUrl")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", "password")
        return password
