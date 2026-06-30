# Examples Of strings
my_str_1 = 'Hello World'
my_str_2 = "Hello"
# In python it doesnt matter wheteher you use double or single quotes.

# Multiline String
my_str_3 = """multiline
string"""

my_str_4 = ''' another
multiline
string'''

# How to check if a string has one or more characters (it should return a boolean)
my_str = 'hello world'
print('hello' in my_str) #output should be true
print('e' in my_str) #output should be true
print('s' in my_str) #output should be false

# How to check the length of a string?
my_str = 'hello world'
print(len(my_str)) #output should be 9

# How to find the position of a character
my_str = 'Hello world'
print(my_str[0]) #Output should be H
print(my_str[5]) #Output should be O