import random


def deal(cards, number_of_players):
    deck = shuffle_deck(cards)

    deal_to_players(deck, number_of_players)
    deal_to_table(deck)


def deal_to_table(deck):
    next(deck)
    flop = ', '.join(str(next(deck)) for _ in range(3))
    print(f"The flop: {flop}")

    next(deck)
    print(f"The turn: {next(deck)}")

    next(deck)
    print(f"The river : {next(deck)}")

    print()


def deal_to_players(deck, number_of_players):
    first_cards = [next(deck) for _ in range(number_of_players)]
    second_cards = [next(deck) for _ in range(number_of_players)]

    hands = zip(first_cards, second_cards)

    print()

    for i, (first, second) in enumerate(hands, start=1):
        print(f"Player {i} was dealt: {first}, {second}")

    print()


def shuffle_deck(deck):
    deck = deck[:]
    random.shuffle(deck)

    return iter(deck)


def get_player():
    while True:
        try:
            number_player = int(input("How many players to play: "))
        except ValueError:
            print("You must enter an integer.")
        else:
            if number_player in range(2, 11):
                return number_player
            elif number_player < 2:
                print("You must have atleast 2 players to play.")
            else:
                print("You can have maximum 10 players")


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = []

for suit in suits:
    for rank in ranks:
        cards.append((rank, suit))

deal(cards, get_player())
