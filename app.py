import discord
import requests
import os
from discord.ext import commands
import json
import uuid

TOKEN = os.environ.get("TOKEN")
GUILD_ID = "YOUR_SERVER_ID"
CHANNEL_ID = "YOUR_CHANNEL_ID"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is connected to Discord!')

METADATA_FILE = 'file_metadata.json'

def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_metadata(metadata):
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

@bot.command(name='upload')
async def upload(ctx, file_path: str):
    if not os.path.exists(file_path):
        await ctx.send(f"File '{file_path}' does not exist.")
        return

    file_id = str(uuid.uuid4())
    chunk_size = 24 * 1024 * 1024

    metadata = load_metadata()
    metadata[file_id] = {'chunks': [], 'original_name': os.path.basename(file_path)}

    with open(file_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break

            part_file_path = f'{file_path}.part{part_num}'
            with open(part_file_path, 'wb') as part_file:
                part_file.write(chunk)
            
            message = await ctx.send(file=discord.File(part_file_path))
            metadata[file_id]['chunks'].append(message.attachments[0].url)
            os.remove(part_file_path)
            part_num += 1

    save_metadata(metadata)
    await ctx.send(f'Upload complete! File ID: {file_id}')

@bot.command()
async def download(ctx, file_id: str):
    metadata = load_metadata()
    if file_id not in metadata:
        await ctx.send(f"No file found with ID '{file_id}'.")
        return

    file_parts = metadata[file_id]['chunks']
    original_name = metadata[file_id]['original_name']

    file_data = bytearray()
    for part_url in file_parts:
        response = requests.get(part_url)
        file_data.extend(response.content)
    
    with open(original_name, 'wb') as f:
        f.write(file_data)

    await ctx.send(f'Download complete! File saved as "{original_name}".')

bot.run(TOKEN)
