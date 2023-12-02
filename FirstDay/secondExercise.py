

dict_number={"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, 
             "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}  

list_number=["1", "2", "3", "4", "5", "6", "7", "8", "9"]    


firts_letters = ["o", "t", "f", "s", "e", "n"]

numbers = []

def find_numbers_in_line(word_list, i):
    word_number = "x"
    if word_list[i+1] == "n" and word_list[i+2] == "e":
        word_number = "one"
    if word_list[i+1] == "w" and word_list[i+2] == "o":
        word_number = "two"
    if word_list[i+1] == "h" and word_list[i+2] == "r" and word_list[i+3] == "e" and word_list[i+4] == "e":
        word_number = "three"
    if word_list[i+1] == "o" and word_list[i+2] == "u" and word_list[i+3] == "r":
        word_number = "four"
    if word_list[i+1] == "i" and word_list[i+2] == "v" and word_list[i+3] == "e":
        word_number = "five"
    if word_list[i+1] == "i" and word_list[i+2] == "x":
        word_number = "six"
    if word_list[i+1] == "e" and word_list[i+2] == "v" and word_list[i+3] == "e" and word_list[i+4] == "n":
        word_number = "seven"
    if word_list[i+1] == "i" and word_list[i+2] == "g" and word_list[i+3] == "h" and word_list[i+4] == "t":
        word_number = "eight"
    if word_list[i+1] == "i" and word_list[i+2] == "n" and word_list[i+3] == "e":
        word_number = "nine"
    jump = len(word_number) if len(word_number)+i <= len(word_list) else len(word_list)-i-1
    return jump, word_number 

#Open the file input.txt
with open("GitHub/AdventOfCode__/FirstDay/input.txt", "r") as input:
    for line in input:
        word_list = []
        for char in line:
            word_list.append(char)
        number_in_lines=[]
        i = 0
        # print(len(word_list))
        while i < len(word_list):
            if word_list[i] in list_number:
                number_in_lines.append(int(word_list[i]))
                i += 1
            elif word_list[i] in firts_letters:
                jump, word_number = find_numbers_in_line(word_list, i)
                number_in_lines.append(dict_number[word_number]) if word_number != "x" else None
                i += jump
            else:
                i += 1
        # print(i)
        print(number_in_lines)
#Selecting only the first and the last number
        first_num = number_in_lines[0] if len(number_in_lines) >= 1 else None
        last_num = number_in_lines[len(number_in_lines)-1] if len(number_in_lines) >=2 else None
        print(first_num, last_num)
# Making operations to get the number the list represent

        if last_num is None:
            last_num = first_num
            first_num = 0
        if first_num is None:
            last_num = 0
            first_num = 0
            
        num = first_num * 10 + last_num
        print(num)
        numbers.append(num)

# Sum of all numbers at the list
print(sum(numbers))
