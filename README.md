# Discord message redirect
A bot and a webhook working together to recreate the conversation from one server to another.<br>
Let's call the server you want to get the messages from, `A`. Now let's call the server you want to send the messages to, `B`. Good? Good.

## Requirements
`Python 3.4<`<br>
`discord.py` - A python wrapper for the Discord API: https://github.com/Rapptz/discord.py<br>
`requests` - A python library that lets you make... requests<br>
One Discord app, it needs to be a bot application. Invite it to server `A`.<br>
One Webhook, it needs to be created on server `B`.<br>

## How to...
Edit config.py like following:
```
'token': 'BOT'S TOKEN',
'webhook': 'THE WEBHOOK URL',
'server_id': 'THE ID OF SERVER 'A'',
'username': 'Message',
'avatar_url': 'https://shecantrade.com/media/SheCanTrade/site-images/icon-two.png?ext=.png'
```
Only strings allowed<br>
You can change the 'username' and 'avatar_url' as you like<br>

Bot created and invited in server `A`? Good.<br>
Weebhook created on server `B`? Good.<br>
Now change directory to the one you cloned this repo in and `python3 message_redirect.py`<br><br>
server A:<br>
![server A](https://i.gyazo.com/1f1c4e7fe8df0e5ccd73c262fd8d9c3a.png)<br>
server B:<br>
![server B](https://i.gyazo.com/62ce32d350305659e35876d18599cee0.png)
