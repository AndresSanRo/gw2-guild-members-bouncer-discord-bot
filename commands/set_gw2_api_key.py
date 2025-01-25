import os

def set_gw2_api_key(api_key: str):
    dc_server_id = os.environ["DISCORD_SERVER_ID"]
    try:
        data_dir = os.path.join("data")
        os.makedirs(data_dir, exist_ok=True)
        with open(os.path.join(data_dir, f"{dc_server_id}.txt"), "w") as f:
            f.write(api_key)
        print(f"API key written to discord server file")
    except Exception as e:
        print(f"Error writing API key: {e}")
        raise e

    