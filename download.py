import requests, sys
from sys import argv

most_recent_id = argv[1]
channel_id = argv[2]
auth = argv[3]
how_many = 1000
how_many = int(argv[4])

def checkArgs():
    if len(auth) != 70:
        print("Authorization code is incorrect length")
        exit()
    if len(most_recent_id) != 19:
        print("Most recent id is incorrect length")
        exit()
    if len(channel_id) != 18:
        print("Channel id is incorrect length")
        exit()

def getMsgs(from_id):
    base = "https://discord.com/api/v10"
    url = f"{base}/channels/{channel_id}/messages?before={from_id}&limit=100"
    headers = {
        "authorization": auth,
    }
    return requests.get(url, headers=headers).json()

def getLots(from_id, how_many):
    last_id = from_id
    msgs = []
    if how_many < 100:
        return getMsgs(last_id)[:how_many]
    for i in range(how_many//100):
        batch = getMsgs(last_id)
        #need to "click" upward in batches of 100. so get 100, get the top one, and get the 100 above that
        last_id = batch[-1]["id"] 
        msgs += batch
    return msgs

checkArgs()
all_msgs = getLots(most_recent_id, how_many)

for msg in reversed(all_msgs): 
    print(msg["content"],'\n')

print(len(all_msgs))
