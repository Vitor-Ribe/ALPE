import re
import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

def is_youtube_link(link):
    # Verifica se o URL corresponde ao formato do YouTube
    youtube_padrao = r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.*$'
    return bool(re.match(youtube_padrao, link))

def limpar_nome(nome_arquivo):
    """Retira caracteres do nome do arquivo de saída para que não atrapalhe no salvamento"""
    return re.sub(r'[\\/*?:"<>|]', "", nome_arquivo)

def formato_saida(video, entrada, formato_saida):
    yt = video
    ys = None
    print("Baixando: " + yt.title + "...")

    if formato_saida == "mp3":
        caminho_destino = criaPasta(formato_saida)
        ys = yt.streams.get_audio_only()
        ys.download(output_path=caminho_destino)

    elif formato_saida == "mp4":
        caminho_destino = criaPasta(formato_saida)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=caminho_destino)


def arquivo_existe(nome_arquivo, extensao, caminho_destino):
    """Verifica se o arquivo já existe no diretório de destino"""
    nome_completo = nome_arquivo + "." + extensao
    return nome_completo in os.listdir(caminho_destino)

def criaPasta(saida):
    caminho_destino = os.path.join(os.path.expanduser("~"), "Downloads", "FilesDownloader", saida)
    if not os.path.exists(caminho_destino):
        os.makedirs(caminho_destino)
    return caminho_destino

def DownloadVideo(link, entrada, saida):
    if entrada == "video":
        if not is_youtube_link(link):
            print("Link do YouTube inválido!")
            return
        print("Link Valido")
        video = YouTube(link, on_progress_callback=on_progress)
        formato_saida(video, entrada, saida)

    elif entrada == "playlist":
        if not is_youtube_link(link):
            print("Link do YouTube inválido!")
            return
        print("Link Valido")
        pl = Playlist(link)
        for video in pl.videos:
            formato_saida(video, entrada, saida)

    print("Download Concluído!")