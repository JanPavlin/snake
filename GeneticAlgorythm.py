import NeuralNetwork as NN


class Child:
    network = None
    id = 0
    batch = 0

    def __init__(self, batch, ids,rows):
        self.batch = batch
        self.id = ids
        self.network = NN.NeuralNetwork(rows)


    def edit_NN(self):
        pass


class GeneticAlgorythm:
    children_num = 3
    children = []
    scores = []
    batch = 0
    id_count = 0
    map_size = (0, 0)
    max_depth = 2
    rows = 0

    def __init__(self, children, rows, width):
        self.children_num = children
        self.map_size = (rows, width)
        self.rows = rows
        for i in range(self.children_num):
            self.children.append(Child(self.batch, self.id_count, rows))
            self.id_count += 1

    def get_parent(self, parent):
        for child in self.children:
            if child.id == parent:
                return child
        print("error_get_parrent")


    def learn(self):

        while self.batch < self.max_depth:

            temp_scores = []
            for child in self.children:
                temp_scores.append([child.id,
                    init.play(self.map_size[0], self.map_size[1], child, player='Bot')])

            self.batch += 1
            print("SCORES:", temp_scores)
            self.batch += 1
            potomci_list = []
            for score in temp_scores:
                for i in range(score[1]):
                    potomci_list.append(score[0])

            import random
            self.batch += 1
            print(potomci_list)
            for i in range(self.children_num):
                new_kiddo = random.choice(potomci_list)
                print(new_kiddo)
                # TODO: za vsakega otroka pridobi network njegovega prednika

                child = self.children.append(Child(self.batch, self.id_count, self.rows))
                parent = self.get_parent(new_kiddo)
                child.edit_NN(parent)
                # TODO: za vsako mrežo od otrok spremeni uteži.
                    # kako?






import init
if __name__ == '__main__':
    print("hello")
    algorythm = GeneticAlgorythm(3, 20, 80),
    child_scores = []
    for child in algorythm.children:
        score = init.play(20, 800, child.network, player='Bot')

        child_scores.append([child.id, score])

    print(child_scores)



