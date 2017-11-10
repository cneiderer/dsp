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

>> The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are often throw-away functions (i.e. they are just needed where they have been created.) Lambda functions are often used as the function argument in the `map()`, `filter()`, and `reduce()` functions which apply a function to all the elements of a sequence.  Lambda functions are also frequently used as the key argument to the `sorted()` function and `sort` method.
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
>> Mapping Example:  
>> `map(func, seq)` applies the function `func` to all the elements of the sequence `seq`. It returns a new list with the elements changed by `func`.  
>> ```python
>> a = [1, 2, 3, 4]
>> b = [17, 12, 11 ,10]
>> list(map(lambda x, y: x + y, a, b))
>> [18, 14, 14, 14]
>> ```
>>
>> Filtering Example:  
>> The function `filter(func, seq)` offers an elegant way to filter out all the elements of a sequence `seq` for which the function `func` returns True.
>> ```python
>> fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>> list(filter(lambda x: x % 2 == 0, fib))
>> [0, 2, 8, 34]
>> ```
>>
>> Sorting Example:
>> `sorted(seq, key=func)` returns a new list with the elements of the sequence `seq` sorted according to function `func`.  
>> ```python
>> mylist = [(3, 5, 8), (6, 2, 8), ( 2, 9, 4), (6, 8, 5)]
>> sorted(mylist, key=lambda x: x[1])
>> [(6, 2, 8), (3, 5, 8), (6, 8, 5), (2, 9, 4)]
>> ```
>> In this example, for each element `x` in `mylist` the lambda returns index 1 of that element, then sort all the elements of the original list `mylist` by the sorted order of the list returned by the lambda function.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehensions are a special notation for building up lists, dictionaries and sets from other lists, dictionaries and sets, modifying and filtering them in the process. They allow you to express complicated looping logic in a tiny amount of space.  
>>
>> Comprehensions are very similar to the `map()` and `filter()` functions which apply a function to each element in a sequence to either modify or filter the elements of the sequence.
>>
>> List comprehensions are the best known and most widely used. A list comprehension provides a compact way of mapping a list into another list by applying a function to each of the elements of the list.
>>
>> List Comprehension vs. `map()` Function Example:  
>> ```python
>> a = [1, 2, 3, 4]
>> b = [17, 12, 11, 10]
>> 
>> # list comprehension
>> [x + y for x, y in zip(a, b)]
>> [18, 14, 14, 14]
>>
>> # map function
>> list(map(lambda x, y: x + y, a, b))
>> [18, 14, 14, 14]
>>
>> ```
>>
>> List Comprehension vs. `filter()` Function Example:
>> ```python
>> fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>
>> # list comprehension
>> [x for x in fib if x % 2 == 0]
>> [0, 2, 8, 34]
>>
>> # filter function
>> list(filter(lambda x: x % 2 == 0, fib))
>> [0, 2, 8, 34]
>> ```
>> 
>> Set Comprehension Example:  
>> The syntax for set comprehensions is almost identical to that of list comprehensions, but it uses curly brackets instead of square brackets. The pattern takes the form `{expr for item in sequence}`, and the result the same as passing the output of the equivalent list comprehension to the set function.
>> ```python
>> {x ** 2 for x in [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]}
>> {1, 4, 9, 16, 25}
>> ```
>>
>> Dictionary Comprehension Example:  
>> The syntax for a dictionary comprehension is similar to a list comprehension; however, it outputs a key in addition to the result of the expression. The pattern takes the form `{key: expr for item in seq}`.
>> ```python
>> n = range(1, 6)
>> {x: x ** 2 for x in n}
>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>> ```

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





