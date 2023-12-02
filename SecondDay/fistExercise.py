import re

def find_id(line):
    """
    This function return the id of the Game
    """
    regex = "Game\s\d+:"
    game_id = re.findall(regex, line)[0]
    id = int(game_id[5: len(game_id)-1])
    return id

def find_color(line, color):
    """
    This function return the max number of cubes observed in the three sets
    """
    regex = "\d+\s" + color
    all_ints = re.findall(regex, line)
    num_cubes = []
    for instance in all_ints:
        num_cubes.append(int(instance[0:len(instance)-len(color)]))
    return max(num_cubes)

def main():
    with open("GitHub/AdventOfCode__/SecondDay/input.txt", "r") as input:   
        sum = 0
        max_cubes = {"red" : 12, "green" : 13, "blue" : 14}
        for line in input.readlines():
            num_cubes = {"red" : 0, "green" : 0, "blue" : 0}
            num_cubes["red"] = find_color(line, color="red")
            num_cubes["green"] = find_color(line, color="green") 
            num_cubes["blue"] = find_color(line, color="blue")
            print(num_cubes)
            if max_cubes["red"] >= num_cubes["red"] and max_cubes["green"] >= num_cubes["green"] and max_cubes["blue"] >= num_cubes["blue"]:
                id = find_id(line)
                print(id)
                sum += id
        print(sum)
    input.close()

if __name__ == "__main__":
    main()