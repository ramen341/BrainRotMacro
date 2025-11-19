import fuzzywuzzy
from fuzzywuzzy import fuzz

s1= "Tralaledon"
s2= "Tralaleo Tralala"

print(fuzz.partial_ratio(s1, s2))
