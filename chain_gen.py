from markov_python.cc_markov import MarkovChain
import fetch_data

lyrics_5 =fetch_data.lyrics_4
#blink_data= open('')

'''with open('/Users/lennykogosov/Desktop/markovproject/text.txt', 'r+') as f:
	text=f.read()'''


my_file= open('/Users/lennykogosov/Desktop/markovproject/text.txt', 'r+')
for x in lyrics_5:
	my_file.write(x) 





#my_file.close()


mc= MarkovChain()
mc.add_file('/Users/lennykogosov/Desktop/markovproject/text.txt')
first_sample= mc.generate_text(20)
print first_sample
my_file.close()