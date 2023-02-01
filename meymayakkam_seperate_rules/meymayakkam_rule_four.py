import tamil

# 4) ஞ் ந் ம் வ் + ய
# ஞ். ந், ம், வ் எழுத்துக்களுக்குப் பின்பு ய எழுத்து மயங்கி வரும். எ-டு. உரிஞ்யாது, தெவ்யாது.

word=input("Enter the sentence to check: ")
letters=tamil.utf8.get_letters(word)
Mei = ["க்", "ங்", "ச்", "ஞ்", "ட்", "ண்", "த்", "ந்", "ப்", "ம்", "ய்", "ர்", "ல்", "வ்", "ழ்", "ள்", "ற்","ன்"]

if "ஞ்" in letters and letters.index("ஞ்")!=len(letters)-1:
	ind=letters.index("ஞ்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="ய்":
			print(True)
		else:
			print(False)

elif "ந்" in letters and letters.index("ந்")!=len(letters)-1:
	ind=letters.index("ந்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="ய்":
			print(True)
		else:
			print(False)
		
elif "ம்" in letters and letters.index("ம்")!=len(letters)-1:
	ind=letters.index("ம்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="ய்":
			print(True)
		else:
			print(False)
		
elif "வ்" in letters and letters.index("வ்")!=len(letters)-1:
	ind=letters.index("வ்")
	if letters[ind+1] in Mei:
		print (False)
	else:
		root_words=tamil.utf8.splitMeiUyir(letters[ind+1])
		if type(root_words)==tuple:
			root_last=root_words[0]
		else:
			root_last=root_words
		if root_last=="ய்":
			print(True)
		else:
			print(False)
