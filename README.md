# Exploring New Programming Languages

We've explored server-side programming with JavaScript, but there are many other options out there. In this assignment, we're going to take a look at working in Python.

There won't be a lot of information here on exactly what you should do. There are some pointers here to get you started, but you'll need to do a lot research on your own. 

> You should work through this assignment yourself, but check in with your group as you go to share what you are learning, useful resources, and ask questions.

## Objectives

- install tools required to work with a new language
- explore basic syntax (variables, types, data structures, loops, conditionals, functions) of new language
- solve a whiteboard logic problem in a new language
- document and share what you've learned in a GitHub readme


# Exploring Python

## Setup 

MacOS already has a version of python installed. However it is likely a version of python 2 and the students will want to be working with python 3. 

### Homebrew Python Install 

Install python version 3:

```
brew install python
```

> If you get the following `Error: Permission denied @ dir_s_mkdir - /usr/local/Frameworks`, it can be fixed by doing the following:
>
>
>- `sudo mkdir /usr/local/Frameworks`
>- `sudo chown $USER /usr/local/Frameworks`


If `sudo` isn't allowed, you can also try:

>install -d -o $(whoami) -g admin /usr/local/Frameworks

Then,

>brew reinstall python

---

## Running

Homebrew sets up python 3 as a separate executable, which keeps it from conflicting with the MacOS version. That's awesome, but means instead of using `python` and `pip` you need to run `python3` and `pip3`.

`Pip` is the package manager for Phython, like `npm` for Node.

Check that they both work:

```
python3 --version
pip3 --version
```

## Hello World

A great place to get started with a new language is by making a Hello World program. 

Search the web for a basic Hello World tutorial for your assigned language to get things started. 


## Basic syntax

Hello World is a great starting point, but you'll need to sort out more language features to get a bigger application up and running. Find a language guide to help you with basic syntax for functions, conditionals, and loops.

Take some time to look into how to buff it up a bit by writing a function. Can you get it to say hello to a person by name using a function parameter? 


## Programming

Here is a list of things you should focus on: 

1. Variables & types :
    - how to make a variable (do variables have types?)
    - write to the console

2. Data structures and loops:
    - arrays or lists of things
    - objects

3. Functions and conditionals:
    - write a function that takes arguments and returns a value (sum 2 numbers)
    - operators - math, logical (and/or/not)

4. Pull things all together in one problem. Solve a whiteboard problem! (FizzBuzz, reverse a string or array, LeapYear, etc.) You can find our old whiteboard challenges in the syllabus repository!

## Put it together

After you are a bit familiar with the basic syntax, solve one of our "whiteboard" problems (FizzBuzz, reverse a string or array, LeapYear, etc.) in your new language! Do this on your computer, not on a whiteboard!



### GitHub Repo

Setup a new GitHub repo with a README file that has instruction for installing the new language tools & resources your group found useful. Then add some notes with an example of each of the items listed above. Think of this Readme as a way to highlight your new language learning journey. This is a great way to show potential employers that you can tackle a challenge and learn a new language quickly! 

When you are done, complete the assignment on the portal with your GitHub repo link. 
