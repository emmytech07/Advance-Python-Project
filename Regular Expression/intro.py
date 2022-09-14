import re 

test_string = "canassava"

pattern = ".a."

result = re.match(pattern, test_string)
print(result)