nric = input('Enter an NRIC number: ')

# Type your code below

# part 1
# check the first letter is S T F G
# check if there are 7digits
# check if there is ONE letter at theback
# print result
# add up sum





nric = nric.lstrip(' ')
if nric[0] == "S" or "T" or "F" or "G" :
    if len(nric[1:8]) == 7 :
      if nric[1:8].isdigit() :
        if nric[-1].isalpha() :
          sum = int(nric[1])*2 + int(nric[2])*7 + int(nric[3])*6 + int(nric[4])*5 + int(nric[5])*4 + int(nric[6])*3 + int(nric[7])*2
          if nric[0] == "T" or nric[0] == "G" :
              sum1 = sum + 4
          else: 
              sum1 = sum
          result, remainder = divmod(sum1, 11)
          if nric[0] == "S" or nric[0] == "T":
              if remainder == 0:
                a = "J"
              elif remainder == 1:
                a = "Z"
              elif remainder == 2:
                a = "I"
              elif remainder == 3:
                a = "H"
              elif remainder == 4:
                a = "G"
              elif remainder == 5:
                a = "F"
              elif remainder == 6:
                a = "E"
              elif remainder == 7:
                a = "D"
              elif remainder == 8:
                a = "C"
              elif remainder == 9:
                a = "B"
              elif remainder == 10:
                a = "A"
              else: 
                print("NRIC is invalid.")

          else:
              if remainder == 0:
                a = "X"
              elif remainder == 1:
                a = "W"
              elif remainder == 2:
                a = "U"
              elif remainder == 3:
                a = "T"
              elif remainder == 4:
                a = "R"
              elif remainder == 5:
                a = "Q"
              elif remainder == 6:
                a = "P"
              elif remainder == 7:
                a = "N"
              elif remainder == 8:
                a = "M"
              elif remainder == 9:
                a = "L"
              elif remainder == 10:
                a = "K"
              else: 
                print("NRIC is invalid.")
          if  nric[8] == a :
              print ("NRIC is valid.")
          else:
              print ("NRIC is invalid.")
            
        else: 
          print ("NRIC is invalid.")
      else:
        print("NRIC is invalid.")
    else:
      print("NRIC is invalid.")
else :
  print("NRIC is invalid.")
