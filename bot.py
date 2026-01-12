import os
import re
import asyncio
from telethon import TelegramClient, events
from flask import Flask
from threading import Thread

# ========== خادم ويب للحفاظ على التشغيل 24/7 ==========
app = Flask('')
@app.route('/')
def home():
    return "✅ Bot is running on Vercel!"
def run_web():
    app.run(host='0.0.0.0', port=8080)
Thread(target=run_web, daemon=True).start()

# ========== إعدادات البوت ==========
api_id = 1234567  # ضع API ID الحقيقي هنا
api_hash = "ضع_API_HASH_هنا"  # ضع API HASH الحقيقي هنا

SOURCE_CHANNELS = [
    "https://t.me/skyproxybot5G",
    "https://t.me/lootearn", 
    "https://t.me/mistcash",
    "https://t.me/flashproxybot"
]

TARGET_BOT = "@flashproxybot"
ACTIVATION_MSG = "🎟️ تفعيل كوبون"

client = TelegramClient("vercel_bot", api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def handler(event):
    if not event.text:
        return
    
    # استخراج الكودات
    codes = re.findall(r'\b[A-Z0-9]{10,15}\b', event.text)
    
    for code in codes:
        try:
            # 1. إرسال رسالة التفعيل
            await client.send_message(TARGET_BOT, ACTIVATION_MSG)
            # 2. إرسال الكود
            await client.send_message(TARGET_BOT, code)
            # 3. إرسال الكود مرة ثانية
            await client.send_message(TARGET_BOT, code)
            print(f"✅ تم إرسال: {code}")
        except Exception as e:
            print(f"❌ خطأ: {e}")

async def main():
    await client.start()
    print("🤖 البوت يعمل على Vercel!")
    await client.run_until_disconnected()

# تشغيل البوت
asyncio.run(main())
