from csv import reader

for data in reader(open('data.tsv', 'r'), delimiter='\t'):
	exam, name, date, place, number, federation = data
	template = open('{}.svg'.format(exam), 'r')
	output = open('output/{}.svg'.format(exam), 'w')
	for line in template:
		if 'Voornaam Voornaam voorvoegsel Achternaam' in line:
			line = line.replace('Voornaam Voornaam voorvoegsel Achternaam', name)
		if '00 maandnaam 0000' in line:
			line = line.replace('00 maandnaam 0000', date)
		if 'Plaatsnaam' in line:
			line = line.replace('Plaatsnaam', place)
		if '0123' in line:
			line = line.replace('0123', number)
		if '04321' in line:
			line = line.replace('04321', federation)
		output.write(line)
