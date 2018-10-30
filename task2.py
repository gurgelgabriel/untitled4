win_counter = 0 # the variable win_counter starts at 0
for x in range(6): # you ask 6 times
    result = input("results?") # you ask for the results
    if result == "w":
        win_counter = win_counter + 1 # if result = "w" increase win_counter by 1, if not do nothing

if win_counter == 6 or win_counter == 5: # if the variable win counter has "w" appearing 5 or 6 times print "group 1"
    print("group 1")
if win_counter== 3 or win_counter == 4: # if the variable win counter has "w" appearing 3 or 4 times print "group 2"
    print("group 2")
if win_counter == 2 or win_counter == 1: # if the variable win counter has "w" appearing 1 or 2 times print "group 3"
    print("group 3")
if win_counter == 0: # if the variable win counter has "w" appearing 5 or 6 times print "eliminated"
    print("eliminated")
