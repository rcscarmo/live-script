# Live Streaming Script

Este projeto permite transmitir uma lista de vídeos como se fossem lives para plataformas de stream.
Ele utiliza FFmpeg para a transmissão em tempo real.

# Plataformas

- [x] Twitch
- [ ] Youtube

## Estrutura de Pastas

- **`videos/`**: Local onde os arquivos de vídeo para transmissão devem ser armazenados.

## Configuração do Ambiente

1. Renomeie o arquivo `.env.sample` para `.env`.
2. Insira as chaves de stream das suas plataformas no arquivo `.env`.

## Pré-requisitos

Certifique-se de que o **Python 3.8+** e o **FFmpeg** estão instalados no seu sistema.

- **FFmpeg**: [Instruções de instalação](https://ffmpeg.org/download.html)
- **Python**: [Download Python](https://www.python.org/downloads/)

## Instalando e Executando

### 1. Crie um ambiente virtual

Execute o comando abaixo para criar um ambiente virtual:

```bash
python -m venv .venv
```

### 2. Ative o ambiente virtual e instale as dependências

- Windows:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

- Linux/Mac

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Execute o script

Certifique-se de que os vídeos estão na pasta `videos` e de que todas as configurações estão corretas. Em seguida, execute:

```bash
python live.py
```
