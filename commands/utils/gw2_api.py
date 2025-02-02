import os
import requests
from .json import read_json

GW2_API_BASE_URL = "https://api.guildwars2.com/v2"

def get_guild_members():
    try:
        dc_server_id = os.environ["DISCORD_SERVER_ID"]
        data_path = os.path.join(f"data/{dc_server_id}.json")
        data = read_json(data_path)

        url = f"{GW2_API_BASE_URL}/guild/{data["guild_id"]}/members?access_token={data["api_key"]}"
        response = requests.get(url)
        response.raise_for_status()
        guild_members = response.json()
        return guild_members
    except Exception as e:
        print(f"Error in guild member API Call: {e}")
        raise e