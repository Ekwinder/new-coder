import csv

MY_FILE = "/home/ekwinder/Documents/projects/newcoderprojects/dataviz/data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file t oa JSON-like object."""

	# Open CSV file
	opened_file = open(raw_file)

	# Read the CSV data
	csv_data =csv.reader(opened_file, delimiter=delimiter)

	# Build a data structure to return parsed_data
	parsed_data = []
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close the CSV file
	opened_file.close()

	return parsed_data

def main():

	new_data = parse(MY_FILE,",")

	print new_data

if __name__ == "__main__":
	main()