grid = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

player = 1          
moves = 0     
end_check = 0


def checker():
    if grid['1'] == 'X' and grid['2'] == 'X' and grid['3'] == 'X':
        print('Player one wins')
        return 1
    if grid['4'] == 'X' and grid['5'] == 'X' and grid['6'] == 'X':
        print('Player One wins')
        return 1
    if grid['7'] == 'X' and grid['8'] == 'X' and grid['9'] == 'X':
        print('Player One wins')
        return 1
    if grid['1'] == 'X' and grid['5'] == 'X' and grid['9'] == 'X':
        print('Player One wins')
        return 1
    if grid['1'] == 'X' and grid['4'] == 'X' and grid['7'] == 'X':
        print('Player One wins')
        return 1
    if grid['2'] == 'X' and grid['5'] == 'X' and grid['8'] == 'X':
        print('Player One wins')
        return 1
    if grid['3'] == 'X' and grid['6'] == 'X' and grid['9'] == 'X':
        print('Player One wins')
        return 1

    if grid['1'] == 'O' and grid['2'] == 'O' and grid['3'] == 'O':
        print('Player Two wins')
        return 1
    if grid['4'] == 'O' and grid['5'] == 'O' and grid['6'] == 'O':
        print('Player Two wins')
        return 1
    if grid['7'] == 'O' and grid['8'] == 'O' and grid['9'] == 'O':
        print('Player Two wins')
        return 1
    if grid['1'] == 'O' and grid['5'] == 'O' and grid['9'] == 'O':
        print('Player Two wins')
        return 1
    if grid['1'] == 'O' and grid['4'] == 'O' and grid['7'] == 'O':
        print('Player Two wins')
        return 1
    if grid['2'] == 'O' and grid['5'] == 'O' and grid['8'] == 'O':
        print('Player Two wins')
        return 1
    if grid['3'] == 'O' and grid['6'] == 'O' and grid['9'] == 'O':
        print('Player Two wins')
        return 1
    return 0


print('1|2|3')
print('______')
print('4|5|6')
print('______')
print('7|8|9')

while True:
    print(grid['1']+'|'+grid['2']+'|'+grid['3'])
    print('-----')
    print(grid['4'] + '|' + grid['5'] + '|' + grid['6'])
    print('-----')
    print(grid['7'] + '|' + grid['8'] + '|' + grid['9'])
    end_check = checker()
    if moves == 9 or end_check == 1:
        break
    while True:     
        if player == 1:  
            p1_input = input('player one')
            if p1_input.upper() in grid and grid[p1_input.upper()] == ' ':
                grid[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print('Try again')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in grid and grid[p2_input.upper()] == ' ':
                grid[p2_input.upper()] = 'O'
                player = 1
                break
            else:  
                print('Try again.')
                continue
    moves += 1
    print()


