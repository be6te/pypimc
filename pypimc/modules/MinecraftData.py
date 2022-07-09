import json

class MinecraftData(data=None):
    def __init__(self) -> None:
        self.get_uid = 'https://api.mojang.com/users/profiles/minecraft/'
        self.get_profile = 'https://api.ashcon.app/mojang/v2/user/'
        self.get_usernames = 'https://api.slothpixel.me/api/players/'
        self.head_skin = 'https://mc-heads.net/head/'
        self.body_skin = 'https://mc-heads.net/player/'