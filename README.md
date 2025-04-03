# A L P E 🏔️

Um baixador de videos do Youtube ![image](https://github.com/simple-icons/simple-icons/blob/develop/icons/youtube.svg)

<div align="center">

![image](https://github.com/Vitor-Ribe/ALPE/blob/master/images/homeScreen.png)

</div>


---

### Entradas 🔗
Você pode escolher baixar apenas um vídeo, ou então baixar uma playlist completa.

Ps: Lembrando que ao tentar baixar uma playlist ela tem que ser pública ou estar marcada como "Não listada". O app ainda não possui suporte para baixar playlists privadas.

---

### Saídas 💾
Atualmente é possível salvar os vídeos nos formatos:
#### Vídeo
    - Mp4
#### Audio
    - Mp3
    - Wav
    - M4a

---

### ▶️ Run
Instale os requerimentos com:
```python
pip install requirements.txt
```
Execute o arquivo `front.py`

---

### Pasta de saída 📁
O app cria a pasta "ALPE" no diretório Downloads em seus arquivos, onde ele distribui os downloads em duas subpastas: 

- Audio
- Video

---

### Bibliotecas utilizadas 📚
- [Pytubefix](https://pytubefix.readthedocs.io/en/latest/) (Downloads)
- [PyQt6](https://doc.qt.io/qtforpython-6/) (Interface Gráfica)
- [MoviePy](https://zulko.github.io/moviepy/getting_started/index.html#getting-started) (Conversão)

---

### Versões
- V1.1.15: 
  - Adição de novos formatos de saída (mp3 e Wav)