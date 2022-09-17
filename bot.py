import telebot
import config
import random
import time
from time import sleep
from telebot import types
from requests import get



kittens = True
puppies = True
jackals = True
hamsters = True
animals = True


bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
  bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nI'm a - <b>{1.first_name}</b>, bot designed to cheer you up.".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
  sti = open('static/welcome.png.webp', 'rb')
  bot.send_sticker(message.chat.id, sti)
  print("[log]Start commands...")
  time.sleep(1.0)
  print("[log]Successfully")
  bot.send_message(message.chat.id, "The bot has been successfully launched. All commands have been successfully run.\nTo see the available commands type /help")
  global kittens
  kittens = True
  global puppies
  puppies = True
  global jackals
  jackals = True
  global hamsters
  hamsters = True
  global animals
  animals = True



	#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Kittens")
item2 = types.KeyboardButton("Puppies")

markup.add(item1, item2)


# commands

@bot.message_handler(commands=["kittens"])
def kittens(message):
  while kittens:
    bot.send_message(message.chat.id, "Kittens:")
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5287/sample_8fa29a89773f3a37a91c703e296106e9.jpg?6024748")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5307/sample_6deb416df3ecccbfe35c55614e978fd52ac48000.jpg?6047874")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5362/sample_18ddca7d72c1c8ba3e36b62b5d49b134.jpg?6109145")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5368/32d9450ff5febe4a7fa9ee84129a6f26.jpeg?6114462")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5398/84ddab2fc28578a2ef3bb1384005e5e4.png?6149108")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5401/03e17c6ed7874729d46148ec6850984e57f5ef1e.jpg?6152150")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5405/9c8cd5f1ec2aace32034f281ccb4f98b.jpeg?6156133")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5416/sample_59d86173c3329cd440b4a7a5c80251cdfc0d27d8.jpg?6167279")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5444/8f0e495f567cdb852101c5a2fbd2c1a247769ab1.jpg?6200940")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5457/sample_bedc08fad37ce0319782b9fba19bb311.jpg?6214557")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5487/4359d3c833b6ae42f9b67acdcfe21fd76911e744.jpg?6246276")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5343/sample_afdeeac86799d09f1c050ede4cae7803.jpg?6351264")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5608/sample_b8554050e9e5e1d34484b15f6e7a3929.jpg?6381941")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_9216828ef9da330f6a228ad1f585532f.jpg?6384014")
    time.sleep(0.5)  
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_56cdf31af4a67562f47637876561521a.jpg?6384024")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5616/sample_66178b6ee607c8697ad8dd549be27dd8.jpg?6391088")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5619/de3c7bc6722f65d7d40f3310b9486d81.jpeg?6393568")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5743/sample_6d113dc406879fa9e0279b15ecfaf2e8.jpg?6530639")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_3ce26b7ea845d60652a5cca1fe9f567c.jpg?6536770")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_253bf6f06d4555552e4c70b97a2af97c.jpg?6536779")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5717/sample_204c466282fba80a33bf01b9ff64d220.jpg?6499428")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5333/sample_726a80bec859891d3923d6e3a9c3184b.jpg?6090035")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5524/bdde4ee59bbe1cfc6f4ae2336f39f055.jpeg?6289180")




@bot.message_handler(commands=["puppies"])
def puppies(message):
  while puppies:
    bot.send_message(message.chat.id, "Puppies:")
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5287/sample_8fa29a89773f3a37a91c703e296106e9.jpg?6024748")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5307/sample_6deb416df3ecccbfe35c55614e978fd52ac48000.jpg?6047874")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5362/sample_18ddca7d72c1c8ba3e36b62b5d49b134.jpg?6109145")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5368/32d9450ff5febe4a7fa9ee84129a6f26.jpeg?6114462")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5398/84ddab2fc28578a2ef3bb1384005e5e4.png?6149108")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5401/03e17c6ed7874729d46148ec6850984e57f5ef1e.jpg?6152150")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5405/9c8cd5f1ec2aace32034f281ccb4f98b.jpeg?6156133")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5416/sample_59d86173c3329cd440b4a7a5c80251cdfc0d27d8.jpg?6167279")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5444/8f0e495f567cdb852101c5a2fbd2c1a247769ab1.jpg?6200940")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5457/sample_bedc08fad37ce0319782b9fba19bb311.jpg?6214557")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5487/4359d3c833b6ae42f9b67acdcfe21fd76911e744.jpg?6246276")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5343/sample_afdeeac86799d09f1c050ede4cae7803.jpg?6351264")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5608/sample_b8554050e9e5e1d34484b15f6e7a3929.jpg?6381941")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_9216828ef9da330f6a228ad1f585532f.jpg?6384014")
    time.sleep(0.5)  
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_56cdf31af4a67562f47637876561521a.jpg?6384024")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5616/sample_66178b6ee607c8697ad8dd549be27dd8.jpg?6391088")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5619/de3c7bc6722f65d7d40f3310b9486d81.jpeg?6393568")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5743/sample_6d113dc406879fa9e0279b15ecfaf2e8.jpg?6530639")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_3ce26b7ea845d60652a5cca1fe9f567c.jpg?6536770")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_253bf6f06d4555552e4c70b97a2af97c.jpg?6536779")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5717/sample_204c466282fba80a33bf01b9ff64d220.jpg?6499428")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5333/sample_726a80bec859891d3923d6e3a9c3184b.jpg?6090035")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5524/bdde4ee59bbe1cfc6f4ae2336f39f055.jpeg?6289180")



