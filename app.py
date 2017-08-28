import discord
import asyncio
import log

##discordapp.com/oauth2/authorize?client_id=351638657225981954&scope=bot&permissions=0

client = discord.Client()
servers = client.servers;
points = {}
coins = 0

def Dictionary():
    global swears
    with open("dictionary.txt") as f:
        content = f.readlines()
    
    swears = [x.strip() for x in content]
    log.Log(str(swears))

@client.event
async def on_ready():
    for usr in client.get_all_members():
        log.Log(usr.name)
        points[usr.name] = 0
    
    log.Log(str(len(points)) + ' users logged.')
    

@client.event
async def on_message(message):

    global coins
    
    n = message.author.name
    if n == "swear-jar":
        return
    
    if message.content.startswith("!coin"):
        await client.delete_message(message)
        msg = 'There '
        if coins == 1:
            msg += 'is 1 coin'
        else:
            msg += 'are ' + str(coins) + ' coins'
        msg += ' in the jar.'
        await client.send_message(message.channel, msg)
    
    swear_count = 0
    for sw in swears:
        if sw in message.content.lower():
            swear_count += 1
    if swear_count > 0:
        msg = 'Plink! '
        msg += n + ' puts ' + str(swear_count) + ' coin'
        if swear_count != 1:
            msg += 's'
        msg += ' in the jar.'
        await client.send_message(message.channel, msg)
        coins += swear_count

Dictionary()

client.run('MzUxNjM4NjU3MjI1OTgxOTU0.DIVs4g.uWJgf7t0WyNeYhV3x4-6Z0xKHtc')
