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

# ------------------------------------------------------------------
# Bubble sort function implementation
def bubble_sort (list):
  for i in range(len(list)-1):
      for j in range(len(list)-i-1):
          if list[j] > list[j+1]:
              temp = list[j]
              list[j] = list[j+1]
              list[j+1] = temp
  return list

# =================================================================
# CASE 1: 
# Define initial unsorted list
unsorted_list1 = [5, 2, 8, 3, 1, 99, 21, 7, 4, 6]

# Print the sorted list
print("CASE1: \nunsorted list: ", unsorted_list1)
print("sorted list:   ", bubble_sort(unsorted_list1))


# =================================================================
# CASE 2: 
# Ask for key parameters of random generated integer list
tot_number = int(input("\n\n\nWieviele Zahlen sollen erzeugt werden? "))
max_number = int(input("Wie gross darf eine Zufallszahl maximal sein? "))

# Generate a list of random generated integers
unsorted_list2 =[]
for _n in range(tot_number):
  unsorted_list2.append(random.randint(1, max_number))

# Print the unsorted list
print("\n\n\nCASE 2: \nunsorted list: ", unsorted_list2)

# Print the sorted list
print("sorted list:   ", bubble_sort(unsorted_list2))
