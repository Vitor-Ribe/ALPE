import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QGraphicsDropShadowEffect
from PyQt6.QtGui import QPalette, QBrush, QPixmap, QColor, QFontDatabase, QFont
from PyQt6.QtCore import Qt
import back

def actionButton(tipe):
    global entrada, saida
    if tipe == 'video':
        inputVideoButton.setStyleSheet("""
            QPushButton {
                background-color: #C4E5EE;
                color: #233C52;
                border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
                border-radius: 20px;
                padding: 8px;
            }
        """)
        inputPlaylistButton.setStyleSheet("""
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
        entrada = tipe
    elif tipe == 'playlist':
        inputPlaylistButton.setStyleSheet("""
            QPushButton {
                background-color: #C4E5EE;
                color: #233C52;
                border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
                border-radius: 20px;
                padding: 8px;
            }
        """)
        inputVideoButton.setStyleSheet("""
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
        entrada = tipe
    elif tipe == 'mp3':
        outputMp3Button.setStyleSheet("""
            QPushButton {
                background-color: #C4E5EE;
                color: #233C52;
                border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
                border-radius: 20px;
                padding: 8px;
            }
        """)
        outputMp4Button.setStyleSheet("""
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
        saida = tipe
    elif tipe == 'mp4':
        outputMp4Button.setStyleSheet("""
            QPushButton {
                background-color: #C4E5EE;
                color: #233C52;
                border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
                border-radius: 20px;
                padding: 8px;
            }
        """)
        outputMp3Button.setStyleSheet("""
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

janela = QWidget()
janela.setFixedSize(800, 600)
janela.setWindowTitle("Downloader do Youtube")



setBackground()

shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(10)
shadow.setColor(QColor(0, 0, 0, 100))  # Cor preta com transparência
shadow.setOffset(2, 2)  # Distância da sombra

# Titulo do App
font_id = QFontDatabase.addApplicationFont('fonts/the real magazine demo.ttf')  # Carregar a fonte personalizada

# Verificar se a fonte foi carregada corretamente
if font_id == -1: print("Erro ao carregar a fonte!")
else: print("Fonte carregada com sucesso!")

titleText = QLabel("BAIXA YOUTOBA", janela)
x = (janela.width() // 2) - (titleText.width() * 2) # Centraliza o titulo na tela
titleText.move(x, 130)
titleText.setStyleSheet("""
    QLabel {
        font-size: 70px;
        font-family: 'the real magazine demo';
        /*font-weight: bold;*/
        color: #54769B;
    }
""")

# Campo para inserir o Link do vídeo
linkLineEdit = QLineEdit("", janela)
linkLineEdit.setPlaceholderText("Cole o Link aqui")
linkLineEdit.setGeometry(50, 290, 700, 40)
linkLineEdit.setStyleSheet("""
    QLineEdit {
        background-color: #2C3E50; 
        border: 2px solid #5387A5;  /* Cor da borda */
        border-radius: 10px;  /* Arredondamento */
        padding: 25px;  /* Espaço interno */
    }
""")
linkLineEdit.setGraphicsEffect(shadow)

# botão para escolher tipo de arquivo de entrada
inputText = QLabel("O que você está baixando?", janela)
inputText.move(560, 370)
inputText.setStyleSheet("""
    QLabel {
        font-size: 15px;
        font-weight: bold;
        color: #FFF3DC;
        /*background-color: rgba(0, 0, 0, 120);  Fundo semi-transparente preto */
    }
""")

inputVideoButton = QPushButton("Um único video", janela)
inputVideoButton.setGeometry(505, 400, 140, 40)
inputVideoButton.setStyleSheet("""
    QPushButton {
        background-color: #3B5A77;
        color: #FFF3DC;
        border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
        border-radius: 20px;
        padding: 8px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #005A9E;
    }
""")
inputVideoButton.clicked.connect(lambda: actionButton('video'))

inputPlaylistButton = QPushButton("Playlist", janela)
inputPlaylistButton.setGeometry(650, 400, 100, 40)
inputPlaylistButton.setStyleSheet("""
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
inputPlaylistButton.clicked.connect(lambda: actionButton('playlist'))

# botão para escolher tipo de arquivo de saída
outputText = QLabel("Como quer salvar?", janela)
outputText.move(50, 370)
outputText.setStyleSheet("""
    QLabel {
        font-size: 15px;              /* Tamanho da fonte */
        font-weight: bold;            /* Negrito */
        color: #FFF3DC;                 /* Cor do texto */
    }
""")

outputMp3Button = QPushButton("Mp3", janela)
outputMp3Button.setGeometry(50, 400, 100, 40)
outputMp3Button.setStyleSheet("""
    QPushButton {
        background-color: #3B5A77;
        color: #FFF3DC;
        border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
        border-radius: 20px;
        padding: 8px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #005A9E;
    }
""")
outputMp3Button.clicked.connect(lambda: actionButton('mp3'))

outputMp4Button = QPushButton("Mp4", janela)
outputMp4Button.setGeometry(155, 400, 100, 40)
outputMp4Button.setStyleSheet("""
    QPushButton {
        background-color: #3B5A77;
        color: #FFF3DC;
        border: 1px solid #1E3A50;  /* Espessura e cor da borda*/
        border-radius: 20px;
        padding: 8px;
        font-size: 14px;
    }
    QPushButton:hover {
        background-color: #005A9E;
    }
""")
outputMp4Button.clicked.connect(lambda: actionButton('mp4'))

# botão download
downloadButton = QPushButton("Download", janela)
downloadButton.setGeometry(20, 540, 750, 40)
downloadButton.setStyleSheet("""
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
downloadButton.setGraphicsEffect(shadow)
downloadButton.clicked.connect(downloadVideo)

janela.show()
app.exec()
