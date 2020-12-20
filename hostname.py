"""
This script is to be executed in an IDE such as Spyder, PyCharm, etc. for Python 3
It manipulates a list of hostnames intoa a usable format for queries
ARGUMENTS:
  file: a text file of hostnames in each line
  
 OUTPUTS:
  host: each hostname will be in the format "[hostname]" OR
  
 USE CASES: Splunk query
"""

file = the_path_of_your_file

f = open(file, "r")
#read the file

for line in f:
#loop over each line in the file
  s = "".join([x.strip() for x in line])
  #join all lines into a string and remove new lines
  host = '"[' + s + ']" OR '
  #surround each host in a square bracket with the word 'OR' trailing it
  print(host)
