import matplotlib.pyplot as plt

kwargs = {
    "linewidth": 36,
    "solid_capstyle": "butt",
}

# OS
plt.plot([0, 7], [0, 0], **kwargs)

# A
plt.plot([0, 3], [1, 1], **kwargs)
plt.plot([0, 3], [2, 2], color=plt.gca().lines[-1].get_color(), **kwargs)
plt.plot([6, 7], [2, 2], color=plt.gca().lines[-1].get_color(), **kwargs)
plt.plot([6, 7], [3, 3], color=plt.gca().lines[-1].get_color(), **kwargs)

# B
plt.plot([1, 5], [3, 3], **kwargs)

# C
plt.plot([2, 7], [4, 4], **kwargs)
plt.plot([2, 7], [5, 5], color=plt.gca().lines[-1].get_color(), **kwargs)

# D
plt.plot([4, 7], [1, 1], **kwargs)

plt.title("swapping example")
plt.xlabel("time")
plt.ylabel("memory address")
plt.xlim(0, 7)
plt.ylim(-0.5, 7)
plt.savefig("IBN_04_3.png")
