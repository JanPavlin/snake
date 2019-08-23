import NeuralNetwork as NN


class Child:
    network = None
    id = 0
    batch = 0

    def __init__(self, batch, ids):
        self.batch = batch
        self.id = ids
        self.network = NN.NeuralNetwork(20)


class GeneticAlgorythm:
    children_num = 3
    children = []
    scores = []
    batch = 0
    id_count = 0
    map_size = (0, 0)
    max_depth = 2

    def __init__(self, children, rows, width):
        self.children_num = children
        self.map_size = (rows, width)
        for i in range(self.children_num):
            self.children.append(Child(self.batch, self.id_count))
            self.id_count += 1

    def learn(self):
        while self.batch < self.max_depth:
            temp_scores = []
            for child in self.children:
                temp_scores.append([child.id,
                    init.play(self.map_size[0], self.map_size[1], child, player='Bot')])

            self.batch += 1




import init
if __name__ == '__main__':
    print("hello")
    algorythm = GeneticAlgorythm(3, 20, 80)
    for child in algorythm.children:
        score = init.play(20, 800, child.network, player='Bot')

