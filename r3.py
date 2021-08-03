lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

with open('3-output.txt', 'w', encoding = 'utf-8-sig') as f:
	new = []
	person = None
	for line in lines:
		s = line.split(' ')
		time = s[0][:5]
		name = s[0][5:]
		s2 = ''
		if name == 'Allen' or name == "Viki":
			person = name
		if name:
			new.append(person + ': ' + s2.join(s[1:]))
	for d in new:
		f.write(d + '\n')
