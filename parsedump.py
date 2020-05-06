import csv

file = 'DUMP-01.csv'
endLine = 1000
apMacAndChannel = {}
stationMacAndAP = {}

with open(file) as csvFile:
	reader = csv.reader(csvFile,skipinitialspace=True)
	for r in reader:

		if reader.line_num > 2 and reader.line_num < endLine:
			if not str(r) == "['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']" and not str(r) == "[]":
				apMacAndChannel[r[0]] = r[3]
			else:
				endLine = reader.line_num
		
		elif reader.line_num > endLine + 1 and not str(r) == "[]" and not r[5] == "(not associated) ":
			stationMacAndAP[r[0]] = r[5]

print(stationMacAndAP)