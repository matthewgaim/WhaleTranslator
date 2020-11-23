import discord
from discord.ext import commands
from discord.ext.commands import Bot
from googletrans import Translator

translator = Translator()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user.name}!')
 

    async def on_message(self, message):
        print('Message from {0.author}: {0.content} {0.author.voice}'.format(message))
        if message.content.startswith('translate'):
            preContent = message.content.split(' ')
            if len(preContent) > 2:
                language = (preContent[1].split('='))[1]
                text = (' '.join(preContent[2:len(preContent)]))
                trans = translator.translate(text, dest=language).text
                mention = '{0.author.mention}'.format(message)
                await message.channel.send('{0} Translation: {1}'.format(mention,trans))
            else:
                await message.channel.send('Incorrect formatting! do translate to={language} {words i want translated}')

client = MyClient()
file = open("discordKey.txt","r")
discordKey = file.read()
file.close()
client.run(discordKey)
