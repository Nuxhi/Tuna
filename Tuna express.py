#This is some line of code that was write by Nuxhi#4601 https://github.com/Nuxhi
#If you find this code and you think that some things can be improved, we invite you to come here: https://github.com/Nuxhi/Tuna
#Message to the developer : thank you for using my code, thank you for leaving these few lines, at least the github link as a credit.


import os 
from requests_html import HTMLSession

# Tuna express : configuration

exp_version = '' #Tuna_ALPHA.exe   --->  Don't forget the extension.
version = '' #Tuna_V1
last_version = '' #Tuna V2.1.exe   --->  Don't forget the extension.
filetype = ''
link = "https://github.com/NAME" #Link to your GitHub profile 

#link_update = link+"/REPO NAME/raw/main/"+last_version #Only if you need to download an .exe file
link_update = link+"/REPO NAME/archive/refs/heads/main.zip" 

path = os.getcwd() # assign folder path

def tuna():
    os.chdir(path)
    #print('Please wait, checking for updates. 1/2')
    s = HTMLSession()
    rqt = s.get(link)
    
    #Check the availability of the servers.
    if rqt.ok:
        print('[Console] : Server available  !')
        try:
            title = rqt.html.find('.p-org')[0].text
        except:
            title = ('UKN')
    else:
        print('[Console] : Server unavailable  ! ', rqt)
        # A vous de mettre en place une procédure en cas d'erreur.
   
    if title != version:
        #print('Please wait, checking for updates. 2/2')
        print('update available !\nVersion : ',title,'available,\nDownload in progress...')

        r_upt = s.get(link_update, allow_redirects=True)
        open(last_version, 'wb').write(r_upt.content)
        os.startfile(last_version) 
        exit

    else:
        print('No update available !')

tuna()