#print each item on the list

shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for series in shows:
    print(series)
    
#print all the numbers from 25 to 50

for i in range(25, 51):
    print(i)

#print each item in the list from the first challenge and their indexes

shows2 = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, show in enumerate(shows2):
    print(index)
    print(show)
