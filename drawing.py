import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import time


def reshape(data):
    dim = int(np.sqrt(len(data)))
    data = np.reshape(data, (dim, dim))
    return data


def plot(data, test, predicted, figsize=(5, 6), size=None):
    data = np.atleast_2d(data)
    test = np.atleast_2d(test)
    predicted = np.atleast_2d(predicted)
    if size is None:
        data = [reshape(d) for d in data]
        test = [reshape(d) for d in test]
        predicted = [reshape(d) for d in predicted]
    else:
        data = [np.reshape(d, (size)) for d in data]
        test = [np.reshape(d, (size)) for d in test]
        predicted = [np.reshape(d, (size)) for d in predicted]

    fig, axarr = plt.subplots(len(data), 3, figsize=figsize)
    if len(data) == 1:
        axarr[0].set_title('Train data')
        axarr[1].set_title("Input data")
        axarr[2].set_title('Output data')
        axarr[0].imshow(data[0], cmap='gray_r')
        axarr[0].axis('off')
        axarr[1].imshow(test[0], cmap='gray_r')
        axarr[1].axis('off')
        axarr[2].imshow(predicted[0], cmap='gray_r')
        axarr[2].axis('off')
    else:
        for i in range(max(len(data), len(test), len(predicted))):
            if i == 0:
                axarr[i, 0].set_title('Train data')
                axarr[i, 1].set_title("Input data")
                axarr[i, 2].set_title('Output data')
            if len(data) > i:
                axarr[i, 0].imshow(data[i], cmap='gray_r')
                axarr[i, 0].axis('off')
                rect = plt.Rectangle((-.5, -.5), 5, 5, fill=False)
                axarr[i, 0].add_patch(rect)
            if len(test) > i:
                axarr[i, 1].imshow(test[i], cmap='gray_r')
                axarr[i, 1].axis('off')
                rect = plt.Rectangle((-.5, -.5), 5, 5, fill=False)
                axarr[i, 1].add_patch(rect)
            if len(predicted) > i:
                axarr[i, 2].imshow(predicted[i], cmap='gray_r')
                axarr[i, 2].axis('off')
                rect = plt.Rectangle((-.5, -.5), 5, 5, fill=False)
                axarr[i, 2].add_patch(rect)

    plt.tight_layout()
    timestr = time.strftime("%d_%m_%Y-%H_%M-%S")
    plt.savefig(f"results/result-{timestr}.png")
    plt.show()
