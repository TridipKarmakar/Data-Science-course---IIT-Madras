lines = []
n = 0
while True: # repeat forever since we are breaking inside
    string_input = input()
    if string_input == "END" : # The terminal condition
        break
    else  :
        lines.insert(0,string_input)
while (n < len(lines)) :
    if ((n+1) % 2 == 0) :
        print(lines[n])
    n+=1
   
    