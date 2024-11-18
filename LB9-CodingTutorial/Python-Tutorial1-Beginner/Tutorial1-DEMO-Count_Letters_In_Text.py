# =================================================================
# Lists and Sorting
# =================================================================
# List of integer numbers and sorting with the classical 
# "bubble sort" algorithm 
#
# See: https://de.wikipedia.org/wiki/Bubblesort
# -----------------------------------------------------------------
# Nov'2023 - dbe - initial version for KETE HS23
# -----------------------------------------------------------------

# ------------------------------------------------------------------
import random


# =================================================================
# CASE 3: 

def count_letter(letter,list):
  #charNo = ord(letter.lower())-97
  charNo = ord(letter)
  #print(letter, charNo)
  if (charNo > 0):
    list[charNo] += 1


def init_letter_counter(no):
  cList = []
  for _n in range(no):
    cList.append(0)
  return cList

letter_counter = init_letter_counter(255)
# print("initial counter: ", letter_counter)

# text  = "This is a simple Text with not other Meaning"
# text = input("Ihr gewünschter Text? ")


myFile = open("sampletext.txt", "r")
text = myFile.read()
myFile.close()

print ("\n\nDer zu analysierende Text:\n" + text)

# -------------------------------------------------------
# Count frequency of characters in a text
count = 0
while (count < len(text)):
  count_letter(text[count],letter_counter)
  count +=1
# -------------------------------------------------------

print ("\nund dessen Buchstaben Häufigkeiten: ")
for i in range(255):
  print(chr(i+97),letter_counter[i])  
  
# print("letter counter: ", letter_counter)
print("\nTotal "+ str(sum(letter_counter)) +" Buchstaben")  


