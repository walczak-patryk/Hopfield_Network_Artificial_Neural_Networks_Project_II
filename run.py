import numpy as np

from common.common_functions import disturb_data, array_to_vector, data_to_array, read_data_as_arrays, read_data_as_vectors
from hopfield import HopfieldNetwork
from drawing import plot
from ui.board import *

if __name__ == "__main__":
    seed = 1
    np.random.seed(seed)
    data = read_data_as_vectors('./data/small-7x7.csv')
    # data = read_data_as_vectors('./data/large-25x25.csv')

    # train_data = data[:-1]
    # test_data = data[-1]
    train_data = data[:]
    test_data = []

    for pattern in train_data:
        test_data.append(disturb_data(pattern,5))

    train_data = np.asarray(train_data)
    test_data = np.asarray(test_data)

    nn = HopfieldNetwork(49)
    # nn.train_oja(train_data,175, 0.0001)
    nn.train(train_data)
    res = []
    for pattern in test_data:
        res.append(nn.predict(pattern, 10, use_async=True, async_iter=10))
    plot(data, test_data, res)
    # board = Board(100, 7)
    # board.overwrite_board(data_to_array(res[0], (7, 7)))
    # board.run() # UNCOMMENT TO SHOW INTERACTIVE BOARD WITH THE FIRST RESULT
