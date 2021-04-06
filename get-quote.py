import random

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  length = len(quotes)
  rnd = random.randint(0, length-1)
  print(quotes[rnd])
  rnd = random.randint(0, length-1)
  print(quotes[rnd])

if __name__== "__main__":
  primary()
