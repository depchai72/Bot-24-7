import os
import random
import re
import aiohttp
import asyncio
import json
import time
import discord
import requests
import io
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image

keep_alive()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print("TOKEN loaded:", bool(TOKEN))

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=["𒈓", "$"], intents=intents)
        
    async def on_ready(self):
        print(f'Hello ae t là {self.user}!')
        try:
            guild = discord.Object(id=1374705648234659972)
            synced = await self.tree.sync(guild=guild)
            print(f'Đã động bộ {len(synced)} lệnh vào guild {guild.id}')

        except Exception as e:
            print(f'Lỗi khi đồng bộ lệnh: {e}')

    async def on_message(self, message): # autoresponses
        if message.author == self.user:
            return
        if self.user in message.mentions:
            if 'ban' in message.content.lower():
                await message.channel.send(f'Something bad about to happen to me💀💀☠️☠️')
            else:
                await message.add_reaction('🇭')
                await message.add_reaction('🇮')
        if 'depchai ngu' in message.content.lower():
            await message.channel.send(f'Watch yo tung tung TOUNGE sahur <@{message.author.id}>🙏🏿')
        if message.content.lower().startswith('jigsaw'):
            await message.channel.send(f'Yo final challenge: let you bih go through yo phone!!!!')
            await message.channel.send(f'Oh hell na yo ás tweakin jigsaw😰😰')
        if message.content.lower() == 'phản động':
            await message.channel.send(f't-t sắp trở thành phản động<:adrenaline:1384034521497735251> \nSIÊU PHẢN ĐỘNG<:thosewhoknow:1384034450769449153> \nko sao đâu mọi người tôi đã hết phản động<:thienthan:1395022239354851348> \nbố đùa thôi<:adrianevil:1410063639641329788><:adrianevil:1410063639641329788> \nsiêu phản động cấp 3<:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778> \nxem đây, siêu phản động thần thánh<:thosewhoknew:1387391329683771402><:thosewhoknew:1387391329683771402> \nt đã đạt đc<:ruangu2:1430185957117919252> \nphản động vô cực<:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443>')
        if 'tick' == message.content.lower():
            await message.add_reaction('<a:acn_tickden:1413824083413696652>')
            await message.add_reaction('<a:acn_tickxanh:1414079548341096520>')
            await message.add_reaction('<a:acn_tickhong:1416068644349411420>')
            await message.add_reaction('<a:a_tickvang:1422566122305097830>')
        if message.content.lower().startswith('ai hỏi'):
            await message.channel.send('https://tenor.com/view/yes-hi-smells-good-done-cooking-stinky-gif-13460406')
        if 'degloved' in message.content.lower():
            await message.channel.send('https://media.discordapp.net/attachments/1421006466445348904/1449692117638058096/IMG_9643.jpeg?ex=693fd27e&is=693e80fe&hm=ec9aedb412f7517351f59c19b84eb5cc5ef50f0de338724ecf66e9217c858dde&=&format=webp&width=1020&height=930')
        if 'tôi yêu depchai' in message.content.lower():
            await message.channel.send('https://tenor.com/view/patrick-bateman-sigma-joker-lightning-god-patrick-bateman-sigma-edit-gif-11768805784532291762')
        if 'tôi ghét depchai' in message.content.lower():
            await message.channel.send('https://cdn.discordapp.com/attachments/1374705648796827671/1448973547044212829/image0.gif')
        await self.process_commands(message)

#cài đặt gì đấy idk
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
client = Client()
GUILD_ID = discord.Object(id=1374705648234659972)



#cho bot ko ping đc everyone
allowed = discord.AllowedMentions(
    everyone=False,
    roles=False,
    users=True
)

# function lọc từ cấm
tu_cam = ["nigga", "nigger", "penis", "hitler", "horny", "dildo", "pussy", "fuck", "dick", "bitch", "nude", "fatass", "porn", "boob", "cunt", "cumming", "asshole", "sperm", "cocaine", "cumshot", "nứng", "chịch", "buồi", "điếm", "cặc", "lồn", "parky", "namki", "trungki", 'tinh dịch', 'ấu dâm', 'hiếp dâm', 'thủ dâm', 'chó đẻ', 'ma túy', 'thuốc lắc', 'bắc kì', 'nam kì', 'trung kì', 'tinh trùng', 'bú vú', 'bú cu', 'cần sa']
tu_cam_rieng = ['đĩ', 'đỉ', 'đụ', 'dái', 'địt', 'iồn', 'anal', 'cum', 'ass', 'sex', 'sexual', 'cock', 'rape', 'pedo', 'pedophiles']

def badwords(word: str) -> bool:
    text = word.lower()

    for tu in tu_cam:
        if tu in text:
            return True
    for tu in tu_cam_rieng:
        if re.search(rf"\b{re.escape(tu)}\b", text):
            return True

    return False



