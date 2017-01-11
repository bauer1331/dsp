Python 2 has 31 keywords:
and
as
assert
break
class
continue
def
del
elif
else
except
exec
finally
for
from
global
if
import
in
is 
lambda 
not
or
pass
print
raise
return
try
while
with 
yield
Python 3 nonlocal


Operators
+ addition
- subtraction
* multiplication
/ division
** exponentiation
% modulus operator - remainder
Python 3 // = floor division


Relational Operators
== true or false boolean, type bool
!=  not equal
x > greater than 
x < less than
x >= greater than or equal to
x <= less than or equal to 
and 
or
not
nonzero number is interpreted as "true"
+= - short way to update a variable, accumulator 

Operators for strings
+  concatinates strings 
* replicates 

#comments code


conditional execution
if x > 0:
	print 'x is positive'

if x < y:
	print 'x is less than y'
elif x> y:
	print 'x is greater than y'
else: #else has to be at the end, but the last one does not have to be else can be elif
	print 'x and y are equal'



Things to watch out for 
a = [1,2,3]
b = a #this does not make a copy, it creates an alias and changing one changes both

for strings + creates a new list, while append modifies a current list

Strings create new strings and leave the original alone. List functions modify lists that
already exist and do not create new ones.

To make a copy do orig = t[:]

