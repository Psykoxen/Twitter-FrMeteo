import json     #Module Json
import log      #Données Login
import time     #Module Time
import tweepy   #Module Twitter
import requests #Module requêtes
import datetime #Module Time II
from meteofrance_api import * #Module météo france
################################################################# - DATA - ############################################################################
"""        
        {'icon': 'p1j', 'desc': 'Ensoleillé'},
        {'icon': 'p1bisj', 'desc': 'Peu nuageux'},
        {'icon': 'p2j', 'desc': 'Eclaircies'},
        {'icon': 'p2bisj', 'desc': 'Variable'},
        {'icon': 'p3j', 'desc': 'Très nuageux'},
        {'icon': 'p3bisj', 'desc': 'Couvert'},
        {'icon': 'p4j', 'desc': 'Ciel voilé'},
        {'icon': 'p5j', 'desc': 'Brume'},
        {'icon': 'p8j', 'desc': 'Brouillard givrant'},
        {'icon': 'p12j', 'desc': 'Pluies éparses'},
        {'icon': 'p12bisj', 'desc': 'Rares averses'},
        {'icon': 'p13j', 'desc': 'Pluies éparses'},
        {'icon': 'p13terj', 'desc': 'Pluie faible'},
        {'icon': 'p14j', 'desc': 'Pluie'},
        {'icon': 'p14bisj', 'desc': 'Averses'},
        {'icon': 'p14terj', 'desc': 'Pluie modérée'},
        {'icon': 'p15j', 'desc': 'Pluie forte'},
        {'icon': 'p16bisj', 'desc': 'Averses orageuses'},
        {'icon': 'p17bisj', 'desc': 'Rares averses de neige'},
        {'icon': 'p18j', 'desc': 'Quelques flocons'},
        {'icon': 'p19bisj', 'desc': 'Averses de pluie et neige mêlées'},
        {'icon': 'p20bisj', 'desc': 'Pluie et neige mêlées'},
        {'icon': 'p26bisj', 'desc': 'Orages'},
        {'icon': 'p27j', 'desc': "Risque d'orages"}
"""
############################################################### - LOGIN TWEET - ####################################################################

auth = tweepy.OAuthHandler(log.consumer_key, log.consumer_secret)
auth.set_access_token(log.access_token, log.access_token_secret)
api = tweepy.API(auth)

############################################################### - INITIALISATION - ####################################################################
certif = True
client = MeteoFranceClient()
locat = {
        "Bordeaux":[44.837789,-0.57918],
        "Lille":[3.057256,50.629250],
        "Lyon":[4.835659,45.764043],
        "Marseille":[5.369780,43.296482],
        "Montpellier":[3.876716,43.610769],
        "Nantes":[1.553621,47.218371],
        "Paris":[2.352222,48.856614],
        "Toulouse":[1.444209,43.604652]
        }
################################################################## - MAIN - ####################################################################
while certif == True:
        x = datetime.datetime.now()
        time.sleep((32-x.hour)*3600+(59-x.minute)*60+(60-x.second))
        tweet = '| #meteo | ~ Prévison de la journée en #France:\n'
        for i in locat:
                weather_forecast = client.get_forecast(latitude=locat[i][1], longitude=locat[i][0])
                print(weather_forecast.daily_forecast[0])
                ico = weather_forecast.daily_forecast[0]['weather12H']['icon']
                if ico == 'p1j' or ico == 'p1bisj':
                        ico = '☀️'
                elif ico == 'p2j' or ico == 'p2bisj':
                        ico = '⛅'
                elif ico == 'p3j' or ico == 'p3bisj' or ico == 'p4j' or ico == 'p4bisj':
                        ico = '☁️'
                elif ico == 'p5j' or ico == 'p5bisj' or ico == 'p6j' or ico == 'p6bisj' or ico == 'p7j' or ico == 'p7bisj' or ico == 'p8j' or ico == 'p8bisj':
                        ico = '🌫️'
                elif ico == 'p10j' or ico == 'p10bisj' or ico == 'p11j' or ico == 'p11bisj' or ico == 'p12j' or ico == 'p12bisj' or ico == 'p13j' or ico == 'p13bisj' or ico == 'p14j' or ico == 'p14bisj' or ico == 'p15j' or ico == 'p15bisj':
                        ico = '🌧️'
                elif ico == 'p17j' or ico == 'p17bisj' or ico == 'p18j' or ico == 'p18bisj' or ico == 'p19j' or ico == 'p19bisj' or ico == 'p20j' or ico == 'p20bisj':
                        ico = '❄️'
                elif ico == 'p26j' or ico == 'p26bisj' or ico == 'p27j' or ico == 'p27bisj':
                        ico = '⛈️'
                else : 
                        print(weather_forecast.daily_forecast[0]['weather12H'])
                tweet+='#'+i+' '+str(weather_forecast.daily_forecast[0]['T']['min'])+'/'+str(weather_forecast.daily_forecast[0]['T']['max'])+'°C | '+ico+'\n'
        print ("Tweet weather "+str(time.ctime(time.time())))
        api.update_status(tweet)