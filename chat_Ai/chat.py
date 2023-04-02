import os
import sys
import json
import asyncio
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='gpt3', help='Generate text with GPT-3')
async def gpt3(ctx, *, prompt):
    url = 'https://api.openai.com/v1/engines/davinci/completions'
    headers = {'Authorization': 'Bearer ' + os.getenv('OPENAI_KEY')}
    data = {'prompt': prompt, 'max_tokens': 100, 'temperature': 0.7, 'top_p': 0.9}
    response = requests.post(url, headers=headers, json=data)
    response = json.loads(response.text)
    if 'choices' in response:
        await ctx.send(response['choices'][0]['text'])
    else:
        await ctx.send('Sorry, I could not generate a response.')

bot.run(TOKEN)
