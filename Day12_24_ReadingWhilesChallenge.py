# Joy of Coding
# via Prof. Emily Hill
# Beginning Python Challenge

# Day 12
# While Loops (2 hours)
#################################################
def numList(i):
# Given the following input entered by the user, what will be output?
# Henry Higgins
# Splendid. And you?
# Pygmalion
# Sure. Can we watch My Fair Lady as well?
# Watch Monty Python skits
# I especially like The Ministry of Silly Walks and Blackmail skits
# Wonderful, but I may have to quit soon. It takes too much of my time.
# Goodbye
  numbers=[]
  while i != 0:
    i = float(input("enter a number, or '0' when done: "))
    numbers.append(i)
    # numbers = numbers.extend(a)
    # numbers = numbers.insert(0,a)
    # numbers = numbers.sort()
    print()
    print()
    print("Sort: ", numbers[:-1])
    print("Sum: ", numbers[:-1])
    print("Average: ", numbers[:-1])
    # print(i)
    # print(numbers[:-1])
  # return(i)
  return(numbers)
# return(numList)

#################################################


def main():
  # print("Day 12 While Loops")
  print("Day12_24_ReadingWhilesChallenge")
  print()

# why this one print zero?
  # print(fourLoopz(4)) 
  # print()

  # print(csciOneFifty("csciOneFifty"))  
  # print(csciOneFifty("CSCI 150"))

  # print()
  # numList("9")
  numList(9)
  # numList("0")
  # numList(0)
  # numList()
  # print(numList("0"))  
  print()
main()  # end of Curled Main.. 