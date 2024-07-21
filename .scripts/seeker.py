import time
import random
import requests
from bs4 import BeautifulSoup

web_urls="""
https://deviantart.com/
https://zillow.com/profile/
https://yelp.com/user_details/
https://linkedin.com/in/
https://skype.com/
https://trulia.com/profile/
https://sketchfab.com/
https://tidal.com/browse/artist/
https://soundclick.com/
https://snapchat.com/add/
https://open.spotify.com/user/
https://zomato.com/
https://xboxgamertag.com/search/
https://society6.com/
https://ebay.com/usr/
https://500px.com/
https://profiles.wordpress.org/
https://weheartit.com/
https://duolingo.com/profile/
https://houzz.com/user/
https://twitch.tv/
https://vimeo.com/
https://kickstarter.com/profile/
https://soundcloud.com/
https://medium.com/@
https://xing.com/profile/
https://behance.net/
https://fitbit.com/user/
https://redbubble.com/people/
https://lendingclub.com/public/
https://reddit.com/user/
https://steamcommunity.com/id/
https://tripadvisor.com/members/
https://paypal.me/
https://mixcloud.com/
https://quikr.com/user/
https://angel.co/
https://weibo.com/
https://udemy.com/user/
https://caringbridge.org/visit/
https://etsy.com/people/
https://meetup.com/members/
https://flickr.com/people/
https://ko-fi.com/
https://twitter.com/
https://patreon.com/
https://overdrive.com/accounts/identificador/
https://imgur.com/user/
https://keybase.io/
https://crunchbase.com/person/
https://last.fm/user/
https://instagram.com/
https://etoro.com/people/
https://venmo.com/
https://github.com/
https://quora.com/profile/
https://goodreads.com/
https://strava.com/athletes/identificador/
https://badoo.com/profile/
https://hootsuite.com/
https://instacart.com/storefronts/
https://reverbnation.com/
https://imdb.com/user/
https://instructables.com/member/
https://myanimelist.net/profile/
https://dribbble.com/
https://pinterest.com/
https://slideshare.net/
https://discordapp.com/users/identificador/
https://indiegogo.com/individuals/
https://thingiverse.com/
https://telegram.me/
https://gaiaonline.com/profile/
https://hubpages.com/@
https://tiktok.com/@
https://couchsurfing.com/people/
https://gofundme.com/
https://care.com/profile/
https://giphy.com/
https://tumblr.com/blog/
https://evernote.com/
https://youtube.com/
https://booking.com/profile/
https://kaggle.com/
https://facebook.com/
https://vsco.co/
https://hackerrank.com/
https://okcupid.com/profile/
https://user.qzone.qq.com/
https://ello.co/
https://community.fandom.com/wiki/User:
https://mixer.com/
https://.academia.edu/
https://bitbucket.org//
https://gravatar.com/
https://dailymotion.com/
https://www.tripit.com/people/
https://espn.com/
https://myspace.com/
https://issuu.com/
https://www.sonico.com/u/
https://www.speedrun.com/user/
https://.myportfolio.com/
https://genius.com/
https://.livejournal.com/
https://pastebin.com/u/
https://.newgrounds.com/
https://slides.com/
https://.wordpress.com/
https://www.blogger.com/profile/
https://www.instapaper.com/p/
https://gist.github.com/
https://gitlab.com/
https://anchor.fm/
https://medium.com/@
https://www.instructables.com/member/
https://kik.me/
https://www.ted.com/profiles/
https://flipboard.com/@
https://sourceforge.net/u/
https://the-dots.com/users/
https://www.smule.com/
https://codepen.io/
https://www.interpals.net/
https://www.kongregate.com/accounts/
https://www.friendster.io/
https://nanowrimo.org/participants/
https://www.couchsurfing.com/people/
https://ko-fi.com/
https://www.yelp.com/user_details
https://patreon.com/
https://www.hexrpg.com/profile/
https://www.namecheap.com/myaccount/profile/
https://foursquare.com/
https://letterboxd.com/
https://nextdoor.com/profile/
https://listen.tidal.com/artist/
https://yourshot.nationalgeographic.com/profile/
https://pixiv.net/en/users/
https://www.habbo.com/profile/
https://imgur.com/user/
https://www.reverbnation.com/
https://www.strava.com/athletes/
https://dlive.tv/
https://boards.4chan.org/
https://en.wikipedia.org/wiki/User:
https://opensea.io/accounts/
https://archiveofourown.org/users/
https://news.ycombinator.com/user
https://www.zhihu.com/people/
https://9gag.com/u/
https://www.zoosk.com/profile/
https://gab.com/
https://www.flightradar24.com/account/show/
https://www.pandora.com/profile/
https://www.flickr.com/people/
https://www.designspiration.com/
https://lichess.org/@/
https://www.pscp.tv/
https://.dreamwidth.org/
https://www.meetme.com/
https://www.gotinder.com/@
https://dev.to/
https://www.trip.skyscanner.com/user/
https://untappd.com/user/
https://www.hackster.io/
https://www.weasyl.com/~
https://bandcamp.com/
https://disqus.com/by/
https://www.wattpad.com/user/
https://www.kickstarter.com/profile/
https://mastodon.social/@
https://www.gaiaonline.com/profiles/
https://www.discogs.com/user/
https://www.roblox.com/user.aspx
https://www.producthunt.com/@
https://www.faceit.com/en/players/
https://vsco.co/
https://www.myheritage.com/member-xxxxxx/
https://www.younow.com/
https://www.draftkings.com/
https://www.dropbox.com/
https://www.pinshape.com/users/
https://community.fandom.com/wiki/User:
https://www.monster.com/profiles/
https://www.bloglovin.com/@
https://ok.ru/profile/
https://connect.garmin.com/modern/profile/
https://www.blackplanet.com/
https://www.namepros.com/members/.123456/
https://www.curseforge.com/members/
https://www.livescore.com/soccer/competitions/
https://opencritic.com/critic/
https://neocities.org/site/
https://pleroma.site/@
https://.newgrounds.com/
https://habitica.com/profile/
https://www.joinclubhouse.com/@
https://mix.com/
https://directory.libsyn.com/shows/view/id/
https://playoverwatch.com/en-us/career/
https://www.bandlab.com/
https://peertube.fr/accounts/
https://my.opera.com/
https://mathoverflow.net/users/
https://anobii.com//profile
https://www.nicovideo.jp/user/
https://www.npmjs.com/~
https://armorgames.com/user/
https://www.codecademy.com/profiles/
https://kik.me/
https://coub.com/
https://hi5.com/
https://www.mocospace.com/
https://mewe.com/i/
https://line.me/ti/p/
https://flattr.com/@
https://www.gog.com/u/
https://www.elance.com/
https://www.lovecrafts.com/en-gb/user/
https://padlet.com/
https://gamefaqs.gamespot.com/community/
https://kit.co/
https://my.minecraft.net/profile/
https://www.caffeine.tv/
https://www.kongregate.com/accounts/
https://www.bearshare.com/
https://www.playfire.com/
https://friendfeed.com/
https://magic.wizards.com/en/users/
https://developer.mozilla.org/en-US/profiles/
https://muckrack.com/
https://yourshot.nationalgeographic.com/profile/
https://www.plurk.com/
https://mixi.jp/show_profile.pl/
https://www.artstation.com/
https://www.funimation.com/user/
https://www.myfitnesspal.com/profile/
https://www.modelmayhem.com/
https://www.coursera.org/user/
https://tieba.baidu.com/home/main
http://www.cyworld.com/
https://photobucket.com/user/
https://dlive.tv/
https://fortnitetracker.com/profile/all/
https://www.opentable.com/profile/
https://www.noteflight.com/profile/
https://www.patreon.com/
https://www.chess.com/member/
https://aminoapps.com/u/
https://www.jamendo.com/artist/
https://www.movellas.com/user/
https://world.kano.me/users/
https://www.humblebundle.com/user/
https://myanimelist.net/profile/
https://www.ludust.com/members//
https://www.pandora.com/profile/
https://mangadex.org/user/
https://www.gettyimages.com/
https://codeforces.com/profile/
https://www.hitbox.tv/
https://app.clickup.com/@
https://carbonmade.com/
https://archive.org/details/@
https://www.pexels.com/@
https://www.fitocracy.com/profile/
https://community.goodhousekeeping.com/
https://www.photocrowd.com/
https://www.bitchute.com/channel/
https://www.crunchyroll.com/user/
https://www.groupon.com/profile/
https://.itch.io/
https://www.ourgroceries.com/groceries/
https://profiles.joomla.org/
https://mastodon.social/@
https://.en.made-in-china.com/
https://www.gotoquiz.com/profile/
https://path.com/
https://www.houzz.com/user/
https://www.overleaf.com/
"""
status_codes = {

    200: "Posible Coincidencia",
    201: "Creado",
    202: "Aceptado",
    203: "Información no autorizada",
    204: "Sin contenido",
    205: "Restablecer contenido",
    206: "Contenido parcial",
    207: "Multi-estado",
    208: "Ya reportado",
    226: "IM utilizado",
    400: "Solicitud incorrecta",
    401: "No autorizado",
    402: "Pago requerido",
    403: "Prohibido",
    404: "No encontrado",
    405: "Método no permitido",
    406: "No aceptable",
    407: "Se requiere autenticación de proxy",
    408: "Tiempo de espera agotado",
    409: "Conflicto",
    410: "Gone (El recurso ya no está disponible y no lo estará nuevamente)",
    411: "Longitud requerida",
    412: "Precondición fallida",
    413: "Carga útil demasiado grande",
    414: "URI demasiado larga",
    415: "Tipo de medio no soportado",
    416: "Rango no satisfactorio",
    417: "Expectativa fallida",
    418: "Soy una tetera (código de estado de broma)",
    421: "Solicitud mal dirigida",
    422: "Entidad no procesable",
    423: "Bloqueado",
    424: "Dependencia fallida",
    425: "Demasiado pronto",
    426: "Se requiere actualización",
    428: "Requisito previo necesario",
    429: "Demasiadas solicitudes",
    431: "Campos de encabezado de solicitud demasiado grandes",
    451: "No disponible por razones legales",
    500: "Error interno del servidor",
    501: "No implementado",
    502: "Puerta de enlace incorrecta",
    503: "Servicio no disponible",
    504: "Tiempo de espera de la puerta de enlace agotado",
    505: "Versión HTTP no soportada",
    506: "La variante también negocia",
    507: "Almacenamiento insuficiente",
    508: "Bucle detectado",
    510: "No extendido",
    511: "Se requiere autenticación de red"

}

