from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#definition of bot
bot = ChatBot('Bot')
#setting the trainer
bot.set_trainer(ListTrainer)

while True:
    message = raw_input('You: ')
    reply = bot.get_response(message)
    print('Chatbot:') + str(reply)

    if message.strip() == 'Bye':
        print('Chatbot: Bye')
        break
