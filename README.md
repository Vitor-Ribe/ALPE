# A L P E 🏔️

Um baixador de videos do Youtube

<div align="center">

![image](https://github.com/Vitor-Ribe/ALPE/blob/master/images/homeScreen.png)

</div>



### Entradas
Você pode escolher baixar apenas um vídeo, ou então baixar uma playlist completa.

Ps: Lembrando que ao tentar baixar uma playlist ela tem que ser pública ou estar marcada como "Não listada". O app ainda não possui suporte para baixar playlists privadas.

### Saídas
Atualmente é possível salvar os vídeos nos formatos Mp4 e M4a

### Run
Execute o arquivo `front.py`

### Pasta de saída
O app cria a pasta "FilesDownloader" na pasta Downloads de seus arquivos, onde ele distribui os downloads em duas subpastas: Mp3 (para os arquivos de audio), e Mp4 (para os arquivos de vídeo).

### Bibliotecas utilizadas
- [Pytubefix](https://pytubefix.readthedocs.io/en/latest/)
- [PyQt6](https://doc.qt.io/qtforpython-6/)
