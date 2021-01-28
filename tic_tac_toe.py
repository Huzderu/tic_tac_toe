import itertools
# declaram un dictionar ca sa tinem scorul
scoreboard = {1: 0, 2: 0}
# declaram o variabila pentru numarul de jocuri
game_count = int(input("How many times do you want to play? Enter a number: "))
# declaram o variabila pentru numarul de miscari
game_moves = 0


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            # adaugam un punct castigatorului
            scoreboard[row[0]] += 1
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally!")
        # adaugam un punct castigatorului
        scoreboard[diags[0]] += 1
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally!")
        # adaugam un punct castigatorului
        scoreboard[diags[0]] += 1
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            # adaugam un punct castigatorului
            scoreboard[check[0]] += 1
            return True

        # verificam daca avem toate miscarile posibile, fara un castigator.
        # adaugam acest if statement la sfarsitul functiei win(), astfel incat
        # daca ultima miscare este castigatoare, sa nu fie considerata egalitate
        if game_moves == game_size * game_size:
            print("Tie!")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False
        print("    " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went wrong...", e)
        return game_map, False


play = True
players = [1, 2]
while play:

    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
            # incrementam numarul de miscari
            game_moves += 1

        if win(game):
            # scadem numarul de jocuri ramase
            game_count -= 1
            game_won = True
            if game_count:
                print("The game is over, restarting....")
            else:
                # afisam scorul
                print(f"The score is: \nPlayer 1: {scoreboard[1]} points\nPlayer 2: {scoreboard[2]} points")
                play = False
