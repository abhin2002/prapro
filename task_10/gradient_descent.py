import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

w = 0

lr = 0.1


for i in range(0,10):

    yi = w*x[i]

    w = w + lr * (y[i] - yi)

    print("X : ",x[i], "Y : ",yi, "w : ",w)


    plt.plot(x, [w * xi for xi in x], label=f"Iteration {i+1}")
    


plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()