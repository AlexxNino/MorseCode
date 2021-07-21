line = ".- ...- ..--- .-- .... .. . -.-. -..-  ....- ....."
code = ""
lists = []
spacer = 0

for i in line:
	if i.isspace() == False:
		spacer = 0
		code+=i
	if i.isspace():
		spacer+=1
		if spacer == 2:
			lists.append(" ")
		if spacer == 1:
			lists.append(code)
			code=""
lists.append(code)

DICT = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1' , ' ': ' '}
letters = ""
print(lists)
for j in lists:
	letters+= DICT[j]
print(letters)
