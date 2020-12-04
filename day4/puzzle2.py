import sys

class Passport():
	def __init__(self):
		self.passport_details = dict()

	def validate_byr(self):
		if not self.passport_details['byr'].isdigit():
			return False
		return 1920 <= int(self.passport_details['byr']) <= 2002

	def validate_iyr(self):
		if not self.passport_details['iyr'].isdigit():
			return False
		return 2010 <= int(self.passport_details['iyr']) <= 2020

	def validate_eyr(self):
		if not self.passport_details['eyr'].isdigit():
			return False
		return 2020 <= int(self.passport_details['eyr']) <= 2030

	def validate_hgt(self):
		measurement, unit = self.passport_details['hgt'][:-2], self.passport_details['hgt'][-2:]
		if measurement.isdigit():
			if unit == 'cm':
				return 150 <= int(measurement) <= 193
			elif unit == 'in':
				return 59 <= int(measurement) <= 76
		return False

	def validate_hcl(self):
		if self.passport_details['hcl'][0] == '#' and \
			len(self.passport_details['hcl'][1:]) == 6 and \
			self.passport_details['hcl'][1:].isalnum():
			return True
		return False

	def validate_ecl(self):
		acceptable = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if self.passport_details['ecl'] in acceptable:
			return True
		return False

	def validate_pid(self):
		if len(self.passport_details['pid']) == 9 and \
			self.passport_details['pid'].isdigit():
			return True
		return False

	def validate_keys(self):
		result = True
		for key, value in self.passport_details.items():
			if key == 'byr': 
				result = result and self.validate_byr()
			elif key == 'hgt': 
				result = result and self.validate_hgt()
			elif key == 'iyr': 
				result = result and self.validate_iyr()
			elif key == 'eyr':
				result = result and self.validate_eyr()
			elif key == 'hcl':
				result = result and self.validate_hcl()
			elif key == 'ecl':
				result = result and self.validate_ecl()
			elif key == 'pid':
				result = result and self.validate_pid()
		return result

	def check_passport(self, current_passport):
		correct_passport_keys = {'hcl', 'eyr', 'ecl', 'pid', 'cid', 'hgt', 'iyr', 'byr'}
		passport_string = ' '.join(current_passport)
		passport_string = passport_string.split(" ")
		self.passport_details = {value.split(":")[0]:value.split(":")[1] for value in passport_string}
		password_keys = set(self.passport_details.keys())	
		diff = correct_passport_keys - password_keys
		if ((not diff or diff == {'cid'}) and self.validate_keys()):
			return True
		return False


def batch_file(filepath):
	with open(filepath, 'r') as f:
	    for line in f:
	    	line = line.strip("\n")
	    	yield line

def compute_correct_passports(filepath):
	current_passport = []
	counter = 0
	for line in batch_file(filepath):
		if line not in ['\n', '\n\r', '']:
			current_passport.append(line)
		else:
			passport = Passport()
			if passport.check_passport(current_passport):
				counter += 1
			current_passport = []

	passport = Passport()
	if passport.check_passport(current_passport):
		counter += 1
	return counter


def main():
	filepath = sys.argv[1]
	num_correct = compute_correct_passports(filepath)
	print(num_correct)


main()
