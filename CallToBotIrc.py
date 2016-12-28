# coding=utf-8

import socket
from urllib2 import Request, urlopen, build_opener, HTTPCookieProcessor
from cookielib import CookieJar
from urllib import urlencode
from macpath import split
import re
from math import sqrt, floor

network = 'irc.root-me.org'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK botty_chall1\r\n' )
irc.send ( 'USER botty botty botty :Python IRC\r\n' )
irc.send ( 'JOIN #Root-Me_Challenge\r\n' )


login = 'anas.guetarni@gmail.com'
password = ''

# On active le support des cookies pour urllib2
#cookiejar = cookielib.CookieJar()
cookiejar = CookieJar()
urlOpener = build_opener(HTTPCookieProcessor(cookiejar))

# On envoie login/password au site qui nous renvoie un cookie de session
values = {'var_ajax':'form', 'page':'login', 'lang':'fr', 'formulaire_action':'login','formulaire_action_args':'UazOXKaaPbFxmeYLBrGBd/dPerFiCwa6K+OzK8NXn5kooOI4r5P6cawt54/MfYin/4gjl1HCa9K2lyGj6sd5+3Ff4eLKEgsS8PY1OIQkg31dDXK7eLWHvnlzwJIClKAYheUK1zWokWYhVUpDRhvl1pJB/g==', 'var_login':login, 'nothing':'', 'password':password,  'session_remember':'oui' }
data = urlencode(values)
request = Request("http://www.root-me.org/spip.php?page=login&lang=fr", data)
url = urlOpener.open(request)  # Notre cookiejar reçoit automatiquement les cookies
page = url.read(500000)

# On s'assure qu'on est bien logué en vérifiant la présence du cookie "id"
# (qui est - sur le site imdb.com - le cookie contenant l'identifiant de session.)
if not 'spip_session' in [cookie.name for cookie in cookiejar]:
     raise ValueError, "Echec connexion avec login=%s, mot de passe=%s" % (login,password)

print "Connection Ok !"

while True:
    data = irc.recv ( 4096 )
    print irc.send ('JOIN #Root-Me_Challenge\r\n')
    if data.find ( 'PING' ) != -1:
       irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    print data
    #nb = irc.send ('PRIVMSG Candy !ep1 -rep <reponse>\r\n')
    irc.send ('PRIVMSG Candy !ep1 -rep <reponse>\r\n')
    data = re.findall(r'.*(\d+/\d+).', data)
    print 'test = ' + str(data)

    if len(data)>0:
        data = data[0]
        print data
        data = data.split('/')

        nb_1 = data[0].strip()
        nb_2 = data[1].strip()

        soluce = round(sqrt(int(nb_1))*int(nb_2),2)

        print soluce

        pageVerif = 'http://www.root-me.org/fr/Challenges/Programmation/Retour-au-college'
        values = {'var_ajax':'form', 'id_rubrique':'17', 'id_challenge':'146', 'page':'challenge', 'formulaire_action':'validation_challenge','formulaire_action_args':'UazOXKaaPbFxmeYLBrGBd/dPerFiCwa6K+OzK8NXn5kooOI4r5P6cawt54/MfYin/4gjl1HCa9K2lyGj6sd5+3Ff4eLKEgsS8PY1OIQkg31dDXK7eLWHvnlzwJIClKAYheUK1zWokWYhVUpDRhvl1pJB/g==', '_jeton':'aa08a9c8f8fd76d5cecb0446b35d1682bc2c1e47', 'passe':soluce, 'nobot':'' }
        data = urlencode(values)
        request = Request(pageVerif, data)
        url = urlOpener.open(request)
        page = url.read(500000)

        print page
        break
