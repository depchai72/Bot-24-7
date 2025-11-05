import os
import random
import re
import aiohttp
import asyncio
import json
import time
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from keep_alive import keep_alive
from datetime import datetime, timedelta

keep_alive()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print("TOKEN loaded:", bool(TOKEN))

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

    async def on_message(self, message): # autoresponses
        if message.author == self.user:
            return
        if self.user in message.mentions:
            if 'ban' in message.content.lower():
               await message.channel.send(f'Something bad about to happen to me💀💀☠️☠️')
               return
            await message.add_reaction('🇭')
            await message.add_reaction('🇮')
        if 'depchai ngu' in message.content.lower():
            await message.channel.send(f'Watch yo tone lil blud🙏🏿')
        if message.content.startswith('jigsaw'):
            await message.channel.send(f'Yo final challenge: let you bih go through yo phone!!!!')
            await message.channel.send(f'Oh hell na yo ás tweakin jigsaw😰😰')
        if message.content.lower() == 'phản động':
            await message.channel.send(f't-t sắp trở thành phản động<:adrenaline:1384034521497735251> \nSIÊU PHẢN ĐỘNG<:thosewhoknow:1384034450769449153> \nko sao đâu mọi người tôi đã hết phản động<:thienthan:1395022239354851348> \nbố đùa thôi<:adrianevil:1410063639641329788><:adrianevil:1410063639641329788> \nsiêu phản động cấp 3<:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778><:thesewhoknow:1391269951977033778> \nxem đây, siêu phản động thần thánh<:thosewhoknew:1387391329683771402><:thosewhoknew:1387391329683771402> \nt đã đạt đc<:ruangu2:1430185957117919252> \nphản động vô cực<:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443><:trollfacelv999:1384893983850893443>')
        if 'tick' == message.content.lower():
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
    if badwords(name) == True:
        await interaction.message.response.send_message('Kid cố nói từ cấm😂😂😂', ephemeral = True)
        return
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    bold = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯" \
           "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕" \
           "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

    trans_table = str.maketrans(normal, bold)
    bold_name = name.translate(trans_table)

    await interaction.response.send_message(f'{chudau.name}{bold_name}{chucuoi.name}')



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



def is_unicode_emoji(s: str) -> bool: # function kiểm tra xem input phải emoji ko
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  
        "\U0001F300-\U0001F5FF"  
        "\U0001F680-\U0001F6FF"  
        "\U0001F1E0-\U0001F1FF"  
        "\U00002700-\U000027BF"  
        "\U000024C2-\U0001F251"  
        "]+"
    )
    return bool(emoji_pattern.fullmatch(s))
def is_custom_emoji(s: str) -> bool:
    return bool(re.fullmatch(r"<a?:\w+:\d+>", s))

@client.tree.command(name="chuvan", description="Sắp xếp một emoji thành chữ vạn", guild=GUILD_ID)
async def chuvan(interaction: discord.Interaction, emoji: str):
    if not is_custom_emoji(emoji) or is_unicode_emoji(emoji):
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

    username = "idtiktok"
    url = "https://tiktok-api23.p.rapidapi.com/user/posts"
    params = {"unique_id": username, "count": "1"}
    headers = {
        "x-rapidapi-key": "c52e6c1eabmshfc53df3be70d170p15736ejsn41970f974d03",
        "x-rapidapi-host": "tiktok-api23.p.rapidapi.com"
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=params, timeout=10) as resp:
                text = await resp.text()
                # Nếu phản hồi quá dài, chỉ in trước 1000 ký tự để log
                print(text[:1000], "..." if len(text) > 1000 else "")
                data = json.loads(text)

        # Tìm danh sách video (API này có thể đổi key)
        videos = (
            data.get("data", {}).get("videos")
            or data.get("data", {}).get("aweme_list")
            or data.get("videos")
            or data.get("aweme_list")
        )

        if not videos:
            await interaction.followup.send("Không tìm thấy video nào, có thể Depchai đã chết 😰😰")
            return

        video = videos[0]
        video_url = (
            video.get("play")
            or video.get("video_url")
            or video.get("video", {}).get("play_addr", {}).get("url_list", ["Không có video"])[0]
        )
        caption = video.get("title") or video.get("desc") or "(không có caption)"

        await interaction.followup.send(f"**Video mới nhất của Depchai:**\n{caption}\n{video_url}")

    except asyncio.TimeoutError:
        await interaction.followup.send("⚠️ Hết thời gian chờ phản hồi từ API TikTok")
    except Exception as e:
        await interaction.followup.send(f"⚠️ Lỗi khi lấy video: `{type(e).__name__}: {e}`")



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
        await interaction.response.send_message("Anh bạn sinh ở tương lai😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh > thang_nay:
        await interaction.response.send_message("Anh bạn sinh ở tương lai😂😂😂", ephemeral = True)
        return
    elif nam_sinh == nam_nay and thang_sinh == thang_nay and ngay_sinh > ngay_nay:
        await interaction.response.send_message("Anh bạn sinh ở tương lai😂😂😂", ephemeral = True)
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
@app_commands.describe(acc="Acc chính hay phụ", doi="Ai hỏi thì m trả lời như nào", vansu="Vạn sự như nào", ny="Có gh* chưa")
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
    if badwords(sothich) == True:
        await interaction.message.response.send_message('Kid cố nói từ cấm😂😂😂', ephemeral = True)
        return
    await interaction.response.send_message(f"{acc.name}\n🍚👕🌾💵\n❤️Mê {sothich}❤️\n{vansu.name}\n{ghe.name}\n🤜Đến là đón, đụng là chạm🤛")
# 🔰Acc chính chủ🔰
# 🍚👕🌾💵
# Đối sao đáp vậy👌
# ❤️Mê xe độ❤️
# 🪷Vạn sự tùy duyên🪷
# 💌Chưa có chủ💌
# 🤜Đến là đón, đụng là chạm🤛



import time
print("🕒 Đang chờ 10 giây trước khi khởi động bot...")
time.sleep(10)

try:
    client.run(TOKEN)
    print("mẹ ơi con làm được rồi🥹🥹")
except Exception as e:

    print("Lỗi khi chạy bot:", e)
