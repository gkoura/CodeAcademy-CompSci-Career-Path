import random

# Define the Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = min(10, rank) if isinstance(rank, int) else 10 if rank in ['J', 'Q', 'K'] else 11

# Define the Deck class
class Deck:
    def __init__(self):
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop()

# Define the Player class
class Player:
    def __init__(self):
        self.hand = []
        self.balance = 100  # Starting balance
        self.bet = 0
    
    def add_card(self, card):
        self.hand.append(card)
    
    def calculate_points(self):
        points = sum(card.value for card in self.hand)
        if points > 21 and any(card.rank == 'A' for card in self.hand):
            points -= 10  # Handle Ace as 1 instead of 11 to avoid busting
        return points

    def place_bet(self, bet):
        if bet <= self.balance:
            self.bet = bet
        else:
            print("Insufficient balance for this bet.")

    def win_bet(self):
        self.balance += self.bet
    
    def lose_bet(self):
        self.balance -= self.bet

# Initialize the game
deck = Deck()
player = Player()

while True:
    # Start a new round
    deck.shuffle()
    player.hand = []
    dealer = Player()

    # Place a bet
    while True:
        try:
            bet = int(input(f"Your balance: ${player.balance}. Place your bet: "))
            player.place_bet(bet)
            break
        except ValueError:
            print("Invalid input. Please enter a valid bet.")

    # Deal initial cards
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())

    # Player's turn
    while True:
        print("\nYour hand:", [f"{card.rank} of {card.suit}" for card in player.hand])
        print("Your points:", player.calculate_points())

        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player.add_card(deck.draw_card())
            if player.calculate_points() > 21:
                print("Bust! You lose.")
                player.lose_bet()
                break
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    # Dealer's turn
    while dealer.calculate_points() < 17:
        dealer.add_card(deck.draw_card())
    
    # Determine the winner
    print("\nYour hand:", [f"{card.rank} of {card.suit}" for card in player.hand])
    print("Your points:", player.calculate_points())
    print("\nDealer's hand:", [f"{dealer.hand[0].rank} of {dealer.hand[0].suit}", "Face Down"])

    if player.calculate_points() <= 21:
        if dealer.calculate_points() > 21 or player.calculate_points() > dealer.calculate_points():
            print("You win!")
            player.win_bet()
        elif player.calculate_points() == dealer.calculate_points():
            print("It's a tie!")
        else:
            print("Dealer wins.")
            player.lose_bet()
    
    print(f"Your balance: ${player.balance}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
