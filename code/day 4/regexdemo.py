'''
Regex:
A regular expression is a sequence of chars
that define a search pattern

Regex contains : literal and meta chars
file+ : literal (constant)
Meta chars : $,+,*,?,^,(),[],{}.....

+ : one or more occurences
? :zero or one
* : zero or more
^ : starts with     ^file
$ : ends with      com$
{n,m}: n to m repetitions {0,3}
[a-z] : small case alphabets from a-z [A-Z] [0-9]
\d : digit : "/\d{3}-\d{5}/"                  3434-4545'

compiling reg. expression:
Regex patterns are compiled into a serios of
bytocode which are then executed by python engine.

import re
re.compile(pattern,flags)  /I,M,/g

match()
search()
findall()
finditer()
group()
sub()
replace()

match(string,pos[0,,endpos])
'''
import re

'''
sentence="Start a sentence and then bring it to an end"

pattern=re.compile('start',re.I)
matches=pattern.search(sentence)
print(matches)

#srirammurthy@gmail.com  edu  net SRIram786
#validate email what user enters from keyboard
pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
mail=input("Enter you email:")
#^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$
if (re.search(pattern,mail)):
    print("Valid Email .. connect to db")
else:
    print("Sorryyy..invalid email")

emails="""
     sriram@gmail.com
     murthy.sri@yahoo.co.in
     sri-786@mywork.net
     johnDoe

     """
matches=re.finditer(pattern,emails)
for m in matches:
    print(f'valid mail {m}')

'''

urls="""
    https://www.google.com
    https://coreyms.com
    https://youtube.com
    https://www.nasa.gov
   """
pattern=re.compile('https?://(www\.)?(\w+)(\.\w+)')
matches=pattern.finditer(urls)
for m in matches:
    print(m.group(3))


subbed_urls=pattern.sub(r'\2\3',urls)
print(subbed_urls)


