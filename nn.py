import numpy as np
import math

class NeuralNetwork:

    def __init__(self, layer_sizes):
        """
        Neural Network initialization.
        Given layer_sizes as an input, you have to design a Fully Connected Neural Network architecture here.
        :param layer_sizes: A list containing neuron numbers in each layers. For example [3, 10, 2] means that there are
        3 neurons in the input layer, 10 neurons in the hidden layer, and 2 neurons in the output layer.
        """
        # TODO (Implement FCNNs architecture here)
        self.biases = [np.random.randn(x, 1)
                      for x in layer_sizes[1:]]
        self.weights = [np.random.randn(y, x)
                       for x, y in zip(layer_sizes[: -1], layer_sizes[1:])]
        self.layer_sizes = layer_sizes
        # pass

    def activation(self, x):
        """
        The activation function of our neural network, e.g., Sigmoid, ReLU.
        :param x: Vector of a layer in our network.
        :return: Vector after applying activation function.
        """
        # TODO (Implement activation function here)
        return 1 / (1 + math.exp(-x))
        # pass

    def forward(self, x):
        """
        Receives input vector as a parameter and calculates the output vector based on weights and biases.
        :param x: Input vector which is a numpy array.
        :return: Output vector
        """
        # TODO (Implement forward function here)
        start = x.reshape(self.layer_sizes[0], 1)

        z1 = self.biases[0] + np.dot(self.weights[0], start)
        a1 = np.vectorize(np.tanh)(z1)

        z2 = self.biases[1] + np.dot(self.weights[1], a1)
        a2 = np.vectorize(self.activation)(z2)

        return a2
        # pass
