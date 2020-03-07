import argparse
import logging
logging.getLogger().setLevel(logging.INFO)
import os
import psycopg2
import time

parser = argparse.ArgumentParser(description='get higgs data from db')
parser.add_argument('--database', type=str)
args = parser.parse_args()

class Higgs:
	def __init__(self):
		self.BATCH_SIZE = 10000
		self.processed = 0
		self.batch = 0

	def execute(self, query, callback):
		connection = None
		try:
			connection = psycopg2.connect(
				user=os.environ['PG_USER'],
				password=os.environ['PG_PASS'],
				host=os.environ['PG_HOST'],
				port=os.environ['PG_PORT'],
				database=args.database
			)

			cursor_name = 'HiggsCursor_'+str(int(time.time()))
			cursor = connection.cursor(cursor_name)
			cursor.execute(query)
		
			while True:
				records = cursor.fetchmany(self.BATCH_SIZE)

				if not records:
					break

				callback(records)
			
			cursor.close()
			connection.close()

		except (Exception, psycopg2.Error) as e:
			logging.warning(e)

		#reset	
		self.processed = 0
		self.batch = 0

	def process(self, records):
		self.batch = self.batch + 1
		for record in records:
			if self.processed % self.BATCH_SIZE == 0:
				logging.info('...processed batch: {}, total: {} '.format(self.batch, self.processed))
			self.processed = self.processed + 1
		return

	def run(self):
		query = "SELECT {} FROM {}".format('*', args.database)
		self.execute(query, self.process)

Higgs().run()
