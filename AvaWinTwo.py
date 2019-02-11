def ask():
    print("Let's have a chat!")
    prompt1 = input("How is the Weather? ")

    print(prompt1 + "?" + " How Interesting!")

    prompt2 = input("Do you like going to the store? Type \"Y\" for Yes, and \"N\" for No: ")
    prompt2 = prompt2.casefold()
    
    if prompt2 == "y":
        print("Good to know!")
    elif prompt2 == "n":
        print("You save money that way!")
    else:
        print("I'm not sure I understand...")

    prompt3 = input("How is the dating scene? good or bad? ")
    prompt3 = prompt3.casefold()

    if prompt3 == "good":
        print("That's Fantastic!")
    elif prompt3 == "bad":
        print("Oh no..sorry to hear...")
    else:
        print("Ah, I see...!")
    
ask()
