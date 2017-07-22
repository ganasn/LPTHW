#Exercise 31 - Making Decisions

print "You enter a dark room with 2 doors. Do you go through door #1 or door #2?"
door = int(raw_input(">"))

if door == 1:
    print "Well, there's more danger. Enter 1 for option-1 and 2 for option-2."
    option = int( raw_input(">"))
    if option == 1:
        print "you're mauled."
    elif option == 2:
        print "you're stabbed."
    else:
        print "you're dead anyways."
elif door == 2:
    option = int(raw_input("How much insanity do you need? 1 or 2>"))
    if option == 1:
        print "level 1 insanity"
    elif option ==  2:
        print "level 2 insanity"
    else:
        print "unparallelled insanity"
else:
    print "you stumble around to fall on your sword and die."