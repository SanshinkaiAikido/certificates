from csv import reader

for data in reader(open('data.tsv'), delimiter='\t'):
	print(data)
	exam, name, date, place, number, federation = data
	if '' == exam or '' == name or '' == place or '' == number or 4 != len(number) or 5 != len(federation):
		print('ERROR: Missing value for exam data: {}'.format(data))
		exit(1)
	if '#' == exam[0]:
		continue
	number = int(number)
	if '' != federation:
		federation = int(federation)
	template = open('{}.svg'.format(exam))
	output = open('output/{}-{:04}.svg'.format(exam, number), 'w')
	for line in template:
		if 'Voornaam Voornaam voorvoegsel Achternaam' in line:
			line = line.replace('Voornaam Voornaam voorvoegsel Achternaam', name)
		if '00 maandnaam 0000' in line:
			line = line.replace('00 maandnaam 0000', date)
		if 'Plaatsnaam' in line:
			line = line.replace('Plaatsnaam', place)
		if '0123' in line:
			line = line.replace('0123', '{:04}'.format(number))
		if 0 == federation:
			if 'lidnummer Aikido Zwitserland:' in line:
				line = line.replace('lidnummer Aikido Zwitserland:', '')
			if '04321' in line:
				line = line.replace('04321', '')
		else:
			if '04321' in line:
				line = line.replace('04321', '{:05}'.format(federation))
		output.write(line)
