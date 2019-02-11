fav_songs = {"Pink": "Blow Me One Last Kiss",
             "Beyonce": "Irreplaceable",
             "Taylor Swift": "Stay"
             }
print(fav_songs)


aboutme = {"height": "5ft3in",
           "fav_color": "turquoise",
           "fav_author": "Edgar Allen Poe",
           "fav_band": "Lifehouse"
           }

answer = input("Type height, fav_color or fav_author")
if answer in aboutme:
    result = aboutme[answer]
    print(result)
