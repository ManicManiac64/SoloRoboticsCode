# PYTHON (PART ONE: THE BEGINNING)

Python. It exists, fun fact. It's a programming language, but you probably already know that part, otherwise you wouldn't be here. Compared to the two other major languages used to program robots, C++ and Java, Python is much more readable and simple to learn. It isn't supported by FRC (yet), but it's got support in RobotPy, a project that allows you to program FRC robots with Python. Speaking of Python, let's get into Python.

## "HELLO WORLD!" AND OTHER BITS OF TRIVIA

"Hello, world!" is what I said when I was born. My parents were not surprised. Anyway, it's also coincidentally the first line most people type in a programming language, so I guess that was foreshadowing back in that hospital. In order to print something to the console (where we get all our output), we use the *print()* function. More on functions later, for now, just type this, and be amazed by the words "Hello, world!" appearing on your screen:

```
print("Hello, world!")
OUTPUT: Hello, world!
```

Breaking this down, we have the *print()* function, as well as stuff inside that function. There are different types of data in Python, and in this case, we are using a string. A string is basically speaking, words. We make a string by encasing whatever we want in the string with either single or double quotation marks.

"Hi!"
"Among Us"
"39 buried, 0 found"

In this case, we have a string "Hello, world!". Passing this to *print()*, you guessed it, prints out "Hello, world!" to the console. You don't have to limit yourself to strings, of course. You can print out integers, aka ints (1, 2, 3, 4); floats, or decimal numbers (1.1, 2.2, 3.3, 23.5791936123), ~~and pieces of paper~~ and other data types.

## OPERATIONS

Remember those numbers from earlier? We can use those to make bigger, different numbers. Math! If you're reading this guide, you probably already have an understanding of how math works, but you might not know how to add things in Python.

To add two numbers in Python, use the + operator. To subtract a number from another number in Python, use the - operator. To multi-

Yeah, you get the idea. Let's say you want to know what 493 * 12 is, and you for some reason don't have access to a calculator, and you don't have me to wow you with my mental math skills, but somehow you have Python. Unrealistic situation, but if we wanted to use Python to figure out what this is, we'd just do 493 * 12. That's it. Well, of course, then there's the issue of printing it.

```
print(493 * 12)
OUTPUT: 5916
```

Issue solved.

Some other operations you're definitely going to be using besides addition (+), subtraction (-), multiplication (\*), and division (/) are as follows:

Modulo (%) finds the remainder when dividing two numbers. 5 % 2 = 1, 572 % 124 = 76, etc.
Floor division (//) finds essentially the quotient rounded down. Remember doing short division? I don't, but basically that quotient you would get from that is floor division. 5 // 2 = 2, 572 // 124 = 4, etc.

## CONCATENATION AND TYPE-CASTING

Two big words, two very simple topics.

Let's say you have two strings. I'll say they're "Hello, ", and " world!", because I'm unoriginal. To smash these together, we can use the + operator. When used on two strings, the + operator links them together.

```
print("Hello, " + " world!")
OUTPUT: Hello, world!
```

Moving on, let's say you've got an integer, 3, and you want to link it to a string, we'll say "I've printed out Hello world! this many times: "



