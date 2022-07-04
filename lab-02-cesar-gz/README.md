[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6867560&assignment_repo_type=AssignmentRepo)
# CPSC 223P Lab - 02 (Strings)

In this lab you will write another simple Python program; but this time it will do a little more than print "Hello, world!".  This exercise is intended to get you started using Python variables and working with strings.  In the process you will likely need to use some basic Python language constructs such as loops, module imports and built-in functions.

# Requirements

Your software will read a sentence from the command line, identify the longest and shortest word, and display those words along with their character count. Your output must match the expected output exactly to be given full credit. Specifically, here are the requirements.
1. The software _shall_ use a single Python file named _str_inspect.py_.
2. The software _shall_ read a sentence from the command line (e.g. python str_inspect.py "Please inspect this sentence thoroughly for the longest and shortest word.")
3. The software _shall_ output four lines of text matching this format:  
  >Shortest word: for    
  It is 3 characters    
  Longest word: thoroughly    
  It is 10 characters
  
Notice that there are several words that are 3 characters in length and are "tied" for the shortest word.  Use the first one (in this case, "for") and ignore the others.  The same applies to the longest word if there are more than one with the same character count.  Also, if the shortest word is a single character ("a", or "I"), make sure the word "character" is not plural! For example:
  >Shortest word: a    
  It is 1 character

# Specification

First, download the project to your local workstation.  I recommend using a source code repository interface such as GitHub Desktop. Start with the template file called str_inspect.py. Modify the header to include your own information, and update the code to meet the requirements. (Hint: you will need to "import sys" and use sys.argv to access the command line). When you are satisfied with your changes, commit them to the repository.

After your code is committed to your GitHub repository, go to your account on GradeScope and find the assignment called Lab-02 - Strings. Under "Submission Method" select GitHub. You will need to point to the correct repository (called something like joates-223p-spring-2021/lab-02-_your user name_).  You may be asked to link your GitHub account with Gradescope at this time.  Next select the Main branch and press Upload. Gradescope will import your project files from GitHub and automatically grade them.  If you like what you see, you are done.  If not, you can make changes and use the Resumbit button on the bottom right of the Gradescope page to try again.
