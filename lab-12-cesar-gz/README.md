# Lab-12 - Multithreading
You've suffered enough this semester, so now it's time for something a little easier. This lab is intended to be a simple introduction to multithreading. The topic of multithreading has much more to it than we will get into in this class, but just doing this lab will give you a basic idea of what a thread is, and how the operating system handles multiple threads within a single application.

# Overview
Write a Python program to demonstrate multithreading.  Your code shall first create a file for writing called "synch.txt" (autograder will be looking for this file).  Then it will create two separate threads, Thread-A and Thread-B (call them whatever you want).  Both threads will open synch.txt and write to it. Thread-A will write the numbers 1 - 26 twenty times in nested for loops then exit. In other words, print 1 - 26 over and over again on separate lines for at least 20 times. Thread-B will write the letters A - Z twenty times in nested for loops then exit.  We will not learn process synchronization in this class, but if you feel like it, you may use a mutex lock to control synchronization between the two threads.  When the program is complete, the synch.txt file "should" look like this:
 

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26   
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26   
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26   
..... 20x   
   
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z   
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z   
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z   
... 20x   
   
However, you will notice that if you do not use a mutex lock, your file might look a little different.  That's ok.  You won't be graded on what your output looks like.  You will only be graded on your use of two threads to write to a file named synch.txt.
