"""
.        Matches any single character
\        Escapes one of the meta characters to treat it as a regular character
[...]    Matches a single character or a range that is contained within brackets
         _- -_ order does not matter but without brackets order does matter
+        Matches the preeceding element one or more times
?        Matches the preeceding pattern element zero or one time
*        Matches the preeceding element zero or more times
{m,n}    Matches the preeceding element at least m and not more than n times
^        Matches the beginning of a line or string
$        Matches the end of a line or string
[^...]   Matches a single character or a range that is not contained within the brackets
?:...|..."Or" operator
()       Matches an optional expression
"""

import re

# #regular expressions
# filenames = ['nov-12.txt', 'november-14.txt', 'Oct-17.txt', 'nov-22.txt']

## search for email addresses
# text = "fgnergnien onero onwrong on_wonf@example.com  weofeowhf wff fff@example.de"

# pattern = re.compile("[^ ]+@[^ ]+.[a-z]+")
# matches = pattern.findall(text)
# print(matches)

# pattern = re.compile("[^ ]+@[^ ]+\.(?:com|de)+")
# matches = pattern.findall(text)
# print(matches)

# ## read urls from txt file
# with open('urls.txt', 'r') as file:
#   content = file.read()

# print(content)
# pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
# matches = pattern.findall(content)
# print(matches)

# ## read ips from txt file
# with open('ips.txt', 'r') as file:
#   content = file.read()

# print(content)
# pattern = re.compile("[0-9]{3}\.[0-9]{3}\.12[0-9]{1}\.[0-9]{3}")
# matches = pattern.findall(content)
# print(matches)

# ##read specific files from
# from pathlib import Path

# root_dir = Path('files_bills')

# filenames = [str(filename.name) for filename in root_dir.iterdir()]

# print(filenames)

# import re

# #find bills documents between nov 1 - nov 20
# pattern = re.compile("nov[a-z]*-(?:[1-9]|1[0-9]|20).txt", re.IGNORECASE)
# matches = [filename for filename in filenames if pattern.findall(filename)]
# print(matches)

#find a word in a text

word = 'Delhi'
data = [
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com",
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog", "mr Sen Kumar Delhi 3456 ants"
]

import re

#.* - any number of any characters
pattern_word_email = re.compile(".*Delhi.*[^ ]+@[^ ]+\.[a-z]+", re.IGNORECASE)
pattern_word_phone = re.compile(".*Delhi.*[0|+][0-9]{4,10}", re.IGNORECASE)
pattern_phone_or_email = re.compile(".*Delhi.*([0|+][0-9]{4,10}|[^ ]+@[^ ]+\.[a-z]+)", re.IGNORECASE)

output = []
for item in data:
  if pattern_phone_or_email.findall(item):
    output.append(item)

print(output)
