import disnake
from disnake.ext import commands

client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print('Olá mundo')

@client.slash_command(name='teste', description='fununcia buceta')
async def testes(inter):
    await inter.response.send_message(f'Comando funcionando {inter}')

client.run('Seu token de bot')
