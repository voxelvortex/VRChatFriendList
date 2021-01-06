"""
This file will act as an in between for the main code and the VRChat API wrapper.

Author: VoxelVortex (Michael)
VRCatFriendList > VRChatAdapter.py
"""

import vrcpy
import json


def login(json_file):
    # Creates a valid session with the VRChat API

    login_info = None
    with open(json_file, 'r') as login_info_file:
        login_info = json.load(login_info_file)

    if login_info is None:
        raise Exception("Something went wrong while trying to retrieve your login credentials")

    client = vrcpy.Client()

    client.login2fa(login_info["username"], login_info["password"])

    code = input("Please enter your 2FA token: ")
    client.verify2fa(code)

    return client


def logout(client):
    # Closes a valid session with the VRChat API
    client.logout()


def fetch_online_friends(client):
    friends_list = client.fetch_friends()
    return parse_friends_list(friends_list)


def fetch_full_online_friends(client):
    friends_list = client.fetch_full_friends()
    return parse_friends_list(friends_list)


def parse_friends_list(friends_list):
    friends_list_dict = {"friends": []}

    for friend in friends_list:
        friends_list_dict["friends"].append(
            {"displayName": friend.displayName,
            "status": friend.status,
            "last_platform": friend.last_platform
        })

    return friends_list_dict
