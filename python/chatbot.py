from chatterbot import Chatbot
chatbot = Chatbot(
  'duy',
  trainer ='chatterbot_py.trainers.ListTrainer')
chatbot.trainer([
    'Hi,can I help you?',
    'Sure,I d like to book afight to lceland.',
    'You fiight has been booked.'
    ])
response = chatbot.get_response('I would like to book a flight.')
print(response)
  
