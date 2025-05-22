# Python exercises from CS50P 2022

## 📁WATCH_ON_YOUTUBE (problem set 7)

It turns out that (most) YouTube videos can be embedded in other websites, just like the above. For instance, if you visit *https://youtu.be/xvFZjo5PgG0* on a laptop or desktop, click Share, and then click Embed, you’ll see HTML (the language in which web pages are written) like the below, which you could then copy into your own website’s source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes” therein, the value of which, between quotes, is *https://www.youtube.com/embed/xvFZjo5PgG0*.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

Because some HTML attributes are optional, you could instead minimally embed just the below:

```html
<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
```

Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages *(e.g., https://www.youtube.com/embed/xvFZjo5PgG0)*, converting them back to shorter, shareable youtu.be URLs *(e.g., https://youtu.be/xvFZjo5PgG0)* where they can be watched on YouTube itself.

In a file called `watch.py`, implement a function called `parse` that expects a str of HTML as input, extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and *returns its shorter, shareable youtu.be equivalent as a str*. Expect that any such URL will be in one of the formats below. Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.

- *http://youtube.com/embed/xvFZjo5PgG0*
- *https://youtube.com/embed/xvFZjo5PgG0*
- *https://www.youtube.com/embed/xvFZjo5PgG0*

## 📁NUMB3RS (problem set 7)

In Season 5, Episode 23 of _NUMB3RS_, a supposed IP address appears on screen, `275.3.6.28`, which isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

In a file called `numb3rs.py`, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

## 📁SCOURGIFY (problem set 6)

Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:

```javascript
name, house
'Abbott, Hannah', Hufflepuff
'Bell, Katie', Gryffindor
'Bones, Susan', Hufflepuff
'Boot, Terry', Ravenclaw
'Brown, Lavender', Gryffindor
'Bulstrode, Millicent', Slytherin
'Chang, Cho', Ravenclaw
'Clearwater, Penelope', Ravenclaw
'Crabbe, Vincent', Slytherin
'Creevey, Colin', Gryffindor
'Riddle, Tom', Slytherin
'Robins, Demelza', Gryffindor
'Scamander, Newt', Hufflepuff
```

Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

> Dear Potter, Harry,

Rather than with, for instance:

> Dear Harry,

In a file called `scourgify.py`, implement a program that:

- Expects the user to provide two command-line arguments:
  - The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
  - The name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
- Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

## 📁LINES_OF_CODE (problem set 6)

One way to measure the complexity of a program is to count its number of lines of code (LOC), excluding blank lines and comments. For instance, a program like

```python
# Say hello

name = input("What's your name? ")
print(f"hello, {name}")
```

has just two lines of code, not four, since its first line is a comment, and its second line is blank (i.e., just whitespace). That’s not that many, so odds are the program isn’t that complex. Of course, just because a program (or even function) has more lines of code than another doesn’t necessarily mean it’s more complex. For instance, a function like

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

isn’t really twice as complex as a function like

```python
def is_even(n):
    return n % 2 == 0
```

even though the former has (more than) twice as many lines of code. In fact, the former might arguably be simpler if it’s easier to read! So lines of code should be taken with a grain of salt.

Even so, in a file called `lines.py`, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

## 📁GUESSING_GAME (problem set 4)

In a file called `game.py`, implement a program that:

Prompts the user for a level _n_

- If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and
  _n_ inclusive, using the random module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
  - If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
  - If the guess is larger than that integer, the program should output Too large! and prompt the user again.
  - If the guess is the same as that integer, the program should output Just right! and exit.

## 📁LITTLE_PROFESSOR (problem set 4)

One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called `professor.py`, implement a program that:

- Prompts the user for a level, `n`. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as `X + Y = `, wherein each of `X` and `Y` is a non-negative integer with `n` digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.

## 📁FELIPES_TAQUERIA (problem set 3)

One of the most popular places to eat in Harvard Square is Felipe’s Taqueria, which offers a menu of entrees, per the dict below, wherein the value of each key is a price in dollars:

```python
{
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
```

In a file called `taqueria.py`, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

## 📁FUEL_GAUGE (problem set 3)

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like `ValueError` or `ZeroDivisionError`.

## 📁VANITY_PLATES (problem set 2)

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”

- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

- “No periods, spaces, or punctuation marks are allowed.”

In `plates.py`, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.

## 📁CAMEL_CASE (problem set 2)

In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (\_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called `camel.py`, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

## 📁COKE_MACHINE (problem set 2)

Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called `coke.py`, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

## 📁MEAL_TIME (problem set 1)

Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In `meal.py`, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

```python
def main():
    ...


def convert(time):
    ...


if __name__ == "__main__":
    main()
```

## 📁HOME_FEDERAL_SAVING_BANKS (problem set 1)

In season 7, episode 24 of Seinfeld, Kramer visits a bank that promises to give $100 to anyone who isn’t greeted with a “hello.” Kramer is instead greeted with a “hey,” which he insists isn’t a “hello,” and so he asks for $100. The bank’s manager proposes a compromise: “You got a greeting that starts with an ‘h,’ how does $20 sound?” Kramer accepts.

In a file called `bank.py`, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

## 📁FILE_EXTENSIONS (problem set 1)

In a file called `extensions.py`, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.

## 📁PLAYBACK_SPEED (problem set 0)

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

## 📁MAKING_FACES (problem set 0)

Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

## 📁INDOOR (problem set 0)

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

## 📁TIP_CALCULATOR (problem set 0)

In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost. Not to worry, though, we’ve written a tip calculator for you, below!

```python
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO


def percent_to_float(p):
    # TODO


main()
```

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:

- dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
- percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.

_Assume that the user will input values in the expected formats._
