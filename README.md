# Python Calculator

A small command-line calculator I built in Python. You pick an operation from a menu, type in your numbers, and it prints the answer. Nothing fancy, just a simple project to practice loops, functions, and user input.

## What it can do

- Add, subtract, multiply and divide
- Raise a number to a power
- Work out a percentage of a number
- Find a square root
- Stop you from dividing by zero or taking the square root of a negative number

## Requirements

Python 3.6 or newer. It only uses the built-in `math` and `os` modules, so there's nothing to install.

## How to run it

Download or clone the project, open a terminal in the folder, and run:

```bash
python calculator.py
```

If that doesn't work, try `python3 calculator.py`.

## Using it

You'll see a menu with eight options. Type the number of the one you want and press Enter. The program asks for the numbers it needs, shows the result, and then waits for you to press Enter before going back to the menu. Choose 8 to quit.

Here's what a couple of runs look like:

```
Enter your choice: 4

Enter first number: 25
Enter second number: 5

Result = 5.0
```

```
Enter your choice: 6

Enter number: 200
Enter percentage: 15

Result = 30.0
```

Note that the percentage option gives you "X percent of a number", so 15% of 200 is 30.

## Known issues

If you type something that isn't a number (like a letter) when it asks for a number, the program crashes. I haven't added error handling for that yet.

## Things I want to add

- Proper handling of bad input
- More operations like modulus, factorial and logarithms
- A history of past calculations
- Maybe a simple GUI with Tkinter

## License

MIT. Feel free to use it however you like.
