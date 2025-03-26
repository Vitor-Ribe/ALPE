import re
import os
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from moviepy import AudioFileClip

def converter_arquivo(input_file, output_format, title):
    output_file = AudioFileClip(input_file)
    output_file.write_audiofile(f"{title}.{output_format}")
    print(f"Conversão concluída!")
    return output_file

def is_youtube_link(link):
    # Verifica se o URL corresponde ao formato do YouTube
    youtube_padrao = r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.*$'
    return bool(re.match(youtube_padrao, link))

def limpar_nome(nome_arquivo):
    """Retira caracteres do nome do arquivo de saída para que não atrapalhe no salvamento"""
    return re.sub(r'[\\/*?:"<>|]', "", nome_arquivo)

def formato_saida(video, formato_saida):
    yt = video
    ys = None
    print("Baixando: " + yt.title + "...")

    # Cria as subpastas
    caminho_destino = criaPasta("audio" if formato_saida in ["mp3", "wav", "m4a"] else "video")

    if formato_saida in ["mp3", "wav", "m4a"]:
        ys = yt.streams.get_audio_only()
        arquivo_baixado = ys.download(output_path=caminho_destino)

        if formato_saida != "m4a":
            arquivo_convertido = converter_arquivo(arquivo_baixado, formato_saida, yt.title)  # converte para o formato escolhido
            os.remove(arquivo_baixado)  # remove o arquivo m4a
            return arquivo_convertido
        else:
            return arquivo_baixado

    elif formato_saida == "mp4":
        caminho_destino = criaPasta("video")
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
    if not is_youtube_link(link):
        print("Link do YouTube inválido!")
        return
    print("Link do Youtube válido!")

    if entrada == "video":
        video = YouTube(link, on_progress_callback=on_progress)
        formato_saida(video, saida)

    elif entrada == "playlist" and "playlist" in link:
        pl = Playlist(link)
        for video in pl.videos:
            formato_saida(video, saida)
    else:
        print("Este link não é de uma Playlist!")
        return
    print("Download Concluído!")