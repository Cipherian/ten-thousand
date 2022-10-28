
# Project: Ten Thousand
---

*Author: Andy Nguyen, Daniel Brott, Natalija Germek*

---

## Description

***[Dice Roll game that implements tuples, dictionaries and methods to pick random dice, calculate score, store score per round, and return Zilch when score of 0 is rolled.]***

---

## Methods

| Method          | Summary                                                                                          | Big O Time | Big O Space | Example           | 
|:----------------|:-------------------------------------------------------------------------------------------------|:----------:|:-----------:|:------------------|
| roll_dice       | Static Method: Rolls a dice with a random integer value and appends it to a tuple.               |    O(n)    |    O(n)     | roll_dice()       |
| calculate_score | Static Method: Takes in the value of the dice roll and calculates based on integers rolled total |    O(n)    |    O(n)     | calculate_score() |



---


### roll_dice
***[Static method to retrieve a random dice roll]***

*The roll_dice method takes in an int as a parameter.* 
*Creates a list of integers from 1-6*
*The int is grabbed by the randint method and then appended to a list and converted tuple*

### Calculated Score
***[Calculating the score of the turn based on the dice roll]***
*The calculating score method will take in the dice roll tuple from rolled dice method.*
*Assigning a variable to the counter method that we imported*
*Assigning the variable total score to the value of zero*
*Assigning third variable to total of dice values*
*If statement checking the sum of dice rolls to 21 and returning score of 1500*
*If statement checking whether we have three sets of two pairs and returning score of 1500*
*Iterating through dice roll keys*
*If statement to check if fewer then three dice are matching and we will calculate the points and add to total*
*Else if statement to check if three or more dice are matching and will calculate the points and add to the total*
*Returning the total score*

---

### Game Directions

1. Create virtual environment

```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

2. User follows input prompts from dice game to store points earned per round through option to bank, roll again or quit game. Returns total points earned prior to quitting.

```bash
python3 ten_thousand/game.py
```

3. Run all tests

```bash
pytest -v
```

4. Deactivate virtual environment

```bash
deactivate
```

---

## Change Log

***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***

1.0: *Completed initial Project Featured Tasks* - 19 Oct 2022

2.0: *Completed Project Feature Tasks* - 22 Oct 2022

3.0: *Version 3 Python test files passing* 27 Oct 2022

---