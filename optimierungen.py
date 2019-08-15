import re

def matchHyphen(word):
	pass

def replaceHyphens(text):
	return text.replace("-","_")

def replaceUnderscores(text):
	return text.replace("_","-")
	
def zahlen(text):
	result = ' '.join([i for i in text.split() if not i.isdigit()])
	print(result)

def huntG20(text):
	if "G 20" in text:
		text = text.replace("G 20", "G20")
	if "G-20" in text:
		text = text.replace("G-20", "G20")
	return text
			
def huntRegex(text):
		if re.search(".* \d$", text):
			text = re.sub("\s", "", text)
			print(text)	
		else:
			print("Nein")
#replaceUnderscores(replaceHyphens("links-grün-schwarze Gesinnungskultur"))
txt = "links-grün-schwarze Gesinnungskultur bei G 20"
#print(replaceUnderscores(replaceHyphens("hallo")))
#zahlen(txt)
#huntG20(txt)
huntRegex(txt)
