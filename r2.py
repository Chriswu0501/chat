def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		s2 = ''
		if name == 'Allen' or name == "Viki":
			person = name

		if name:
			new.append(person + ': ' + s2.join(s[2:]))

	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	write_file('output-LINE.txt', lines)
	
main()