random_usera={

    1:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
    2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.34567",
    3: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36",
    5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Whale/1.0.0.0 Safari/537.36",
    6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 OPR/12.3456.7890 Safari/537.36",
    7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Vivaldi/1.2.3.4 Safari/537.36",
    8: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Brave/9.8.7 Safari/537.36",
    9: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
    10: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"

}

headers= { # Especifica los valores necesarios para que get funcione correctamente
    
    "User-Agent": "{}".format(random_usera.get(random.randint(1,10))),
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Expires': '0'
    
}

save=open(".bdd", "w")
save.write(web_urls)
save.close() 

def pausa():
    input("\nPresiona enter para continuar...")


def buscador():
    global usuario

    while True:
        
        try:
            
            usuario=input("Nombre de usuario a buscar: ")
            
            while len(usuario) == 0:
                usuario=input("Nombre de usuario a buscar: ")
                
        except:
            pass
        
        else:
            print("[Tipo de busqueda] ===> [URL] A [{}]\n".format(usuario))
            
            leer=open(".bdd")
            lectura=leer.readlines()
            
            save=open("capture.txt", "w")
            for word in lectura:
                
                if "\n" in word:
                    word=word.replace("\n","")
                 
                try:
                    soli=requests.get("{}{}".format(word, usuario), timeout=20)            
                    
                    if soli.status_code == 200:
                        save.write("\n[URL] "+word+usuario)
                    #a=soli.status_code
                    
                    print("[URL] {}{}\n[{}]".format(word,usuario,status_codes.get(soli.status_code)))

                except:
                    pass
                    
            # Bloque de finalizacion
            
            save.close()
            leer.close()

            print("\nSiguiente busqueda: [IN WEB]->>60 sec")

            time.sleep(60)
            siguiente()
            break

