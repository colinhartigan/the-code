import ciphers.v2 as v2

def encode(text):
	# encode in v2
	encoded = v2.encode(text)

	# split the text into pairs of 2, v2's encoder guarantees that the length is even
	split = [[encoded[i], encoded[i+1]] for i in range(0, len(encoded), 2)]

	sums = []

	# sum every pair
	for pair in split:
		a = pair[0] if pair[0].isnumeric() else 0
		b = pair[1] if pair[1].isnumeric() else 0

		s = int(a)+int(b)

		# if the sum is > 9, set it to 9
		if s > 9:
			s = 9

		sums.append(s)

	# prepare the table for sorting numbers
	table = {num: [] for num in set(sums)} 

	# organize the pairs into a table
	for i, pair in enumerate(split):
		table[sums[i]].append("".join(pair))

	freqs = [len(i) for i in table.values()]

	data = ["".join(i) for i in table.values()]

	# frequency encoding format:
	# 1. # of digits
	# 2. number of digits
	freqs_encoded = []
	for i in freqs:
		freqs_encoded.append(str(len(str(i))))
		freqs_encoded.append(str(i))

	# format is:
	# sum # to pop 
	# frequencies separated by 00
	# number data in pairs of 2
	string = f"{''.join(str(i) for i in sums)} {''.join(str(i) for i in freqs_encoded)} {''.join(data)}"

	return string


def decode(text):
	# preprocess
	# find first space
	space = text.find(" ")

	# split the text into 3 parts
	sums = text[:space]

	# find the next space
	space1 = text.find(" ", space+1)

	# prepare text for undoing into the data
	undo = text[space+1:space1]

	# organize the data
	sums = [int(i) for i in sums]
	data = text[space1+1:]
	freqs = []
	data = "".join(data)[::-1]

	# split data into pairs of 2
	data = [data[i:i+2] for i in range(0, len(data), 2)]

	# undo the frequency encoding
	chain = []
	length = 0
	reading = False
	for i in range(0, len(undo)):

		# search for the length tag
		# this falls apart if the the length of the number is > 9, but that will probably never happen
		if not reading:
			# the first number in a sequence will be the length of the number
			length = int(undo[i])
			reading = True
		
		# read the number and save it
		else:
			chain.append(int(undo[i]))
			if len(chain) == length:
				freqs.append("".join(str(i) for i in chain))
				chain = []
				reading = False

	sums_ordered = list(set(sums))

	table = {num: [] for num in set(sums)}

	# reconstruct the frequency table
	for i,v  in enumerate(freqs):
		for j in range(int(v)):
			table[sums_ordered[i]].append(data.pop())

	new_table = {}

	# reverse the table items
	for i,v in table.items():
		new_table[i] = []
		for j in v:
			j = j[::-1]
			new_table[i].append(j)

	for i,v in new_table.items():
		new_table[i] = v[::-1]

	# reconstruct the original text
	decoded = []
	for i in sums:
		decoded.append(new_table[i].pop())

	# join the string then decode with v2
	decoded = "".join(decoded)

	return v2.decode(decoded)