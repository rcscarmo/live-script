import subprocess
import signal
import os
from segredos import *
# from stream import *

BASE_DIR = os.path.abspath(".")

def load_videos():
    '''
    Carrega todos os arquivos que esta na pasta `Videos`
    '''
    arquivos = []
    for _, _, files in os.walk("./videos/"):
        for file in files:
            if file != ".gitkeep":
                if file != "file_list.txt":
                    arquivos.append(f"{BASE_DIR}/videos/{file}")
    return arquivos
video_files = load_videos()

# Função para transmitir um único vídeo
def stream_videos_in_sequence(video_files, stream_url, stream_key):
    '''
    Funcao que transmite o video para a plataforma escolhida
    '''

     # Cria uma lista de arquivos para a concatenação
    with open("./videos/file_list.txt", "w") as file_list:
        for video in video_files:
            file_list.write(f"file '{video}'\n")
            
    command = [
        "ffmpeg",
        "-re",  # Lê o vídeo em tempo real
        "-f","concat",
        "-safe","0",
        "-i", "./videos/file_list.txt",  # Arquivo de entrada
        "-c:v", "libx264",  # Codec de vídeo
        "-preset", "veryfast",  # Preset para baixa latência
        "-maxrate", "1000k",  # Taxa máxima de bits
        "-bufsize", "4000k",  # Tamanho do buffer
        "-pix_fmt", "yuv420p",  # Formato de pixels
        "-c:a", "aac",  # Codec de áudio
        "-b:a", "128k",  # Taxa de bits de áudio
        "-ar", "44100",  # Taxa de amostragem de áudio
        "-rtbufsize", "1500M",  # Buffer adicional para leitura em tempo real
        "-s","1024x768",
        "-f", "flv",  # Formato de saída
        f"{stream_url}/{stream_key}",  # URL completa de ingest
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        process.communicate()
    except KeyboardInterrupt:
        print("Encerrando transmissão...")
        process.send_signal(signal.SIGINT)  # Envia sinal para encerrar o processo
        process.wait()
    finally:
         if process.poll() is None:  # Verifica se o processo ainda está ativo
            process.terminate()
            process.wait()

stream_videos_in_sequence(video_files, twitch_stream_url, twitch_stream_key)
print("Transmissão concluída!")