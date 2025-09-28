import os
import time
from funcoes import url_verify, local_verify,playlist_downloader,mp3_downloader


url = None

#loop principal de acoes
while True:
    local = None
    i = None
    print("*********MP3 Downloader*********")
    print()
    p_or_v = input("Deseja baixar uma [P]laylist ou um [V]ideo especifico?: ").lower()
    
    if not (p_or_v.startswith('p') or p_or_v.startswith('v')):
        os.system('cls')
        print('Comando invalido!')
        continue
    print()
    url = input("Cole a url aqui: ")
    if url_verify(url):
        continue
    
    print()
    local = input('Digite o local de download (caso seja o mesmo do programa deixe em branco): ')
    local = local_verify(local)
    if local==0:
        continue
    #definindo de vai baixar playlist ou um video individual
    if p_or_v.startswith('p'):
        os.system('cls')
        sucesso = playlist_downloader(url, local)
    else:
        os.system('cls')
        sucesso = mp3_downloader(url, local)
    if sucesso:
        print("\narquivos baixados e convertidos!!\n")
    else:
        print("\n[ERRO] Nenhum áudio foi baixado. A playlist ou audio pode ser privada/o, não existir ou estar vazia no caso de playlist.\n")
    
    while True:
        choice = input("Deseja fazer outro download?: ").lower()
        os.system('cls')

        if choice.startswith('s'):
            break
        elif choice.startswith('n'):
            i = True
            break
        else:
            print('Comando invalido!')
    if i:
        break

os.system('cls')
print("sessao finalizada!")
time.sleep(1)
    
        
        

        
