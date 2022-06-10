import csv
import dice_roller


def write_to_csv():
    # Generate arrays with numbers amount of dice from 1 to 10
    one = dice_roller.generate_pools(1)
    two = dice_roller.generate_pools(2)
    three = dice_roller.generate_pools(3)
    four = dice_roller.generate_pools(4)
    five = dice_roller.generate_pools(5)
    six = dice_roller.generate_pools(6)
    seven = dice_roller.generate_pools(7)
    eight = dice_roller.generate_pools(8)
    nine = dice_roller.generate_pools(9)
    ten = dice_roller.generate_pools(10)

    # Creating a .csv file with provided arrays
    with open('rolls.csv', mode='w') as rolls:
        roll_writer = csv.writer(rolls, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        # Manually setting the top value for each column
        column_heads = ['1T6', '2T6', '3T6', '4T6', '5T6', '6T6', '7T6', '8T6', '9T6', '10T6']

        # Writing a row using the index value from all arrays
        roll_writer.writerow(column_heads)
        for x in range(100):
            roll_writer.writerow(
                [one[x], two[x], three[x], four[x], five[x], six[x], seven[x], eight[x], nine[x], ten[x]])
