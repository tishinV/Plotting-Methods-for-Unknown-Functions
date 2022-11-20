import numpy as np
import matplotlib.pyplot as plt
f = lambda x: np.sin(x) * np.sqrt(x) + 1
h = np.pi / 7
x = (0.5 * h, 1.5 * h, 2.5 * h, 4.5 * h, 6.5 * h)
n = 5
coords_x = []
coords_y = []
F1 = [[], [], [], [], []]
F2 = [[], [], [], [], []]
for i in range(1,640):
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
fig, ax = plt.subplots()
ax.grid()
ax.plot(coords_x, coords_y)
ax.set_title('График полинома Лагранжа')
ax.scatter(x, list(map(f,x)))
ax.set_ylim([-3, 3])
plt.show()

fig, ax = plt.subplots()
ax.grid()
# ax.plot(coords_x, coords_y)
ax.plot(coords_x, list(map(f, coords_x)))
ax.set_title('График точной функции')
ax.set_ylim([-3, 3])
ax.scatter(x, list(map(f,x)))
plt.show()

for i in range(n):
    figure, axe = plt.subplots()
    axe.set_title(f'Базисная функция Ф(x) для i = {i + 1}')
    axe.grid()
    axe.set_xlim([0,np.pi])
    axe.set_ylim([-3,3])
    axe.scatter(x, list(map(lambda y: 1 if x[i] == y else 0, x)))
    axe.plot(F2[i],F1[i])
    plt.show()

figure, axe = plt.subplots()
axe.grid()
axe.set_xlim([0, np.pi])
axe.set_ylim([-3, 3])
for i in range(n):
    axe.scatter(x, list(map(lambda y: 1 if x[i] == y else 0, x)))
    axe.plot(F2[i], F1[i])
plt.show()