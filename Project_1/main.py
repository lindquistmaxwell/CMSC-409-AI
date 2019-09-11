import matplotlib.pyplot as plt
import sys
import re


class point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


# Gets data file
try:
    letter = sys.argv[1]
    if (letter.islower()):
        letter = letter.upper()
    f_name = './data/group' + letter + '.txt'
    f = open(f_name)
except:
    print('\n > add valid group letter please\n')
    quit()

# List for all points to be plotted
all_pts = []

# Points that will be used to create and plot line
p1 = point(0, 0, 'black')
p2 = point(0, 0, 'black')

# Lists for
weights = []
heights = []
colors = []

# Lists to classify where the points are relative to the line
menBelow = []
menAbove = []
womenBelow = []
womenAbove = []
oopsies = []

# Converts each line into a point object and adds to list of all point objects
for line in f:
    token = re.split(',', line)
    pt = point(float(token[1]), float(token[0]), '')
    if int(token[2]) == 0:
        pt.color = 'blue'
    else:
        pt.color = 'red'
    all_pts.append(pt)

# Sets the values of the points used to draw the line base on which file is used
if (letter == 'A'):  # Group A line => y = ((-1/30)x)+(42/4)
    p1.x = 165
    p1.y = 4.75
    p2.x = 120
    p2.y = 6.25
elif (letter == 'B'):  # Group B line => y = ((-1/20)x)+(131/10)
    p1.x = 160
    p1.y = 5.1
    p2.x = 134
    p2.y = 6.4
elif (letter == 'C'):  # Group C line => y = ((-3/100)x)+(209/20)
    p1.x = 165
    p1.y = 5.5
    p2.x = 135
    p2.y = 6.4

# Breaks each point into a list of x, y, and color for the plotting
for p in all_pts:
    weights.append(p.x)
    heights.append(p.y)
    colors.append(p.color)

# Plot the information
plt.title('Group ' + letter)
plt.xlabel('Weight')
plt.ylabel('Height')
plt.scatter(weights, heights, color=colors, s=1, alpha=1)
plt.plot([p2.x, p1.x], [p2.y, p1.y], color='black', lw=1)

# Calculates m and b to help determine if a point is above or below the line
changeX = p1.x-p2.x
changeY = p1.y-p2.y
m = changeY / changeX
b = p2.y - (m * p1.x) + changeY

# Goes through each point in the list and puts it in a new List based on where it falls relative to the line
for pt in all_pts:
    if pt.color == 'blue':
        if (pt.y < m * pt.x + b):
            menBelow.append(pt)
        elif(pt.y > m * pt.x + b):
            menAbove.append(pt)
        else:
            oopsies.append(pt)
    else:
        if (pt.y < m * pt.x + b):
            womenBelow.append(pt)
        elif(pt.y > m * pt.x + b):
            womenAbove.append(pt)
        else:
            oopsies.append(pt)

a = len(womenBelow)
b = len(womenAbove)
c = len(menBelow)
d = len(menAbove)

# Formulas from the nots: Lecture 7 slide 20
ACC = (a+d)/(a+b+c+d)
TP = a/(a+b)
FP = c/(c+d)
TN = d/(c+d)
FN = b/(a+b)
P_1 = a/(a+c)
P_2 = d/(b+d)

print('  men below line:', len(menBelow))
print('  men above line:', len(menAbove))
print('       total men:', len(menBelow) + len(menAbove))
print('women below line:', len(womenBelow))
print('women above line:', len(womenAbove))
print('     total women:', len(womenBelow) + len(womenAbove))
print('         oopsies:', len(oopsies))

#  true pos = woman below line
#  true neg = man above line
# false pos = men below line
# false neg = woman above line

print(' true pos = a = ', len(womenBelow))
print('false neg = b = ', len(womenAbove))
print('false pos = c = ', len(menBelow))
print(' true neg = d = ', len(menAbove))

print('ACC = ', ACC)
print(' TP = ', TP)
print(' FP = ', FP)
print(' TN = ', TN)
print(' FN = ', FN)
print('P_1 = ', P_1)
print('P_2 = ', P_2)

plt.show()
