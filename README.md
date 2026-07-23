# Blackjack CLI

A simple command-line Blackjack game written in Python.

The player starts by choosing a balance and betting amount. Cards are then dealt to the player and dealer, and the player can continue drawing cards or stand. The dealer automatically draws cards until reaching 17 or higher.

## Current Version

**Version 0.3**

## Features

* Custom starting balance
* Custom betting amount
* Insufficient balance validation
* Complete 52-card deck
* Random card drawing
* Cards are removed from the deck after being drawn
* Player receives two starting cards
* Player can choose to hit or stand
* Dealer automatically draws until reaching at least 17
* Blackjack detection
* Bust detection
* Win, loss, draw, and push detection
* Dealer and player totals are displayed during the game

## Requirements

* Python 3

No external libraries are required. The game only uses Python's built-in `random` module.

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd <repository-folder>
```

Run the game:

```bash
python blackjack.py
```

Depending on your Python installation, you may need to use:

```bash
python3 blackjack.py
```

## How to Play

1. Enter your starting balance.
2. Enter the amount you want to bet.
3. The player is dealt two cards.
4. The dealer draws cards automatically.
5. Enter `Y` to draw another card.
6. Enter `N` to stand.
7. The game compares the player's hand against the dealer's hand.

## Game Rules

* The goal is to reach a total as close to 21 as possible without exceeding it.
* Number cards use their displayed value.
* Jacks, Queens, and Kings are worth 10.
* Aces are currently worth 11.
* The dealer draws while its total is 16 or lower.
* The dealer stands when its total reaches 17 or higher.
* A total above 21 is a bust.
* A total of exactly 21 wins unless both the player and dealer have 21.
* When the player and dealer finish with the same total, the result is a push.

## Example

```text
Select starting money
100
Current Balance: 100
Insert betting amount:
20
8 of Hearts
8
King of Clubs
18
Dealer is standing at 17
Do you want to hit? (Y/N)
N
Player is standing at 18
Player Wins!
```

## Changelog

### Version 0.3

* Added a complete 52-card deck.
* Added random card selection.
* Added card removal after drawing to prevent duplicate cards.
* Added the player's initial two-card hand.
* Added player hit and stand controls.
* Added automatic dealer card drawing.
* Added dealer standing behaviour at 17 or higher.
* Added player and dealer bust detection.
* Added Blackjack detection for both the player and dealer.
* Added draw detection when both sides reach 21.
* Added push detection when both sides have equal totals.
* Added starting balance and betting input.
* Added validation for bets larger than the player's balance.

## Current Limitations

The following features are not implemented yet:

* Aces cannot currently change from 11 to 1 to prevent a bust.
* The player's balance is not updated after winning or losing.
* The betting amount is collected but is not yet used for payouts.
* Only one round can be played before restarting the program.
* Input validation is not included for non-numeric balances or bets.
* Player input is case-sensitive.
* Any response other than uppercase `N` is treated as a hit.
* Natural Blackjack is not distinguished from reaching 21 with additional cards.
* Blackjack payouts, doubling down, splitting, and insurance are not implemented.

## Planned Features

Possible features for future versions include:

* Dynamic Ace values
* Balance updates
* Betting payouts
* Multiple rounds
* Replay functionality
* Improved input validation
* Lowercase input support
* Double down
* Card splitting
* Insurance
* Improved terminal formatting
* Player and dealer hand displays

## Project Structure

```text
blackjack/
├── blackjack.py
└── README.md
```

## Technologies

* Python
* Python `random` module

## License

This project is currently provided for educational and personal use.
