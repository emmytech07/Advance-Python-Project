import re 

#  | Alternation (Find either the value)
match_result = re.finditer("a|bd", "Adachtbd")

for match in match_result:
    print(match)

#  | Group (looking for any of letter but should end with outer value)
# match_result = re.finditer("(a|bd)xz", "Adaxzchtbdxz")

for match in match_result:
    print(match)

#  \ Backslash (to escape and becoming neutral)
match_result = re.finditer("\^xy", "^xy")

for match in match_result:
    print(match)