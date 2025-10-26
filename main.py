import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
import subprocess
subprocess.Popen(["python", "keep_alive.py"])

keep_alive()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class Client(commands.Bot):
    @client.event 
    async def on_ready(self):
        print(f'Hello ae t là {self.user}!')

        try:
            guild = discord.Object(id=1374705648234659972)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} command to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user in message.mentions:
            await message.channel.send(f'Hello mấy cháu')
        if message.content.startswith(f'depchai ngu'):
            await message.channel.send(f'Watch yo tone lil blud🙏🏿')
        if message.content.startswith('jigsaw'):
            await message.channel.send(f'Yo final challenge: let you bih go through yo phone!!!!')
            await message.channel.send(f'Oh hell na yo ás tweakin jigsaw😰😰')
        if 'tick' in message.content:
            await message.add_reaction('<a:acn_tickden:1413824083413696652>')
            await message.add_reaction('<a:acn_tickxanh:1414079548341096520>')
            await message.add_reaction('<a:acn_tickhong:1416068644349411420>')
            await message.add_reaction('<a:a_tickvang:1422566122305097830>')
        await self.process_commands(message)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
client = Client(command_prefix="𒈓", intents=intents)

GUILD_ID = discord.Object(id=1374705648234659972)


@client.tree.command(name="helu", description="Heli", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message('Chào mấy cháu')



@client.tree.command(name="embed", description="Tạo embed", guild=GUILD_ID)
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Depchai", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="T la Depchai", color=discord.Color.yellow())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1374705648796827671/1431545974748086463/image0.png?ex=68fdce95&is=68fc7d15&hm=0f1ff4b2dcdee8df798cdb6472631c61d2d5ef2d00bac97580496ef22a515015&=&format=webp&quality=lossless&width=668&height=668")
    embed.add_field(name="Depchai 1", value="T la Depchai", inline=True)
    embed.add_field(name="Depchai 2", value="T la Depchai", inline=True)
    embed.set_footer(text="Depchai")
    embed.set_author(name=interaction.user.name)
    await interaction.response.send_message(embed=embed)



class View(discord.ui.View):
    @discord.ui.button(label="Depchai", style=discord.ButtonStyle.red, emoji="<:depchai:1383790515941670912>")
    async def button_depchai(self, button, interaction):
        await button.response.send_message("M da bi depchai grape💀💀☠️☠️", ephemeral=True)
    
    @discord.ui.button(label="Trollface", style=discord.ButtonStyle.blurple, emoji="<:thosewhoknow:1384034450769449153>")
    async def button_trollface(self, button, interaction):
        await button.response.send_message("M da bi trollface grape💀💀☠️☠️", ephemeral=True)

    @discord.ui.button(label="Rùa", style=discord.ButtonStyle.green, emoji="<a:ruanhay:1387395274518958181>")
    async def button_rua(self, button, interaction):
        await button.response.send_message("Rùa ko làm gì m :3", ephemeral=True)

@client.tree.command(name="button", description="Nút", guild=GUILD_ID)
async def nut(interaction: discord.Interaction):
    await interaction.response.send_message("Hãy chọn nút đúng", view=View())



class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption
            (
                label="Mango",
                description="Ăn mango",
                emoji="<:mango2:1387397188426006678>"
            ),
            discord.SelectOption
            (
                label="Mustard",
                description="Chấm mustard",
                emoji="<:mustard:1388153561870766192>"
            ),
            discord.SelectOption
            (
                label="Baby oil",
                description="Dùng baby oil",
                emoji="<:babyoil:1383790990850134097>"
            )
        ]
        super().__init__(placeholder="M sẽ ăn gì?", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Mango": 
           await interaction.response.send_message(f'Mango rat ngon nen m ko bi gi<:depchai:1383790515941670912>', ephemeral=True)
        elif self.values[0] == "Mustard": 
           await interaction.response.send_message(f'Mustard qua cay nen m bi chet<:depchaitoi:1388784332180688906>', ephemeral=True)
        elif self.values[0] == "Baby oil": 
           await interaction.response.send_message(f'M da bi diddy grape do lay baby oil cua ong<:diddy:1384162279649444012>', ephemeral=True)

class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())

@client.tree.command(name="menu", description="Menu", guild=GUILD_ID)
async def menu(interaction: discord.Interaction):
    await interaction.response.send_message(view=MenuView())




@client.tree.command(name="free_fire_name_generator", description="Tạo tên fi fai", guild=GUILD_ID)
async def ff(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'꧁༺,{name}ᴾᴿᴼシ')




client.run(TOKEN)