@bot.message_handler(commands=["jackals"])
def jackals(message):
  while jackals:
    bot.send_message(message.chat.id, "Jackals:")
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5287/sample_8fa29a89773f3a37a91c703e296106e9.jpg?6024748")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5307/sample_6deb416df3ecccbfe35c55614e978fd52ac48000.jpg?6047874")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5362/sample_18ddca7d72c1c8ba3e36b62b5d49b134.jpg?6109145")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5368/32d9450ff5febe4a7fa9ee84129a6f26.jpeg?6114462")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5398/84ddab2fc28578a2ef3bb1384005e5e4.png?6149108")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5401/03e17c6ed7874729d46148ec6850984e57f5ef1e.jpg?6152150")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5405/9c8cd5f1ec2aace32034f281ccb4f98b.jpeg?6156133")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5416/sample_59d86173c3329cd440b4a7a5c80251cdfc0d27d8.jpg?6167279")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5444/8f0e495f567cdb852101c5a2fbd2c1a247769ab1.jpg?6200940")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5457/sample_bedc08fad37ce0319782b9fba19bb311.jpg?6214557")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5487/4359d3c833b6ae42f9b67acdcfe21fd76911e744.jpg?6246276")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5343/sample_afdeeac86799d09f1c050ede4cae7803.jpg?6351264")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5608/sample_b8554050e9e5e1d34484b15f6e7a3929.jpg?6381941")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_9216828ef9da330f6a228ad1f585532f.jpg?6384014")
    time.sleep(0.5)  
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_56cdf31af4a67562f47637876561521a.jpg?6384024")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5616/sample_66178b6ee607c8697ad8dd549be27dd8.jpg?6391088")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5619/de3c7bc6722f65d7d40f3310b9486d81.jpeg?6393568")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5743/sample_6d113dc406879fa9e0279b15ecfaf2e8.jpg?6530639")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_3ce26b7ea845d60652a5cca1fe9f567c.jpg?6536770")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_253bf6f06d4555552e4c70b97a2af97c.jpg?6536779")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5717/sample_204c466282fba80a33bf01b9ff64d220.jpg?6499428")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5333/sample_726a80bec859891d3923d6e3a9c3184b.jpg?6090035")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5524/bdde4ee59bbe1cfc6f4ae2336f39f055.jpeg?6289180")

@bot.message_handler(commands=["hamsters"])
def hamsters(message):
  while hamsters:
    bot.send_message(message.chat.id, "Hamsters:")
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5287/sample_8fa29a89773f3a37a91c703e296106e9.jpg?6024748")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5307/sample_6deb416df3ecccbfe35c55614e978fd52ac48000.jpg?6047874")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5362/sample_18ddca7d72c1c8ba3e36b62b5d49b134.jpg?6109145")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5368/32d9450ff5febe4a7fa9ee84129a6f26.jpeg?6114462")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5398/84ddab2fc28578a2ef3bb1384005e5e4.png?6149108")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5401/03e17c6ed7874729d46148ec6850984e57f5ef1e.jpg?6152150")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5405/9c8cd5f1ec2aace32034f281ccb4f98b.jpeg?6156133")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5416/sample_59d86173c3329cd440b4a7a5c80251cdfc0d27d8.jpg?6167279")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5444/8f0e495f567cdb852101c5a2fbd2c1a247769ab1.jpg?6200940")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5457/sample_bedc08fad37ce0319782b9fba19bb311.jpg?6214557")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5487/4359d3c833b6ae42f9b67acdcfe21fd76911e744.jpg?6246276")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5343/sample_afdeeac86799d09f1c050ede4cae7803.jpg?6351264")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5608/sample_b8554050e9e5e1d34484b15f6e7a3929.jpg?6381941")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_9216828ef9da330f6a228ad1f585532f.jpg?6384014")
    time.sleep(0.5)  
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_56cdf31af4a67562f47637876561521a.jpg?6384024")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5616/sample_66178b6ee607c8697ad8dd549be27dd8.jpg?6391088")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5619/de3c7bc6722f65d7d40f3310b9486d81.jpeg?6393568")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5743/sample_6d113dc406879fa9e0279b15ecfaf2e8.jpg?6530639")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_3ce26b7ea845d60652a5cca1fe9f567c.jpg?6536770")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_253bf6f06d4555552e4c70b97a2af97c.jpg?6536779")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5717/sample_204c466282fba80a33bf01b9ff64d220.jpg?6499428")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5333/sample_726a80bec859891d3923d6e3a9c3184b.jpg?6090035")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5524/bdde4ee59bbe1cfc6f4ae2336f39f055.jpeg?6289180")


		
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "When you enter a command, the bot sends a cute picture of an animal.\nCommand List: \n/kittens - Photos of kittens.\n/puppies - Photos of puppies.\n/jackals - Photos of jackals.\n/hamsters - Photos of hamsters.\n/animals - Random photo of animal.\n/start - Running commands.\n/stop - Stop commands.\nAttention! The developer is not responsible for the bot. The bot was created for the purpose of pranking your friends.", parse_mode='html')

		


