--MP3 Downloader for YouTube


----------------
-- Descrição --
----------------

Este projeto é uma aplicação de desktop para Windows que permite baixar o áudio de vídeos ou playlists do YouTube e salvá-los como arquivos MP3. A interface gráfica foi construída com PySide6 para ser simples e intuitiva.

O programa utiliza a biblioteca 'yt-dlp' para gerenciar os downloads e o 'FFmpeg' (já incluído no projeto) para realizar a conversão para MP3, garantindo alta qualidade de áudio. O executavel se encontra na pasta dist, bate abrir e usar.

--------------------
-- Funcionalidades --
--------------------

- Download de Vídeo Único: Cole a URL de um vídeo para baixar seu áudio em MP3.
- Download de Playlist: Cole a URL de uma playlist para baixar todos os vídeos em MP3.
- Interface Gráfica Simples: Uma janela fácil de usar para colar a URL e iniciar o download.
- Seleção de Diretório: Permite escolher onde salvar os arquivos MP3.
- Barra de Progresso e Status: Acompanhe o andamento do download em tempo real.
- Processamento em Segundo Plano: A interface não trava durante os downloads.


------------------------------------------
-- Como Executar a Partir do Código-Fonte --
------------------------------------------

Para rodar o projeto no seu computador de desenvolvimento, siga os passos abaixo.

1.  **Pré-requisitos:**
    - Python 3 instalado (visite python.org).

2.  **Clone o Repositório:**
    - Baixe ou clone este repositório para a sua máquina.

3.  **Instale as Dependências:**
    - Abra o terminal (Prompt de Comando, PowerShell, etc.) na pasta do projeto e execute o comando abaixo. Ele instalará todas as bibliotecas necessárias listadas no arquivo `requirements.txt`.

      pip install -r requirements.txt

4.  **Execute a Aplicação:**
    - Após a instalação das dependências, execute o seguinte comando no terminal:

      python MP3_UI.py


-----------------------------------
-- Como Gerar o Executável (.exe) --
-----------------------------------

Este projeto já está configurado para ser compilado em um único arquivo executável (.exe) que inclui todas as dependências, inclusive o FFmpeg.

1.  **Instale o PyInstaller:**
    - Se você ainda não o tem, instale-o com o comando:

      pip install pyinstaller

2.  **Gere o Executável:**
    - O arquivo `MP3_Downloader.spec` já contém todas as configurações necessárias. Para gerar o executável, simplesmente execute o PyInstaller com este arquivo de especificação. No terminal, na pasta do projeto, digite:

      pyinstaller MP3_Downloader.spec

3.  **Encontre o Arquivo:**
    - Após o processo terminar, o arquivo `MP3_Downloader.exe` estará pronto para ser usado dentro da pasta `dist`. Este arquivo pode ser compartilhado e executado em outros computadores com Windows sem a necessidade de instalar nada.
