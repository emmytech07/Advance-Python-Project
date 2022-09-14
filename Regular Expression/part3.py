import re
#*.*.*>  Plus (it matches one or more than one occurrence )
# match_result = re.finditer("ma+n", "mn")
# match_result = re.finditer("ma+n", "man")

# for match in match_result:
#     print(match)

#**** Occurence() it matches 0 or one occurences
# match_result = re.finditer("ma?n", "mn")
# match_result = re.finditer("ma?n", "maan")

# for match in match_result:
#     print(match)


#****Braces  setting range of occurrences, at most or least
match_result = re.finditer("a{2,4}", "abc dat")
match_result = re.finditer("a{2,4}", "abc daaaat")
match_result = re.finditer("[0-6]{2,4}", "abc 123 654 234 346 67 9345")

# match_result = re.finditer("ma?n", "maan")

for match in match_result:
    print(match)