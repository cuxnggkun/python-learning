import argparse
import random


def parse_roll(args):
    try:
        quantity, dice_size = [int(x) for x in args.dice.split('d')]
        return quantity, dice_size
    except Exception as e:
        raise e


def write_log(file_path, data):
    with open(file_path, 'a') as fo:
        fo.write(data)


parser = argparse.ArgumentParser(description="A command line dice roller")

parser.add_argument("dice", help="A representation of the dice you want to roll")

parser.add_argument(
    "-l", "--log",
    type=str,
    default="rolls_log.txt",
    help="A file to use to log the result of the rolls",
)

parser.add_argument(
    "-r", "--repeat",
    type=int,
    default=1,
    help="How many times to roll the specifed set of dice"
)

args = parser.parse_args()

quantity, dice_size = parse_roll(args)
repetitions = args.repeat
log_file = args.log

for _ in range(repetitions):
    rolls = [random.randint(1, dice_size) for _ in range(quantity)]
    total = sum(rolls)
    average = total / len(rolls)

    rolls_formatting = ', '.join(map(str, rolls))
    data = f"""Rolls: {rolls_formatting}
Total: {total}
Average: {average:.2f}\n\n"""
    write_log(log_file, data)

