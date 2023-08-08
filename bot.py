import discord
from discord import app_commands
import os
import aiohttp
import random
import asyncio
import openai
from config import get_settings
from payloads import ImaginePayload
from utils import prompt_to_dict, dict_to_prompt, validate_prompt, gen_multiple_prompts
from typing import Union
from discord.app_commands import locale_str
from pydantic import ValidationError


def sliding_windows(s: str, window_size):
    step_size = window_size // 2  # We want to overlap the windows

    strings = []
    for i in range(0, len(s) - window_size + 1, step_size):
        start = i
        end = min(i + window_size, len(s))
        strings.append(s[start:end])

    # Fix the last string to include the last characters
    if len(strings) > 1:
        last_start = len(s) - window_size
        last_end = len(s)
        strings[-1] = s[last_start:last_end]
    return strings


def summarize(prompt: str, model: str, window_size: int, max_tokens: int):
    """
    Summarize a long text using Chatgpt
    """
    onests = "Summarize the following text in one short sentence \n"
    merged_content = onests + prompt
    openai.api_key = settings.openai_api_key
    while (len(merged_content) > window_size):
        texts = sliding_windows(merged_content, window_size)
        response_list = []
        for i in texts:
            merged = onests + i
            response = openai.Completion.create(
                model=model, prompt=merged)
            response_list.append(response.choices[0].text)
        merged_content = '.'.join(response_list)
    to_sum = onests + merged_content
    response = openai.Completion.create(
        model=model, prompt=to_sum, max_tokens=max_tokens)
    return response


def chatgpt(prompt: str, model: str, max_tokens: int):
    openai.api_key = settings.openai_api_key
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=max_tokens)
    return response


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        self.directory = os.getcwd()

    async def on_ready(self):
        await self.wait_until_ready()
        os.environ['SESSION_ID'] = self.ws.session_id
        self.session_id = os.environ['SESSION_ID']
        print("Bot connected")
        if not self.synced:
            await tree.sync(guild=discord.Object(id=os.environ['GUILD_ID']))
            self.synced = True


settings = get_settings()
client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="test", description="Test", guild=discord.Object(id=os.environ['GUILD_ID']))
async def interaction_test(interaction: discord.Interaction, arg: str = ""):
    await interaction.response.defer(ephemeral=True)
    if arg == "":
        await interaction.followup.send("Test success!")
    else:
        await interaction.followup.send("Test " + arg + " success!")


@tree.command(name="chatgpt", description="Ask chatgpt", guild=discord.Object(id=os.environ['GUILD_ID']))
async def interaction_chatgpt(interaction: discord.Interaction,
                              prompt: str,
                              model: str = "text-davinci-003",
                              max_tokens: int = 300):
    await interaction.response.defer(ephemeral=True)
    # payload = {"prompts": prompt}
    response = chatgpt(prompt, model, max_tokens)
    try:
        answer = response['choices'][0]['text'].strip()
        print(answer)
        print(len(filter(None, answer.splitlines())))
        await interaction.followup.send(answer)
    except:
        # Need elaborate what error could get
        await interaction.followup.send("error!")


@tree.command(name="summarize", description="Summarize a long text to a short sentence", guild=discord.Object(id=os.environ['GUILD_ID']))
async def interaction_summarize(interaction: discord.Interaction,
                                prompt: str,
                                model: str = "text-davinci-003",
                                max_tokens: int = 300,
                                window_size: int = 1200):
    await interaction.response.defer(ephemeral=True)
    response = summarize(prompt, model, window_size, max_tokens)
    try:
        answer = response['choices'][0]['text'].strip()
        await interaction.followup.send(answer)
    except:
        # Need elaborate what error could get
        await interaction.followup.send("error!")
    # Need some error handling here


@tree.command(name="muse", description="Generate images for an article", guild=discord.Object(id=os.environ['GUILD_ID']))
async def interaction_muse(interaction: discord.Interaction,
                           prompt: str,
                           model: str = "text-davinci-003",
                           max_tokens: int = 300,
                           window_size: int = 1200,
                           multiple: bool = False):
    await interaction.response.defer(ephemeral=True)
    if multiple:
        prompt_dicts = gen_multiple_prompts(prompt)
    else:
        prompt_dicts = [prompt_to_dict(prompt)]
    for prompt_dict in prompt_dicts:
        valid = validate_prompt(**prompt_dict)
        if valid != []:
            for e in valid:
                await interaction.followup.send(e)
            return
        await interaction.followup.send(prompt_dict['prompt'])
        response = summarize(
            prompt_dict['prompt'], model, window_size, max_tokens)
        try:
            answer = response['choices'][0]['text'].strip()
        except:
            # Need elaborate what error could get
            await interaction.followup.send("Summarizing failed!")
            return

        header = {
            "Content-Type": "application/json",
            'authorization': settings.user_token
        }
        prompt_dict["prompt"] = answer
        answer = dict_to_prompt(prompt_dict)
        payroad_imagine = ImaginePayload(settings, answer).model_dump()
        async with aiohttp.ClientSession() as session:
            async with session.post('https://discord.com/api/v9/interactions',
                                    json=payroad_imagine,
                                    headers=header) as resp:
                if resp.ok:
                    await interaction.followup.send("Midjourney Imagine job started!")
                else:
                    await interaction.followup.send("Midjourney Imagine job failed!")

# TODO: For multiple generation fix the midjourney concurrent problem


@tree.command(name="mucha", description="Generate a long text with images based on the prompt to ChatGPT", guild=discord.Object(id=os.environ['GUILD_ID']))
async def interaction_mucha(interaction: discord.Interaction,
                            prompt: str,
                            model: str = "text-davinci-003",
                            max_tokens: int = 300,
                            window_size: int = 1200,
                            multiple: bool = False):
    await interaction.response.defer(ephemeral=True)
    prompt_dict = prompt_to_dict(prompt)
    valid = validate_prompt(**prompt_dict)
    if valid != []:
        for e in valid:
            await interaction.followup.send(e)
        return
    response = chatgpt(prompt_dict['prompt'], model, max_tokens)
    try:
        answer = response['choices'][0]['text'].strip()
        await interaction.followup.send(answer)
    except:
        # Need elaborate what error could get
        await interaction.followup.send("Cannot generate the story!")
        return
    if multiple:
        prompt_dicts = gen_multiple_prompts(answer)
    else:
        prompt_dicts = [prompt_to_dict(answer)]
    for prompt_dict in prompt_dicts:
        await interaction.followup.send(prompt_dict['prompt'])
        response = summarize(
            prompt_dict['prompt'], model, window_size, max_tokens)
        try:
            answer = response['choices'][0]['text'].strip()
        except:
            # Need elaborate what error could get
            await interaction.followup.send("Summarizing error!")
            return
        header = {
            "Content-Type": "application/json",
            'authorization': settings.user_token
        }
        prompt_dict["prompt"] = answer
        answer = dict_to_prompt(prompt_dict)
        payroad_imagine = ImaginePayload(settings, answer).model_dump()
        async with aiohttp.ClientSession() as session:
            async with session.post('https://discord.com/api/v9/interactions',
                                    json=payroad_imagine,
                                    headers=header) as resp:
                if resp.ok:
                    await interaction.followup.send("Midjourney Imagine job started!")
                else:
                    await interaction.followup.send("Midjourney Imagine job failed!")


discord_token = os.environ['DISCORD_TOKEN']
client.run(discord_token)
