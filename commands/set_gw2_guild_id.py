import os
from .utils.write_json import write_json

def set_gw2_guild_id(guild_id: str):
    dc_server_id = os.environ["DISCORD_SERVER_ID"]
    try:
        data_dir = os.path.join("data")
        os.makedirs(data_dir, exist_ok=True)
        guild_id_data = {"guild_id": guild_id}
        write_json(os.path.join(data_dir, f"{dc_server_id}.json"), guild_id_data)

        print(f"Guild Id written to discord server file")
    except Exception as e:
        print(f"Error writing API key: {e}")
        raise e

    