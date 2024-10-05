## Lab exercise 3
### Provide a list comprehension that implementation for a function called vowelsToUpper with the following signature:

# method name : vowelsToUpper

# input argument : String 

# return argument : String

# vowelsToUpper must return a version of its String argument with all its vowels changed to their uppercase forms. Nonvowel characters stay as is.

### Sample Calls

# vowelsToUpper "" == ""

# vowelsToUpper "Hello, world!" == "HEllO, wOrld!"

# vowelsToUpper "hello hi bye" == "hEllO hI byE"
x = input("Please input a text: ")

# Create a new string with vowels capitalized
y = ''.join([a.upper() if a.lower() in 'aeiou' else a for a in x])

print(f'"{x}" == "{y}"')  # Output: HEllO, wOrld!
