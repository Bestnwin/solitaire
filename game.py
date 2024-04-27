import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# Function to shuffle a deck of cards
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to divide the deck into 2 different decks
def divide_deck(deck):
    half_length = len(deck) // 2
    first_half = deck[:half_length]
    second_half = deck[half_length:]
    return first_half, second_half

# Function to print the rules of the game
def Rules():
    print("\n\nRules of the game: \n")
    print("You are given a deck of cards which are shuffled and divided into two equal halves.")
    print("You will be given the option to draw cards from one of the halves.")
    print("You need to match cards of different suits having the same number in a pair.")
    print("You can also remove a card if its suit is the same and its number is n and n+2 or n-2.")
    print("You can keep the card in the empty list if you do not find any match.")
    print("After removing, you will be given a choice whether to take cards from the first half, second half, or both.")
    print("You need to complete the game until you are out of cards or you write 'end'.\n\n\n")

# Function to draw cards from the deck
def draw_cards(cards, num):
    return cards[:num]

# Printing a list of Cards:
def Print_card(selected_cards):
    for card in selected_cards:
        print(f"{card.value} of {card.suit}", end="        ")

# Taking input from the user for the card
def User_Card():
    value = int(input("Enter the card rank (1-13): "))
    suit = input("Enter the card suit (hearts, diamonds, spades, clubs): ")
    return Card(value, suit)

# Removing a card from the deck
def remove_card_from_deck(card, deck):
    if card in deck:
        deck.remove(card)
    else:
        print(f"{card.value} of {card.suit} is not in the deck.")
    return deck

# Interacting with the cards
def interact_with_cards(cards, empty_list):
    print("\nChoose an option:")
    print("1. Remove a card")
    print("2. Put a card in an empty list")
    print("3. Quit")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        print("Available cards:")
        card1 = User_Card()  # taking input from user
        card2 = User_Card()
        if card1.value == card2.value:
            cards = remove_card_from_deck(card1, cards)
            cards = remove_card_from_deck(card2, cards)
        elif card1.suit == card2.suit and (card1.value == card2.value + 2 or card1.value - 2 == card2.value):
            cards = remove_card_from_deck(card1, cards)
            cards = remove_card_from_deck(card2, cards)
    elif choice == 3:
        print("Game Over")
        cards = None
    elif choice == 2:
        card1 = User_Card()  # taking input from user
        card2 = User_Card()
        empty_list.append(card1)
        empty_list.append(card2)
        print("Card put in an empty list.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
    return empty_list, cards

suits = ['hearts', 'diamonds', 'spades', 'clubs']  # suits

# Creating a deck of cards
deck = [Card(value, suit) for value in range(1, 14) for suit in suits]

# Shuffling the deck of cards
shuffle_deck(deck)

# Dividing deck into 2 parts
first_half, second_half = divide_deck(deck)

# Displaying the cards in the first half
for card in first_half:
    print(f"{card.value} of {card.suit}")

# Rules of the Game
Rules()

# Choosing an option
print("Choose an option:")
print("1. Draw from the first half")
print("2. Draw from the second half")
choice = int(input("Enter your choice (1/2): "))
num_cards = int(input("How many cards do you want to draw from each half? (if doing for the first time, use 4) "))
if choice == 1:
    selected_cards = draw_cards(first_half, num_cards)
    first_half = first_half[num_cards:]  # Remove drawn cards
elif choice == 2:
    selected_cards = draw_cards(second_half, num_cards)
    second_half = second_half[num_cards:]  # Remove drawn cards
else:
    print("Invalid choice. Please choose 1 or 2.")

print("Selected Cards are : \n")
Print_card(selected_cards)

# Creating a list of 4 elements to store those card values if no unique number is found to be matched
empty_list = []

while True:
    empty_list, selected_cards = interact_with_cards(selected_cards, empty_list)
    if selected_cards is None:
        break
    if len(empty_list) > 0:
        print("Empty List contains:")
        Print_card(empty_list)
        print("\n")
    if len(selected_cards) == 0:
        print("Congratulations! You won the game.")
        break
    print("Remaining Cards:")
    Print_card(selected_cards)
    print("\n")

    # Choosing an option to draw more cards
    print("Choose an option:")
    print("1. Draw from the first half")
    print("2. Draw from the second half")
    choice = int(input("Enter your choice (1/2): "))
    if choice == 1:
        x = draw_cards(first_half, 1)
        for i in x:
            selected_cards.append(i)
        first_half = first_half[1:]  # Remove drawn cards
    elif choice == 2:
        x = draw_cards(second_half, 1)
        for i in x:
            selected_cards.append(i)
        second_half = second_half[1:]  # Remove drawn cards
    else:
        print("Invalid choice. Please choose 1 or 2.")
