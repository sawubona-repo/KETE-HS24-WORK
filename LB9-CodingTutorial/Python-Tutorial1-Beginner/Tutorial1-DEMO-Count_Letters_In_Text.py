# =================================================================
# DEMO: Lists and Letter Counting
# =================================================================
# Count letters in a given text e.g. for a frequency analysis
# -----------------------------------------------------------------
# Nov'2023 - dbe - initial version for KETE HS23
# Nov'2024 - dbe - minor corrections for KETE HS24
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# Import Libraries
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# Define Helper Functions/Subroutines
# -----------------------------------------------------------------
def count_letter(letter,list):
  charNo = ord(letter)
  if (charNo > 0):
    list[charNo] += 1

def init_letter_counter(no):
  cList = []
  for _n in range(no):
    cList.append(0)
  return cList

# -----------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------

# Die counter list variable initialisieren
letter_counter = init_letter_counter(255)
print("Initial counter list: \n", letter_counter)

# -----------------------------------------------------------------
# INPUT Data

text  = "This is a simple Text with no other meaning than be a Text for testing the Letter Counter Program"
# text = input("Ihr gewünschter Text? ")

# myFile = open("sampletext.txt", "r")
# text = myFile.read()
# myFile.close()

# -------------------------------------------------------
# PROCESS Data: Count frequency of characters in a given text

count = 0
while (count < len(text)):
  count_letter(text[count],letter_counter)
  count +=1


# -----------------------------------------------------------------
# OUPUT Data/Results

print ("\n\nDer zu analysierende Text:\n" + text)
print ("\nund die Häufigkeiten der darin enthaltenen Buchstaben: ")

for i in range(32,255):
  if letter_counter[i]>0:
    print(chr(i),letter_counter[i])  

# print("letter counter: ", letter_counter)
print("\nTotal "+ str(sum(letter_counter)) +" Buchstaben")  


