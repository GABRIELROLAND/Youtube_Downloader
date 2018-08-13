from pytube import *
from bs4 import BeautifulSoup
import requests
import os

#Variáveis Globais
test = 'n'
file_name = ''

Down_list=[]

def mass_down():
    global test
    os.system('cls')
    for i in range(0,len(Down_list)):
        down_fixed = Down_list[i].split('+')
        print('===  #'+str(i+1)+' ===' )
        download_yt(down_fixed[0].replace('+',',').replace("'",''),down_fixed[1].replace('+',',').replace("'",''))
        test = input('\n'+'\n'+'Exit ? (y/n): ')
        

def make_list(url_item):
    choice = input('a - Audio (160kbps) // v - Video (1080p): ')
    Down_list.append(url_item+'+'+choice)
    print(Down_list)
    check = input('Do you want to add more items? (y/n): ')
    if (check == 'n'):
        mass_down()
        
def download_yt(url,choice):
    global test
    yt= YouTube(url)
    #print(yt.streams.filter(only_audio=False).all())
    #choice = input('a - Audio (160kbps) // v - Video (1080p): ')
    if choice == 'a':
        print('- Downloading audio from '+url)
        yt.streams.get_by_itag(140).download()
    else:
        print('- Downloading video from '+url)
        yt.streams.get_by_itag(137).download()
    print('\n'+'~ Download Completed ~'+'\n')
    

def main():
    os.system('cls')
    while(test != 'y'):
        musica = input('Name of the Music/Video(or link): ')
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
            opt = int(input('Choose one option to download(#): '))
            opt = vetor[opt]
            make_list(opt)
            #download_yt(opt)
                
    os.system('pause')
main()
