import os

def get_env_variable(key):
    api_key = os.getenv(key)
    return api_key
    
api_key = get_env_variable("APIKEY")
print(f"API KEY: {api_key}")

