import os
from threading import Thread
from flask import Flask
import discord
from discord.ext import commands

# --- [ส่วน Keep Alive สำหรับ Render + UptimeRobot] ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is online and active 24/7!"

def run_web():
    # Render จะส่งค่า PORT มาทาง Environment Variable ต้องรับให้ตรง
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# --- [เรียกใช้งาน Keep Alive ก่อนรันบอท] ---
keep_alive()

# --- [ตั้งค่า และ รัน Discord Bot] ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# วาง TOKEN บอทของคุณตรงนี้
bot.run('YOUR_DISCORD_BOT_TOKEN')
