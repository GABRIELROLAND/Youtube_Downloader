
from pytube import YouTube
from bs4 import BeautifulSoup
import requests

file_name = ''

def download_yt(url):

    yt= YouTube(url)
    #print(yt.streams.filter(only_audio=False).all())
    choice = input('Digite a para áudio e v para vídeo: ')
    if choice == 'a':
        yt.streams.get_by_itag(140).download()
    else:
        yt.streams.get_by_itag(137).download()

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
    musica = input('Digite a música a ser baixada: ')
    musica = musica.replace(" ","+")
    source = requests.get('https://www.youtube.com/results?search_query='+musica).text
    soup = BeautifulSoup(source,"html5lib")
    count=0
    vetor=[]
    for link in soup.find_all('div',class_="yt-lockup-content"):
        download_link = link.find('a')['href']
        vetor.insert(count,('youtube.com'+download_link))
        print(str(count)+"-"+'Nome: '+link.h3.a.text)
        print('Link: youtube.com'+download_link+'\n')
        count +=1
    escolha = int(input('Escolha a opção para fazer download: '))
    download_yt(vetor[escolha])
main()