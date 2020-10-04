import discord
import random
import giphy_client
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


token="" #insert bot token here
client=discord.Client()
server_id= #Insert server ID here
giphy_token='' #insert giphy token here
api_instance=giphy_client.DefaultApi()




pro_members=["Severia", "Hieren1"]
players=[]
#Librerias de imagenes
jesh_images=["https://imgur.com/iXGV53S", "https://imgur.com/ox4D6Uv", "https://imgur.com/FXRsXHw", "https://imgur.com/ujsX0fr",
             ]
chango="https://imgur.com/a/NUdNIkA"
chango_pies="https://imgur.com/a/hr5bu9w"
chango_rezando="https://imgur.com/a/kmKgO9Y"
client=commands.Bot(command_prefix="")

@client.event
async def on_message(message):
    id=client.get_guild(server_id)
    sent_message=str(message.content).lower()
    print(sent_message)
    block="```"


    if sent_message.find("matex say ")!=-1:
        message_list=str(message.content).split(" ")
        message_list[0]=message_list[0].lower()
        message_list[1] = message_list[1].lower()
        fixed_message=" ".join(message_list)
        print(fixed_message)
        new_message=fixed_message.split("matex say ")[1]
        await message.channel.send(f"{block}{new_message}{block}")
    elif sent_message=="matex count users":
        await message.channel.send(f"{block}There are #{id.member_count} users in this server{block}")
    elif sent_message=="matex gay":
        await message.channel.send(f"{block}{message.author.name} is GAY{block}")
    elif sent_message=="matex iq":
        if message.author.name in pro_members:
            await message.channel.send(f"{block}{message.author.name}'s IQ is over 5000{block}")
        else:
            await message.channel.send(f"{block}{message.author.name}'s IQ is less than 3{block}")
        #{message.author.name} is retarded
    #Librerias de imagenes para comendos MATEX SEND
    elif sent_message=="matex send jesh" or sent_message=="matex send jeshua" or sent_message=="matex send pigihunter":
        await message.channel.send(f"{random.choice(jesh_images)}")
    elif sent_message=="matex send chango":
        await message.channel.send(f"{chango}")
    elif sent_message=="matex send chango rezando":
        await message.channel.send(f"{chango_rezando}")
    elif sent_message=="matex send chango pies":
        await message.channel.send(f"{chango_pies}")
    #Matex gifs
    elif sent_message.find("matex gif")!=-1:
        if sent_message=="matex gif":
            #tema=sent_message.split("matex gif ")[1]

            response=api_instance.gifs_search_get(giphy_token, "random", limit=100, rating='g')
            gif_list=list(response.data)
            gif=random.choices(gif_list)
            await message.channel.send(f"{gif[0].url}")

        else:
            tema = sent_message.split("matex gif ")[1]
            response = api_instance.gifs_search_get(giphy_token, tema, limit=5, rating='g')
            gif_list=list(response.data)
            gif=random.choices(gif_list)
            await message.channel.send(f"{gif[0].url}")
    """
    elif sent_message.find("matex play ")!=-1:
        print("attempting to play")
        message_list=str(sent_message).split(" ")
        message_list[0]=message_list[0].lower()
        message_list[1] = message_list[1].lower()
        fixed_message=" ".join(message_list)
        print(fixed_message)
        url=fixed_message.split("matex play ")[1]
        channel = message.author.voice.channel
        guild=message.guild
        voice_client=await channel.connect()
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                          'options': '-vn'}
        voice = get(client.voice_clients, guild=message.guild)

        with YoutubeDL(YDL_OPTIONS ) as ydl:
            info = ydl.extract_info("https://www.youtube.com/watch?v=dQw4w9WgXcQ", download=False)
        URL = info['formats'][0]['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    """

"""
        channel = message.author.voice.channel
        guild=message.guild
        voice_client=await channel.connect()
        player = await voice_client.create_ytdl_player(url)
        players[guild.id]=player
        player.start
        print("Success")
"""

#754146281969942619
#754146053049155645
#754145713692344410

client.run(token)
