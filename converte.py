from moviepy import AudioFileClip

output = "mp3"
name = "musga"
audio = AudioFileClip("musica.m4a")
audio.write_audiofile(f"{name}.{output}")