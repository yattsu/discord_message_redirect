import discord
import requests
import config

client = discord.Client()

@client.event
async def on_ready():
    print('Bot online')

last_user = False
last_channel = False
@client.event
async def on_message(message):
	global last_user
	global last_channel

	server_id = message.server.id
	if config.prefs['server_id'] != '' and config.prefs['server_id'] == server_id:
		if message.author.bot == False:
		    author_name = message.author.display_name
		    author_id = message.author.id
		    content = message.content
		    channel_name = message.channel.name
		    server_name = message.server.name

		    data = {
		    	'username': config.prefs['username'] + ' [' + server_name + ']',
		    	'avatar_url': config.prefs['avatar_url'],
		    	'content': ''
		    	}

		    if last_user != author_id or last_channel != channel_name:
		    	data['content'] = '**`' + author_name + '`** - **`#' + channel_name + '`**' + "\n" + content
		    else:
		    	data['content'] = content

		    requests.post(config.prefs['webhook'], data = data)
		    last_user = author_id
		    last_channel = channel_name

client.run(config.prefs['token'])