"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#I think this will define and create a list using the square brackets
some_words = ["what", "does", "this", "line", "do", "?"] #Since this one does not return anything, I cannot confirm. However, I can assume that it did this job due to later commands working as they do

# I think that this will print out each word in the some_words list, each on a separate line
for word in some_words:
    print(word) #it printed out each word on the list as a separate line

# I think that this will be the same as the previous code
for x in some_words:
    print(x) # it gave the exact same answer as the last code

# I think that this will print the entire list on one line
print(some_words) #it printed the entire list on one line, however it added a square bracket on either side, put each word in between apostrophes and commas, with spaces

# I think that this will do flow control on whether the length of the list is longer than 3, if it is it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words") # it printed "some_words contains more than 3 words"

# I think that this will give names of certain computer parts in a tuple
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction() #It printed the computer parts, however in 6 sections, system, node, release, version and machine
