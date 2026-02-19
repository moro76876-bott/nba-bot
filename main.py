
import discord
import requests
import asyncio
import feedparser
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
last_tweet = None

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # temporarily remove int()

print("TOKEN:", TOKEN)
print("CHANNEL:", CHANNEL_ID)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

seen = set()

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup



def get_latest_tweet():
    url = "https://nitter.net/UnderdogNBA/rss"

    feed = feedparser.parse(url)

    if feed.entries:
        entry = feed.entries[0]
        return entry.title, entry.link

    return None, None






@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    client.loop.create_task(loop())

async def loop():
    await client.wait_until_ready()
    channel = await client.fetch_channel(int(CHANNEL_ID))


    global last_tweet

    while True:
        try:
            # 👇 PUT IT HERE
            tweet_text, tweet_link = get_latest_tweet()

            if tweet_link and tweet_link != last_tweet:
                last_tweet = tweet_link

                embed = discord.Embed(
                    title="🐦 NBA Alert",
                    description=tweet_text,
                    color=0x1DA1F2
                )

                embed.url = tweet_link
                embed.set_footer(text="@UnderdogNBA")

                await channel.send(embed=embed)

        except Exception as e:
            print("ERROR:", e)

        await asyncio.sleep(30)





        
client.run(TOKEN)
