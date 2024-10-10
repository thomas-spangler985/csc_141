print("STARTOFPRINTSTARTOFPRINTLOOKBELOWFORTHECODEITSTARTSHERE")


list = ['Ska' , 'Punk Rock' , 'Vaporwave' , 'Funk' , 'Rap', 'Country']

print("\nHeres a list Of Music Genres I like :")
print(list)

list.insert(1,'Swing')
list.append('Hip-Hop')
list.pop(5)

worse = 'Country'
list.remove(worse)


print("\nHeres the list with a few changes made to it :")
print(list)

list.sort()

list.sort(reverse=True)

print("\nHeres the lFinal Version of the list sorted in a order:")
print(list)

