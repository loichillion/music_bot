from django.shortcuts import render
from .tools import *

from .models import *

# Create your views here.
def index(request,accord):
	liste_accord_proche = Accord.objects.get(nom=accord).accords_proche.all()
	print(request.session.session_key)

	context = locals()
	template = "index.html"
	return render(request, template, context)




from django.conf import settings
from django.http import HttpResponseRedirect

#Les importations
from django.views import generic
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json, requests, random, re
from pprint import pprint

import sys


import json
import os

import re

#Variable Global
PAGE_ACCESS_TOKEN = "EAACbS79U6IABAKhWVbD7HnW0GLzh8fdlr2lnZCjdTtpnBZC3EzOugYn3wYRaZB2YBkmduRPgVquv9TvZA8jqhptFzfhpvZBdatODtEYmDmF5wC2Fp9IdYOJsEtSggodwWpmYcJuDQomqfsOeaA4I6dVRsKLp1jVnny6MgRMH8TgZDZD"
VERIFY_TOKEN   = "EAACbS79U6IABAKhWVbD7HnW0GLzh8fdlr2lnZCjdTtpnBZC3EzOugYn3wYRaZB2YBkmduRPgVquv9TvZA8jqhptFzfhpvZBdatODtEYmDmF5wC2Fp9IdYOJsEtSggodwWpmYcJuDQomqfsOeaA4I6dVRsKLp1jVnny6MgRMH8TgZDZD"
SITE = "https://f73a1c904af2.ngrok.io"

pattern1 = "(hello|hi|hey|salut|bonjour)"
pattern2 = "(use|sers)"
pattern3 = "(créateur|créer|création|create|crée|créé|created)"
pattern4 = "(non|Non|NON)"
pattern5 = "(merci|thx|thanks|ty|thank)"

def message_accueil(fbid):
	params = {
		'access_token':PAGE_ACCESS_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}
	data = json.dumps({
		"recipient": {
			"id": fbid
		},

		"message":{
				"text":"Bonjour, je suis là pour t'aider a mieux comprendre et composer la musique qui te corespond :D"
			}
			})

	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)



def message(fbid,reponse):
	params = {
		'access_token':PAGE_ACCESS_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}
	data = json.dumps({
		"recipient": {
			"id": fbid
		},

		"message":{
				"text":reponse
			}
			})

	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)



