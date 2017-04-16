import discord
import random
import os
import time
import sys
import datetime
from pprint import pprint
import requests
import pyowm
import re
import time
import math 
import json
import urllib.request
import urllib
import urllib.parse
from bs4 import BeautifulSoup

os.chdir("/Shitty_bot_public")
owm = pyowm.OWM('pyowm API KEY')
client = discord.Client()


async def joinVoiceChannel():

    channel = client.get_channel('Voice channel number here')
    
    
    print('Bot joined the Channel')
    return(channel)



@client.event
async def on_message(message):
    opq = 0
    
    qui = str(message.author)
    azerty = 0
    nombre = random.randint(0,100)
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

        
    elif message.content.startswith('!song'):
        
        await client.send_message(message.channel, "What song do you want to play?")
        songname = await client.wait_for_message(author=message.author)
        songname = str(songname.content)
        query = urllib.parse.quote(songname,safe='%20')

        print(query)
        response = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
        html = response.read()
        soup = BeautifulSoup(html)
        songs = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            print ('https://www.youtube.com' + vid['href'])
            songs.append("https://www.youtube.com" + vid['href'])
        i=0
        while i != 3:
            print("I = "+songs[i])
            i=i+1

        a = title_song = []
        i = 0
        while i != 3:
            response = urllib.request.urlopen(songs[i])
            html = response.read()
            soup = BeautifulSoup(html)
            url01 = "https://www.youtube.com/watch?v=mtf7hC17IBM"
            for thing in soup.findAll(attrs={'class':'watch-title'}):
                title_song.append(thing['title'])
            i = i+1
        print(title_song)
        await client.send_message(message.channel, "Which one is the good song?")
        await client.send_message(message.channel, "\n".join(a))
        songchoice = await client.wait_for_message(author=message.author)
        songchoice = int(songchoice.content)
        voice = await client.join_voice_channel(await joinVoiceChannel())
        player = await voice.create_ytdl_player(songs[songchoice])
        player.start()
        await client.send_message(message.channel,"Playing : {0}".format(player.title))
        stop = await client.wait_for_message(author=message.author)
        if message.content.startswith('!song'):
            player.stop()
            await voice.disconnect()


    elif message.content.startswith('!stop'):
        
        await voice.disconnect()
    elif message.content.startswith('!gangsta'):

        voice = await client.join_voice_channel(await joinVoiceChannel())
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=vQNtTW2sIqE')
        player.start()
        await client.send_message(message.channel,"Playing : {0}".format(player.title))
        #rep = await client.wait_for_message(author=message.author)
        print("likes : "+str(player.likes)+" Dislikes : "+str(player.dislikes))
        """async def end_song():
            while player.is_playing() == True:
                pass
            else:
                player.stop()
                await voice.disconnect()
        await end_song()"""
        #await voiceout(rep, player, voice)



    elif message.content.startswith('!coinflip'):
        result = random.randint(0,1)
        if result == 1:
            await client.send_message(message.channel, "Heads")
        else:
            await client.send_message(message.channel, "Tails")

    elif message.content.startswith('!rolladice'):
        dice = random.randint(0,6)
        dice = str(dice)
        await client.send_message(message.channel, dice)



    elif message.content.startswith('!8ball'):
        file = open("log.txt","a")
        phrases = ["Totally","I think yes","Probably not","¯\_(ツ)_/¯ maybe ¯\_(ツ)_/¯","You'll find the answer in your but","NEIN NEIN NEIN NEIN!!","Hell no!","As the old chineese proverb says: DAAAAAYUM HELL YEAH!"]
        num = random.randint(0,7)
        reponse = phrases[num]
        await client.send_message(message.channel, reponse)
        print ("{0} : {1} asked boules magiques".format(datetime.datetime.now(),qui) )
    
    elif message.content.startswith('!play'):
        file = open("log.txt","a")
        file.write("{0} : {1} asked play\n".format(datetime.datetime.now(),qui))
        try:
            print ("{0} : {1} asked play".format(datetime.datetime.now(), qui) )
            await client.send_message(message.channel, "Guess the number between 0 and 100")
            num = random.randint(0,100)
            choix = await client.wait_for_message(author=message.author)
            choix = float(choix.content)
            play = 1
            file = open("log.txt","a")
            file.write("{0} : {1} asked play".format(datetime.datetime.now(),qui))
            file.close()

            while play == 1:
                if choix < num:
                    await client.send_message(message.channel, "More")
                    print("plus")
                    choix = await client.wait_for_message(author=message.author)
                    choix = float(choix.content)
                elif choix > num:
                    await client.send_message(message.channel, "Less")
                    print("moins")
                    choix = await client.wait_for_message(author=message.author)
                    choix = float(choix.content)
                elif choix == num:
                    await client.send_message(message.channel, "Yaaaaaaaaaaaaaaaaay!")
                    print("won")
                    play = 0
        except:
            await client.send_message(message.channel, "This isn't a number..")
            time.sleep(1)
            await client.send_message(message.channel, "..so you loose I guess?")
            print("bug")
            


    elif message.content.startswith('!dis'):
        if qui == "Bastos#8837":
            await client.send_message(message.channel,"lol no")
        else:
            file = open("log.txt","a")
            file.write("{0} : {1} asked disconnect\n".format(datetime.datetime.now(),qui))                              #TEST
            print ("{0} : {1} asked dc".format(datetime.datetime.now(),qui) )
            await client.send_message(message.channel,"Bye bitchies")
            await client.logout()
        

    
    elif message.content.startswith('!spam'):
        file = open("log.txt","a")
        print ("{0} : {1} asked spam".format(datetime.datetime.now(),qui) )
        if qui == "FunkyBOT#9166":
            file.write("{0} : {1} asked spam(refusé)\n".format(datetime.datetime.now(),qui))
            await client.send_message(message.channel,"No spam for you")
        else:
            file.write("{0} : {1} asked spam\n".format(datetime.datetime.now(),qui))
            await client.send_message(message.channel,"__**THE ULTIMATE SPAM BOT HAS BEEN SUMMONED**__\nWhat message do you want to spam?")
            guess = await client.wait_for_message(author=message.author)
            await client.send_message(message.channel,"How many times?")
            guess2 = await client.wait_for_message(timeout=10.0,author=message.author)
            i=0
            guess2 = int(guess2.content)
            await client.send_message(message.channel,"__**SPAM INCOMING**__")
            while i < guess2:
                await client.send_message(message.channel,guess.content)
                i=i+1
            else :
                await client.send_message(message.channel,"*End of spam*")

    elif message.content.startswith('!commands'):
        file = open("log.txt","a")
        file.write("{0} : {1} asked commands\n".format(datetime.datetime.now(),qui))
        file.close()
        print ("{0} : {1} asked commands".format(datetime.datetime.now(),qui) )
        await client.send_message(message.channel,"```!spam\ncalculer\n!boules magiques\nping\n!square\n!lulz\n!lel\n!funkybot\n!bye\n!play\n!connard\n!meteo\n!film\n!caca\nimage shit\n!meteo\n!dc```")

    elif message.content.startswith('!film'):

        file = open("log.txt","a")
        print ("{0} : {1} asked film".format(datetime.datetime.now(),qui) )
        file.write("{0} : {1} asked film\n".format(datetime.datetime.now(),qui))

        works = 0
        while works == 0 :
            try:
                rand = random.randint(10,9900)
                rand = str(rand)
                print(rand)
                url = "https://api.themoviedb.org/3/movie/"+rand+"?api_key=387be639893de8792299f4ce3db41af0"
                response = urllib.request.urlopen(url)
                data = response.read().decode("utf-8")
                a = json.loads(data)
                titre = a["original_title"]
                date = a["release_date"]
                resume = a["overview"]
                notes = a["vote_average"]
                notes = str(notes)
                notes_total = a["vote_count"]
                notes_total = str(notes_total)
                await client.send_message(message.channel,"Title : "+titre+"\n"+"Release date : "+date+"\n"+"Resume : "+resume+"\n"+"Rating : "+notes+"/10\n"+"Numbers of ratings : "+notes_total)
                works = 1
            except:
                print("No movie found for the ID : "+rand)
                works = 0

    elif message.content.startswith('!weather'):
        file = open("log.txt","a")
        file.write("{0} : {1} asked meteo\n".format(datetime.datetime.now(),qui))
        print ("{0} : {1} asked meteo".format(datetime.datetime.now(),qui) )
        await client.send_message(message.channel,"which city?")
        ville = await client.wait_for_message(author=message.author)
        ville = str(ville.content)
        observation = owm.weather_at_place(ville)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')
        w=str(w)
        m = re.search('(?<=status=)(.*)', w)
        meteo=(m.groups())
        meteo = str(meteo)
        temp = str(temp)
        reponse = ("Temps : " + meteo[2:-4])
        reponse_temp = (temp[1:-1])
        try:
            await client.send_message(message.channel,reponse)
            await client.send_message(message.channel,reponse_temp)
        except:
            await client.send_message(message.channel,"error")

    elif message.content.startswith('!jerk'):
        print ("{0} : {1} asked insult".format(datetime.datetime.now(),qui) )
        #file.write("{0} : {1} asked insult\n".format(datetime.datetime.now(),qui))
        insulte1=['You bloody','You poor','You fat']
        insulte2=['fuckface','dickhead','asshole']
        insulte3=['you are','you should be','you look like','you stink as much as','you worth less than ']
        insulte4=['a pile of your mom\'s shit','a hobbo\'s underwear','a goat','a glass of puke','some rotten cyprin']
        insulte5=['which flows from everywhere','shitting on himself','always ready to lick everybody\'s ass','sweating from the ass','unclean','disgusting']
        insulte6=['I\'d like to','I dream to','I\'m dying to','I laugh at the idea of']
        insulte7=['burst your face','kick your ass','crush your balls','puke on you','piss on your face','put my balls on your forehead']
        insulte8=['in front of your family','on your grandpa\'s grave','on your grandma\'s grave','in front of your bitch','at your job','at your mother\'s house','in front of your grandpa']
        insulte9=['until the morning','just for fun','if you got 5 minutes','while watching tv','while I\'m fucking your mom']
        sentence = insulte1[random.randint(0,len(insulte1) -1)],insulte2[random.randint(0,len(insulte2) -1)],',',insulte3[random.randint(0,len(insulte3) -1)],insulte4[random.randint(0,len(insulte4) -1)],insulte5[random.randint(0,len(insulte5) -1)],',',insulte6[random.randint(0,len(insulte6) -1)],insulte7[random.randint(0,len(insulte7) -1)],insulte8[random.randint(0,len(insulte8) -1)],insulte9[random.randint(0,len(insulte9) -1)]
        #print(' '.join(sentence))
        await client.send_message(message.channel,"{0}".format(' '.join(sentence)))
        #await client.send_message(message.channel,"Espece de {1} {2}, {3} {4} {5}, {6} {7} {8} {9}".format(insulte1[random.randint(0,7)],insulte2[random.randint(0,7)],insulte3[random.randint(0,5)],insulte4[random.randint(0,7)],insulte5[random.randint(0,7)],insulte6[random.randint(0,7)],insulte7[random.randint(0,7)],insulte8[random.randint(0,7)],insulte9[random.randint(0,7)]) )
        await client.send_message(message.channel,"With love, Shitty Bot <3")


@client.event
async def on_ready():
    os.chdir("/shitty_bot")
    clear = lambda: os.system('cls')
    #os.system('set PATH=%PATH%;C:/ffmpeg/bin/ffmpeg.exe')
    
    clear()
    def delay_print(s):
        for c in s:
            sys.stdout.write( '%s' % c )
            sys.stdout.flush()
            time.sleep(0.005)
    delay_print(""" _____ _     _ _   _                _           _     _____  _____  __  
/  ___| |   (_) | | |              | |         | |   |  _  ||  _  |/  | 
\ `--.| |__  _| |_| |_ _   _ ______| |__   ___ | |_  | |/' || |/' |`| | 
 `--. \ '_ \| | __| __| | | |______| '_ \ / _ \| __| |  /| ||  /| | | | 
/\__/ / | | | | |_| |_| |_| |      | |_) | (_) | |_  \ |_/ /\ |_/ /_| |_
\____/|_| |_|_|\__|\__|\__, |      |_.__/ \___/ \__|  \___(_)\___(_)___/
                        __/ |                                           
                       |___/                                            """)

    print("\nMade by Sebastien.M")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_status(game=discord.Game(name='shit'))

client.logout()
client.run('TOKEN')
