import os 
import getpass
from requests_html import HTMLSession

# Tuna express : configuration

exp_version = 'TunaV0.py'
version = 'TunaV01'
last_version = 'TunaV1.py'
filetype = 'py'

link = "https://github.com/Nuxhi" #Lien de votre profile GitHub 

if filetype == 'py':
    link_update = "https://github.com/Nuxhi/Tuna/archive/refs/heads/main.zip"

if filetype == 'exe':
    link_update = "https://github.com/Nuxhi/Tuna/raw/main/"+last_version #Lien de téléchargement directe de votre fichier sur GitHub

path = os.getcwd() # assign folder path
username = getpass.getuser() # assign user os


def tuna():
    os.chdir(path)
    print(path) 
    
    print('Please wait, checking for updates. 1/2')
    s = HTMLSession()
    rqt = s.get(link)
    
    #Vérification de la disponibilité des serveurs.
    if rqt.ok:
        print('[Console] : Serveur disponible !')
        try:
            title = rqt.html.find('.p-org')[0].text
        except:
            title = ('UKN')
    else:
        print('[Console] : Serveur indisponible ! ', rqt)
   
    if title != version:
        print('Please wait, checking for updates. 2/2')
        print('update disponible !\nVersion : ',title,'disponible,\nTéléchargement en cours...')
        print(title, link_update)
        r_upt = s.get(link_update, allow_redirects=True)
        open(last_version, 'wb').write(r_upt.content)
        os.startfile(last_version) 
        exit

    else:
        print('Aucune update disponible !')

tuna()
