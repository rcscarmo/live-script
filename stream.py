from segredos import *
import requests
from dotenv import load_dotenv
load_dotenv()


def get_titulo():
    titulo = str(input("Titulo da transmissao:\n"))
    return titulo

def get_game_id():
    game_name = str(input("Coloque o nome da categoria:\n"))
    url = f"https://api.twitch.tv/helix/search/categories?query={game_name}"
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Client-Id': CLIENT_ID}
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'data' in data and data['data']:
        return data['data'][0]['id']
    else:
        print("Categoria não encontrada.")
        return None
    
def get_tags():
    run = True
    tags = []
    while run:
        tag = str(input("Digite a tag que deseja usar: \n"))
        tags.append(tag)
        stop = int(input("Deseja adicionar outras? 1 - S / 2 - N"))
        if stop == 1:
            run = False
    return tags

def get_idioma():
    print("Idioma da live:\n")
    print("PT-BR\nEN-US")
    idioma = str(input(""))
    return idioma

def update_twitch_broadcast(title, game_id, tags, language):
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={BROADCASTER_ID}"
    headers = {'Authorization': f'Bearer {ACCESS_TOKEN}', 'Client-Id': CLIENT_ID, 'Content-Type': 'application/json'}
    payload = {'title': title, 'game_id': game_id, 'tags': tags, 'broadcaster_language': language}
    
    response = requests.patch(url, json=payload, headers=headers)
    if response.status_code == 204:
        print("Transmissão atualizada com sucesso!")
    else:
        print("Erro ao atualizar transmissão:", response.json())


titulo = get_titulo()
game_id = get_game_id()
while game_id == None: game_id = get_game_id()
all_tags = get_tags()
idioma = get_idioma()

update_twitch_broadcast(title=titulo, game_id=game_id, tags=all_tags, language=idioma)