# lệnh bằng prefix
@client.hybrid_command()
async def sync(ctx):
    try:
        synced = await client.tree.sync(guild=ctx.guild)
        await ctx.send(f'Đã động bộ {len(synced)} lệnh vào {ctx.guild}')

    except Exception as e:
        print(f'Lỗi khi đồng bộ lệnh: {e}')
        await ctx.send('M có cục sạc nào ko bot t chết rồi')



COLORS = { #copy trên zootube
    (0, 0, 0): "⬛",
    (0, 0, 255): "🟦",
    (255, 0, 0): "🟥",
    (255, 255, 0): "🟨",
    (190, 100, 80):  "🟫",
    (255, 165, 0): "🟧",
    (160, 140, 210): "🟪",
    (255, 255, 255): "⬜",
    (0, 255, 0): "🟩",
}

def euclidean_distance(c1, c2):
    r1, g1, b1 = c1
    r2, g2, b2 = c2
    d = ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5

    return d

def find_closest_emoji(color):
    c = sorted(list(COLORS), key=lambda k: euclidean_distance(color, k))
    return COLORS[c[0]]

def emojify_image(img, size=14):

    WIDTH, HEIGHT = (size, size)
    small_img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    emoji = ""
    small_img = small_img.load()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            emoji += find_closest_emoji(small_img[x, y])
        emoji += "\n"
    return emoji

@client.command()
async def emojify(ctx, url: str, size: int = 16):
    def get_emojified_image():
            r = requests.get(url, stream=True)
            image = Image.open(r.raw).convert("RGB")
            res = emojify_image(image, size)

            if size > 32:
                res = 'To quá 😰😰'
            return res
    result = get_emojified_image()
    await ctx.send(result)



# slash commands
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



# slash command thực sự dùng đc😂😂😂
@client.tree.command(name="free_fire_name_generator", description="Tạo tên fi fai", guild=GUILD_ID)
@app_commands.describe(chudau="Chọn chữ đầu",chucuoi="Chọn chữ cuối")
@app_commands.choices(
    chudau=[
       app_commands.Choice(name="꧁༺", value="canh"),
       app_commands.Choice(name="★彡", value="sao"),
       app_commands.Choice(name="ミᵒ°", value="bong"),
       app_commands.Choice(name="『", value="khung"),
       app_commands.Choice(name="۝ঔৣ✞", value="longden"),
       app_commands.Choice(name="㊪", value="trung"),
       app_commands.Choice(name="㋰", value="nhat"),
       app_commands.Choice(name="☭", value="bualiem"),
       app_commands.Choice(name="☯", value="amduong"),
       app_commands.Choice(name="❤", value="tim")], 
    chucuoi=[
       app_commands.Choice(name="༻꧂", value="canhc"),
       app_commands.Choice(name="ミ★", value="saoc"),
       app_commands.Choice(name="°ᵒ彡", value="bongc"),
       app_commands.Choice(name="』", value="khungc"),
       app_commands.Choice(name="✞ঔৣ۝", value="longdenc"),
       app_commands.Choice(name="㊪", value="trungc"),
       app_commands.Choice(name="㋰", value="nhatc"),
       app_commands.Choice(name="☭", value="bualiemc"),
       app_commands.Choice(name="☯", value="amduongc"),
       app_commands.Choice(name="❤", value="timc"), 
       app_commands.Choice(name="ᴾᴿᴼシ", value="pro"),
       app_commands.Choice(name="⁀ᶦᵈᵒᶫ", value="idol"),
       app_commands.Choice(name="︵❻❼", value="67")
    ])

async def ff(interaction: discord.Interaction, name: str, chudau: app_commands.Choice[str], chucuoi: app_commands.Choice[str]):
    if badwords(name):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    bold = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯" \
           "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕" \
           "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

    trans_table = str.maketrans(normal, bold)
    bold_name = name.translate(trans_table)

    await interaction.response.send_message(f'{chudau.name}{bold_name}{chucuoi.name}', allowed_mentions=allowed)



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



def is_custom_emoji(s: str) -> bool:
    return bool(re.fullmatch(r"<a?:\w+:\d+>", s))

@client.tree.command(name="chuvan", description="Sắp xếp một emoji thành chữ vạn", guild=GUILD_ID)
async def chuvan(interaction: discord.Interaction, emoji: str):
    if len(emoji.strip()) > 1:
        if is_custom_emoji(emoji) == False:
            await interaction.response.send_message("del phải emoji🤬🤬😡", ephemeral = True)
            return

    e = emoji
    t = '<:empty:1423996972431577240>'
    await interaction.response.send_message(f"{e}{t}{t}{e}{e}{e}{e}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{t}{t}{e}{t}{t}{t}\n{e}{e}{e}{e}{e}{e}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{t}{t}{t}{e}{t}{t}{e}\n{e}{e}{e}{e}{t}{t}{e}")



