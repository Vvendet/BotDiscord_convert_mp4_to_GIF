import discord
import asyncio
from discord.ext import commands
from moviepy.editor import VideoFileClip
import requests
from io import BytesIO
from discord.ext import commands
from discord import Embed, File
import os


########################################################################################

client = discord.Client()
token = 'TOKEN HERE'


##########################################################################################


@client.event
async def on_ready():
	print("ESTOU ONLINE")
	print(client.user.name)
	print(client.user.id)



@client.event
async def on_message(message):
	if message.content.startswith("!converter help"):
		await message.channel.send('Para converter algum vídeo em gif, mande um vídeo CURTO com a mensagem "!converter".')


@client.event
async def on_message(message):
	

	if message.content.startswith("!converta"):

		print(message.attachments[0])
		attachment = message.attachments[0]
		autor = message.author
		print(autor)
		print(autor.id)
		url = attachment.url
		video = attachment.filename
		print(video,url)
		await message.channel.send('Aguarde {mencao}, estou tentando converter o vídeo {video}...'.format(mencao=autor.mention,video=video))
		r = requests.get(url)
		with open(video, 'wb') as f:
  			novo_video = f.write(r.content)
		videomp4 = VideoFileClip(video)
		gif = videomp4.write_gif('novogif.gif', fps=5)
		await message.channel.send('Aguarde {mencao}, estou tentando enviar o {video} convertido...'.format(mencao=autor.mention,video=video))
		

		###################################################################
		####### MUDE AQUIIII    ###########################################


		file_e = File(r"C:\Users\PcdaMae\Desktop\cursoWEB Julio\hackerrank\novogif.gif", filename=f"novogif.gif")
		
		#####################################################################
		####################################################################


		embed = discord.Embed(title="GIF", description = 'Ta aí teu gif convertido S2,{}.'.format(autor.mention))
		embed.set_image(url="attachment://novogif.gif")
		await message.channel.send(file=file_e, embed=embed)
		os.remove(video)
		os.remove("novogif.gif")



@client.event
async def on_member_join(member):
	channel = alfred.get_channel(850173134509441025)
	embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
	await channel.send(embed=embed)




client.run(token)
#########################
###JULIO FROES###########
#########################
