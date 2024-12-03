# =================================================================
# DEMO: Modify String in Text File using regex
# =================================================================
# Regex ist ein Mustererkennungsmodul (re). 
# Es kann verwendet werden, um zu überprüfen, ob ein bestimmtes Muster 
# in einem gegebenen Text vorhanden ist. Es hat Anwendungen in vielen 
# Bereichen und ist in der Programmierwelt überall zu sehen. 
# Das Regex-Modul verfügt über Funktionen, die uns bspw. helfen, Text in einer Datei zu modifizieren.
#
# -----------------------------------------------------------------
# Nov'2024 - dbe - initial version for KETE HS24
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# Import Libraries
# -----------------------------------------------------------------
import re       # import regex module

# -----------------------------------------------------------------
# Define Helper Functions/Subroutines
# -----------------------------------------------------------------
# FUNCTION modify
# A function to modify a particular text in a given file. 
# It takes file+path, a string that is supposed to be changed, and a new string as parameters. 
# First, we open the file. Then we read it using the read() function. 
# Then we split the old string from the text file using the split() function. 
# We join the new string with the remaining text and write the entire text back into it. 
# -----------------------------------------------------------------
def modify(filepath, from_, to_):

    file = open(filepath,"r+")
    text = file.read()
    pattern = from_
    splitted_text = re.split(pattern,text)
    modified_text = to_.join(splitted_text)
    with open(filepath, 'w') as file:
        file.write(modified_text)
        
# -----------------------------------------------------------------
# MAIN program
# -----------------------------------------------------------------
# read text file
file = open("myFile.txt","r+")
text = file.read()
print("Before modification:\n",text)
file.close()

# search and modify string
modify("myFile.txt","Robert","Charles")

# write (modified) text file
file = open("myFile.txt","r+")
text = file.read()
print("\n\nAfter modification:\n",text)
file.close()