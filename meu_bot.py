import discord
import os

intents = discord.Intents.default()  
intents.messages = True
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} as regras do servidor são:{os.linesep}1-Não desrespeitar os membros{os.linesep}2- Proibido divulgação de link afiliados e de terceiros')
        elif message.content == '?nivel':
            await message.author.send('Nível1')
        
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)

client = MyClient(intents=intents)
client.run('MTExNTM4MjA2NDY4NzA5OTkwNQ.GdBYaR.sDWI3-_3aoVMcsYvVcpqcj2uUzDBTrM02Zxvek')
