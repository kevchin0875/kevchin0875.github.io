themessage=input("Put in a selection of text")
# l = ["the", "turtle"]
str1= themessage
from gf import load_words
for z in load_words():
  w=(str1.find(z))
  y=True
  if w ==-1:    
    continue

  else:
    y=False 
    # print('this is a dirty word')
    import random
    WholesomeWords = ["purple","french fry","rainbow"]
    themessage = themessage.replace(z, random.choice(WholesomeWords))
    
    
print (themessage)
