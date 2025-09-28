import sys
from PySide6.QtCore import QThread
from worker import Worker
from funcoes import url_verify, local_verify
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton, QFileDialog,

    QProgressBar, QTextEdit
)
from PySide6.QtCore import Qt

class Mp3DownloaderUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # --- Configurações da Janela Principal ---
        self.setWindowTitle("MP3 Downloader")
        self.setGeometry(100, 100, 500, 450)

        # --- Widget Central e Layout Principal ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- 1. Seção de Tipo de Download ---
        self.download_type_label = QLabel("Selecione o tipo de download:")
        self.video_radio_button = QRadioButton("Vídeo Único")
        self.playlist_radio_button = QRadioButton("Playlist Completa")
        self.video_radio_button.setChecked(True)  # Inicia com "Vídeo" selecionado

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.video_radio_button)
        type_layout.addWidget(self.playlist_radio_button)

        # --- 2. Seção da URL ---
        self.url_label = QLabel("URL do YouTube:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Cole a URL aqui...")

        # --- 3. Seção do Local de Download ---
        self.local_label = QLabel("Salvar em:")
        self.local_input = QLineEdit()
        self.local_input.setPlaceholderText("Deixe em branco para salvar na pasta do programa")
        self.browse_button = QPushButton("Procurar...")

        local_layout = QHBoxLayout()
        local_layout.addWidget(self.local_input)
        local_layout.addWidget(self.browse_button)

        # --- 4. Botão de Download ---
        self.download_button = QPushButton("Baixar MP3")
        self.download_button.setStyleSheet("font-weight: bold; padding: 8px;")

        # --- 5. Seção de Progresso e Status ---
        self.progress_bar = QProgressBar()
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setValue(0)
        self.status_label = QLabel("Aguardando um download...")
        self.status_label.setAlignment(Qt.AlignCenter)

        # --- Adicionando widgets ao layout principal ---
        main_layout.addWidget(self.download_type_label)
        main_layout.addLayout(type_layout)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.url_label)
        main_layout.addWidget(self.url_input)
        main_layout.addSpacing(10)
        main_layout.addWidget(self.local_label)
        main_layout.addLayout(local_layout)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.download_button)
        main_layout.addSpacing(20)
        main_layout.addWidget(self.status_label)
        main_layout.addWidget(self.progress_bar)

        # --- Conexões (serão implementadas) ---
        self.browse_button.clicked.connect(self.abrir_seletor_de_pasta)
        self.download_button.clicked.connect(self.iniciar_download) # Conectar o botão

        self.thread = None
        self.worker = None

    def abrir_seletor_de_pasta(self):
        # Abre um diálogo para o usuário selecionar uma pasta
        pasta = QFileDialog.getExistingDirectory(self, "Selecionar Pasta")
        if pasta:
            self.local_input.setText(pasta)
    
    def iniciar_download(self):
        url = self.url_input.text()
        local = self.local_input.text()

        # Validações (versão GUI)
        if url_verify(url): # Reutilizando sua função
            self.status_label.setText("URL inválida! Forneça uma URL do YouTube.")
            return
        
        local_path = local_verify(local) # Reutilizando sua função
        if local_path == 0:
            self.status_label.setText("Erro ao criar ou acessar o diretório.")
            return
        
        is_playlist = self.playlist_radio_button.isChecked()
        
        # --- Configuração do Thread e Worker ---
        self.thread = QThread()
        self.worker = Worker(url=url, local=local_path, is_playlist=is_playlist)
        self.worker.moveToThread(self.thread)

        # --- Conectar sinais do worker aos slots da UI ---
        self.thread.started.connect(self.worker.executar)
        self.worker.finalizado.connect(self.thread.quit)
        self.worker.finalizado.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.progresso_atualizado.connect(self.atualizar_progresso)
        self.worker.status_atualizado.connect(self.atualizar_status)
        self.worker.finalizado.connect(self.download_finalizado)

        # --- Iniciar o processo ---
        self.thread.start()

        # Desabilitar o botão para evitar múltiplos downloads
        self.download_button.setEnabled(False)
        self.status_label.setText("Iniciando download...")

    # --- Slots para receber os sinais do Worker ---
    def atualizar_progresso(self, percent, status_text):
        self.progress_bar.setValue(percent)
        self.status_label.setText(status_text)

    def atualizar_status(self, mensagem):
        self.status_label.setText(mensagem)

    def download_finalizado(self, sucesso, mensagem):
        self.status_label.setText(mensagem)
        if sucesso:
            self.progress_bar.setValue(100)
        else:
            self.progress_bar.setValue(0)
        
        # Reabilitar o botão
        self.download_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mp3DownloaderUI()
    window.show()
    sys.exit(app.exec())