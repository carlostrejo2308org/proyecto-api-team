import pylast
import json


class APIConnection:
    def __init__(self):
        self.__API_SECRET = "93700682270fbaecfdf2943ca9c25e9a"
        self.__API_KEY = "1780b18a0490c40d21d2d9d6ea19900b"

    def __load_user_data(self):
        with open('user_data.json') as json_file:
            user_data = json.load(json_file)

        self._username = user_data["username"]
        self._password = user_data["password"]
        self.__password_hash = pylast.md5(self._password)

    def get_network(self):
        self.__load_user_data()
        self.__network = pylast.LastFMNetwork(
            api_key=self.__API_KEY,
            api_secret=self.__API_SECRET,
            username=self._username,
            password_hash=self.__password_hash)
        return self.__network
