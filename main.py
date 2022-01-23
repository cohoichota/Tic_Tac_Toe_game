import sys
import random
from logo import logo

chosen_comb = 0
W = 0
L = 0
D = 0


def game():
    print(logo)
    slots_available = ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']
    winning_comb = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'],
                    ['C1', 'C2', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
    cpu_combs = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'],
                 ['C1', 'C2', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
    slots = {"A1": " ", "B1": " ", "C1": " ",
             "A2": " ", "B2": " ", "C2": " ",
             "A3": " ", "B3": " ", "C3": " ",
             }

    user_slots = ['PLAYER']
    cpu_slots = ['CPU']

    user_symbol = 'X'
    cpu_symbol = 'O'

    print(f'You play with the "{user_symbol}" symbol.')

    def show_table():
        print(f'  A   B   C \n'
              f'1 {slots["A1"]} | {slots["B1"]} | {slots["C1"]} \n'
              f' ---|---|---\n'
              f'2 {slots["A2"]} | {slots["B2"]} | {slots["C2"]} \n'
              f' ---|---|---\n'
              f'3 {slots["A3"]} | {slots["B3"]} | {slots["C3"]} ')

    def user_mark(sign):
        slot = input("Where do you want to mark: (e.g. b2)").upper()
        if slot in slots_available:
            slots[slot] = sign
            slots_available.remove(slot)
            user_slots.append(slot)
        else:
            print("The slot you selected isn't available or doesn't exists.")
            user_mark(user_symbol)

    def cpu_mark(sign):
        global chosen_comb
        for comb in cpu_combs:
            for item in comb:
                if item in user_slots:
                    cpu_combs.remove(comb)
                    break
        if len(cpu_combs) > 0:
            if chosen_comb not in cpu_combs:
                chosen_comb = random.choice(cpu_combs)
                slot = chosen_comb[-1]
                if slot in slots_available:
                    slots[slot] = sign
                    slots_available.remove(slot)
                    cpu_slots.append(slot)
                    for comb in cpu_combs:
                        for item in comb:
                            if item == slot:
                                comb.remove(item)
                else:
                    slot = random.choice(slots_available)
                    slots[slot] = sign
                    slots_available.remove(slot)
                    cpu_slots.append(slot)
            else:
                slot = chosen_comb[-1]
                if slot in slots_available:
                    slots[slot] = sign
                    slots_available.remove(slot)
                    cpu_slots.append(slot)
                    for comb in cpu_combs:
                        for item in comb:
                            if item == slot:
                                comb.remove(item)
                else:
                    slot = random.choice(slots_available)
                    slots[slot] = sign
                    slots_available.remove(slot)
                    cpu_slots.append(slot)
        else:
            slot = random.choice(slots_available)
            slots[slot] = sign
            slots_available.remove(slot)
            cpu_slots.append(slot)

    def check_end(who):
        global W, L, D
        for comb in winning_comb:
            if comb[0] in who and comb[1] in who and comb[2] in who:
                if who[0] == 'PLAYER':
                    show_table()
                    print("Congratulations! You Win.")
                    W += 1
                    print(f'Total Score = Wins: {W}, Loses: {L}, Draws: {D}')
                    return True
                if who[0] == "CPU":
                    show_table()
                    print("Sorry, You Lose.")
                    L += 1
                    print(f'Total Score = Wins: {W}, Loses: {L}, Draws: {D}')
                    return True
        if len(slots_available) < 1:
            show_table()
            print("It's a draw!")
            D += 1
            print(f'Total Score = Wins: {W}, Loses: {L}, Draws: {D}')
            return True

    while True:
        show_table()
        user_mark(user_symbol)
        if check_end(user_slots):
            play_again = input('Do you want to play again? (Y/N): ').upper()
            if play_again == 'Y':
                game()
            else:
                sys.exit()
        else:
            cpu_mark(cpu_symbol)
            if check_end(cpu_slots):
                play_again = input('Do you want to play again? (Y/N): ').upper()
                if play_again == 'Y':
                    game()
                else:
                    sys.exit()


game()
