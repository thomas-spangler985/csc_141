list =[' Luke S.', ' Kappa L.', ' Elijah K.' ]

message = f"I'm Inviting all by best friends to a party! The guest list includes..."

print (message)

print(list[0])
print(list[1])
print(list[2])

message0 = f"Unfortuately, It seems Gabriel Could not make it do to not having a car, Hope everyone else can still come. "
message1 = f"The new updated list with more guest on it is as follows..."
message2 = f"Can't wait to see everyone!"
message3 = f".... OH NO! Im so sorry everyone for making so many changes, but it seems I only have space for two people to come over at the moment..."
message4 = f"Sorry again for all this confusion, hope we can meet up again all proper soon."
print(message0)
print(message1)


list.insert(0,' Cole G.')
list.insert(2,' Zack S.')
list.append(' Gage M.')

print(list)

print(message2)
print(message3)

nospace =list.pop(0)
print (f" Sorry {nospace.title()}, but I cant invite you over.")

nospace =list.pop(1)
print (f" Sorry {nospace.title()}, but I cant invite you over.")
nospace =list.pop(1)
print (f" Sorry {nospace.title()}, but I cant invite you over.")
nospace =list.pop(2)
print (f" Sorry {nospace.title()}, but I cant invite you over.")

print( f"Well {list[0]}, it seems you can still make it if you want...")
print( f"As to you{list[1]}, I still got space for you aswell, let me know soon if eveyone is ok with these plans, goodbye for now.")

del list[0]
del list[0]

print (list)