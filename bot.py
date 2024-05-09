import discord


intents = discord.Intents.default()
intents.typing = False
intents.presences = False


TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
