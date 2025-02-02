import datetime
import discord
from .utils.gw2_api import get_guild_members


def search_guild_member(account_name: str):
    try:
        if len(account_name) < 3:
            return account_length_guard_embed()
        
        guild_members = get_guild_members()
    
        for member in guild_members:
            if member["name"] == account_name:
                return build_guild_member_found_embed(member)

        possible_matches = []

        for member in guild_members:
            member_name_part, member_number_part = member["name"].rsplit('.', 1)
            if account_name in member_name_part or account_name in member_number_part:
                possible_matches.append(member)
            elif account_name in member["name"]:
                possible_matches.append(member)

        if possible_matches:
            return build_guild_member_multiple_matches_embed(possible_matches)
        else:
            return build_guild_member_not_found_embed(account_name)
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
    embed = discord.Embed(title="Guild member not found", description=f"The player {account_name} is not on the guild", color=discord.Color.red())
    return embed

def build_guild_member_multiple_matches_embed(possible_matches):
    embed = discord.Embed(title="Multiple matches for guild member", description="The exact account name couldn't be found, but maybe it's one of these. Refine your search for a more accurate result.", color=discord.Color.yellow())
    for member in possible_matches:
        embed.add_field(name="Account name", value=member["name"], inline=False)
    return embed

def account_length_guard_embed():
    embed = discord.Embed(title="Account name too short!", description="The account name must be at least 3 characters long", color=discord.Color.red())
    return embed