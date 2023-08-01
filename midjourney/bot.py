import discord
from discord import app_commands
import os
import aiohttp
import asyncio


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=os.environ['GUILD_ID']))
            self.synced = True


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="test", description="Test", guild=discord.Object(id=os.environ['GUILD_ID']))
async def foo(interaction: discord.Interaction, arg: str = ""):
    await interaction.response.defer(ephemeral=True)
    if arg == "":
        await interaction.followup.send("Test success!")
    else:
        await interaction.followup.send("Test " + arg + "success!")


@tree.command(name="chatgpt", description="Ask chatgpt", guild=discord.Object(id=os.environ['GUILD_ID']))
async def foo(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer(ephemeral=True)
    payload = {"prompts": prompt}
    async with aiohttp.ClientSession(base_url="http://127.0.0.1:8000") as session:
        async with session.post("/chatgpt", json=payload) as resp:
            if resp.status == 200:
                chatgpt_resp = await resp.json()
                answer = chatgpt_resp['choices'][0]['text'].strip()
                await interaction.followup.send(answer)
            else:
                await interaction.followup.send("Error!")


@tree.command(name="mucha", description="Generate an image for an article", guild=discord.Object(id=os.environ['GUILD_ID']))
async def foo(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer(ephemeral=True)
    payload = {"prompts": prompt}
    async with aiohttp.ClientSession(base_url="http://127.0.0.1:8000") as session:
        async with session.post("/chatgpt/summarize", json=payload) as resp:
            if resp.status == 200:
                chatgpt_resp = await resp.json()
                answer = chatgpt_resp['choices'][0]['text'].strip()
                # await interaction.response.send_message(answer)
            else:
                await interaction.followup.send("Error!")
                return
        async with session.post("/midjourney/imagine?prompt=" + answer) as resp:
            if resp.ok:
                await interaction.followup.send("Midjourney Imagine job started!")
                # asyncio.sleep(100)
                # await interaction.followup.fetch_message()
            else:
                await interaction.followup.send("Error!")


@tree.command(name="fairytale", description="Generate a ChatGPT fairytale with a Midjourney image", guild=discord.Object(id=os.environ['GUILD_ID']))
async def foo(interaction: discord.Interaction, fairytalestyle: str = "any"):
    await interaction.response.defer(ephemeral=True)
    async with aiohttp.ClientSession(base_url="http://127.0.0.1:8000") as session:
        payload = {"prompts": "generate a fairy tale in " +
                   fairytalestyle + " style"}
        async with session.post("/chatgpt", json=payload) as resp:
            if resp.ok:
                chatgpt_resp = await resp.json()
                answer = {
                    "prompts": chatgpt_resp['choices'][0]['text'].strip()}
                await interaction.followup.send(answer["prompts"])
            else:
                await interaction.followup.send("Cannot generate the story!")
        async with session.post("/chatgpt/summarize", json=answer) as resp:
            if resp.ok:
                chatgpt_resp2 = await resp.json()
                answer2 = chatgpt_resp2['choices'][0]['text'].strip()
                # await interaction.response.send_message(answer)
            else:
                await interaction.followup.send("Cannot summarize the story!")
        async with session.post("/midjourney/imagine?prompt=" + answer2) as resp:
            if resp.ok:
                await interaction.followup.send("Midjourney Imagine job started!")
                # asyncio.sleep(100)
                # await interaction.followup.fetch_message()
            else:
                await interaction.followup.send("Cannot genrate the image!")


discord_token = os.environ['DISCORD_TOKEN']
client.run(discord_token)
