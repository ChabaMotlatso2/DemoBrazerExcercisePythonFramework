import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")

class ReadConfigs() :
    def getDemoBrazerURL(self):
        return config.get("URLS", "demoBrazerURL")


