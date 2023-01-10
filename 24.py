s = open('hh.txt').readline()

s = s.replace("C", 'S')
s = s.replace("D", 'S')
s = s.replace("F", 'S')
s = s.replace("A", 'G')
s = s.replace("O", 'G')

s = s.replace("SSG", '*')
s = s.replace('G', " ")
s = s.replace("S", " ")

m = max(s.split(' '), key = len)

print(len(m))