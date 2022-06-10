import time

import csv_writer
import dice_roller

menu_options = {
    1: "Generate rolls as .CSV",
    2: "Do improvement rolls",
    3: "Exit"
}


def print_main_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


while True:
    try:
        print_main_menu()
        option = int(input('Enter your choice: '))
        if option == 1:

            print('Starting generating a .CSV file.')
            csv_writer.write_to_csv()
            print('...')
            print('Done. A .CSV-file has been created in this folder.')
            print('')
        elif option == 2:
            try:
                chars = list(input('Enter the level of the skill (e.g "3T6+2"): '))
                modifier = 0
                first_question = False
                while not first_question:
                    easy = input('Easy to learn?: (y/n) ')
                    if easy == 'y':
                        modifier += -2
                        first_question = True

                    if easy == 'n':
                        first_question = True
                        second_question = False
                        while not second_question:
                            hard = input('Hard to learn?: (y/n) ')
                            if hard == 'y':
                                modifier += 4
                                second_question = True
                            if hard == 'n':
                                second_question = True

                third_question = False
                while not third_question:
                    lower = input('Skill lower than governing attribute?: (y/n) ')
                    if lower == 'y':
                        modifier += -2
                        third_question = True
                    if lower == 'n':
                        third_question = True

                to_beat = 0

                if chars.__len__() == 5:
                    to_beat = dice_roller.calc_improvement_diff(int(chars[0]), int(chars[4]), modifier)
                    dice_roller.roll_improvement(int(chars[0]), int(chars[4]), int(to_beat))
                elif chars.__len__() == 3:
                    to_beat = dice_roller.calc_improvement_diff(int(chars[0]), 0, modifier)
                    dice_roller.roll_improvement(int(chars[0]), 0, int(to_beat))
                else:
                    print('')
                    print('Dice formatting error.')
                    print('')
            except IndexError:
                print('An error occurred. Did you enter a valid skill level?')

        elif option == 3:
            print('')
            print('Exiting.')
            time.sleep(0.5)
            exit()
        else:
            print('')
            print('Invalid option. Please enter a valid number.')
            print('')

    except ValueError:
        print('')
        print('Invalid option. Please enter a valid number.')
        print('')
