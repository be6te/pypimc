from requests import Session

class Credits:
    __version__ = '1.1'
    __author__ = 'https://github.com/lbeete'

class Minecraft():
    def __init__(self):
        self.session = Session()
        self.get_uid = 'https://api.mojang.com/users/profiles/minecraft/'
        self.get_profile = 'https://api.ashcon.app/mojang/v2/user/'
        self.get_usernames = 'https://api.slothpixel.me/api/players/'
        
        self.username = ''
        self.uuid = ''
    
    def minecraft(self, username=None, uuid=None):
        info = []
        if uuid is None:
            try:
                get_username = self.session.get(url=self.get_profile + username)
                
                data = get_username.json()
                get_username = data['username']
                first_username = data['username_history'][0]
                get_first_username = first_username['username']
                slim_skin = data['textures']['slim']
                head_skin = 'https://mc-heads.net/head/{}'.format(username)
                body_skin = 'https://mc-heads.net/player/{}'.format(username)

                if slim_skin == 'true':
                    slim_skin = 'Slim Skin'
                else:
                    slim_skin = 'None'

                info.append(get_username)
                info.append(get_first_username)
                info.append(slim_skin)
                info.append(head_skin)
                info.append(body_skin)
                return info
            except:
                return 'Invalid Username or uuid is not found'
        elif username is None:
            try:
                get_username = self.session.get(url=self.get_profile + uuid)
                data = get_username.json()

                get_username = data['username']
                first_username = data['username_history'][0]
                get_first_username = first_username['username']

                slim_skin = data['textures']['slim']
                head_skin = 'https://mc-heads.net/head/{}'.format(uuid)
                body_skin = 'https://mc-heads.net/player/{}'.format(uuid)

                if slim_skin == 'true':
                    slim_skin = 'Slim Skin'
                else:
                    slim_skin = 'None'

                info.append(get_username)
                info.append(get_first_username)
                info.append(slim_skin)
                info.append(head_skin)
                info.append(body_skin)
                return info
            except:
                return 'Invalid Username or uuid is not found'
        return ''

class Hypixel:
    def __init__(self):
        self.api = ''
        self.session = Session()
    
    def hypixelstats(self, username=None, uuid=None):
        info = []

        if uuid is None:
            try:
                data = self.session.get('https://api.slothpixel.me/api/players/{}'.format(username)).json()
                rank = str(data['rank'])
                
                if '_PLUS' in rank:
                    rank = rank.replace('_PLUS', '+')

                info.append(str(data['online']))
                info.append(str(rank))
                info.append(str(data['language']))
                info.append(str(data['exp']))
                info.append(str(data['level']))
                info.append(int(data['total_coins']))

                return info
            except:
                return 'Invalid Username or uuid is not found'
        elif username is None:
            try:
                data = self.session.get('https://api.slothpixel.me/api/players/{}'.format(username)).json()
                rank = str(data['rank'])
                
                if '_PLUS' in rank:
                    rank = rank.replace('_PLUS', '+')

                info.append(str(data['online']))
                info.append(str(rank))
                info.append(str(data['exp']))
                info.append(str(data['level']))
                info.append(int(data['total_coins']))

                return info
            except:
                return 'Invalid Username or uuid is not found'
        return ''

    def bedwarstats(self, username=None, uuid=None, mode=None):
        info = []

        if uuid is None:
            try:
                data = self.session.get('https://api.slothpixel.me/api/players/{}'.format(username)).json()
                rank = str(data['rank'])
                
                if mode is None:
                    if '_PLUS' in rank:
                        rank = rank.replace('_PLUS', '+')
                        
                    info.append(int(data['stats']['BedWars']['coins']))
                    info.append(int(data['stats']['BedWars']['exp']))
                    info.append(int(data['stats']['BedWars']['level']))
                    return info
                elif mode == 'solo':
                    info.append(str(data['stats']['BedWars']['wins']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['deaths']))
                    info.append(str(data['stats']['BedWars']['losses']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['winstreak']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['games_played']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['iron_resources_collected']))
                    return info
                elif mode == 'three':
                    info.append(str(data['stats']['BedWars']['wins']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['deaths']))
                    info.append(str(data['stats']['BedWars']['losses']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['winstreak']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['games_played']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['iron_resources_collected']))
                    return info
            except:
                return 'Invalid Username or uuid is not found'

        elif username is None:
            try:
                data = self.session.get('https://api.slothpixel.me/api/players/{}'.format(uuid)).json()
                rank = str(data['rank'])
                
                if mode is None:
                    if '_PLUS' in rank:
                        rank = rank.replace('_PLUS', '+')
                        
                    info.append(int(data['stats']['BedWars']['coins']))
                    info.append(int(data['stats']['BedWars']['exp']))
                    info.append(int(data['stats']['BedWars']['level']))
                    return info
                elif mode == 'solo':
                    info.append(str(data['stats']['BedWars']['wins']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['deaths']))
                    info.append(str(data['stats']['BedWars']['losses']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['winstreak']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['games_played']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['solo']['iron_resources_collected']))
                    return info
                elif mode == 'three':
                    info.append(str(data['stats']['BedWars']['wins']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['deaths']))
                    info.append(str(data['stats']['BedWars']['losses']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['winstreak']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['games_played']))
                    info.append(str(data['stats']['BedWars']['gamemodes']['3v3v3v3']['iron_resources_collected']))
                    return info
            except:
                return 'Invalid Username or uuid is not found'
        return ''