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
# Making operations to get the number the list represent
        num = 0
        dim = len(number_word) - 1
        i = 0
        while dim >= 0:
            num += number_word[i] * 10 ** dim
            i += 1
            dim += -1
        numbers.append(num)

# Sum of all numbers at the list
print(sum(numbers))
