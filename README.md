# MP3 Downloader for YouTube

## Descrição

Este projeto é uma aplicação de desktop desenvolvida em Python que permite aos usuários baixar o áudio de vídeos ou playlists do YouTube e salvá-los como arquivos MP3. A interface gráfica foi construída utilizando PySide6, garantindo uma experiência de uso simples e intuitiva.

O programa utiliza a poderosa biblioteca `yt-dlp` para gerenciar os downloads e o `FFmpeg` para a conversão dos arquivos de áudio, garantindo alta qualidade e compatibilidade.

## Funcionalidades

-   **Download de Vídeo Único**: Cole a URL de um vídeo do YouTube para baixar e converter seu áudio para MP3.
-   **Download de Playlist**: Forneça a URL de uma playlist do YouTube para baixar todos os vídeos e convertê-los para MP3.
-   **Interface Gráfica Simples**: Uma janela fácil de usar onde você pode colar a URL, escolher o local para salvar os arquivos e iniciar o download.
-   **Seleção de Diretório**: Permite ao usuário escolher uma pasta específica para salvar os arquivos MP3 baixados ou usar o diretório padrão do programa.
-   **Barra de Progresso e Status**: Acompanhe o andamento do download em tempo real com uma barra de progresso e mensagens de status detalhadas.
-   **Processamento em Segundo Plano**: A interface do usuário permanece responsiva durante os downloads, pois o processo é executado em uma thread separada.

## Requisitos

Para executar este projeto a partir do código-fonte, você precisará ter o Python 3 instalado, juntamente com as seguintes bibliotecas:

-   `PySide6`: Para a interface gráfica.
-   `yt-dlp`: Para o download de conteúdo do YouTube.
-   `colorama`: Utilizada nas funções de linha de comando.
-   `FFmpeg`: Essencial para a conversão de áudio para MP3. **O FFmpeg precisa ser baixado separadamente** e seu executável (`ffmpeg.exe` no Windows) deve estar acessível pelo sistema.

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/gabriel448/MP3_Downloader.git
    cd MP3_Downloader
    ```

2.  **Instale as dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Baixe o FFmpeg:**
    * Vá para o [site oficial do FFmpeg](https://ffmpeg.org/download.html) e baixe a versão compatível com seu sistema operacional.
    * Extraia o arquivo e coloque o executável (`ffmpeg.exe` no Windows) na pasta principal do projeto.

## Como Usar

Para executar a aplicação, basta rodar o script da interface gráfica:

```bash
python MP3_UI.py
