from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#definition of bot
bot = ChatBot('Bot')
#setting the trainer
bot.set_trainer(ListTrainer)

#Loading files to train the both
for files in os.listdir('/media/ian/Work Station/Dev/Python/Practise/Chatbot/chatterbot-corpus/chatterbot_corpus/data/english/'):
    #open the data and store it in a variable called data
    data = open('/media/ian/Work Station/Dev/Python/Practise/Chatbot/chatterbot-corpus/chatterbot_corpus/data/english/' + files,'r').readlines()
    #train the bot using the data gathered
    bot.train(data)

while True:
    message = input('You: ')
    reply = bot.get_response(message)
    print('Chatbot: ', reply)

    if message.strip() == 'Bye':
        print('Chatbot: Bye')
        break

