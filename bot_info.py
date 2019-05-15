#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import telepot
import time
from telepot.loop import MessageLoop
import urllib3
import urllib
import urllib3.request
from pprint import pprint
from random import randint
from InstagramAPI import InstagramAPI
global bot
import re
foto = open("C:\Users\devnu\Downloads\Hikxploit-master\oto_programmate.txt",'r').read().splitlines()
testi_orari = open("C:\Users\devnu\Downloads\Hikxploit-master\esto_orari.txt", 'r').read().splitlines()
print foto
"""proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))"""

admin = ['119080849','366813371','131527423','438967874','130752603','411115708']
ore_minuti = ['12:30','16:30','19:10']
bot = telepot.Bot('616834617:AAH6osb_zWjSy0dtOzA7r90qpKEeCa-TNW8')

def handle(msg):
    acc = 0
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)
    username = msg['from']['username']
    user_id = msg['from']['id']
    for i in admin:
        if str(user_id) == i:
            acc = 1
    if content_type == 'text' and acc == 1:
        text1 = msg['text']
        text = text1.split()
        if text[0] == '/new':
            try:
                testo_pic = text[1]
                orario_pic = text[2]
                with open("C:\Users\devnu\Downloads\Hikxploit-master\esto_orari.txt", "a") as testOrari:
                    testOrari.write(testo_pic+ '___'+orario_pic)
                    testOrari.write("\n")
                bot.sendMessage(chat_id,'Fatto')
            except IndexError:
                bot.sendMessage(chat_id,'Ti serve un testo e un orario!')
        if text[0] == 'send_pic':
            Instagramapi = InstagramAPI("username", "password")
            Instagramapi.login()
            photopath = "/home/Nothing/picAgADBAADVq8xG2OpqVMQYvFVjMXtWRfyHhsABPHqpo76XjjZnSsDAAEC.png"
            caption = "test_pubb_inf_suicidio"
            Instagramapi.uploadPhoto(photopath, caption=caption)
            bot.sendMessage(chat_id, "Pubblicato")
        if text[0] == "/list":
            foto_aggiornato_lista = open("C:\Users\devnu\Downloads\Hikxploit-master\oto_programmate.txt",'r').read().splitlines()
            testi_aggiornato = open("C:\Users\devnu\Downloads\Hikxploit-master\esto_orari.txt", 'r').read().splitlines()
            print foto_aggiornato_lista
            print testi_aggiornato
            i = 0
            try:
                while i < len(foto_aggiornato_lista):
                    bot.sendMessage(chat_id, str(i + 1)+ ')    ' + foto_aggiornato_lista[i] + '   |  ' + testi_aggiornato[i])
                    i +=1
            except IndexError:
                bot.sendMessage(chat_id, 'errore, non me lo dire che tanto non mi importa')
        if text[0] == '/start':
            bot.sendMessage(chat_id,
                            'Benvenuto, questo è il bot di informatica del suicidio per la programmazione dell pic su instagram\n'
                            'i comandi disponibili sono:\n'
                            '1)/edit_testo (numero pic) testo scelto[WIP]\n'
                            '2)/edit_orario (numero_pic) orario scelto[WIP]\n'
                            '3)/list visualizza le pic programmate\n'
                            '4)/new (numer_pic) testo + orario \nPer caricare una nuova pic ti bastera mandarmi una pic, ti verrà fornito un numero\n'
                            ' Quel numero lo potrai usare nel comando new per impostare orario e testo della pic desiderata\n'
                            '5)/pubb (numero pic) [se vuoi pubblicare una pic senza aspettare l''orario][WIP]')
        if text[0] == '/reboot' and int(user_id) == int(130752603):
            bot.sendMessage(chat_id, 'Reboot in corso...')
            time.sleep(2)
        if text[0] == '/edit_testo':
            bot.sendMessage(chat_id,"HO DETTO WIP PORCA PUTTANA!")
        if text[0] == '/edit_orari':
            bot.sendMesssage(caht_id,"WIP DIO CANE WIP, NON FUNZIONA PORCA MADONNA FUORI DALLA MIA PALUDE")
        if text[0] == '/pubb':
            bot.sendMessage(chat_id, "SEMPRE WIP, INCREDIBILE VERO FRA? SE DICO WIP E WIP!")
        elif text[0] == '/reboot' and int(user_id) != int(130752603):
            bot.sendMessage(chat_id, 'Non sei nothing')

    elif content_type == 'photo':
        random = str(randint(0,150))
        path_foto_download = './pic'+ username+ random + '.png'
        file_id = msg['photo'][-1]['file_id']
        bot.download_file(file_id, path_foto_download)
        print foto
        with open("C:\Users\devnu\Downloads\Hikxploit-master\oto_programmate.txt", "a") as foto_download:
            foto_download.write(username + random + '.png')
            foto_download.write("\n")
        foto_aggiornato = open("C:\Users\devnu\Downloads\Hikxploit-master\oto_programmate.txt", "r").read().splitlines()
        posizione_foto = foto_aggiornato.index(username + random + '.png')
        bot.sendMessage(chat_id, 'la foto è in posizione:'+ str(posizione_foto))
        bot.sendMessage(chat_id, 'ora usa il comando /new (testo) + (orario) per impostare a che ora pubblicare ciò, ricorda il tempismo è fondamentale per non confodersi\nquindi hai esattamente 180 secondi per inserire un testo anche base,dopo di che la pic verrà eliminata')
    elif content_type == 'text' and acc == 0:
        bot.sendMessage(chat_id, 'non sei admin')


MessageLoop(bot, handle).run_as_thread()
print("starting")b
while True:
    localtime = time.localtime(time.time())
    meseLocale = localtime[1]
    giornoLocale = localtime[2]
    oraLocale = localtime[3]
    minutiLocale = localtime[4]
    for orario in testi_orari:
        """for ore in ore_minuti:
            pattern_minuti = r'(\:).*'
            pattern_ore = r'.*(\:)'
            matchMinuti = re.search(pattern_minuti, ore)
            matchOre = re.search(pattern_ore, ore)
            oreRaw = matchOre.group()
            minutiRaw = matchMinuti.group()
            ore = oreRaw[:2]
            minuti = minutiRaw[1:]"""
        pattern = r'(\___).*'
        patternMese = r'(\/).*'
        patternGiorno = r'.*(\/)'
        match = re.search(pattern, orario)
        timeSetRaw = match.group()
        timeSet = timeSetRaw[3:]
        matchMese = re.search(patternMese, timeSet)
        meseRaw = matchMese.group()
        mese = meseRaw[1:]
        matchGiorno = re.search(patternGiorno, timeSet)
        giornoRaw = matchGiorno.group()
        giorno = giornoRaw[:2]
        if int(giorno) == giornoLocale and int(mese) == meseLocale and oraLocale == 19 and minutiLocale == 29 :
            Instagramapi = InstagramAPI("gibo.py", "xxxxxxx")
            Instagramapi.login()
            photopath = "C:\Users\devnu\Pictures\photo_2019-02-25_23-43-36.jpg"
            caption = "test_pubb_inf_suicidio"
            Instagramapi.uploadPhoto(photopath, caption=caption)
            time.sleep(60)





while 1:
    time.sleep(10)


