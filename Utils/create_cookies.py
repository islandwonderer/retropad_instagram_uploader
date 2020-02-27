from instapy_cli import client
import ssl
import json

config_file = "config.json"


def load_config(json_file):
    with open(json_file, "r") as file:
        temp_config = json.load(file)
    return temp_config


config = load_config(config_file)

ssl._create_default_https_context = ssl._create_unverified_context

username = config["login"]
password = config["password"]
cookie_file = username + "_ig.json"

with client(username, password, cookie_file=cookie_file, write_cookie_file=True) as cli:
    # get string cookies
    cookies = cli.get_cookie()
    print(type(cookies)) # == str
    print(cookies)
    # do stuffs with cli
    ig = cli.api()
    me = ig.current_user()
    print(me)
