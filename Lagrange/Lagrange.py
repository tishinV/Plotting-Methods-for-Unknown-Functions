import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x) * np.sqrt(x) + 1    # Our "unknown" function
h = np.pi / 7
n = 5   #The number of points known to us.
x = (0.5 * h, 1.5 * h, 2.5 * h, 4.5 * h, 6.5 * h)   # Points at which we know the values of our function
coords_x = []   #The points of our function on the x-axis
coords_y = []   #The points of our function on the y-axis
F1 = [[], [], [], [], []]   #Points on the y-axis for each basis function
F2 = [[], [], [], [], []]   #Points on the x-axis for each basis function

for i in range(1, 640):
    coord_x = i/639*(2*np.pi)
    coord_y = 0
    coords_x.append(coord_x)
    for ii in range(n):
        s = 1
        for jj in range(n):
            if jj != ii:
                s *= (coord_x - x[jj])/(x[ii] - x[jj])
        F1[ii].append(s)
        F2[ii].append(coord_x)
        coord_y += s * f(x[ii])
    coords_y.append(coord_y)


fig1, ax1 = plt.subplots()
ax1.grid()
ax1.plot(coords_x, coords_y)
ax1.set_title('Lagrange polynomial graph')
ax1.scatter(x, list(map(f, x)))
ax1.set_ylim([-3, 3])
plt.show()

fig2, ax2 = plt.subplots()
ax2.grid()
ax2.plot(coords_x, list(map(f, coords_x)))
ax2.plot(coords_x, coords_y)
ax2.set_title('Comparison with "unknown" function')
ax2.set_ylim([-3, 3])
ax2.scatter(x, list(map(f,x)))
plt.show()

figure, axe = plt.subplots()
axe.grid()
axe.set_xlim([0, np.pi])
axe.set_ylim([-3, 3])
axe.set_title("Graphs of basis functions")
for i in range(n):
    axe.scatter(x, list(map(lambda y: 1 if x[i] == y else 0, x)))
    axe.plot(F2[i], F1[i])
plt.show()

"""

    Graphs of basis functions separately

for i in range(n):
    figure, axe = plt.subplots()
    axe.set_title(f'Basis function Ф(x) for i = {i + 1}')
    axe.grid()
    axe.set_xlim([0,np.pi])
    axe.set_ylim([-3,3])
    axe.scatter(x, list(map(lambda y: 1 if x[i] == y else 0, x)))
    axe.plot(F2[i],F1[i])
    plt.show()
"""

