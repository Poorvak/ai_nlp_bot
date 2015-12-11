import Checksum
import config
import witty

def aggregator(input_text=None):
	'''
	aggregator for inputing text

	:input_text:
	'''
	try:
		if not input_text:
			raise config.MESSAGES['empty_message']
		else:
			response = witty.witty_responder(input_text=input_text)
			outcomes = response.get('outcomes', None)[0]
			if outcomes:
				if outcomes.get('confidence', 0) > 0.0:
					entities = outcomes.get('entities', None)
					name = entities.get('name', outcomes.get('intent', None))[0]
					if name:
						return  name.get('value', None)
		return None
	except Exception as e:
		raise e


'''
The below methods are for PayTM wallet integration and can add money to the wallet using the seller merchant merchant_key
'''
data_dict = {
        'MID': self.merchant_guid,
        'ORDER_ID': order_id,
        'TXN_AMOUNT': amount,
        'CUST_ID': self.user_id,
        'INDUSTRY_TYPE_ID': self.config['industry_type'],
        'WEBSITE': self.config['website'],
        'CHANNEL_ID': self.config['channel_id'],
    }

__sign__(param, dict)
	
# create checksum
def __sign__(param_dict):
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict=param_dict, merchant_key={YOUR_MERCHANT_KEY})

# verify checksum
def validate(param_dict, merchant_key):
        if 'CHECKSUMHASH' not in param_dict:
            return False
        checksum = param_dict.pop('CHECKSUMHASH')[0]
        return Checksum.verify_checksum(param_dict=param_dict, merchant_key=merchant_key, checksum=checksum)