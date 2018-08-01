from pytube import *
from bs4 import BeautifulSoup
import requests
import os

file_name = ''

def download_yt(url):

    yt= YouTube(url)
    #print(yt.streams.filter(only_audio=False).all())
    choice = input('Digite a para áudio e v para vídeo: ')
    if choice == 'a':
        print('Baixando áudio de '+url)
        yt.streams.get_by_itag(140).download()
    else:
        print('Baixando video de '+url)
        yt.streams.get_by_itag(137).download()
    print('~ Download Completo ~')

# def get_extension(url):
#     if 'youtube' in url:
#         download_yt(url)
#         file_name = ''
#     else:
#         splitted = url.split("/")
#         file_name = splitted[-1]
#         if '?' in splitted[-1]:
#             final = splitted[-1].split('?')
#             file_name = final
#         else:
#             file_name = file_name+'.zip'
#     return file_name

def main():
    musica = input('Digite a música ou link a ser baixado do Youtube: ')
    if 'youtube.com' in musica:
        download_yt(musica)
    else:
        musica = musica.replace(" ","+")
        source = requests.get('https://www.youtube.com/results?search_query='+musica).text
        soup = BeautifulSoup(source,"html5lib")
        count=0
        vetor=[]
        for link in soup.find_all('div',class_="yt-lockup-content"):
            download_link = link.find('a')['href']
            vetor.insert(count,('youtube.com'+download_link))
            print(str(count)+" - "+'Nome: '+link.h3.a.text)
            print('Link: youtube.com'+download_link+'\n')
            count +=1
        escolha = int(input('Escolha a opção para fazer download: '))
        escolha = vetor[escolha]
        download_yt(escolha)
    os.system('pause')
main()
