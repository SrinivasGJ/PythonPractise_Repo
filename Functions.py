'Refactor homeworks from module 2 and 3 using functional approach with decomposition.'

###########################  MODULE-2 Collections Home assignment ###########################

#To import functions random and string.
import random, string

'deciding number of dicts in a list and number of key value pairs in each dict'
number_of_dicts = random.randint(2,10) # to decide number of dicts
number_of_key_value_pairs= random.randint(2,3) # to decide number of key value pairs in each dict
a={} # empty set
dict_list = ['default']*number_of_dicts #list with some default values

'Creating empty lists, one to hold keys and other to hold values from the list created in above step'
key_list=[]
value_list=[]
final_dict = {}
'creating a list with dicts based on number of dicts and number of key value pairs decided in above step'
def create_list_with_dicts(x,y):
    for j in range(x):
        for i in range(y):
            a[random.choice(string.ascii_lowercase)] = random.randint(2, 100)
        dict_list[j] = a.copy()
        a.clear()


create_list_with_dicts(number_of_dicts, number_of_key_value_pairs)

'Inserting keys into key list'
for each in dict_list:
    for x in each.items():
        key_list.append(x[0])

key_list_counts = list(range(len(key_list)))
new_key_list = list(range(len(key_list)))
new_value_list = list(range(len(value_list)))

'function to find out the number of times each key exists and appending that value to keys'
def new_keys():
    for i in range(len(key_list)):
        key_list_counts[i] = (key_list.count(key_list[i]))
        new_key_list[i] = key_list[i] + '_' + str(key_list_counts[i])
    return new_key_list

'function to finding out minimum out of given values for each key'
def new_values():
    for key in key_list:
        for values in dict_list:
            if values.get(key) is not None:
                value_list.append(values.get(key))
        new_value_list.append(min(value_list))
        value_list.clear()
    return new_value_list

'function to create to desired dict list'
def new_dict_list(new_key_list,new_value_list):
    'creating final dict with new key,value pairs'
    for i in range(len(new_key_list)):
        final_dict[new_key_list[i]] = new_value_list[i]

'function to print output'
def module2_output():
    print ('\n',"######## Module 2 output #####",'\n')
    # new_keys()
    # new_values()
    new_dict_list(new_keys(), new_values())
    print(dict_list)
    print(final_dict)


###########################  MODULE 3 Strings Home assignment  #####################


# Copying given text to a variable
input_string="""homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

import re

#Normalizing the given text so that
#first letter of every sentence starts with Capital letter and rest of the letters follow lowercase'''


def normalize_function(input_string):
    first_word_flag = 'Y'
    normalized_words = []
    normalized_string = ''
    for eachline in input_string.splitlines():  # Splitting each line in given text
        normalized_words = eachline.lower().split(' ')  # Applying lower case and splitting each word in each sentence.
        for i in range(len(normalized_words)):
            if first_word_flag == 'Y' and len(normalized_words[i]) > 1:
                normalized_words[i] = normalized_words[i].title()  # Camel case for first word
                first_word_flag = 'N'
            # Replacing the word "iz" with "is"
            if normalized_words[i].lower() == 'iz':
                normalized_words[i] = normalized_words[i].replace('iz', 'is')

            if i != len(normalized_words) - 1:
                normalized_string = normalized_string + normalized_words[i] + ' '
            else:
                normalized_string = normalized_string + normalized_words[i]
        normalized_words.clear()
        normalized_string = normalized_string + '\n'
        first_word_flag = 'Y'
    return normalized_string


def sentence_with_last_words(normalized_string):
    capture_last_words = []
    last_words = []
    # Fetching last words of each line
    for each in normalized_string.splitlines():
        capture_last_words.append(each.split(' ').pop())

    # Storing last words into a list
    for i in range(len(capture_last_words)):
        if len(capture_last_words[i]) > 1:
            last_words.append(capture_last_words[i])

    # Framing new sentence from last words
    new_sentence = ''
    for each in last_words:
        new_sentence.join(' ').join(each)
    return new_sentence

def module3_output():
    print('\n',"######## Module 3 output #####", '\n')
    normalized_string = normalize_function(input_string)
    last_words_sentence=sentence_with_last_words(normalized_string)
    updated_string = (normalized_string + '\n' + last_words_sentence)
    whitespaces_count = len(re.findall(r'( )|\n', updated_string))
    print('Following is updated string: \n', updated_string)
    print(f"Number of whitespaces:  {whitespaces_count}")



#Calling module 2 and 3 outputs

module2_output()
module3_output()






