
from keras.models import Sequential
from keras.layers import Dense


class NeuralNetwork:
    model = None
    acc = 0

    def __init__(self, size):
        self.model = Sequential()
        self.model.add(Dense(4, input_dim=size**2, activation='sigmoid'))
        # model.add(Dense(4, activation='sigmoid'))

    def get_weights(self, printable=False):
        if self.model is not None:
            weights = self.model.layers[0].get_weights()[0]
            if printable:
                print(weights)
            return weights



if __name__ == '__main__':
    network = NeuralNetwork(3)
    print(network)

    weights[0][2] = .2


    print(weights)