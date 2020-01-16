import random
rn=random.randint(1,1000)
YG = int(input("What number am I thinking of?"))
if YG == rn:
  print("Correct")
else:
  if YG > rn:
    print("Too High")
  if YG < rn:
    print("Too Low")