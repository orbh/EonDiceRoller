import random
import numpy


def roll_dice(num_of_dice):
    # Generates a result from the number of dice provided.
    dicebag = []
    dice_to_roll = num_of_dice
    while dice_to_roll > 0:
        dice = random.randint(1, 6)
        # Eon uses exploding dice (a rolled 6 re-rolls itself + adds another dice)
        if dice != 6:
            dicebag.append(dice)
            dice_to_roll = dice_to_roll - 1
        else:
            dice_to_roll = dice_to_roll + 2

    # Returns the sum of all rolled dice
    return numpy.sum(dicebag)


def generate_pools(num_of_dice):
    # Generates an array with 100 results based on provided number of dice to roll
    pool = []
    for y in range(100):
        pool.append(roll_dice(num_of_dice))
    return pool


def roll_improvement(num_of_dice, additional_points, target_number):
    roll = roll_dice(num_of_dice)
    total = roll + additional_points
    print('')
    print('Target number: ' + str(target_number))
    print('Your roll: ' + str(total) + '(' + str(roll) + '+' + str(additional_points) + ')')
    if total >= target_number:
        print('Success!')
        print('')
    else:
        print('Failure.')
        print('')
    return


def calc_improvement_diff(num_of_dice, additional_points, modifier):
    # The book-provided formula for calculating the difficulty.
    # The modifier parameter is calculated in the main function and
    # sent here as a finished number.
    x = num_of_dice * 8
    y = additional_points * 2
    starting_reduction = -12
    return x + y + starting_reduction + modifier

