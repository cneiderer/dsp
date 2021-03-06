# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> 1. `pwd`&emsp;show current working directory
>> 2. `mkdir`&emsp;create an empty directory
>> 3. `rm -r`&emsp;delete a directory and all of its children
>> 4. `touch`&emsp;create an empty file
>> 5. `rm`&emsp;delete a file
>> 6. `mv`&emsp;rename a file
>> 7. `ls -a`&emsp;clist all contents in directory, including hidden files
>> 8. `cp`&emsp;copy a file or directory from one directory to another
>> 9. `cd`&emsp;change directory
>> 10. `alias`&emsp;create a command shortcut
>> 11. `grep`&emsp;find all files that contain specified pattern or expression

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> * `ls`&emsp;list all contents, not including hidden items
>> * `ls -a`&emsp;list all contents, including hidden files and directories
>> * `ls -l`&emsp;list all contents in a directory in long format
>> * `ls -lh`&emsp;list all contents in directory in long format with readable file size
>> * `ls -lah`&emsp;list all contents in directory, including hidden files and directories, in long format with readable file size
>> * `ls -t`&emsp;order files and directories by the time they were last modified
>> * `ls -Glp`&emsp;list all contents in directory in long format, excluding display group and directories with a slash

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> 1. `ls -r`&emsp;list contents in reverse order
>> 2. `ls -R`&emsp;list contents as recursive directory tree
>> 3. `ls -s`&emsp;list contents with file size
>> 4. `ls -S`&emsp;list contents sorted by file size
>> 5. `ls -X`&emsp;list contents sorted by extension name

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> `xargs` reads data from standard input (stdin) and executes the command (supplied to it as an argument) one or times based on the input read. Any blanks and spaces in input are treated as delimiters, while blank lines are ignored.


