import datetime
import discord
import os
import requests
from .utils.json import read_json


def get_guild_member(account_name: str):
    try:
        dc_server_id = os.environ["DISCORD_SERVER_ID"]
        data_path = os.path.join(f"data/{dc_server_id}.json")
        data = read_json(data_path)

        url = f"https://api.guildwars2.com/v2/guild/{data["guild_id"]}/members?access_token={data["api_key"]}"
        response = requests.get(url)
        response.raise_for_status()
        guild_members = response.json()
        for member in guild_members:
            if member["name"] == account_name:
                return member
        return None
    except Exception as e:
        print(f"Error getting guild member: {e}")
        raise e

def build_guild_member_found_embed(member):
    joined_date = datetime.datetime.fromisoformat(member["joined"])
    formatted_date = joined_date.strftime("%d/%m/%Y %H:%M")

    embed = discord.Embed(title="Guild member found!", color=discord.Color.green())
    embed.add_field(name="Account name", value=member["name"], inline=False)
    embed.add_field(name="Rank", value=member["rank"], inline=False)
    embed.add_field(name="Joined on", value=formatted_date, inline=False)
    return embed