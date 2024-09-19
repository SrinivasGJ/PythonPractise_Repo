"""
	tHis iz your homeWork, copy these Text to variable.

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


import re
import operator as op
from itertools import count
from string import whitespace

# Copying given text to a variable
a="""homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

import re

#Normalizing the given text so that
#first letter of every sentence starts with Capital letter and rest of the letters follow lowercase'''

normalized_words=[]
normalized_string=''
first_word_flag='Y'

for eachline in a.splitlines(): # Splitting each line in given text
    normalized_words=eachline.lower().split(' ') # Applying lower case and splitting each word in each sentence.
    for i in range(len(normalized_words)):
        if first_word_flag=='Y' and len(normalized_words[i])>1:
            normalized_words[i]=normalized_words[i].title() #Camel case for first word
            first_word_flag='N'

        if i!=len(normalized_words)-1:
            normalized_string= normalized_string+normalized_words[i]+' '
        else:
            normalized_string= normalized_string+normalized_words[i]
    normalized_words.clear()
    normalized_string = normalized_string + '\n'
    first_word_flag = 'Y'

# Replacing "space and new line" with "newline"
normalized_string=normalized_string.replace(' \n','\n')


capture_last_words=[]
last_words=[]

#Replacing the word "iz" with "is"
for eachline in normalized_string.splitlines():
    for everyword in eachline:
        if everyword=='iz':
            everyword.replace('iz','Is')

# Fetching last words of each line
for each in normalized_string.splitlines():
    capture_last_words.append(each.split(' ').pop())

# Storing last words into a list
for i in range(len(capture_last_words)):
    if len(capture_last_words[i])>1:
        last_words.append(capture_last_words[i])

# Framing new sentence from last words
new_sentence=''
for each in last_words:
    new_sentence.join(' ').join(each)

normalized_string=normalized_string+ '\n' + new_sentence
whitespaces_count=len(re.findall(r'( )|\n',normalized_string))


print ('Following is normalized string: \n', normalized_string)
print (f"Number of whitespaces:  {whitespaces_count}")






