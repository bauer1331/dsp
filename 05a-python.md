# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples both have sequences of values that are indexed, and can be used with most list operators. They are different because list are mutable while tuples are immutable, and instead can only replace a tuple with another tuple. Lists being mutable aren't hashable and therefore cannot be used as keys in dictionaries, but tuples being immutable can be used as keys in dictionaries. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both sequences of values, but a set cannot have duplicates and are unordered and hashable. Lists can contain all kinds of objects. To find a specific element, meaning to find if an element is within a sequence of values, sets are much more efficient, because they are implemented using hash tables. An item's existance in a set can be checked using mapping and without searching through every value as a list would. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's `lambda` is a way to create a function object, and is useful for one off functions, where `def` is used more for functions with repeated uses.  
pets = [  
	('Max', 'dog', 13),  
	('Sam', 'cat', 11),  
	('Murphy', 'cat', 9),]  
sorted(pets, key=lambda pet: pet[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to make a new list that iterates over each value in an original list while performing a computation or operation.  
numbers = [1,2,3]  
addone = [n + 1 for n in numbers if n % 2 == 1]  
addonemf = map(lambda n: n + 1, filter(lambda n: n % 2 == 1, numbers))  
While there is much discussion over which, list comprehension or using `map` and `filter` where appropriate, much of the functional uses are the same between the two. `map` incurs an additional function for each element and when used with a lambda function, while list comprehension is compiled into a loop. With existing functions, usng `map` can be beneficial.  
Set comprehensions are similar to list comprehensions:  
setcomp = {x for x in 'settled' if x not in 'moved'}  
Dictonary comprehensions:  
addonedict = {n: n + 1 for n in numbers if n % 2 == 1}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





