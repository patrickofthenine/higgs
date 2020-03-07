import argparse
import boto3
from botocore.exceptions import ClientError
import logging
import time

parser = argparse.ArgumentParser(description='Upload files to S3')
parser.add_argument('--Bucket', type=str)
parser.add_argument('--Filename', type=str)
parser.add_argument('--Key', type=str)
parser.add_argument('--Action', type=str)
args = parser.parse_args()

class S3:
	def __init__(self):
		self.s3 = boto3.client('s3') 
		self.actions = {
			'upload': self.s3.upload_file,
		}

	def do(self, callback, using):
		try:
			callback(**using)
		except ClientError as e:
			logging.error(e)
			return False
		
		# did successfully upload	
		return True

	def get_params(self):
		params = { k:v for k,v in vars(args).items() if not k == 'Action'}
		return params

	def run(self):
		start = time.time()
		if args.Action in self.actions:
			action = self.actions[args.Action]
			using  = self.get_params()
			self.do(action, using)
		else:
			return logging.warning('Action unavailable {}, available: {}'.format(args.Action, self.actions.keys()))
		end = time.time()
		return logging.warning('Done. Started: {}, Ended: {}, Duration: {}'.format(start, end, end-start))


S3().run()