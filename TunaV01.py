import os 
import getpass
from requests_html import HTMLSession


# Tuna configuration

exp_version = 'TunaV0.py'
version = 'TunaV01'
last_version = 'TunaV1.py'

link = "https://github.com/Nuxhi" #Lien de votre profile GitHub 
link_update = "https://github.com/Nuxhi/Tuna/raw/main/"+last_version #Lien de téléchargement directe de votre fichier sur GitHub

path = os.getcwd() # assign folder path
username = getpass.getuser() # assign user os


def tuna():

    print('Please wait, checking for updates. 1/2')
    os.chdir(path) # peut importe l'emplacement de votre fichier, Tuna se met la ou vous l'avez executer.
    try:
        os.remove(exp_version)
    except:
        print('')

    #Ouverture de la session HTML, début de la procésdure 

    print('Please wait, checking for updates. 2/2')
    s = HTMLSession()
    rqt = s.get(link)
    
    #Vérification de la disponibilité des serveurs.
    if rqt.ok:
        print('[Console] : Serveur disponible !')
    else:
        print('[Console] : Serveur indisponible ! ', rqt)
   
    try:
        title = rqt.html.find('.p-org')[0].text
    except:
        title = ('UKN')

    if title != version:
        print('update disponible !\nVersion : ',title,'disponible,\nTéléchargement en cours...')
        r_upt = s.get(link_update, allow_redirects=True)
        open(last_version, 'wb').write(r_upt.content)

        os.startfile(last_version) 
        print('start', last_version)
        exit

    else:
        print('Aucune update disponible !')