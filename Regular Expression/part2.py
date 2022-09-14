import re 
#.......Caret
# it check if the string start with  the first alphabet 
match_result = re.finditer("^a", "adf")
match_result = re.finditer("^a", "sdf")

for match in match_result:
    print(match)

#.......Dollar (check if any string end with it alphabet)
match_result = re.finditer("f$", "formulaf")

for match in match_result:
    print(match)

# @.......Start...use to get no of occurrence match
match_result = re.finditer("ma*n", "mn")
match_result = re.finditer("ma*n", "maaaaaaaaan")

for match in match_result:
    print(match)