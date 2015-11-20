"""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""
import re
st = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

ext = re.findall('\S+?@\S+', st)
print ext

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y

numbers = "here is 10 8 and here 768 is some more 6"
s = re.findall('[0-9]+', numbers)

