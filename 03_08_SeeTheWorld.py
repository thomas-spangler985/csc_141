locations =[' Dublin Ireland' , 'Sydney australia' , 'Kabukicho Tokyo' , 'Yosemite National Park' , 'San Francisco Ca.'  ]
print("\nHeres my base list, in random order:")
print(locations)

print("\nNow heres the list but sorted:")
print(sorted(locations))

print("\nHeres my base list again, to show its unchanged:")
print(locations)


print("\nNow heres the list but reveresed:")
locations.reverse()
print(locations)

locations.reverse()
print("\nNow its back to how it started:")
print(locations)

locations.sort()
print("\nNow its sorted for good this time:")
print(locations)

locations.sort(reverse=True)
print("\nNever mind now its fliped in reverse :P oh well")
print(locations)