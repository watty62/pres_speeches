import string

stop_list = ("the", "and", "of", "to", "a", "or", "on", "be", "so", "in", "are", "for", "but","not", "it", "is", "as")

fname = "obama.txt"
fout = fname.split(".")[0]+".csv"

dump = open(fout, 'w')

try:
	fhand = open (fname)
except: 
	print "File cannot be opened"
	exit()

word_count = 0
counts = dict()
for line in fhand:
	line = line.translate(None, string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		word_count +=1
		if word.strip() in stop_list: continue
		else:
			if word.strip() not in counts:
				counts[word.strip()] = 1
			else:
				counts [word.strip()] += 1
l = list()
for key, val in counts.items():
	l.append ((val, key))

l.sort(reverse =True)

dump.write('count, word \n')
for key, val in l[:50]:
	dump.write( str(key)+', ' +val +'\n')

dump.write ('\n')
dump.write ('word count, '+ str(word_count))
dump.close()
