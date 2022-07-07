<center><a href="https://github.com/lbeete"><img src="https://i.imgur.com/AREiNyC.png" alt="bot-icon-1" border="0"></a></center>

---
<div align="center">
  <a><img align="center" alt="version" src="https://img.shields.io/badge/Version-1.0-brightgreen"></a>
  <a><img align="center" alt="stars" src="https://img.shields.io/github/stars/lbeete/NamePY"></a>
  <a><img align="center" alt="forks" src="https://img.shields.io/github/forks/lbeete/NamePY"></a>
  <a><img align="center" alt="tweet" src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Flbeete%2FNamePY"</a>
</div>

---

## Install
```
$ pip install pypimc
```

## Examples
```py
from pypimc.Minecraft import Minecraft # Minecraft account information 

info = Minecraft()

print(info.minecraft(username='wDirty')) # Display minecraft account information on screen
```
Output:
```
['wDirty', 'buzzdlux', 'None', 'https://mc-heads.net/head/wDirty', 'https://mc-heads.net/player/wDirty']
```
## Hypixel stats examples
```py
from pypimc.Minecraft import Minecraft # Hypixel Information

info = Minecraft()
username = 'wDirty'

print(info.hypixelstats(username=username)) # Display hypixel stats in list
print(info.hypixelstats(username=username)[0]) # Shows if the user is connected to hypixel True/False
print(info.hypixelstats(username=username)[1]) # Show user rank in hypixel
print(info.hypixelstats(username=username)[2]) # Shows the total experience on the server
print(info.hypixelstats(username=username)[3]) # Shows hypixel level
print(info.hypixelstats(username=username)[4]) # Shows total coins in hypixel
```
Output:
```
['False', 'VIP', '832905', '23.54', 330716]
```

## A list to facilitate the use and to make it more understandable

```py
from pypimc.Minecraft import Minecraft

info = Minecraft()
username = 'wDirty'

print(info.minecraft(username=username)) # Show minecraft account information in list
print(info.minecraft(username=username)[0]) # Show minecraft username
print(info.minecraft(username=username)[1]) # Show first minecraft username
print(info.minecraft(username=username)[2]) # Slim skin
print(info.minecraft(username=username)[3]) # Minecraft head skin Output example: https://mc-heads.net/head/wDirty
print(info.minecraft(username=username)[4]) # Full minecraft skin
```

- This is just a small test and is not finished and may have bugs.
> Please consider leaving a ⭐ in the top right on the repo :D
