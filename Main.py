"""
This file will act as the main logic for the program

Author: VoxelVortex (Michael)
VRCatFriendList > Main.py
"""
import vrcpy
import VRChatAdapter


def main():
    user_in = ""
    client = VRChatAdapter.login('login_info.json')

    while user_in.strip() == "":
        friends = VRChatAdapter.fetch_online_friends(client)

        print_friends(friends)
        user_in = input("Press ENTER to continue, or type QUIT to quit: ")

    VRChatAdapter.logout(client)


def print_friends(friends):
    for friend in friends["friends"]:
        print("{0}\n\tStatus: {1}\n\tPlatform: {2}"
              .format(friend["displayName"], friend["status"], friend["last_platform"]))


if __name__ == '__main__':
    main()
