file = open('noaa_sunspot_predictions.txt')
s = 'data = ['
for line in file:
	if line[0] == '#' or line[0] == ':':
		pass
	else:
		s += '('
		vals = line.split()
		for v in vals:
			s += v + ','		
		s = s[0:-1] + ')'
		s += ','
s = s[0:-1] + ']'
print s