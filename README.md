"# music_bot" 

voici un bot qui a été crée pour vous aider à crée une musique qui vous correspond notament grace a un systeme de recomendation basé sur une ACP et un 
algorithme d'accords proches de ma confection :D 

comment le mettre en marche : 

telechargé ngrok (le server) : https://ngrok.com/download   --> téléchargé le sur votre bureau

allez dans facebook developer:
--> mes apps --> créer une app --> Ajouter des produits à votre app --> Messenger 
-->Paramètres (messenger) --> Creer une page (ajouter le nom la catégorie et la description) --> creer la page 
--> Enregistrer --> retourner sur Messenger parramètre dans la section Token d'accès --> Ajouter ou supprimer des pages
--> selectinner la page que vous venez de creer --> Générer un token 
--> copiez le, il ressemble à : EAACbS79U6IABAKThpmeFWJN3kWdZA4zYehWYZBPASZCMSpT5nQKPBQ0SeyaTb92ze5fwTWPvw3l4JT9l4HVJvjDhuTXsJZBw1R4vFaK3Xprnyl1ZAETMToQXxCAnDPiQ9EM4mw50OAC6F2qNt6cj2jLRXCCCjqAwPZChjJPM1FgwZDZD 

code :
--> allez dans templates\views.py et remplessez le PAGE_ACCESS_TOKEN et le VERIFY_TOKEN par le token généré plus tôt
--> allez dans templates\tools.py et remplassez le path ou vous avez le dataset 
pour l'intant il y a ca comme path : 'C:/Users/99loi/Desktop/music_bot_final/bot/static/bot/data/data.csv'
--> changez le avec le votre 

cliquez sur ngrok.exe qui est normalement sur votre bureau 
--> tapez dans l'invite de commande qui viens de s'ouvrir la commande  : ngrok http 8000   (ne plus rien marquer dans cette invite de commande là) 
--> copiez url qu'il y a marqué sur Forwarding : expemple, https://f73a1c904af2.ngrok.io  
--> allez dans templates\views.py et remplassez le SITE par le site généré pour mon exemple: https://f73a1c904af2.ngrok.io

-->ouvrez une invite de commande cmd allez dans le folder music_bot ( utilisez la comande cd pour vous baladez dans vos folder exemple cd Desktop puis cd music_bot )
--> exectutez la commande >>>python manage.py runserver
   --> si il vous manque des packages téléchargez les avec pip install le nom du package (exemple: Django, sklearn) 
   --> personellement il me maquait aussi sklearn.utils et pour ressoudre cet import je suis allez dans mon Anaconda Prompt
--> le server est en marche et il fonctionne si vous n'avez pas erreur dans votre invite de commande   

--> retournez dans facebook for developpers --> mes apps --> nom de l'apps --> Paramètre (Messenger)
--> dans la section Webhooks --> cliquez sur Appeler l'URL de rappel
--> dans URL de rappel tapez l'url qui a été généré par ngrok avec /incoming-message/ exemple : https://f73a1c904af2.ngrok.io/incoming-message/
--> et dans Vérifier le jeton mettez le token généré 

--> un div apprarait --> cliquez sur Ajoutez des abonnements 
--> cochez tous ceux de gauche, tous ceux du millieu sauf 'messaging_checkout_updates' et puis cochez 'messaging_optins' à droite 
--> enregistrez

--> allez sur votre compte facebook --> ouvrez la page que vous avez crée
--> cliquez sur Ajouter un bouton --> cliquez sur Envoyer un message
--> cliquez sur Modifier Envoyer un message --> Tester bouton 
--> il se peut que vous ayez à kill le server si le bot n'est pas encore fonctionel : faire ctrl + c sur votre invite de commande et de le relancez avec >>>python manage.py runserver
   --> dans ce cas la cliquez sur supprimer la conversation puis refaite tester le bouton
--> si vous voyez le petit bouton dans le chat 'Démarrer' cliquez dessus 
--> puis dites lui bonjour si il vous réppond: Salut, je suis music_bot c qu'il est en marche et fonctionnel


Ammusez vous bien avec music bot  !! :D
