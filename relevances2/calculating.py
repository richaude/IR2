import json

def precisionEach():
	i = 1
	f = open("precisions.txt", "w")
	f.write("precisions fuer alle topics:\n")
	f.flush
	f.close
	averagePrecisions = 0
	undefiniert = 0
	while i < 51:
		#print(str(i))
		with open("topic"+str(i)+".json", 'r') as file_handle:
			parsed_json = json.loads(file_handle.read())
			relevant = 0
			k = 1
			averagePrecisionAll = 0
			for retrieved in parsed_json["relevances"]:
				if retrieved["isRelevant"] == 1:
					relevant += 1
					precisionK = relevant/k
					averagePrecisionAll += precisionK
					f1 = open("precisions.txt", "a")
					f1.write("\nTopic "+str(i)+", precision@"+str(k)+": "+str(precisionK)+"\n")
					f1.flush
					f1.close
					
				k += 1
				if k > 5:
					#print("noch alte Parameter")
					break
			if relevant > 0:
				averagePrecision = averagePrecisionAll/relevant
			else:
				#print("undefiniert!")
				undefiniert += 1
				print("Undefiniertes Topic: "+str(i))
			f2 = open("precisions.txt", "a")
			f2.write("\naverage precision topic "+str(i)+": "+str(averagePrecision)+"\n")
			f2.flush
			f2.close
			averagePrecisions += averagePrecision
			i += 1
	meanAveragePrecision = averagePrecisions/(50)
	print(str(undefiniert))
	f3 = open("precisions.txt", "a")
	f3.write("\nMean Average Precision: "+str(meanAveragePrecision))
	f3.flush
	f3.close


precisionEach()
