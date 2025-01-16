import os

#TWITCH
# ARQUIVO QUE PEGA TODAS AS SECRETS DO .ENV
twitch_stream_url = os.environ.get('twitch_stream_url')
twitch_stream_key = os.environ.get('twitch_stream_key')
# Configurações de stream
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
BROADCASTER_ID = os.environ.get("BROADCASTER_ID")