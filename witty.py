from wit import Wit
import config

wit_object = Wit(config.ACCESS_TOKEN)

def witty_learner(learning_text=None, intent=None, sound_file=None):
	'''
	witty_learner is used for learning sets in PyWit

	:learning_text:
	:config.MESSAGES:
	'''
	if not learning_text:
		raise config.MESSAGES['empty_message']
		return None
	else:
		try:
			wit_object.put_entities(values=learning_text)
			witty_responder(input_text=learning_text)
		except Exception as e:
			raise e

def witty_responder(input_text=None):
	'''
	witty_responder is used for respondig to the messages

	:witty_response:
	'''
	if input_text:
		witty_response = wit_object.get_message(query=input_text)
		return witty_response