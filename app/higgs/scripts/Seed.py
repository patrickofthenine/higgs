from backend import models
import logging
logging.basicConfig(level=logging.INFO)
from scripts import Describe
import time

class Seed:
	def run(self, file=None):
		self.file = file
		if not file:
			file = './static/HIGGS.csv'

		self.descriptor = Describe.Describe().fields
		self.key = 0
		self.log_every = 1000
		self.runtime = 0

		self.file_handler(file)

	def fields_handler(self, fields):
		event = {}

		counter = 0
		for field in self.descriptor:
			event[field] = float(fields[counter])
			counter = counter + 1

		return models.Higgs.objects.create(**event)

	def file_handler(self, file):
		with open(file) as fh:
			line = fh.readline()
			start = int(time.time())
			
			while line:
				if self.key % self.log_every == 0:
					end = int(time.time())
				
					batch_time = end - start
					self.runtime = self.runtime + batch_time
					try:
						avg_batch_time = int(self.runtime/self.key * self.log_every)
						logging.info('Processed total: {}, batch size: {}, batch time: {}s, average batch time: {}s, runtime: {}s'.format(self.key, self.log_every, batch_time, avg_batch_time, self.runtime))
					except:
						None
					start = end
				self.line_handler(line)
				self.key = self.key+1

				#move onto next line
				line = fh.readline()	
		
		fh.close()

	def line_handler(self, line):
		fields = line.split(',')
		return self.fields_handler(fields)


Seed().run()
