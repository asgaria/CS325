def read_input_file():
	input_file = open("imp2input.txt", "r")

	for line in input_file:
		line = line.split(",");
		sequence1 = line[0].strip();
		sequence2 = line[1].strip();
		calc_edit_distance(sequence1, sequence2)
		break;
		#print(sequence1);
		#print(sequence2);
	input_file.close()

def read_cost_file():
	input_lines = open("imp2cost.txt", "r")

	cost_dictionary = {};

	for line in input_lines:
		if(line[0] != "*"):
			line.strip()
			line = line.split(",");
			cost_dictionary[line[0]] = {}
			cost_dictionary[line[0]] = {'-': int(line[1]), 'A': int(line[2]), 'T':int(line[3]), 'G':int(line[4]), 'C':int(line[5].strip())}

	#return cost_dictionary;
	"""for x in cost_dictionary:
		print(x)
		for y in cost_dictionary[x]:
			print(y, ":", cost_dictionary[x][y])
	"""
	return cost_dictionary;

def diff(x, y):
	return int(costs[x][y])

def calc_edit_distance(sequence1, sequence2):
	editDistance = []
	editDirections = []
	output = ['', '']
	pair = [[],[]]


	# Build up edit distance and direction matrices
	for i in xrange(len(sequence1) + 1):
		curDistances = []
		curDirections = []
		for j in xrange(len(sequence2) + 1):
			# Base cases
			if i == 0:
				curDistances.append(j)
				curDirections.append('down')
			elif j == 0:
				curDistances.append(i)
				curDirections.append('left')
				# Otherwise compute min cost
			else:
				costDelete = editDistance[i-1][j] + costs[sequence1[i-1]]['-']
				costInsert = curDistances[j-1] + costs[sequence2[j-1]]['-']
				costAlign = editDistance[i-1][j-1] + costs[sequence1[i-1]][sequence2[j-1]]

				if costInsert < costDelete:
					if costAlign <= costInsert:
						curDistances.append(costAlign)
						curDirections.append('diag')
					else:
						curDistances.append(costInsert)
						curDirections.append('down')
				else:
					if costAlign <= costDelete:
						curDistances.append(costAlign)
						curDirections.append('diag')
					else:
						curDistances.append(costDelete)
						curDirections.append('left')

		editDistance.append(curDistances)
		editDirections.append(curDirections)

	totalDistance = editDistance[i][j]


	print totalDistance;
	return;

costs = read_cost_file();
read_input_file();
