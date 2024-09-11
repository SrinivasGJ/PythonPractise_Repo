""""
Create a python script:
1. create list of 100 random numbers from 0 to 1000
2. sort list from min to max(without using sort())
3. calculate average for even and odd numbers
4. print both average result in console
5. Each line of code should be commented with description.
6. Commit script to git repository and provide link as home task result.
"""
# To import sample function from random module
from random import sample

"To generate 100 random numbers in the range of 0 to 1000"
number_of_digits =100 #Confirming how many random numbers are required
random_numbers = sample(range(0, 1000), number_of_digits) #Generating 100 random numbers from 0 to 1000

"To sort the random numbers list from min to max without using sort()"
random_numbers_sorted = list(range(number_of_digits)) #Creating a list to capture sorted list of random numbers generated above
for i in range(number_of_digits): #Loop to sort the random numbers and store it to list created in above line
    min_value=min(random_numbers)
    random_numbers_sorted[i]=min_value
    random_numbers.remove(min_value)

# To find out average of even and odd numbers
even_numbers_total=0 #Initilizing variable "even numbers total"
even_numbers_count=0 #Initilizing variable "even numbers count"
odd_numbers_total=0 #Initilizing variable "odd numbers total"
odd_numbers_count=0 #Initilizing variable "odd numbers total"
for i in range(number_of_digits): #Loop to find out sum and count of even and odd numbers
    if random_numbers_sorted[i]%2==0:
        even_numbers_total=even_numbers_total+random_numbers_sorted[i]
        even_numbers_count=even_numbers_count+1
    else:
        odd_numbers_total=odd_numbers_total+random_numbers_sorted[i]
        odd_numbers_count=odd_numbers_count+1

even_numbers_average=round((even_numbers_total/even_numbers_count),2) #To find out average of even numbers and rounding off the result to 2 digits
odd_numbers_average=round((odd_numbers_total/odd_numbers_count),2) #To find out average of odd numbers and rounding off the result to 2 digits
print ('even numbers average: ',even_numbers_average) #To print even numbers average
print('odd numbers average: ',odd_numbers_average) #To print odd numbers average