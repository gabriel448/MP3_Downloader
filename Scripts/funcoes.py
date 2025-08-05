import os
import re
from yt_dlp import YoutubeDL
from colorama import Fore, Style, init
init(autoreset=True)

#definindo um CustomLogger pra silenciar as milhares de mensagens que o yt_dlp mande pro terminal enquanto faz o download
class CustomLogger:
    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        print(f'[AVISO] {msg}')

    def error(self, msg):
        print(f'[ERRO] ocorreu um problema: {msg}')
#funcao que recebe as informacoes de progresso e faz a barra dos downloads
def progresso_hook(d):
    if d['status'] == 'downloading':
        if d.get('total_bytes') is not None and d.get('downloaded_bytes') is not None:
            perc_float = (d['downloaded_bytes']/d['total_bytes'])*100
            percent = f'{perc_float:.1f}'
        else:
            percent = 'Unknow'
            perc_float = 0.0
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()

        total_blocos = 30
        blocos_preenchidos = int((perc_float/100)*total_blocos)
        blocos_vazios = total_blocos - blocos_preenchidos
        barra = Fore.GREEN + ('▇' * blocos_preenchidos) + Fore.WHITE + ('░'*blocos_vazios)

        print(f"{Fore.GREEN}[⇩] Baixando: {percent} | Velocidade: {speed} | Tempo estimado: {eta} | {barra}      ", end='\r', flush=True)

    elif d['status'] == 'finished':
        total_blocos = 30
        barra_completa = Fore.GREEN + '▇' * total_blocos
        print(f"{Fore.GREEN}[⇩] Baixando: 100.0% | Velocidade: Unknown | Tempo estimado: 00:00 | {barra_completa}      ", end='\r', flush=True)
        print(f"\n{Fore.GREEN}[✓] Download finalizado. Convertendo para MP3...", flush=True)

def playlist_downloader(url, local):
    try:   
        #basicamente instrucoes de download do arquivo
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(local,'%(playlist)s','%(title)s.%(ext)s'),
            'ignoreerrors': True,
            'progress_hooks': [progresso_hook],
            'logger': CustomLogger(),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': False,
        }
    
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        #verificacao se foi baixado algo na subpasta
        playlist_id = url.split("list=")[-1].split("&")[0]
        subfolders = [f for f in os.listdir(local) if playlist_id in f or os.path.isdir(os.path.join(local, f))]

        for folder in subfolders:
            folder_path = os.path.join(local, folder)
            if os.path.isdir(folder_path):
                mp3s = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
                if mp3s:
                    return True
        return False
    #caso nada for baixado gera um erro
    except Exception as e:
        print(f'\n[ERRO] Falaha inesperada: {e}')

def mp3_downloader(url, local):
    try:   
        #basicamente instrucoes de download do arquivo dnv
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(local, '%(title)s.%(ext)s'),
            'progress_hooks': [progresso_hook],
            'logger': CustomLogger(),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'noplaylist': True,
        }
        
        #fazer a mesmo verificacao se baixou algo porem apenas com um arquivo agora
        
        arquivos_antes = set(os.listdir(local))#faz uma lista dos arquivos da pasta antes do download
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        #ve se tem algo novo
        arquivos_depois = set(os.listdir(local))
        novos_arquivos = arquivos_depois - arquivos_antes

        for nome in novos_arquivos:
            if nome.endswith(".mp3"):
                return True    
        return False
    except Exception as e:
        print(f'\n[ERRO] Falaha inesperada: {e}')

#verificando se a url eh do youtube e se eh valida
def url_verify(url):
    if not url.startswith(("http://", "https://")) or "youtu" not in url:
        os.system('cls')
        print("URL incorreta! forneca uma URL do YouTube.")
        return True
    return False
#verificando se o local existe, se nao existir ele cria um com o nome fornecido
def local_verify(local):
    if local.strip() == "":
        return os.getcwd()
    try:
        if not os.path.exists(local):
            os.makedirs(local)
        return local
    except Exception as e:
        os.system('cls')
        print(f'Erro ao criar ou acessar o diretorio: {e}')
        return 0