class CounterButton(discord.ui.View):
    def __init__(self, limit):
        super().__init__(timeout=None)  
        self.value = 0
        self.last_user = "Chưa có ai bấm <:ruabatngo:1420409581598806107>"
        self.limit = limit if limit > 0 else None

    @discord.ui.button(label="0", style=discord.ButtonStyle.blurple)
    async def count_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.last_user == interaction.user.display_name:
            await interaction.response.send_message(f"Không được bấm 2 lần liên tục <a:sussybaka:1422928147577307166>", ephemeral=True)
            return
        self.value += 1
        if self.limit is not None and self.value >= self.limit:
            button.disabled = True
            button.style = discord.ButtonStyle.red
            await interaction.response.edit_message(content=f"Đã đạt giới hạn {self.limit} lượt bấm🎉, **người chiến thắng là: ** <@{interaction.user.id}>", view=self)
            return
        self.last_user = interaction.user.display_name
        button.label = str(self.value)
        await interaction.response.edit_message(content=f"**Người bấm gần nhất:** {self.last_user}", view=self)

@client.tree.command(name="counter", description="Tạo một nút bấm đếm số", guild=GUILD_ID)
@app_commands.describe(limit="Số lần bấm tối đa của nút (nhập 0 nếu muốn không giới hạn)")
async def counter(interaction: discord.Interaction, limit: int):
    view = CounterButton(limit)
    await interaction.response.send_message(content="**Bấm vào nút để tăng số!**", view=view)



