base = [
	["A", "B", "C", "D", "E", "F",],
	["G", "H", "I", "J", "K", "L",],
	["M", "N", "O", "P", "Q", "R",],
	[["S", "Z"], "T", "U", ["V", "W"], "X", "Y"],
]

def decode(text):

	# convert text to uppercase for consistency
	text = text.upper()

	# split text into words
	split = text.split()

	output = []

	for word in split:

		built = []

		# iterate through each number in the word
		# instead of going a number pair at a time, we instead go character by character to easily find any punctuation
		i = 0
		while i < len(word):
			char = word[i]

			# if the character is not a number, add it to the done list
			if not char.isnumeric():
				built.append(char)
				i += 1
				continue
			
			else:
				# separate the number pair into the indicies
				i1 = int(char)
				i2 = int(word[i+1])

				# get the value at the index
				value = base[i1 - 1][i2 - 1]

				# for multi-value entries, just use the first one
				if isinstance(value, list):
					value = value[0]
				
				built.append(value)

				i += 2
				continue
		
		output.append("".join(built))

	return " ".join(output) 


def encode(text):

	output = []

	text = text.upper()

	split = text.split()

	for word in split:

		built = []

		for char in word:

			if not char.isalpha():
				built.append(char)
				continue
			
			else:
				# find the index of the character
				enc = ""
				for i1, row in enumerate(base):
					for i2, value in enumerate(row):
						
						if isinstance(value, list):
							if char in value:
								enc = str(i1+1) + str(i2+1)
						elif char == value:
							enc = str(i1+1) + str(i2+1)

				built.append(enc)
		
		output.append("".join(built))
	
	return " ".join(output)