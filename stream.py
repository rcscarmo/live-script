import os
from dotenv import load_dotenv
load_dotenv()

twitch_stream_url = os.environ.get('twitch_stream_url')
twitch_stream_key = os.environ.get('twitch_stream_key')