TODO: Reflect on what you learned this week and what is still unclear.
i am once again redoing some configuration, making sure this thing works

REVISION MATERIALS: 
Dictionaries use keys and values to define things
keys are strings
everything only has ONE value, just the value can be a list or another dictionary, which is a collection of data
in a string, you can treat it as a list (so in the string "algorithm", you write string[2], which will return g)

use the "with" function to open another file (with open(file_path, mode, encoding = "utf-8") as history_book)
using the other option other than with means you have to manually close the gile
utf-8 encoding lets you use more character sets within the code
reading a file means you do not change the encoding as you must read it with the encoding the author intended it to be
.read()gets the whole file as a single string
.readline() reads the first line, if you say readline() again it will read the next one
.readlines() reads all lines as a separate string in a list
(import os first) os.path.isfile(path_string) checks if the file exists
\n = new line
\t = tab (both are used in an f string if you wanna format it)