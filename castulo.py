import telepot
import time
#import serial
#ser = serial.Serial('COM10', 9600)

def handle(msg):

	#userName = msg['from']['first_name']+" "+msg['from']['last_name']

	content_type, chat_type, chat_id = telepot.glance(msg)

	if (content_type == 'text'):
		command = msg['text']
		print ('Got command: %s' % command)

		#if  '/hello' in command:
			#bot.sendMessage(chat_id, "Hello "+userName+", how are you doing today?")

		if 'Hola' in command:
			#ser.write(b'Y')
			bot.sendMessage(chat_id, "Que Salma")

		if 'que tal?' in command:
			#ser.write(b'N')
			bot.sendMessage(chat_id, "nada, aqui haciendo tarea")
		if 'xd' in command:
			#ser.write(b'N')
			bot.sendMessage(chat_id, "huhuhuhuhe")	
		if 'Ten un buen dia' in command:
			#ser.write(b'N')
			bot.sendMessage(chat_id, "No me digas qué hacer")
			
# Create a bot using the token given by BotFather
bot = telepot.Bot('386924041:AAG45Htm1E-bBxcRWz7kUeh_ZXY97TtewwA')

# Add handle function to be called every received message.
bot.message_loop(handle)

# Wait for new messages
while 1:
	time.sleep(20)
