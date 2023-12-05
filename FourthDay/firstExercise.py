import re

def main():
    with open("GitHub/AdventOfCode__/FourthDay/input.txt", "r") as input:

        lines = input.readlines()
        patron = "\s\d+|\|"
        total = 0
        for line in lines:
            points = 0
            win = True
            list = re.findall(patron, line)
            # for element in list:
            #     if element == "|":
            #         win = False
            #     elif win:
            #         lista_win.append(element)
            #     elif not win:
            #         lista_num.append(element)
            index = list.index("|")
            lista_win = list[1:index]
            lista_num = list[index+1:len(list)]
            print(lista_num)
            # lista_num[len(lista_num)-1] = lista_num[len(lista_num)-1][0:len(lista_num[len(lista_num)-1])-1]
            # if lista_num[len(lista_num)-1][len(lista_num[len(lista_num)-1])-1] != " ":
            # lista_num[len(lista_num)-1] += " "
            print(lista_win,lista_num)
            for number in lista_num:
                if number in lista_win:
                    print(number)
                    if points == 0:
                        points += 1
                    else:
                        points = points * 2
            total += points
        #     print(points)
        print(total)


            

    input.close()

if __name__ == "__main__":
    main()