import sys


def batch_file(filepath):
	with open(filepath, 'r') as f:
	    for line in f:
	    	line = line.strip("\n")
	    	yield line

def check_passport(current_passport):
	correct_passport = {'hcl', 'eyr', 'ecl', 'pid', 'cid', 'hgt', 'iyr', 'byr'}

	passport_details = ' '.join(current_passport)
	passport_details = passport_details.split(" ")
	passport_details = set([value.split(":")[0] for value in passport_details])
	
	diff = correct_passport - passport_details
	if not diff or diff == {'cid'}:
		return True
	return False

def compute_correct_passports(filepath):
	current_passport = []
	counter = 0
	for line in batch_file(filepath):
		if line not in ['\n', '\n\r', '']:
			current_passport.append(line)
		else:
			if check_passport(current_passport):
				counter += 1
			current_passport = []
	if check_passport(current_passport):
		counter += 1
	return counter


def main():
	filepath = sys.argv[1]
	num_correct = compute_correct_passports(filepath)
	print(num_correct)


main()
