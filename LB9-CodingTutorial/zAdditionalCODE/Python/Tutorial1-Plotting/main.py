# Sample Plotting with mathplotlib
# Nov'2023 v1 dbe - inital version for KETE-HS23

import matplotlib.pyplot as plt
import numpy as np

slideNr = int(input("Slide number ?: "))

if (slideNr == 12):
  # Sample Plot - Slide#12
  plt.plot([1, 2, 3, 4])
  plt.ylabel('some numbers')
  plt.xlabel('A meaningless axis')
  plt.show()

elif (slideNr == 13):
  # Sample Plot - Slide#13
  plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2])
  plt.ylabel('some numbers')
  plt.xlabel('A meaningless axis')
  plt.show()

elif (slideNr == 14):
  # Sample Plot - Slide#14
  plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], 'ro')
  plt.ylabel('some numbers')
  plt.xlabel('A meaningless axis')
  plt.show()

elif (slideNr == 15):
  # Sample Plot - Slide#15
  plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], '-', linewidth=3.0)
  plt.ylabel('some numbers')
  plt.xlabel('A meaningless axis')
  plt.show()

elif (slideNr == 16):
  # Sample Plot - Slide#16
  plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 50, 2], '-', linewidth=3.0)
  plt.axis([0, 10, 0, 60])
  plt.xticks([0, 5, 10])
  plt.yticks([0, 25, 50, 60])
  plt.ylabel('some numbers')
  plt.xlabel('A meaningless axis')
  plt.show()

elif (slideNr == 19):
  # Sample Plot - Slide#19
  # evenly sampled values t at 200ms time intervals
  t = np.arange(0., 5., 0.2)
  plt.plot(t, t, 'rx', t, t**2, 'b*', t, t**3, 'go')
  plt.ylabel('measured values')
  plt.xlabel('time (s)')
  plt.show()

elif (slideNr == 21):
  # Sample Plot - Slide#21
  # evenly sampled values t at 200ms time intervals
  t = np.arange(0., 5., 0.2)
  # red dashes, blue squares and green triangles
  plt.plot(t, t, 'r-', t, t**2, 'b*', t, t**3, 'go')

  plt.ylabel('measured values')
  plt.xlabel('time (s)')
  plt.title('An example graph')
  plt.text(0.25,
           90,
           'This is a cool graph!',
           color='r',
           fontsize=15,
           fontstyle='italic')

  plt.show()

elif (slideNr == 23):
  # Sample Plot - Slide#23
  # evenly sampled values t at 200ms time intervals
  t = np.arange(0., 5., 0.2)
  # red dashes, blue squares and green triangles
  lines = plt.plot(t, t, 'r-', linewidth=2.0, label='Thing 1')
  lines = plt.plot(t, t**2, 'b*', linewidth=2.0, label='Thing 2')
  lines = plt.plot(t, t**3, 'go', linewidth=2.0, label='Thing 3')

  plt.title('An example graph - with legends')
  plt.ylabel('measured values')
  plt.xlabel('time (s)')
  plt.legend(loc='upper left')
  plt.show()

elif (slideNr == 24):
  # Sample Plot - Slide#24
  # evenly sampled values t at 200ms time intervals
  t = np.arange(0., 5., 0.2)
  # red dashes, blue squares and green triangles
  lines = plt.plot(t, t, 'r-', linewidth=2.0, label='Thing 1')
  lines = plt.plot(t, t**2, 'b*', linewidth=2.0, label='Thing 2')
  lines = plt.plot(t, t**3, 'go', linewidth=2.0, label='Thing 3')

  plt.title('An example graph - with legends')
  plt.ylabel('measured values')
  plt.xlabel('time (s)')
  plt.legend(loc='upper left')
  plt.savefig('test.png') 
  plt.show()

else:
  print("Slide number not found")
