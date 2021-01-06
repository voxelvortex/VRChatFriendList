"""
This file will act as the main logic for the program

Author: VoxelVortex (Michael)
VRCatFriendList > Main.py
"""
import vrcpy, VRChatAdapter


def main():
    client = VRChatAdapter.login('login_info.json')

    VRChatAdapter.logout(client)


if __name__ == '__main__':
    main()