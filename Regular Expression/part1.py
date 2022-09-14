import re 
# Grab alphabet that matches 
match_result = re.finditer("[abc]", "a")
match_result = re.finditer("[abc]", "ac")
match_result = re.finditer("[abc]", "hey there")
match_result = re.finditer("[a-e]", "abc da ca dog elephant")
# grab value
match_result = re.finditer("[0-2]", "22,33,4,5,66")
# Grab alphabet that does not belong 
match_result = re.finditer("[^a-e]", "abc da ca dog elephant")
# Used to grab all items 
match_result = re.finditer(".", "123")
match_result = re.finditer(".", "abc")

# Used to grab 2 set ot object sitting next to each othr
match_result = re.finditer("..", "abcd")

for match in match_result:
    print(match)