def message_menu(fbid):
	params = {
		'access_token':PAGE_ACCESS_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}
	data = json.dumps({
		"recipient": {
			"id": fbid
		},

		"message":{
			"text": "Dis moi si tu as besoin, je suis la !",
			"quick_replies":[
			  {
				  "content_type":"text",
				  "title":"!tempo",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
			  {
				  "content_type":"text",
				  "title":"!key",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
				{
				  "content_type":"text",
				  "title":"!musique_similaire",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
				{
				  "content_type":"text",
				  "title":"!createur_de_musique",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
				{
				  "content_type":"text",
				  "title":"!accord_associe",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
				{
				  "content_type":"text",
				  "title":"!musique_triste",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
				{
				  "content_type":"text",
				  "title":"!musique_heureuse",
				  "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
				},
			]
		  }

		}

			
			
		)
			   
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)
	pprint(status.json())




	

def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False


def post_facebook_message(fbid, recevied_message):
	Message_facebook.objects.create(facebook_id=fbid,message=recevied_message).save()
	# Remove all punctuations, lower case the text and split it based on space
	if (recevied_message) == "!musique_triste":
		message(fbid,"une musique triste est composée de nombreux accords mineurs comme Em et a un tempo faible (<100)")
		message_menu(fbid)
	elif (recevied_message) == "!musique_heureuse":
		message(fbid,"une musique heureuse est composée de nombreux accords majeurs comme E et a un tempo rapide(>100)")
		message_menu(fbid)
	elif (recevied_message) == "!createur_de_musique":
		message(fbid,"Est ce que vous avez lu mes tips sur musique heureuse et musique triste ?")
		Message_facebook.objects.create(facebook_id=fbid,message="Est ce que vous avez lu mes tips sur musique heureuse et musique triste ?")
	elif Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[1].message == "Est ce que vous avez lu mes tips sur musique heureuse et musique triste ?":
		reponse = Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[0].message
		if (re.search(pattern4, reponse)):
			message(fbid,"Eh bien allez les voir ils sont cools et interessants")
		else :
			message(fbid,"Ok pour creer une musique facilement il te faut 4 accords similaires que tu peux trouver grâce a ma fonctionalitée !accord_associe et il te faut aussi un tempo. Pour trouver le tempo et l'accord de base pour ta chanson utilise mes autres fonctionalitées :D")
		message_menu(fbid)
	elif (recevied_message) == "!accord_associe":
		message(fbid,"Donne moi un accord :")
		Message_facebook.objects.create(facebook_id=fbid,message="Donne moi un accord :")
	elif Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[1].message == "Donne moi un accord :":
		accord = Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[0].message
		liste_accord_proche = Accord.objects.get(nom=accord).accords_proche.all()
		liste_accord_proche_f = []
		for ob in liste_accord_proche:
			liste_accord_proche_f.append(ob.nom)
		message(fbid,"Merci, les accords associés sont " + str(liste_accord_proche_f))
		message_menu(fbid)
	elif (recevied_message) == "!tempo" or (recevied_message) == "!key" or (recevied_message) == "!musique_similaire":
		print(1)
		message(fbid,"Donne moi un artiste :")
		Message_facebook.objects.create(facebook_id=fbid,message="Donne moi un artiste :")
	elif Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[1].message == "Donne moi un artiste :":
		print(2)
		message(fbid,"Donne moi une chanson :")
		Message_facebook.objects.create(facebook_id=fbid,message="Donne moi une chanson :")
	elif Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[1].message == "Donne moi une chanson :":
		chanson = Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[0].message
		artiste = Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[2].message
		if Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[4].message == "!tempo":
			tempo = get_tempo(artiste,chanson)
			if tempo == None:
				message(fbid,"l'orthographe de la musique ou de l'auteur n'est pas bonne ou tous simplement la musique recherchée n'est pas dans le dataset")
			else:
				message(fbid,"Merci, le tempo est " + str(tempo))
		elif Message_facebook.objects.filter(facebook_id=fbid).order_by('-pk')[4].message == "!key":
			key = get_key(artiste,chanson)[0]
			if key == None:
				message(fbid,"l'orthographe de la musique ou de l'auteur n'est pas bonne ou tous simplement la musique recherchée n'est pas dans le dataset")
			else:
				message(fbid,"Merci, la key est " + str(key))
		else:
			musique_similaire = prediction(artiste,chanson)
			if musique_similaire == None:
				message(fbid,"l'orthographe de la musique ou de l'auteur n'est pas bonne ou tous simplement la musique recherchée n'est pas dans le dataset")
			else:
				message(fbid,"Merci, les musiques similaires sont : " + str(musique_similaire))
		message_menu(fbid)
	elif (re.search(pattern1, recevied_message)):
		message(fbid,"Salut, je suis music_bot")
		message_menu(fbid)	
	elif (re.search(pattern2, recevied_message)):
		message(fbid,"J'ai plusieurs fonctionalitées, je peux te dire le tempo, la key et 4 chansons similaires à une chanson que tu aime. Je suis aussi là pour t'aider à créer ta propre musique :D ")
		message_menu(fbid)
	elif (re.search(pattern3, recevied_message)):
		message(fbid,"C'est Loïc HILLION qui m'a crée")
		message_menu(fbid)
	elif (re.search(pattern5, recevied_message)):
		message(fbid,"Y'a pas de quoi merci à toi d'utiliser music_bot !! :D <3 <3 <3")
		message_menu(fbid)				
	else:
		message_accueil(fbid)
		message_menu(fbid)


	
	
	


# Cette fonction permet d'envoyer les information sur 
# le la page d'accueil du bot messenger (get started)
def demarer():

	params = {
		'access_token':PAGE_ACCESS_TOKEN
	}
	headers = {
		"Content-Type": "application/json"
	}
	data = json.dumps({
		
		"get_started": {
			"payload": "demarer"
			},
		"greeting":[
		  {
			"locale":"default",
			"text":"Salut {{user_first_name}}, bienvenue sur Musicbot"
		  }
		]

	  })

	post_message_url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=%s'%PAGE_ACCESS_TOKEN
	status = requests.post(post_message_url,  params=params, headers=headers, data=data)
	pprint(status.json())






# Classe et fonctions qui gére les réponse du bot
class QuotesBotView(generic.View):

	
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	# Post function to handle Facebook messages
	def post(self, request, *args, **kwargs):
		# Converts the text payload into a python dictionary
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		# Facebook recommends going through every entry since they might send
		# multiple messages in a single call during high load
		#pprint(incoming_message)

		demarer()

		try:

			for entry in incoming_message['entry']:
				for message in entry['messaging']:
					# Check to make sure the received call is a message call
					# This might be delivery, optin, postback for other events 
					if 'message' in message:
						# Print the message to the terminal
						# Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
						# are sent as attachments and must be handled accordingly. 
						post_facebook_message(message['sender']['id'], message['message']['text'])  

					# elif 'postback' in message:
					# 	if message['postback']['payload'] == 'demarer':
					# 		#Réupération de profils + envoie du premier message
					# 		message_accueil(message['sender']['id'])
					# 	else:
					# 		post_facebook_message(message['sender']['id'], message['postback']['title'])

					else:
						pass
		except:
			pass

					 
		return HttpResponse()   