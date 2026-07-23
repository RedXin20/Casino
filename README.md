# Blackjack V0.3

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

## Technologies

* Python
* Python `random` module

## License

This project is currently provided for educational and personal use.
