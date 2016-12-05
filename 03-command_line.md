# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > grep: search for a string in a file  
cd -: toggles between two most recent directories  
ps: displays information of what processes are running on the system  
top: displayes top processes running sorted by cpu usage  
kill, combined with ps -ef | grep: find process id and then kill the process  
chmod: changes the permission of a directory  
whatis: description of the unix command  
tail: prints last 10 lines of a file  
less: loads less of a log file for efficiency  
wget: download software etc from the internet  




---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: lists files in the current directory  
ls -a: list all files in the current directory, including hidden files  
ls -l: lists files in long form in the current directory  
ls -lh: lists files in long form with readable file sizes  
ls -lah: lists all files in long form with readable file sizes, including hidden files  
ls -t: lists files in the current directory, sort by time and date  
ls -Glp: lists files in long form in the current directory with syntax highlighting  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -c: displays files by timestamp  
ls -d: displays only directories  
ls -R: displays subdirectories as well  
ls -1: displays each entry on a new line
ls -t: displays newest file first

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Xargs turns the output of a command into the input for a second command, or where you would use a pipe to have multiple commands.  
`find . | xargs cksum | sort`  
This creates a list of sorted check sums of the working directory.


 

