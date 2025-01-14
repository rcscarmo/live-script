import subprocess
import os
from stream import *

BASE_DIR = os.path.abspath(".")
LOOPS = 1

def load_videos():
    '''
    Carrega todos os arquivos que esta na pasta `Videos`
    '''
    arquivos = []
    for _, _, files in os.walk("./videos/"):
        for file in files:
            if file != ".gitkeep":
                arquivos.append(f"{BASE_DIR}/videos/{file}")
    return arquivos
video_files = load_videos()

# Função para transmitir um único vídeo
def stream_video(video_path, stream_url, stream_key):
    '''
    Funcao que transmite o video para a plataforma escolhida
    '''
    command = [
        "ffmpeg",
        "-re",  # Lê o vídeo em tempo real
        "-i", video_path,  # Arquivo de entrada
        "-c:v", "libx264",  # Codec de vídeo
        "-preset", "veryfast",  # Preset para baixa latência
        "-maxrate", "3000k",  # Taxa máxima de bits
        "-bufsize", "6000k",  # Tamanho do buffer
        "-pix_fmt", "yuv420p",  # Formato de pixels
        "-c:a", "aac",  # Codec de áudio
        "-b:a", "128k",  # Taxa de bits de áudio
        "-ar", "44100",  # Taxa de amostragem de áudio
        "-f", "flv",  # Formato de saída
        f"{stream_url}/{stream_key}",  # URL completa de ingest
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for loops in range(LOOPS):
    for video in video_files:
        print(f"Transmitindo: ''' {video} '''")
        stream_video(video, twitch_stream_url, twitch_stream_key)

print("Transmissão concluída!")
