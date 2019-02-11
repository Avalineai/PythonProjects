randomstring = "Camus"
print(randomstring[0])
print(randomstring[1])
print(randomstring[2])
print(randomstring[3])
print(randomstring[4])


questions = "Where now?", "Who now?", "When now?"
edited = "," .join(questions)
print(edited)


correctthis = "aldous Huxley was born in 1894." .capitalize()
print(correctthis)


fixthis = "A screaming comes across the sky."
fixthis = fixthis.replace("s", "$")
print(fixthis)


first_index = "Hemingway" .index("H")
print(first_index)


threestring = "three" + " "
result = threestring * 3
print(result)

print("three " + "three " + "three ")
print("three " * 3)


firstentry = input("What did you write yesterday?")
secondentry = input("Where did you go yesterday?")

newstring = "Yesterday I wrote a {}. I sent it to {}." .format(firstentry, secondentry)

print(newstrong)
