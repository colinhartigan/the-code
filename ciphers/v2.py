import ciphers.base as base

def factorize(s):
	# find factors
	factors = [i for i in range(1, s+1) if s % i == 0]
	print(factors)

	# get middle 2 factors
	factors = factors[len(factors)//2-1:len(factors)//2+1]

	return factors

def diagonalize(factors):
	# generates the path for the diagonal traversal
	rows = factors[0]
	cols = factors[1]

	order = []

	for diagonal_num in range(1, (sum(factors))):

		# calcualte which column to start at
		# when diagonal_num is less than the # of rows, start at 0
		start_col = max(0, diagonal_num - rows)

		# caluclate how many numbers there will be in the diagonal
		count = min(diagonal_num, (cols - start_col), rows)

		# find the diagonal coordinates and add them to the output
		for j in range(0, count):
			order.append((min(rows, diagonal_num) - j - 1, start_col + j))

	return order


def decode(text):

	nums = [i for i in text]
	s = len(nums)

	factors = factorize(s)

	new = []

	rows = factors[0]
	cols = factors[1]
	
	# split up the array into the new matrix form
	for i in range(rows):
		new.append(nums[i*cols:i*cols+cols])

	reformatted = []

	coords = diagonalize(factors)

	for coord in coords:
		reformatted.append(str(new[coord[0]][coord[1]]))

	# use regular decoding for the rest
	return base.decode("".join(reformatted))


def encode(text):

	# use regular encoding
	# reverse it to make it easier to build the matrix
	encoded = list(base.encode(text))[::-1]

	s = len(encoded)

	if s % 2 != 0:
		encoded.append(" ")
		s = len(encoded)

	factors = factorize(s)

	rows = factors[0]
	cols = factors[1]

	# fill array with placeholders
	new = [
		[0 for i in range(cols)] for j in range(rows)
	]

	# find diagonal path coords
	coords = diagonalize(factors)

	# fill in the table
	for coord in coords:
		new[coord[0]][coord[1]] = encoded.pop()

	print(new)

	# compress it to one line and join it
	new = ["".join(i) for i in new]

	return str("".join(new))