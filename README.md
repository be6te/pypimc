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
from pypimc.Minecraft import Minecraft

info = Minecraft()

print(info.minecraft(username='wDirty')) # Display minecraft account information on screen
```
## Output
```
['wDirty', 'buzzdlux', 'None', 'https://mc-heads.net/head/wDirty', 'https://mc-heads.net/player/wDirty']
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