def siguiente():
    print("[Tipo de busqueda] ===> [IN WEB] A [{}]\n".format(usuario))

    head_up={
        "User-Agent": "{}".format(random_usera.get(random.randint(1,10)))
        }
    
    headers.update(head_up)

    red=[]
    base="https://www.bing.com"
    busca= '/search?q="{}"'.format(usuario)

    try:
        dox=requests.get(base+busca, headers=headers)
        time.sleep(2)
    except:
        pass

    else:
        save=open("capture.txt", "a")
        sopa=BeautifulSoup(dox.text, "html.parser") # Obtengo la web en etiquetas
        
        for word in sopa.find_all("a"): # Busco parametros <a en sopa

            palabra=str(word.get("href")) # Obtengo la etiqueta especifica href

            if "https://" in palabra:
                print("[URL] {}\n[{}]".format(palabra,status_codes.get(dox.status_code)))
                save.write("\n[URL] {}".format(palabra))
            
            if "first=" in palabra:
                red.append(palabra)
        
        for word in red:

            try:
                dox=requests.get(base+word, headers=headers)
                time.sleep(2) # SI SE DESCOMENTA, NO SE ALCANZA A LEER COMPLETA LA PAGINA /ALL time.sleep
            except:
                pass
            
            else:
                sopa=BeautifulSoup(dox.text, "html.parser")
                
                for word_soup in sopa.find_all("a"):

                    palabra=str(word_soup.get("href"))

                    if "https://" in palabra:
                        print("[URL] {}\n[{}]".format(palabra,status_codes.get(dox.status_code)))
                        save.write("\n[URL] {}".format(palabra))

        print("\nDatos de {} guardados en capture.txt!!".format(usuario))
        pausa()
        save.close()

        exit(0)

buscador()