@client.tree.command(name="videomoi", description="Xem video mới nhất của Depchai", guild=GUILD_ID)
async def tictac(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    url = "https://tiktok-scraper7.p.rapidapi.com/user/posts"
    querystring = {"user_id":"7146137203961070618","count":"10","cursor":"0"}
    headers = {
        "x-rapidapi-key": "c52e6c1eabmshfc53df3be70d170p15736ejsn41970f974d03",
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    video = data['data']['videos'][0]['play']

    r = requests.get(video)
    bytes_mp4 = io.BytesIO(r.content)
    if video == -1:
        await interaction.followup.send("Không tìm thấy video nào, có thể depchai đã chết😰😰")
        return 
    await interaction.followup.send(f"Video mới nhất của Depchai:\n", file=discord.File(bytes_mp4, filename="video.mp4"))




@client.tree.command(name="nitro_generator", description="Tạo một link Discord gift ngẫu nhiên và cầu nguyện rằng nó là nitro thật", guild=GUILD_ID)
async def nitri(interaction: discord.Interaction):
    chuthuong = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chuhoa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    so = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    code = ''
    for i in range (16):
        ar = random.randint(1, 3)
        if ar == 1:
            choice = random.choice(chuthuong)
        elif ar == 2:
            choice = random.choice(chuhoa)
        elif ar == 3:
            choice = random.choice(so)
        code = (f"{code}{choice}")
    await interaction.response.send_message(f"https://discord.gift/{code}")



@client.tree.command(name="death_date", description="Dự đoán ngày m chết☠️☠️ (j4f)", guild=GUILD_ID)
async def death(interaction: discord.Interaction, ngay_sinh: int, thang_sinh: int, nam_sinh: int):
    if (ngay_sinh <= 0 or ngay_sinh > 31):
        await interaction.response.send_message(f"Làm del gì có ngày {ngay_sinh}😂😂<:dumbahh:1391405354687926273>", ephemeral = True)
        return
    elif (thang_sinh <= 0 or thang_sinh > 12):
        await interaction.response.send_message(f"Làm del gì có tháng {thang_sinh}😂😂<:dumbahh:1391405354687926273>", ephemeral = True)
        return
    localtime = time.localtime(time.time())
    nam_nay = localtime.tm_year
    thang_nay = localtime.tm_mon
    ngay_nay = localtime.tm_mday
    if nam_sinh > nam_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh > thang_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh == thang_nay and ngay_sinh > ngay_nay:
        await interaction.response.send_message("Anh bạn sinh ở ngày sinh nhật😂😂😂", ephemeral = True)
        return
    
    nam_chet = random.randint(1, 93)
    thang_chet = random.randint(1, 12)
    if thang_chet in [1,3,5,7,8,10,12]:
        ngay_chet = random.randint(1, 31)
    elif thang_chet in [4,6,9,11]:
        ngay_chet = random.randint(1, 30)
    elif thang_chet == 2:
        ngay_chet = random.randint(1, 28)
    
    dt = datetime(nam_sinh + nam_chet, thang_chet, ngay_chet, 6, 7, 41)
    unix_time = int(dt.timestamp())
    
    ly_do = ['tuổi già', 'tai nạn', 'ung thư', 'bệnh tật', 'chết đói', 'chết đuối', 'bị ám sát', 'bị đầu độc', 'bị giết', '44']

    await interaction.response.send_message(f"M sẽ chết vào: {ngay_chet}/{thang_chet}/{nam_sinh + nam_chet} (<t:{unix_time}:R>) ☠️☠️\nVới lý do: {random.choice(ly_do)} <:thosewhodontknow:1393572894558126121>\nHưởng dương {nam_chet} tuổi🍚🍚🍚")



@client.tree.command(name="bio_generator", description="Tạo một bio mà sẽ del ai dùng", guild=GUILD_ID)
@app_commands.describe(acc="Acc chính hay phụ", doi="Ai hỏi thì m trả lời như nào", vansu="Vạn sự như nào", ghe="Có gh* chưa")
@app_commands.choices(
    acc=[
       app_commands.Choice(name="🔰Acc chính chủ🔰", value="chinh"),
       app_commands.Choice(name="🔰Acc clone🔰", value="clone")], 
    doi=[
       app_commands.Choice(name="Đối sao đáp vậy👌", value="doidap"),
       app_commands.Choice(name="Hỏi đâu mà đáp👌", value="aihoi")],
    vansu=[
       app_commands.Choice(name="🪷Vạn sự tùy duyên🪷", value="duyen"),
       app_commands.Choice(name="☠️Vạn sự tùy TAO☠️", value="tao"),
       app_commands.Choice(name="🪷Vạn sự như chó🪷", value="cho")],
    ghe=[
       app_commands.Choice(name="💌Chưa có chủ💌", value="chua"),
       app_commands.Choice(name="💌Đã có chủ💌", value="roi")
    ])
async def bio(interaction: discord.Interaction, acc: app_commands.Choice[str], doi: app_commands.Choice[str], sothich: str, vansu: app_commands.Choice[str], ghe: app_commands.Choice[str]):
    if badwords(sothich):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    await interaction.response.send_message(f"{acc.name}\n🍚👕🌾💵\n❤️Mê {sothich}❤️\n{vansu.name}\n{ghe.name}\n🤜Đến là đón, đụng là chạm🤛", allowed_mentions=allowed)
# 🔰Acc chính chủ🔰
# 🍚👕🌾💵
# Đối sao đáp vậy👌
# ❤️Mê xe độ❤️
# 🪷Vạn sự tùy duyên🪷
# 💌Chưa có chủ💌
# 🤜Đến là đón, đụng là chạm🤛



# https://www.gstatic.com/android/keyboard/emojikitchen/20201001/u1f923/u1f923_u1f422.png
emoji_ranges = [
    (0x1F600, 0x1F64F),  # Mặt cảm xúc
    (0x1F300, 0x1F5FF),  # Biểu tượng, thiên nhiên
    (0x1F680, 0x1F6FF),  # Giao thông
    (0x1F900, 0x1F9FF),  # Cử chỉ, đồ vật
    (0x1FA70, 0x1FAFF),  # Biểu tượng mở rộng
    (0x1F300, 0x1F5FF),
]

@client.tree.command(name="turtle_emoji", description="Lấy emoji rùa ngẫu nhiên từ emoji kitchen", guild=GUILD_ID)
async def turtle_emoji(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    turtle_unicode = "1f422"
    url = None
    chosen_unicode = None

    async with aiohttp.ClientSession() as session:
        while (6 < 7):  
            start, end = random.choice(emoji_ranges)
            emoji_code = hex(random.randint(start, end))[2:]
            url = f"https://www.gstatic.com/android/keyboard/emojikitchen/20201001/u{emoji_code}/u{emoji_code}_u{turtle_unicode}.png"
            async with session.get(url) as response:
                if response.status != 404:
                    chosen_unicode = emoji_code
                    break
                
    await interaction.followup.send(url)



teencode_map = {
    "a": "4", "á": "4'", "à": "4`", "ạ": "4.", "ả": "4?", "ã": "4~",
    "ă": "4", "ắ": "4'", "ằ": "4`", "ẳ": "4?", "ẵ": "4~", "ặ": "4.",
    "â": "4", "ấ": "4'", "ầ": "4`", "ẩ": "4?", "ẫ": "4~", "ậ": "4.",
    "b": "|3", "c": "c", "d": "])", "đ": "+)", "e": "3",
    "ê": "3^", "g": "g", "h": "k", 
    "i": "j", "í": "j'", "ì": "j`", "ỉ": "j?", "ĩ": "j~", "ị": "j.", 
    "k": "]<", "l": "1", "m": "m", "n": "π", 
    "o": "0", "ó": "0'", "ò": "0`", "ỏ": "0?", "õ": "0~", "ọ": "0.", 
    "ô": "0", "ố": "0'", "ồ": "0`", "ổ": "0?", "ỗ": "0~", "ộ": "0.", 
    "ơ": "0", "ớ": "0'", "ờ": "0`", "ở": "0?", "ỡ": "0~", "ợ": "0.", 
    "p": "p", "q": "⃀|", "r": "r", "s": "5", "t": "t", 
    "u": "u", "ú": "u", "ù": "u", "ủ": "u", "ũ": "u", "ụ": "u", 
    "ư": "u", "ứ": "u", "ừ": "u", "ử": "u", "ữ": "u", "ự": "u",
    "v": "√", "x": "><", "y": "7"
}

# Hàm chuyển đổi sang teencode
def to_teencode(text: str) -> str:
    result = ""
    for ch in text:
        low = ch.lower()
        if low in teencode_map:
            converted = teencode_map[low]
            # Giữ nguyên hoa/thường
            result += converted.upper() if ch.isupper() else converted
        else:
            result += ch
    return result

@client.tree.command(name="teencode", description="Chuyển đổi Tiếng Việt sang teencode", guild=GUILD_ID)
async def teencode(interaction: discord.Interaction, text: str):
    if badwords(text):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    converted = to_teencode(text)
    await interaction.response.send_message(f'{converted}', allowed_mentions=allowed)



tieqviet_map = {
    'kh':'x', 'ch':'k', 'q':'k', 'ch':'c', 'tr':'c', 'd':'z', 'gi':'z', 'r':'z',
    'gi':'zi', 'gí':'zí', 'gì':'zì', 'gỉ':'zỉ', 'gĩ':'zĩ', 'gị':'zị', 
    'đ':'d', 'ph':'f', 'ng':'q', 'ngh':'q', 'gh':'g', 'th':'w', "nh":"n'"
}
def to_tieqviet(text: str) -> str:
    result = ""
    keys = sorted(tieqviet_map.keys(), key=len, reverse=True)
    for i in range(len(text)):
        matched = False
        
        for k in keys:
            segment = text[i:i+len(k)]
            
            if segment.lower() == k:
                converted = tieqviet_map[k]
                # giữ nguyên chữ hoa
                if segment.isupper():
                    converted = converted.upper()
                elif segment[0].isupper():
                    converted = converted.capitalize()

                result += converted
                i += len(k)
                matched = True
                break

        if not matched:
            result += text[i]
            i += 1
    return result

@client.tree.command(name="tieq_viet", description="Chuyển đổi Tiếng Việt truyền thống sang Tiếq Việt", guild=GUILD_ID)
async def tieqviet(interaction: discord.Interaction, text: str):
    if badwords(text):
        await interaction.response.send_message('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    tieqviet = to_tieqviet(text)
    await interaction.response.send_message(f'{tieqviet}', allowed_mentions=allowed)



def level(id: int): 
    level = requests.get(f"https://gdbrowser.com/{id}")
    soup = BeautifulSoup(level.text, "html.parser")
    name = soup.find("span", attrs={"class":"pre"})
    author1 = soup.find("a", attrs={"class":"linkButton"})
    chiso = soup.find_all("h1", attrs={"class":"valign inline smaller spaced"})
    img = soup.find("img", {"class": "help"}) 
    desc = soup.find("p", attrs={"class":"pre"})
    songname = soup.find('h1', attrs={'class':'pre slightlySmaller'})
    songauthor1 = soup.find('h2', attrs={'class':'pre smaller'})
    top = soup.find('h1', attrs={'class': 'smaller inline demonList'})

    values = []
    for tag in chiso:
        text = tag.text.strip()
        values.append(text)

    downloads = values[0]
    likes = values[1]
    length = values[2]
    icon = urljoin("https://gdbrowser.com/", img["src"])
    author = author1.text.strip().replace("By ","")
    songauthor = songauthor1.text.strip().replace("By: ", "")
    if songauthor in songname.text:
        song = songname.text.strip()
    else:
        song = f'{songname.text.strip()} - {songauthor}'

    if not '[[DEMONLIST]]' in top.text:
        embed = discord.Embed(title=name.text.strip(), description=f"🛠️ Tác giả: {author}\n⤵️ Downloads: {downloads}\n👍 Likes: {likes}\n🕓 Độ dài: {length}\n🏆 Hạng: {top.text}\n🎵 Nhạc: {song}", color=discord.Color.yellow())
    else:
        embed = discord.Embed(title=name.text.strip(), description=f"🛠️ Tác giả: {author}\n⤵️ Downloads: {downloads}\n👍 Likes: {likes}\n🕓 Độ dài: {length}\n🎵 Nhạc: {song}", color=discord.Color.yellow())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Mô tả", value=desc.text.strip(), inline=False)
    embed.set_image(url=f'https://levelthumbs.prevter.me/thumbnail/{id}')
    return embed

def searchlvl(query:str, count: int):
    search = requests.get(f"https://gdbrowser.com/api/search/{query.replace(" ", "%20")}")
    data = search.json()
    if data == -1:
        return None
    if count > len(data):
        return None
    id = data[count]["id"]
    return id

class nextlvl(discord.ui.View):
    def __init__(self, query: str, thutu: int):
        super().__init__()
        self.thutu = thutu
        self.query = query
    @discord.ui.button(label="", style=discord.ButtonStyle.blurple, emoji='⬅️')
    async def back(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.thutu -= 1
        if self.thutu < 0:
            await interaction.followup.send('Đang ở đầu trang🥱', ephemeral = True)
            self.thutu = 0
            return
        h = searchlvl(self.query, self.thutu)
        await interaction.message.edit(embed=level(h), view = self)
    @discord.ui.button(label="", style=discord.ButtonStyle.blurple, emoji='➡️')
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        self.thutu += 1
        h = searchlvl(self.query, self.thutu)
        if h == None:
            await interaction.followup.send('Đến cuối trang rồi🥱', ephemeral = True)
            self.thutu -= 1
            return
        await interaction.message.edit(embed=level(h), view = self)

@client.tree.command(name="gdbrowser", description="Tìm thông tin của một level trong Geometry Dash", guild=GUILD_ID)
async def gdbrowser(interaction: discord.Interaction, query: str):
    await interaction.response.defer(thinking=True)
    id = searchlvl(query, 0)
    if id == None:
        await interaction.followup.send('Không tìm thấy kết quả🙄')
    await interaction.followup.send(embed=level(id), view = nextlvl(query, 0))



@client.tree.command(name="dictionary", description="Tìm định nghĩa của một từ tiếng Anh trên Cambridge Dictionary", guild=GUILD_ID)
async def dictionary(interaction: discord.Interaction, word: str):
    await interaction.response.defer(thinking=True)
    if badwords(word):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    r = requests.get(
        f"https://dictionary.cambridge.org/dictionary/english/{word.replace(" ", "%20")}",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(r.text, "html.parser")

    block = soup.find("div", class_="def ddef_d db")
    if block:
        definition = block.get_text(separator=" ", strip=True)
        await interaction.followup.send(f'# {word.capitalize()}\n{definition.capitalize()}')
    else:
        await interaction.followup.send("Không tìm thấy kết quả🙄")



@client.tree.command(name="tudien", description="Tìm định nghĩa của một từ tiếng Việt trên tratu.soha", guild=GUILD_ID)
async def tudien(interaction: discord.Interaction, word: str):
    await interaction.response.defer(thinking=True)
    if badwords(word):
        await interaction.followup.send('nuh uh<:ruachemieng:1440560108676321320>', ephemeral=True)
        return
    r = requests.get(
        f"http://tratu.soha.vn/dict/vn_vn/{word.replace(" ", "%20")}",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    soup = BeautifulSoup(r.text, "html.parser")
    block = soup.find_all("span", class_="mw-headline")
    if block:
        for d in block:
            parent = d.find_parent("h5")
            if parent:   
                dinhnghia = d.text[1:] 
                await interaction.followup.send(f'# {word.capitalize()}\n{dinhnghia.capitalize()}')
                return
    else:
        await interaction.followup.send("Không tìm thấy kết quả🙄")
    


@client.tree.command(name="wordle", description="Chơi Wordle với từ ngẫu nhiên", guild=GUILD_ID)
async def wordle(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    while(6 < 7):
        year = random.randint(2021, 2025)
        mon = random.randint(1, 12)
        day = random.randint(1, 31)
        r = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{year}-{mon:02d}-{day:02d}.json")
        try:
            data = r.json()
        except:
            continue

        if data.get("status") == "ERROR":
            continue

        ans = data["solution"]
        break

    def check(msg):
        return msg.author.id == interaction.user.id and msg.channel.id == interaction.channel.id
    
    await interaction.followup.send(f"⬜⬜⬜⬜⬜")
    await interaction.channel.send('Đoán xem <:thosewhodontknow:1393572894558126121>')
    tries = 6
    while tries > 0:
        msg = await client.wait_for("message", timeout=None, check=check)
        if len(msg.content) != 5:
            if 'sotp' in msg.content.lower() or 'cút' in msg.content.lower() or 'chịu' in msg.content.lower():
                await interaction.channel.send(f'Okiiiii😁😁\nĐáp án là: {ans}')
                break
            else:
                await interaction.channel.send('Không đủ 5 kí tự <:packgod:1384036888402333726>')
                continue
            
        response = ['⬜'] * 5

        # check từng ký tự
        for i in range(5):
            if msg.content[i].lower() == ans[i]:
                response[i] = '🟩'
            elif msg.content[i].lower() in ans:
                response[i] = '🟨'

        result = ''.join(response)
        await interaction.channel.send(result)

        if result == '🟩🟩🟩🟩🟩':
            await interaction.channel.send('Ayooooo đúng rồi😹😹😹')
            break

        tries -= 1

    if tries == 0:
        await interaction.channel.send(f"Mất hết lượt<:ruachemieng:1440560108676321320>\nĐáp án là: {ans}")



@client.tree.command(name="guess_that_flag", description="Đoán lá cờ", guild=GUILD_ID)
async def flag(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)
    countries = {
    'vn': 'Vietnam', 
    'ad': 'Andorra', 
    'ae': 'United Arab Emirates', 
    'af': 'Afghanistan', 
    'ag': 'Antigua and Barbuda', 
    'al': 'Albania', 
    'am': 'Armenia', 
    'ao': 'Angola', 
    'ar': 'Argentina', 
    'at': 'Austria', 
    'au': 'Australia', 
    'az': 'Azerbaijan', 
    'ba': 'Bosnia and Herzegovina', 
    'bb': 'Barbados', 
    'bd': 'Bangladesh', 
    'be': 'Belgium', 
    'bf': 'Burkina Faso', 
    'bg': 'Bulgaria', 
    'bh': 'Bahrain', 
    'bi': 'Burundi', 
    'bj': 'Benin', 
    'bn': 'Brunei', #mọe dài quá del sửa hết đc
    'bo': 'Bolivia', 'br': 'Brazil', 'bs': 'Bahamas', 'bt': 'Bhutan', 'bw': 'Botswana', 'by': 'Belarus', 'bz': 'Belize', 'ca': 'Canada', 'cd': 'DR Congo', 'cf': 'Central African Republic', 'cg': 'Republic of the Congo', 'ch': 'Switzerland', 'ci': "Côte d'Ivoire (Ivory Coast)", 'cl': 'Chile', 'cm': 'Cameroon', 'cn': 'China', 'co': 'Colombia', 'cr': 'Costa Rica', 'cu': 'Cuba', 'cv': 'Cape Verde', 'cy': 'Cyprus', 'cz': 'Czechia', 'de': 'Germany', 'dj': 'Djibouti', 'dk': 'Denmark', 'dm': 'Dominica', 'do': 'Dominican Republic', 'dz': 'Algeria', 'ec': 'Ecuador', 'ee': 'Estonia', 'eg': 'Egypt', 'er': 'Eritrea', 'es': 'Spain', 'et': 'Ethiopia', 'fi': 'Finland', 'fj': 'Fiji', 'fm': 'Micronesia', 'fr': 'France', 'ga': 'Gabon', 'gb': 'United Kingdom', 'gd': 'Grenada', 'ge': 'Georgia', 'gh': 'Ghana', 'gl': 'Greenland', 'gm': 'Gambia', 'gn': 'Guinea', 'gq': 'Equatorial Guinea', 'gr': 'Greece', 'gt': 'Guatemala', 'gw': 'Guinea-Bissau', 'gy': 'Guyana', 'hk': 'Hong Kong', 'hn': 'Honduras', 'hr': 'Croatia', 'ht': 'Haiti', 'hu': 'Hungary', 'id': 'Indonesia', 'ie': 'Ireland', 'il': 'Israel', 'in': 'India', 'iq': 'Iraq', 'ir': 'Iran', 'is': 'Iceland', 'it': 'Italy', 'jm': 'Jamaica', 'jo': 'Jordan', 'jp': 'Japan', 'ke': 'Kenya', 'kg': 'Kyrgyzstan', 'kh': 'Cambodia', 'ki': 'Kiribati', 'km': 'Comoros', 'kn': 'Saint Kitts and Nevis', 'kp': 'North Korea', 'kr': 'South Korea', 'kw': 'Kuwait', 'kz': 'Kazakhstan', 'la': 'Laos', 'lb': 'Lebanon', 'lc': 'Saint Lucia', 'li': 'Liechtenstein', 'lk': 'Sri Lanka', 'lr': 'Liberia', 'ls': 'Lesotho', 'lt': 'Lithuania', 'lu': 'Luxembourg', 'lv': 'Latvia', 'ly': 'Libya', 'ma': 'Morocco', 'mc': 'Monaco', 'md': 'Moldova', 'me': 'Montenegro', 'mf': 'Saint Martin', 'mg': 'Madagascar', 'mh': 'Marshall Islands', 'mk': 'North Macedonia', 'ml': 'Mali', 'mm': 'Myanmar', 'mn': 'Mongolia', 'mo': 'Macau', 'mr': 'Mauritania', 'mt': 'Malta', 'mu': 'Mauritius', 'mv': 'Maldives', 'mw': 'Malawi', 'mx': 'Mexico', 'my': 'Malaysia', 'mz': 'Mozambique', 'na': 'Namibia', 'ne': 'Niger', 'ng': 'Nigeria', 'ni': 'Nicaragua', 'nl': 'Netherlands', 'no': 'Norway', 'np': 'Nepal', 'nr': 'Nauru', 'nz': 'New Zealand', 'om': 'Oman', 'pa': 'Panama', 'pe': 'Peru', 'pf': 'French Polynesia', 'pg': 'Papua New Guinea', 'ph': 'Philippines', 'pk': 'Pakistan', 'pl': 'Poland', 'pm': 'Saint Pierre and Miquelon', 'pr': 'Puerto Rico', 'ps': 'Palestine', 'pt': 'Portugal', 'pw': 'Palau', 'py': 'Paraguay', 'qa': 'Qatar', 'ro': 'Romania', 'rs': 'Serbia', 'ru': 'Russia', 'rw': 'Rwanda', 'sa': 'Saudi Arabia', 'sb': 'Solomon Islands', 'sc': 'Seychelles', 'sd': 'Sudan', 'se': 'Sweden', 'sg': 'Singapore', 'si': 'Slovenia', 'sk': 'Slovakia', 'sl': 'Sierra Leone', 'sm': 'San Marino', 'sn': 'Senegal', 'so': 'Somalia', 'sr': 'Suriname', 'ss': 'South Sudan', 'st': 'São Tomé and Príncipe', 'sv': 'El Salvador', 'sy': 'Syria', 'sz': 'Eswatini', 'td': 'Chad', 'tg': 'Togo', 'th': 'Thailand', 'tj': 'Tajikistan', 'tl': 'Timor-Leste', 'tm': 'Turkmenistan', 'tn': 'Tunisia', 'to': 'Tonga', 'tr': 'Turkey', 'tt': 'Trinidad and Tobago', 'tv': 'Tuvalu', 'tw': 'Taiwan', 'tz': 'Tanzania', 'ua': 'Ukraine', 'ug': 'Uganda', 'us': 'United States', 'uy': 'Uruguay', 'uz': 'Uzbekistan', 'va': 'Vatican City', 'vc': 'Saint Vincent and the Grenadines', 've': 'Venezuela', 'vu': 'Vanuatu', 'ws': 'Samoa', 'xk': 'Kosovo', 'ye': 'Yemen', 'za': 'South Africa', 
    'zm': 'Zambia',
    'zw': 'Zimbabwe'
    }
    def check(msg):
        return msg.author.id == interaction.user.id and msg.channel.id == interaction.channel.id
    correct = 0
    wrong = 0
    i = 0
    for i in range(5):
        code, ans = random.choice(list(countries.items()))
        flag = f"https://flagcdn.com/w1280/{code}.png"
        r = requests.get(flag)
        flag_img = io.BytesIO(r.content)
        if i == 0:
            await interaction.followup.send('Đây là cờ nước gì?', file=discord.File(flag_img, filename='flag.png'))
        else:
            await interaction.channel.send('Đây là cờ nước gì?', file=discord.File(flag_img, filename='flag.png'))            

        msg = await client.wait_for("message", timeout=None, check=check)
        if msg.content.lower().strip() == ans.lower():
            await interaction.channel.send('Chính xác <a:a_tickvang:1422566122305097830>')
            correct += 1
        elif msg.content.lower().strip() == 'sotp' or msg.content.lower().strip() == 'chịu' or msg.content.lower().strip() == 'cút':
            await interaction.channel.send(f'Okiiiii😁😁 đáp án là: {ans}')
            return
        else:
            await interaction.channel.send(f'Sai <:cuoiteghe:1432707173892231288><:cuoiteghe:1432707173892231288><:cuoiteghe:1432707173892231288> đáp án là: {ans}')
            wrong += 1

    await interaction.channel.send(f'M đã đoán đúng {correct} lần và sai {wrong} lần <:votay:1421701691316895854><:votay:1421701691316895854><:votay:1421701691316895854>')



@client.tree.command(name="tiktok_mp4", description="Gửi video Tiktok dưới dạng video", guild=GUILD_ID)
async def tictac_mp4(interaction: discord.Interaction, link: str):
    await interaction.response.defer()

    url = "https://tiktok-scraper2.p.rapidapi.com/video/no_watermark"
    querystring = {"video_url":link}
    headers = {
        "x-rapidapi-key": "c52e6c1eabmshfc53df3be70d170p15736ejsn41970f974d03",
        "x-rapidapi-host": "tiktok-scraper2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    if data:
        video = data['no_watermark']
        if video:
            r = requests.get(video)
        else:
            r = requests.get(data)
        bytes_mp4 = io.BytesIO(r.content)
        await interaction.followup.send(file=discord.File(bytes_mp4, filename='tiktok.mp4'))
    else:
        await interaction.followup.send('Del tìm thấy video nào🙄')



import time
print("🕒 Đang chờ 10 giây trước khi khởi động bot...")
time.sleep(10)

try:
    client.run(TOKEN)
    print("mẹ ơi con làm được rồi🥹🥹")
except Exception as e:
    print("Lỗi khi chạy bot:", e)