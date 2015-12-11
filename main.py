#Author: Poorvak Kapoor
#Date: 1st December, 2015
#Name: AI/NLP Chatbot 
#Purpose: Recharges

import witty
import chatty
import config

'''
config file is for handling static files
witty file is for wit.ai handler
loggy file is for logging
chatty is for responding to the chat messgaes

:input_text is used for inputting text from the terminal:
rest variables are self explinatory
'''
if __name__ == '__main__':
	try:
		input_text = raw_input(config.MESSAGES['hi_message'])
		if input_text:
			while input_text:
			    response = chatty.aggregator(input_text=input_text)
			    print 'response', response
	        	input_text = raw_input(response)
	except Exception as e:
		raise e

