"""
Write a code, which will:
1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example:[{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example:{'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.
Commit script to git repository and provide link as home task result.
"""

#To import functions random and string.
import random, string

'deciding number of dicts in a list and number of key value pairs in each dict'
number_of_dicts = random.randint(2,10) # to decide number of dicts
number_of_key_value_pairs= random.randint(2,3) # to decide number of key value pairs in each dict


a={} # empty set
dict_list = ['default']*number_of_dicts #list with some default values

'creating a list with dicts based on number of dicts and number of key value pairs decided in above step'
for j in range(number_of_dicts):
    for i in range(number_of_key_value_pairs):
        a[random.choice(string.ascii_lowercase)]=random.randint(2,100)
    dict_list[j]=a.copy()
    a.clear()

'Creating empty lists, one to hold keys and other to hold values from the list created in above step'
key_list=[]
value_list=[]

'Inserting keys into key list'
for each in dict_list:
    for x in each.items():
        key_list.append(x[0])


key_list_counts=list (range(len(key_list)))
new_key_list=list (range(len(key_list)))
new_value_list=list (range(len(value_list)))

'To find out the number of times each key exists'
for i in range(len(key_list)):
    key_list_counts[i]=(key_list.count(key_list[i]))

'Transforming the value of keys as defined in requirement and loading to new key list'
for i in range(len(key_list)):
    new_key_list[i]=key_list[i]+'_'+str(key_list_counts[i])

'Counting number of times values exists for each key'
for key in key_list:
    for values in dict_list:
        if values.get(key) is not None:
            value_list.append(values.get(key))
    new_value_list.append(min(value_list))
    value_list.clear()

print(dict_list)

'creating final dict with new key,value pairs'
final_dict= {}
for i in range(len(new_key_list)):
    final_dict[new_key_list[i]]=new_value_list[i]
print (final_dict)
