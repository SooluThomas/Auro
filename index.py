import wikipedia
import wolframalpha
from nltk.tokenize import PunktSentenceTokenizer
import nltk

expected_questions = {'what is your name':'Auro', 'who developed you':'Soolu and Team','when were you developed':'I am still under delopment', 'what is auro': 'I am a personal Digital Assistant developed by Soolu and Team', 'who are you':'I am Auro, the personal Assistant'}

def newFn():
	while True:
		try:
			input = raw_input("Question: ")
			app_id = "587E79-677J3JTXE3"
			client = wolframalpha.Client(app_id)
			res_exp = expected_questions[input]
			if res_exp is None :
				res = client.query(input)
				answer = next(res.results).text
			else:
				answer = res_exp
			print answer
		except:
			wikipedia.set_lang("en")
			print wikipedia.summary(input, sentences=2)

def oldFn():
	filename = "./Files/userinput.txt"
	filename1 = "./Files/dictionary.txt"
	user = input("Enter Data: ")

	with open (filename, "w") as fd:
		fd.write(user)

	fd = open(filename,"r")
	print(fd.read())
	fd.close()

	fd = open(filename, "r")
	fd1 = open(filename1, "r")
	train_text = fd.read()
	# sample_tect = fd1.read()


	custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

	tokenized = custom_sent_tokenizer.tokenize(train_text)

	def process_content():
		try:
			for i in tokenized[:5]:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)
				print(tagged)
				with open("./Files/tokenized.txt", "w") as fd, open(filename) as fd1, open("./Files/comp.txt") as fd2:
					# myWords = set(line.split(',') for line in tagged)
					with open("./Files/newtokens.txt", "w") as f:
						for line in tagged:
							print(line)
							freq1 = line[1]
							f.write(line + "\n")
						for line1 in fd2:
							freq= line1[1]
							if freq in freq1:
								print(freq)
								# fd.write(myWords)
				fd.close()
				chunkGram = r"""Chunk: {<.*>+}}<VB.?|IN|DT|TO>+{"""
				chunkParser = nltk.RegexpParser(chunkGram)
				chunked = chunkParser.parse(tagged)
				print(chunked)

		except Exception as e:
			print(str(e))
		
	process_content()
	fd1.close()
	fd.close()

newFn();