import datetime
import discord
from .utils.gw2_api import get_guild_members


def search_guild_member(account_name: str):
    try:
        guild_members = get_guild_members()
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

def build_guild_member_not_found_embed(account_name):
    embed = discord.Embed(title="Guild member not found!", description=f"The player {account_name} is not on the guild", color=discord.Color.red())
    return embed