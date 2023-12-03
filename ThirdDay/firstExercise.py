import numpy as np

def main():
    with open("GitHub/AdventOfCode__/ThirdDay/input.txt", "r") as input:
        
        lines = input.readlines()

        matrix = np.zeros((len(lines), len(lines[0])-1), dtype=str)

        for i in range(len(lines)):
            for j in range(len(lines[i])-1):
                matrix[i,j] = lines[i][j]
        matrix[139,139] = "."

        elements = np.unique(matrix)
        number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        for number in number_list:
            elements = np.delete(elements, np.where(elements == number))
        number_list.remove(".")

        print(elements)
        nums = []
        num = []
        validate = False
        for i in range(len(lines)):
            nums.append(num)
            num = []
            validate = False
            for j in range(len(lines[i])-1):
                element = matrix[i, j]
                if element in number_list and validate:
                    num.append(element)
                    # print(element)
                elif element in number_list and not validate:
                    if i > 0:
                        if j > 0:
                            if matrix[i, j - 1] in elements:
                                validate = True
                        if j < 139:
                            if matrix[i, j + 1] in elements:
                                validate = True
                        if matrix[i - 1, j] in elements:
                            validate = True
                    if i < 139:
                        if j > 0:
                            if matrix[i, j -1] in elements:
                                validate = True
                        if j < 139:
                            if matrix[i, j + 1] in elements:
                                validate = True
                        if matrix[i - 1, j] in elements:
                            validate = True
                    if i > 0 and i < 139 and j > 0 and j < 139:
                        if matrix[i - 1, j - 1] in elements:
                            validate = True
                        if matrix[i -1, j + 1] in elements:
                            validate = True
                        if matrix[i + 1, j - 1] in elements:
                            validate = True
                        if matrix[i + 1, j + 1] in elements:
                            validate = True
                    if i == 0:
                        if matrix[i + 1, j - 1] in elements:
                            validate = True
                        if matrix[i + 1, j + 1] in elements:
                            validate = True
                    if i == 139:
                        if matrix[i - 1, j - 1] in elements:
                            validate = True
                        if matrix[i -1, j + 1] in elements:
                            validate = True
                    if j == 0:
                        if matrix[i -1, j + 1] in elements:
                            validate = True
                        if matrix[i + 1, j + 1] in elements:
                            validate = True
                    if j == 139:
                        if matrix[i + 1, j - 1] in elements:
                            validate = True
                        if matrix[i - 1, j - 1] in elements:
                            validate = True
                    num.append(element)
                    # print(element)
                
                elif element not in number_list: 
                    if num != [] and validate:
                        nums.append(num)
                        print(num)
                    num = []
                    validate = False    

        print(nums)
        last_nums = []
        sum = 0
        for i in range(len(nums)):
            num = nums[i]
            dim = len(nums[i]) - 1
            result = 0
            total = 0
            for i in range(len(num)):
                result = int(num[i]) * 10 ** (dim-i)
                total += result
            last_nums.append(total)
            sum += total

        print(sum)
        print(last_nums)
        input.close()





if __name__ == "__main__":
    main()
