import os
import discord
import random
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
from datetime import datetime, timedelta

keep_alive()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# print("TOKEN loaded:", bool(TOKEN))

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="$", intents=intents)
        
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
            await message.add_reaction('🇭')
            await message.add_reaction('🇮')
        if message.content.startswith(f'depchai ngu'):
            await message.channel.send(f'Watch yo tone lil blud🙏🏿')
        if 'ban' in message.content and self.user in message.mentions:
            await message.channel.send(f'Something bad about to happen to me💀💀☠️☠️')
        if message.content.startswith('jigsaw'):
            await message.channel.send(f'Yo final challenge: let you bih go through yo phone!!!!')
            await message.channel.send(f'Oh hell na yo ás tweakin jigsaw😰😰')
        if 'tick' in message.content:
            await message.add_reaction('<a:acn_tickden:1413824083413696652>')
            await message.add_reaction('<a:acn_tickxanh:1414079548341096520>')
            await message.add_reaction('<a:acn_tickhong:1416068644349411420>')
            await message.add_reaction('<a:a_tickvang:1422566122305097830>')
        if message.content.startswith('𒈓trickortreat'):
            await message.channel.send(f'Phần thưởng của bạn là...')
            num = (random.randint(1,2))
            if num==1:
                await message.channel.send(f'1 viên kẹo🍬')
            elif num==2:
                await message.channel.send(f'Mute 1 phút <:thosewhodontknow:1393572894558126121>')
                duration = timedelta(minutes=1)
                await message.author.timeout(duration, reason = 'hjhj')
        await self.process_commands(message)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
client = Client()

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
@app_commands.describe(chudau="Chọn chữ đầu",chucuoi="Chọn chữ cuối")
@app_commands.choices(
    chudau=[
       app_commands.Choice(name="꧁༺", value="canh"),
       app_commands.Choice(name="★彡", value="sao"),
       app_commands.Choice(name="ミᵒ°", value="bong"),
       app_commands.Choice(name="㊪", value="trung"),
       app_commands.Choice(name="㋰", value="nhat")], 
    chucuoi=[
       app_commands.Choice(name="༻꧂", value="canhc"),
       app_commands.Choice(name="ミ★", value="saoc"),
       app_commands.Choice(name="°ᵒ彡", value="bongc"),
       app_commands.Choice(name="㊪", value="trungc"),
       app_commands.Choice(name="㋰", value="nhatc"),
       app_commands.Choice(name="ᴾᴿᴼシ", value="pro"),
       app_commands.Choice(name="⁀ᶦᵈᵒᶫ", value="idol")
    ])
async def ff(interaction: discord.Interaction, name: str, chudau: app_commands.Choice[str], chucuoi: app_commands.Choice[str]):
    await interaction.response.send_message(f'{chudau.name}{name}{chucuoi.name}')



@client.tree.command(name="uhh", description="Tạo 100 chữ à ừ ờ ừm ngẫu nhiên", guild=GUILD_ID)
async def uhh(interaction: discord.Interaction):
    letters1 = ''
    for i in range(100):
        numbers = (random.randint(1, 4))
        if numbers==1:
            letters="à"
        elif numbers==2:
            letters="ừ"
        elif numbers==3:
            letters="ờ"
        elif numbers==4:
            letters="ừm"
        letters1 = (f'{letters1}{letters} ')
    result = (letters1)
    await interaction.response.send_message(result)



@client.tree.command(name="chuvan", description="Sắp xếp một emoji thành chữ vạn", guild=GUILD_ID)
async def chuvan(interaction: discord.Interaction, emoji: str):
    e = emoji
    t = '<:empty:1423996972431577240>'
    await interaction.response.send_message(f"{e}{t}{t}{e}{e}{e}{e}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{e}{e}{e}{e}{e}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{e}{e}{e}{e}{t}{t}{e}")



class CounterButton(discord.ui.View):
    def __init__(self, limit):
        super().__init__(timeout=None)  # timeout=None = không bao giờ tắt
        self.value = 0
        self.last_user = "Chưa có ai bấm <:ruabatngo:1420409581598806107>"
        self.limit = limit if limit > 0 else None

    @discord.ui.button(label="0", style=discord.ButtonStyle.blurple)
    async def count_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.limit is not None and self.value >= self.limit:
            button.disabled = True
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content=f"Đã đạt giới hạn {self.limit} lượt bấm🎉, **người chiến thắng là: ** {self.last_user}", view=self)
            return
        if self.last_user == interaction.user.display_name:
            await interaction.response.send_message(f"Không được bấm 2 lần liên tục <a:sussybaka:1422928147577307166>", ephemeral=True)
            return
        self.value += 1
        self.last_user = interaction.user.display_name
        button.label = str(self.value)
        await interaction.response.edit_message(content=f"**Người bấm gần nhất:** {self.last_user}", view=self)

@client.tree.command(name="counter", description="Tạo một nút bấm đếm số", guild=GUILD_ID)
async def counter(interaction: discord.Interaction, limit: int):
    view = CounterButton(limit)
    await interaction.response.send_message(content="**Bấm vào nút để tăng số!**", view=view)



import time
print("🕒 Đang chờ 10 giây trước khi khởi động bot...")
time.sleep(10)

try:
    client.run(TOKEN)
    print("mẹ ơi con làm được rồi🥹🥹")
except Exception as e:
    print("Lỗi khi chạy bot:", e)