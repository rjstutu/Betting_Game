import random

MAX_LINES = 3
MAX_BET = 5
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}
symbol_value = {
    "A":8,
    "B":3,
    "C":2,
    "D":2,
}


def check_winnings(columns,lines, bet ,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1 )

    return winnings , winning_lines


def refresh_balance(balance, winnings, bet):
    return balance - bet + winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns




def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="\n")



def deposit():
    while True:
        amount = input("Enter amount to be Deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amound must be greater than 0")

        else:
            print("Amount must be a number")

    return amount



def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on 1- {MAX_LINES}? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Number of lines must be between 1 and {MAX_LINES}")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What is your bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else: 
                print(f"Amount must be between {MIN_BET} and {MAX_BET}")
        else:
            print("Please enter a number")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to bet ${total_bet}")

        print(f"you are betting ${bet} on {lines}. Total bets are ${total_bet}")
        print(balance, lines)

        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}")
        print(f"Winning lines:", *winning_lines)
        # balance = refresh_balance(balance, winnings,total_bet)
        # print(f"Your balance is ${balance}")
        return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}")
        ans = input("Would you like to spin? (y/n) ")
        if ans == "y":
            balance += spin(balance)
        else:
            break

main()




    