"""
This file will act as an in between for the main code and the VRChat API wrapper.

Author: VoxelVortex (Michael)
VRCatFriendList > VRChatAdapter.py
"""

import vrcpy, json


def login(json_file):
    login_info = None
    with open(json_file, 'r') as login_info_file:
        login_info = json.load(login_info_file)

    if login_info is None:
        raise Exception("Something went wrong while trying to retrieve your login credentials")

    client = vrcpy.Client()

    client.login2fa(login_info["username"], login_info["password"])

    code = input("Please enter your 2FA token: ")
    client.verify2fa(code)

    print(client)

    client.logout()
