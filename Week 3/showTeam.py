import copy
import math
def show_team(names, team_size, result_list, position):
    # Base case 1: we get enough person in the result_list.
    # Base case 2: we went through all the players.
    if len(result_list) == team_size:
        print(result_list)
    elif position >= len(names):
        return
    else:
        result_list_copy = copy.deepcopy(result_list)
        result_list_copy.append(names[position])
        show_team(names, team_size, result_list, position + 1)
        show_team(names, team_size, result_list_copy, position + 1)
    # Create two branches
    # Branch 1 add current person to result_list
    # Branch 2 does not add current person to result_list(copy)
    # use deepcopy function from the copy module
    # Increment current person


players = ["Dey", "Ruowen", "Josh", "Kinder", "Mario", "Rock", "LOL"]
# Check the number we should get using the formula for r numbers at a time
# from a total set of n numbers: n! / (r!(n - r)!)

numPlayers = len(players)
toPick = 4
fac = math.factorial
numTeams = fac(numPlayers) / (fac(toPick)*(fac(numPlayers - toPick)))
print("Choosing a team of %d out of %d players, there are %d different teams.\n"
    %(toPick, numPlayers, numTeams))
show_team(players, toPick, [], 0)
