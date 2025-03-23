import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QGraphicsDropShadowEffect
from PyQt6.QtGui import QPalette, QBrush, QPixmap, QColor, QFontDatabase, QFont
from PyQt6.QtCore import Qt
import back

def titleConfigStyle(title):
    x = (janela.width() // 2) - (title.width() + (title.width() // 2))  # Centraliza o titulo na tela
    title.move(x, 130)
    title.setStyleSheet("""
        QLabel {
            font-size: 70px;
            font-family: 'the real magazine demo';
            /*font-weight: bold;*/
            color: #54769B;
        }
    """)

def lineEditConfigStyle(le):
    le.setGeometry(50, 290, 700, 40)    # posição
    le.setStyleSheet("""
        QLineEdit {
            background-color: #2C3E50; 
            border: 2px solid #5387A5;  /* Cor da borda */
            border-radius: 10px;  /* Arredondamento */
            padding: 25px;  /* Espaço interno */
        }
    """)
    # Sombreamento
    le.setGraphicsEffect(loadShadows())

def defaultConfigStyle(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #3B5A77;
            color: #FFF3DC;
            border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
            border-radius: 20px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #005A9E;
        }
        QPushButton:pressed {
            background-color: #004080;
        }
    """)

def clickedConfigStyle(button):
    button.setStyleSheet("""
        QPushButton {
            background-color: #C4E5EE;
            color: #233C52;
            border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
            border-radius: 20px;
            padding: 8px;
        }
    """)

def fontConfigStyle(font):
    font.setStyleSheet("""
        QLabel {
            font-size: 15px;
            font-weight: bold;
            color: #FFF3DC;
            /*background-color: rgba(0, 0, 0, 120);  Fundo semi-transparente preto */
        }
    """)

def downloadConfigStyle(download):
    download.setGeometry(20, 540, 750, 40)
    download.setStyleSheet("""
        QPushButton {
            background-color: #5087A4;
            color: #FFF3DC;
            border-radius: 16px;
            padding: 8px;
        }
        QPushButton:hover {
            background-color: #005A9E;
        }
    """)
    download.setGraphicsEffect(shadow)

def loadFonts():
    font_id = QFontDatabase.addApplicationFont('fonts/the real magazine demo.ttf')  # Carregar a fonte personalizada
    # Verificar se a fonte foi carregada corretamente
    if font_id == -1:
        print("Erro ao carregar a fonte!")
    else:
        print("Fonte carregada com sucesso!")

def loadShadows():
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(10)
    shadow.setColor(QColor(0, 0, 0, 100))  # Cor preta com transparência
    shadow.setOffset(2, 2)  # Distância da sombra
    return shadow

def actionButton(tipe):
    global entrada, saida
    if tipe == 'video':
        clickedConfigStyle(inputVideoButton)
        defaultConfigStyle(inputPlaylistButton)
        entrada = tipe

    elif tipe == 'playlist':
        clickedConfigStyle(inputPlaylistButton)
        defaultConfigStyle(inputVideoButton)
        entrada = tipe

    elif tipe == 'mp3':
        clickedConfigStyle(outputMp3Button)
        defaultConfigStyle(outputMp4Button)
        saida = tipe

    elif tipe == 'mp4':
        clickedConfigStyle(outputMp4Button)
        defaultConfigStyle(outputMp3Button)
        saida = tipe

def downloadVideo():
    link = linkLineEdit.text().strip()
    if not entrada or not saida:
        QMessageBox.warning(janela, "Aviso", "Por favor, preencha todos os campos e selecione opções válidas!")
        return
    else:
        back.DownloadVideo(link, entrada, saida)

def setBackground():
    """Define uma imagem de fundo sem afetar os widgets."""
    palette = QPalette()
    pixmap = QPixmap('images/background.jpg')  # Carrega a imagem
    palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))  # Aplica ao fundo da janela
    janela.setPalette(palette)

app = QApplication(sys.argv)

entrada = None
saida = None

# configurações da janela
janela = QWidget()
janela.setFixedSize(800, 600)
janela.setWindowTitle("Downloader do Youtube")

setBackground() # Foto background
shadow = loadShadows() # Carrega as conifgurações de sombreamento

# Titulo do App
loadFonts()
titleText = QLabel("Peak Saver", janela)
titleConfigStyle(titleText)

# Campo para inserir o Link do vídeo
linkLineEdit = QLineEdit("", janela)
linkLineEdit.setPlaceholderText("Cole o Link aqui")
lineEditConfigStyle(linkLineEdit)

# botão para escolher tipo de arquivo de entrada
inputText = QLabel("O que você está baixando?", janela)
inputText.move(560, 370)
fontConfigStyle(inputText)

inputVideoButton = QPushButton("Um único video", janela)
inputVideoButton.setGeometry(505, 400, 140, 40)
defaultConfigStyle(inputVideoButton)
inputVideoButton.clicked.connect(lambda: actionButton('video'))

inputPlaylistButton = QPushButton("Playlist", janela)
inputPlaylistButton.setGeometry(650, 400, 100, 40)
defaultConfigStyle(inputPlaylistButton)
inputPlaylistButton.clicked.connect(lambda: actionButton('playlist'))

# botão para escolher tipo de arquivo de saída
outputText = QLabel("Como quer salvar?", janela)
outputText.move(50, 370)
fontConfigStyle(outputText)

outputMp3Button = QPushButton("M4a", janela)
outputMp3Button.setGeometry(50, 400, 100, 40)
defaultConfigStyle(outputMp3Button)
outputMp3Button.clicked.connect(lambda: actionButton('mp3'))

outputMp4Button = QPushButton("Mp4", janela)
outputMp4Button.setGeometry(155, 400, 100, 40)
defaultConfigStyle(outputMp4Button)
outputMp4Button.clicked.connect(lambda: actionButton('mp4'))

# botão download
downloadButton = QPushButton("Download", janela)
downloadConfigStyle(downloadButton)
downloadButton.clicked.connect(downloadVideo)

janela.show()
app.exec()
