#!/usr/bin/python3
# coding=utf8
from tkinter import *
from discord_webhook import DiscordWebhook
import os

def test():
	webhook = DiscordWebhook(url=webhook_entry.get(), rate_limit_retry=True,
                         content=qcm_entry.get())
	response = webhook.execute()



 
#Fênetre 
window = Tk()

#Créer la frame
frame = Frame(window, bg='#1d1d1f', bd=1, relief=RAISED)


#Personnalisation de la fênetre 
window.title("Discord Webhook Sender")
window.geometry("720x480")
window.minsize(480, 360)
window.config(background='#18191c')

#ajouter un premier texte
label_title = Label(frame, text="Webhook", font=("Arial", 40), bg='#1d1d1f', fg = 'white')
label_title.pack()
label_title = Label(frame, text="By Zaidorox#1369", font=("Arial", 10), bg='#1d1d1f', fg = 'white')
label_title.pack()


#crer un champs
qcm_entry = Entry(frame, text="Text", font=("Arial", 40), bg='#1d1d1f', fg = 'white')
qcm_entry.pack(fill=X)

#crer un 2eme champs
webhook_entry = Entry(frame, text ="Webhook URL", font=("Arial", 40), bg='#1d1d1f', fg = 'white')
webhook_entry.pack(fill=X)

#bouton
dsc_button = Button(frame, text="Lancer", font=("Arial", 25), bg='#1d1d1f', fg='white', command=test)
dsc_button.pack(pady=25 ,fill=X)



#sous boite
right_frame = Frame(frame, bg='#18191c')

# ajouter
frame.pack(expand=YES)


#Afficher la fênetre
window.mainloop()

