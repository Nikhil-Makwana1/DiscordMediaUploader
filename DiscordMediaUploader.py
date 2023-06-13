import datetime
import os
import shutil
import discord
from discord.ext import commands
import config

LARGE_MEDIA = ""
CONTENT_FOLDER = ""
LOG_FILE = ""
COMMAND_EXECUTED = False

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


def initialize():
    global CONTENT_FOLDER, LOG_FILE, LARGE_MEDIA

    current_dir = os.getcwd()
    content_dir = "media"
    large_dir = "large"

    CONTENT_FOLDER = os.path.join(current_dir, content_dir)
    LARGE_MEDIA = os.path.join(current_dir, large_dir)
    LOG_FILE = os.path.join(current_dir, "logs.log")

    prerequisite()


def prerequisite():
    if not os.path.exists(CONTENT_FOLDER):
        os.makedirs(CONTENT_FOLDER)

    if not os.path.exists(LARGE_MEDIA):
        os.makedirs(LARGE_MEDIA)

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as file:
            file.write("----------------------------------------\n")
            file.write("        Time           Size (MB)    Name\n")
            file.write("----------------------------------------\n")


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print("To start uploading, type !kaboom in the Discord channel")


@bot.command()
async def kaboom(ctx):
    global COMMAND_EXECUTED

    if not COMMAND_EXECUTED:
        COMMAND_EXECUTED = True
        channel = ctx.channel

        with open(LOG_FILE, 'r') as file:
            logs = file.read()

        with open(LOG_FILE, 'a') as file:
            for filename in os.listdir(CONTENT_FOLDER):

                file_path = os.path.join(CONTENT_FOLDER, filename)

                if os.path.isfile(file_path) and filename not in logs:
                    try:
                        filesize = os.path.getsize(file_path) / (1024 * 1024)
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        await channel.send(file=discord.File(file_path, filename))

                        file.write(f"{current_time} {filesize:10.2f}    {filename}\n")
                        print(f"Uploaded: {current_time} {filesize:6.2f} MB  {filename}")

                    except Exception as e:
                        large_file_path = os.path.join(LARGE_MEDIA, filename)
                        shutil.move(file_path, large_file_path)

                        if "Payload Too Large" in str(e):
                            print(f"Too large: {filename}")

        print("\nNo Remaining Files")


def logo():
    line1 = "·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      • ▌ ▄ ·. ▄▄▄ .·▄▄▄▄  ▪   ▄▄▄·      ▐▄▄▄▄▄▄ .▄▄▄▄▄"
    line2 = "██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ·██ ▐███▪▀▄.▀·██▪ ██ ██ ▐█ ▀█       ·██▀▄.▀·•██  "
    line3 = "▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▐█ ▌▐▌▐█·▐▀▀▪▄▐█· ▐█▌▐█·▄█▀▀█     ▪▄ ██▐▀▀▪▄ ▐█.▪"
    line4 = "██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ██ ██▌▐█▌▐█▄▄▌██. ██ ▐█▌▐█ ▪▐▌    ▐▌▐█▌▐█▄▄▌ ▐█▌·"
    line5 = "▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ▀▀  █▪▀▀▀ ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀  ▀      ▀▀▀• ▀▀▀  ▀▀▀ "
    information = "    ⭐️ Star the Repository  |  https://github.com/Nikhil-Makwana1/DiscordMediaUploader ⭐️    "

    console_width = shutil.get_terminal_size().columns
    center_offset = (console_width - len(line1)) // 2
    print()
    print(" " * center_offset)
    print(" " * center_offset + line1)
    print(" " * center_offset + line2)
    print(" " * center_offset + line3)
    print(" " * center_offset + line4)
    print(" " * center_offset + line5)
    print()
    print(" " * center_offset + information)
    print()


if __name__ == '__main__':
    logo()
    initialize()
    TOKEN = config.TOKEN

    if not TOKEN:
        TOKEN = input("Discord bot token: ")

    print("Loaded Config: ")
    print(f"Token: {TOKEN}\n")

    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("Invalid token or bot lacks permissions.")
