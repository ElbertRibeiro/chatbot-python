from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyChatBot')
bot.set_trainer = bot.set_trainer(ListTrainer)


conversation = open('chats.txt', 'r').readline()


bot.train = bot.train(conversation)

while True:
    message = input("Usuário: ")

    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print('ChatBot:', reply)
    
    elif message.strip() == 'Bye':
        print('ChatBot:Bye')
        break
