import matplotlib.pyplot as plt


centers = ['631, 433', '635, 436', '643, 442', '648, 448', '652, 456', '658, 466', '667, 471', '673, 481', '683, 491', '691, 493', '703, 505', '717, 506', '730, 507', '742, 508', '753, 511', '776, 517', '797, 514', '816, 514', '847, 519', '877, 516', '892, 514', '948, 514']
dims = ['124 x 270', '129 x 281', '135 x 290', '136 x 298', '139 x 318', '150 x 327', '156 x 346', '158 x 365', '173 x 372', '177 x 381', '189 x 403', '198 x 414', '206 x 399', '220 x 420', '232 x 416', '232 x 403', '266 x 409', '280 x 409', '290 x 399', '307 x 405', '335 x 411', '367 x 411']
rxs = [6.2, 8.2, 11.2, 11.2, 12.2, 17.2, 20.2, 21.2, 28.2, 30.2, 36.2, 40.2, 44.2, 51.2, 57.2, 57.2, 74.2, 81.2, 86.2, 94.2, 108.2, 124.2]
rys = [13.5, 18.5, 22.5, 26.5, 36.5, 40.5, 49.5, 58.5, 61.5, 65.5, 76.5, 81.5, 73.5, 83.5, 81.5, 74.5, 77.5, 77.5, 72.5, 75.5, 78.5, 78.5]

centersX = []
centersY = []
width = []
height = []
print("centers\t\tdims")
for i in range(len(centers)):
    print(f"{centers[i].split(',')[0]}\t\t\t{dims[i]}")
    centersX.append(int(centers[i].split(',')[0]))
    centersY.append(int(centers[i].split(',')[1]))
    width.append(int(dims[i].split(" x ")[0]))
    height.append(int(dims[i].split(" x ")[1]))

x = [i for i in range(len(centersX))]
plt.plot(x, centersX, label="center x")
plt.plot(x, centersY, label="center y")
plt.plot(x, width, label="width")
plt.plot(x, height, label="height")
plt.plot(x, rxs, label="rx")
plt.plot(x, rys, label="ry")
plt.legend()
plt.show()
