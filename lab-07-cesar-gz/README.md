# Lab-07 - Functions
In this lab you will implement your own version of built in string manipulation functions.  This exercise is intended to get you introduced to writing and calling functions, and generally, more familiarity with Python and thinking like a coder.

# Assignment Requirements and Specifications
The library module will contain three constants and eight function definitions.
It will include the following constants (provided for you):
>ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"  
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
DECIMAL_DIGITS = "0123456789"

It will include the following functions (you will define these):
>is_alpha( str ) -> bool  
is_digit( str) -> bool  
to_lower( str ) -> str  
to_upper( str ) -> str  
find_chr( str, str ) -> int  
find_str( str, str ) -> int  
replace_chr( str, str, str ) -> str  
replace_str( str, str, str ) -> str

The notation above gives the name of each function, the number and type of its argument(s), and
the type of its return value. The function names **shall** be spelled exactly as shown (for example, is_digit).
Each function **shall** contain a docstring (a string literal occurring as the first statement of the function)
that briefly describes what the function does.

1. Function _is_alpha_ has one parameter (a string). It returns True if all of the characters in
the string are upper case or lower case ASCII letters (it returns False otherwise).
2. Function _is_digit_ has one parameter (a string). It returns True if all of the characters in
the string are ASCII decimal digits (it returns False otherwise).
3. Function _to_lower_ has one parameter (a string). It returns the string which is a copy of the
parameter, but where all of the upper case ASCII letters have been converted to lower case
ASCII letters. Any digits or lower case letters will be left alone.
4. Function _to_upper_ has one parameter (a string). It returns the string which is a copy of the
parameter, but where all of the lower case ASCII letters have been converted to upper case
ASCII letters. Any digits or upper case letters will be left alone.
5. Function _find_chr_ has two parameters (both strings), where the second parameter must be
of length 1. It returns the lowest index where the second parameter is found within the first
parameter (it returns -1 if the second parameter is not of length 1 or is not found within the first
parameter).
6. Function _find_str_ has two parameters (both strings). It returns the lowest index where the
second parameter is found within the first parameter (it returns -1 if the second parameter is not
found within the first parameter).
7. Function _replace_chr_ has three parameters (all strings), where the second and third
parameters must be of length 1. It returns the string which is a copy of the first parameter, but
where all occurrences of the second parameter have been replaced by the third parameter (it
returns the empty string if the second or third parameter are not of length 1). If there are no occurrences 
of the second parameter in the first, it returns a copy of the first parameter.
8. Function _replace_str_ has three parameters (all strings). It returns the string which is a
copy of the first parameter, but where all occurrences of the second parameter have been
replaced by the third parameter. If there are no occurrences of the second parameter in the first,
it returns a copy of the first parameter. If the second parameter is the empty string, it returns a
copy of the first parameter.

9. The library module **shall not** use any of the string methods listed in Section 4.7.1 of the [Python
Standard Library](http://docs.python.org/3.3/library/stdtypes.html#string-methods)
10. The library module **shall not** contain any import statements.
11. The library module **shall not** perform any input or output operations. For example, it will not
call function input or function print.
