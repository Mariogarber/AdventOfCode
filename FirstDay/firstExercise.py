#The purpuse is tu get the numbers of each line and the sum all.


#List of numbers in str
list_number=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]    

numbers = []

#Open the file input.txt
with open("GitHub/AdventOfCode__/FirstDay/input.txt", "r") as input:
    for line in input:
        number_word = []
# Split the str in a list of every character and select only the integers
        for char in line:
            if char in list_number:
                number_word.append(int(char))
#Selecting only the first and the last number
        first_num = number_word[0]
        last_num = number_word[len(number_word)-1]
# Making operations to get the number the list represent
        num = first_num * 10 + last_num
        numbers.append(num)

# Sum of all numbers at the list
print(sum(numbers))
input.close()
