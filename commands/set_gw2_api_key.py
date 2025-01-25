import os
from .utils.write_json import write_json

def set_gw2_api_key(api_key: str):
    dc_server_id = os.environ["DISCORD_SERVER_ID"]
    try:
        data_dir = os.path.join("data")
        os.makedirs(data_dir, exist_ok=True)
        api_key_data = {"api_key": api_key}
        write_json(os.path.join(data_dir, f"{dc_server_id}.json"), api_key_data)

        print(f"API key written to discord server file")
    except Exception as e:
        print(f"Error writing API key: {e}")
        raise e

    