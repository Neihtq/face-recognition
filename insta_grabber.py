import sys
import json
from InstagramAPI import InstagramAPI

target_name = "samanthakimr"

USERNAME = "neiht"
PASSWORD = "Dergeraet95"
api = InstagramAPI(USERNAME, PASSWORD)
api.login()

api.searchUsername(target_name)
name_id = api.LastJson["user"]["pk"]
api.getUserFeed(name_id)
user_feed = api.LastJson["items"]


print(json.dumps(user_feed[0], indent=4))