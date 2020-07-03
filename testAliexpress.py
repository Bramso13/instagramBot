#import requests

#url = 'https://www.google.com/'
#r = requests.get(url)

#print(r.text)
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def makeSite(nom):
    return "https://www." + nom + ".com"

driver = webdriver.Chrome("/Users/Bramso/Documents/chromedriver83")

listeReseauxSociaux = ['instagram']
i = 0
for i in range(len(listeReseauxSociaux)):
    nomSite = makeSite(listeReseauxSociaux[i])
    print nomSite
    driver.get(nomSite)
    time.sleep(2)
    if(listeReseauxSociaux[i] == 'instagram'):
        inputI = driver.find_element_by_name('username')
        inputIdentifiant = 'VOTREIDENTIFIANT'
        inputI.send_keys(inputIdentifiant)
        time.sleep(2)
        inputPass = driver.find_element_by_name('password')
        inputPassword = 'VOTREMOTDEPASSE'
        inputPass.send_keys(inputPassword)
        time.sleep(1)
        form = driver.find_element_by_css_selector('form')
        form.submit()
        time.sleep(5)
        butPlusTard = driver.find_element_by_css_selector('button')
        butPlusTard.click()
        time.sleep(12)
        driver.find_element_by_class_name('aOOlW').click()
        time.sleep(15)
        driver.find_element_by_css_selector('input[type=text]').send_keys('#covid')
        time.sleep(2)
        driver.find_element_by_css_selector('input[type=text]').send_keys(Keys.ENTER)
        time.sleep(9)
        driver.find_element_by_class_name('sqdOP').click()
        collectionPosts = driver.find_elements_by_css_selector('.v1Nh3 a')
        for j in range(len(collectionPosts)):
            collectionPosts[j].click()
            time.sleep(2)
            commentaire = []
            user = driver.find_element_by_css_selector('.C4VMK h2').text.encode('utf-8')
            description = driver.find_element_by_css_selector('.C4VMK span').text.encode('utf-8')
            lienimg = driver.find_element_by_css_selector('.KL4Bh img').get_attribute('src')
            collectionCom = driver.find_elements_by_css_selector('.Mr508 .C4VMK span')
            print commentaire
            print user
            print description
            print lienimg
            with open('data.txt', 'a') as fichier:
                fichier.write('<post>')
                fichier.write('<site>'+listeReseauxSociaux[i]+'</site>')
                fichier.write('<type>post</type>')
                fichier.write('<username>'+user+'</username>')
                fichier.write('<description>'+description+'</description>')
                fichier.write('<img>'+lienimg+'</img')
                fichier.write('</post>')
            driver.find_element_by_css_selector('.fm1AK button.wpO6b').click()
            time.sleep(3)
        print collectionPosts




    time.sleep(10)


