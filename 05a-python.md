# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both containers for an ordered sequence of elements; however, lists are mutable and tuples are not (i.e., you can change list items in-place, but you cannot change tuple items in-place.)  
>>
>> Because dictionaries are implemented using a hash table the keys must be immutable; therefore, tuples can be used as keys in dictionaries and lists cannot.  

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both containers for a sequence of elements; however, lists are ordered and sets are unordered and cannot contain duplicate elements.  Sets use a hash lookup to find elements, which is why they are unordered and cannot contain duplicate elements. Because of the hash lookup sets are more efficient at determining if an element is present in the set but slower than lists when it comes to iterating over their contents.  
>>
>> In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are often throw-away functions (i.e. they are just needed where they have been created.) Lambda functions are often used as the function argument in the `map()`, `filter()`, and `reduce()` functions which apply a function to all the elements of a sequence.  Lambda functions are also frequently used as the key argument to the `sorted' function and `sort` method.
>>
>> The general syntax of a lambda function is quite simple:  
>> ```python
>> lambda argument_list: expression
>> ```
>>
>> The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.  
>> 
>> Simple Example:
>> ```python
>> f = lambda x, y: x+y
>> f(1, 1)
>> 2
>> ```
>>
>> Map Example:  
>> `map(func, seq)` applies the function `func` to all the elements of the sequence `seq`. It returns a new list with the elements changed by `func`.  
>> ```python
>> a = [1, 2, 3, 4]
>> b = [17, 12, 11 ,10]
>> map(lambda x, y: x+y, a,b)
>> [18, 14, 14, 14]
>> ```
>>
>> Sort Example:
>> ```python
>> mylist = [(3, 5, 8), (6, 2, 8), ( 2, 9, 4), (6, 8, 5)]
>> sorted(mylist, key=lambda x: x[1])
>> [(6, 2, 8), (3, 5, 8), (6, 8, 5), (2, 9, 4)]
>> ```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