@bot.message_handler(commands=["animals"])
def animals(message):
  while animals:
    bot.send_message(message.chat.id, "Animals:")
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5287/sample_8fa29a89773f3a37a91c703e296106e9.jpg?6024748")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5307/sample_6deb416df3ecccbfe35c55614e978fd52ac48000.jpg?6047874")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5362/sample_18ddca7d72c1c8ba3e36b62b5d49b134.jpg?6109145")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5368/32d9450ff5febe4a7fa9ee84129a6f26.jpeg?6114462")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5398/84ddab2fc28578a2ef3bb1384005e5e4.png?6149108")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5401/03e17c6ed7874729d46148ec6850984e57f5ef1e.jpg?6152150")
    time.sleep(0.5) 
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5405/9c8cd5f1ec2aace32034f281ccb4f98b.jpeg?6156133")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5416/sample_59d86173c3329cd440b4a7a5c80251cdfc0d27d8.jpg?6167279")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5444/8f0e495f567cdb852101c5a2fbd2c1a247769ab1.jpg?6200940")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5457/sample_bedc08fad37ce0319782b9fba19bb311.jpg?6214557")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5487/4359d3c833b6ae42f9b67acdcfe21fd76911e744.jpg?6246276")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5343/sample_afdeeac86799d09f1c050ede4cae7803.jpg?6351264")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5608/sample_b8554050e9e5e1d34484b15f6e7a3929.jpg?6381941")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_9216828ef9da330f6a228ad1f585532f.jpg?6384014")
    time.sleep(0.5)  
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5610/sample_56cdf31af4a67562f47637876561521a.jpg?6384024")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5616/sample_66178b6ee607c8697ad8dd549be27dd8.jpg?6391088")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5619/de3c7bc6722f65d7d40f3310b9486d81.jpeg?6393568")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5743/sample_6d113dc406879fa9e0279b15ecfaf2e8.jpg?6530639")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_3ce26b7ea845d60652a5cca1fe9f567c.jpg?6536770")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5747/sample_253bf6f06d4555552e4c70b97a2af97c.jpg?6536779")
    time.sleep(0.5)    
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5717/sample_204c466282fba80a33bf01b9ff64d220.jpg?6499428")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://rule34.xxx//samples/5333/sample_726a80bec859891d3923d6e3a9c3184b.jpg?6090035")
    time.sleep(0.5)     
    bot.send_photo(message.chat.id, "https://wimg.rule34.xxx//images/5524/bdde4ee59bbe1cfc6f4ae2336f39f055.jpeg?6289180")
  



@bot.message_handler(commands=['stop'])
def stop(message):
  print("[log]Stop commands...")
  print("[log]Successfully")
  bot.send_message(message.chat.id, "The bot has completed its work. All commands successfully stopped. To start the bot and commands type /start")

  global kittens
  kittens = False
  global puppies
  puppies = False
  global jackals
  jackals = False
  global hamsters
  hamsters = False 
  global animals
  animals = False 
   


# commands ------	



@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Kittens':
			bot.send_message(message.chat.id, 'I very like Kittens!')
		elif message.text == 'Puppies':
		 	bot.send_message(message.chat.id, 'Great choice!')
		else:
			bot.send_message(message.chat.id, 'I dont know what to say!')




# RUN
bot.polling(none_stop=True)
#none_stop=True