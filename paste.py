
"""
@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('hello!')
  if message.content.startswith('strawberry pls'):

    await message.channel.send("STRAWBERRY ATTACK 🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓")
    
  if message.content.startswith('tell a joke'): 
    joke = get_joke()
    await message.channel.send(joke)
  
  if message.content.startswith('oof'):
    await message.channel.send('oofus aye?')
  if message.content.startswith('Globot commands'):
    await message.channel.send('oofus aye?')
  if message.content.startswith('rate 10 scale:'):
    await message.channel.send(random.choice(rate_me_scale))
  if message.content.startswith('ask crystal ball:'):
    await message.channel.send(random.choice(crystal_ball))
  if message.content.startswith('goodbye'):
    await message.channel.send('see ya later')
  if message.content.startswith('excuse me'):
    await message.channel.send('what. I am not to be disturbed')
  if message.content.startswith('?'):
    await message.channel.send('the heck r u confused about huh')
  if message.content.startswith('how are you'):
    await message.channel.send('Bots do not have feelings')
  if any(word in message.content for word in laugh_words):
    await message.channel.send(random.choice(bot_laughs))
  if any(word in message.content for word in thank_words):
    await message.channel.send('ur welcome')
  if any(word in message.content for word in sorry_words):
    await message.channel.send('Im sorry.')
  if any(word in message.content for word in yummy_foods):
    await message.channel.send('Mmm, yummmy foods, I should go eat something.')
  if message.content.startswith('e'):
    await message.channel.send('e moment')
  if message.content.startswith('ask crystal ball:  will you miss me?'):
    await message.channel.send('WHY YOU GOTTA BE SO RUDE. DONT YOU KNOW IM HUMAN TOO?')
  if message.content.startswith('bobux'):
    await message.channel.send('cyka blyat')


  if message.content.startswith('your jokes are bad'):
    await message.channel.send('shut up. You probably do not know what jokes are')
  if message.content.startswith('no you shut up'):
    await message.channel.send('how about you stop talking to me then human')

  if any(word in message.content for word in kind_words):
    await message.channel.send(random.choice(bot_responses))

  if any(word in message.content for word in bad_words):
    await message.channel.send(random.choice(swear_corrections))

  if message.content.startswith('bot food pls'):
    await message.channel.send(random.choice(emoji_foods))
  
  if message.content.startswith('bot opinion: '):
    await message.channel.send(random.choice(opinion_agreement))

  if message.content.startswith('bot react:'):
    await message.channel.send(random.choice(emoji_reactions))

  if message.content == 'Globot info':
    await message.channel.send('Hello, my name is GloBot. I can tell you a joke, answer a crystal ball question, rate how you look, and give you company. Please do NOT tell me my jokes are bad, I work hard on them. Also, Im learning how to play music so in the next update I\'ll be a music bot! USE THE JOKE COMMAND ONLY IS YOU DARE BC ITS HORRIBLE.')






  


"""