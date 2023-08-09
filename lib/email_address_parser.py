import re
import ipdb

class EmailAddressParser():
	def __init__(self, str):
		self.str = str

	def parse(self):
		split_pat = re.compile(r'\s|,\s*')

		words = split_pat.split(self.str)

		email_pat = re.compile(r'[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}')

		emails = []



		for word in words:
			if email_pat.match(word):
				emails.append(word)

		emails.sort()

		return emails