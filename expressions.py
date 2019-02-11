import re
line = "I am dutch"
matches = re.findall("dutch", line)
print(matches)

line2 = "Arizona 479, 501, 870. California 209,213, 650."
m = re.findall("\d", line2, re.IGNORECASE)
print(m)

match2 = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match2)
