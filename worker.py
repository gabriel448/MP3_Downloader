from PySide6.QtCore import QObject, Signal, Slot
from funcoes import playlist_downloader, mp3_downloader, url_verify, local_verify

class Worker(QObject):
    # --- Sinais que o Worker pode emitir ---
    # Sinal para atualizar a barra de progresso (int: porcentagem)
    progresso_atualizado = Signal(int, str) # porcentagem, texto_status
    # Sinal para enviar mensagens de status (str: mensagem)
    status_atualizado = Signal(str)
    # Sinal emitido quando o download termina (bool: sucesso, str: mensagem final)
    finalizado = Signal(bool, str)

    def __init__(self, url, local, is_playlist):
        super().__init__()
        self.url = url
        self.local = local
        self.is_playlist = is_playlist
        
    # progresso_hook modificado para emitir sinais em vez de imprimir
    def progresso_hook_gui(self, d):
        if d['status'] == 'downloading':
            if d.get('total_bytes') is not None:
                percent = int((d['downloaded_bytes'] / d['total_bytes']) * 100)
                speed = d.get('_speed_str', 'N/A').strip()
                eta = d.get('_eta_str', 'N/A').strip()
                status_text = f"Baixando... | Velocidade: {speed} | Tempo: {eta}"
                self.progresso_atualizado.emit(percent, status_text)
        elif d['status'] == 'finished':
            self.progresso_atualizado.emit(100, "Download concluído. Convertendo...")

    @Slot()
    def executar(self):
        try:
            # Substituir o progresso_hook original pelo novo
            # As funções de download precisam ser um pouco ajustadas para aceitar o hook
            if self.is_playlist:
                # Modifique a função playlist_downloader para receber 'progress_hooks' como argumento
                sucesso = playlist_downloader(self.url, self.local, progress_hook=self.progresso_hook_gui)
            else:
                # Modifique a função mp3_downloader para receber 'progress_hooks' como argumento
                sucesso = mp3_downloader(self.url, self.local, progress_hook=self.progresso_hook_gui)

            if sucesso:
                self.finalizado.emit(True, "Arquivos baixados e convertidos com sucesso!")
            else:
                self.finalizado.emit(False, "Erro: Nenhum áudio foi baixado. Verifique a URL.")

        except Exception as e:
            self.finalizado.emit(False, f"Erro inesperado: {e}")