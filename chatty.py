import os
import subprocess
import datetime
import config
import witty
import json 
from paython import CreditCard, AuthorizeNet

def aggregator(input_text=None):
	'''
	aggregator for inputing text

	:input_text:
	'''
	number_list=[] 
	if not input_text:
		raise config.MESSAGES['empty_message']
	else:
		number_list=has_numbers(input_text=input_text)
		if number_list:
			if (len(number_list)>=2):
				base_string = input_text.split('Rs. ')[-1]
				phone_number_string = int(base_string.split('number')[-1])
				amount_string = int(base_string.split('number')[0])
				recharggy(phone_number=phone_number_string, amount=amount_string)
		else:
			return witty.witty_learner(learning_text=input_text)

def has_numbers(input_text=None):
	'''
	returns list of numbers from a string
	'''
	return [int(s) for s in input_text.split() if s.isdigit()]

def recharggy(phone_number=None, amount=None):
	'''
	recharggy module is used for recharging

	:credit_card:
	:customer_data:
	:input_text:
	'''
	input_text = raw_input(config.MESSAGES['recharge_message'])
	if not input_text:
		return config.MESSAGES['response_message']
	credit_card = CreditCard(
		number = input_text['number'],
		exp_mo = input_text['exp_mo'],
		exp_yr = input_text['exp_yr'],
		first_name = input_text['first_name'],
		last_name = input_text['last_name'],
		cvv = input_text['cvv'],
		strict = False
	)
	if not credit_card.is_valid(): 
	 	return 'hey we have a problem' # checks card number + expiration date
	customer_details={} #Supposing customer data have all the data 
	customer_data = dict(
		address=customer_data['address'], 
		address2=customer_data['address2'], 
		city=customer_data['city'], 
		state=customer_data['state'], 
		zipcode=customer_data['zipcode'], 
		country=customer_data['country'], 
		phone=customer_data['phone'], 
		email=customer_data['email'], 
		ip=customer_data['ip'])
	try:
		api = AuthorizeNet(username=username, password=password, debug=True, test=True)
	except MissingDataError, DataValidationError as e:
		raise e
	try:
		gateway_response = api.auth(amount=amount, credit_card=credit_card, billing_info=customer_data, shipping_info=None)
		response = gateway_response = api.settle(amount=amount, trans_id=trans_id)
	except MissingTranslationError, GatewayError as e:
		raise e

	return response