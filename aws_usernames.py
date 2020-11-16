"""
This script is to be executed in an IDE such as Spyder, PyCharm, etc. for Python 3
It manipulates a list of names to the format of AWS usernames.

ARGUMENTS:
  file: a text file of names in the format of Lastname, Firstname in each line
  
 OUTPUTS:
  name: a list of names in the format of *FirstnameLastname
  
 USE CASES: Splunk lookup tables
"""

file = the_path_of_your_file

f = open(file, "r")
#read the file

for line in f:
#loop over each line in the file
  s = "".join([x.strip() for x in line])
  #join all lines into a string and remove new lines
  name = '*' + s.split(',')[1] + s.split(',')[0]
  #use split(',') to split the string into an array at the comma (,)
  print(name)
