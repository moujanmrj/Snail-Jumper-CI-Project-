import copy
import math
import random
from matplotlib.pyplot import step
import numpy as np
from player import Player

MUTATION_PROB = 0.1


def roulette_wheel(x, num) :
    fittness_rec = list(np.cumsum(list(map(lambda i: i.fitness, x))))
    result = []
    for i in range(num):
        rnd = np.random.random() * fittness_rec[-1]
        index = fittness_rec.index(next(i for i in fittness_rec if rnd <= i))
        result.append(x[index])
    return result



def sus(x, num) :
    fittness_rec = list(np.cumsum(list(map(lambda i: i.fitness, x))))
    result = []
    length = fittness_rec[-1] / num
    rnd = np.random.random() * length
    for i in range(num) :
        index = fittness_rec.index(next(j for j in fittness_rec if (rnd + (i * length)) <= j))
        result.append(x[index])
    return result



class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """
        # TODO (Implement top-k algorithm here)
        # players__= sorted(players, key=lambda i: i.fitness, reverse= True)
        # return players__[:num_players]

        # TODO (Additional: Implement roulette wheel here)
        next_population = roulette_wheel(players, num_players)

        # TODO (Additional: Implement SUS here)
        # return sus(players, num_players)
        
        # TODO (Additional: Learning curve)
        sum_of_vals = 0
        least_fit = players[0].fitness
        fittest = players[0].fitness
        for player in players:
            sum_of_vals += player.fitness  #sum of fitness
            if player.fitness < least_fit:
                least_fit = player.fitness  #the least fit
            if player.fitness > fittest:
                fittest = player.fitness  #fittest
        fitness_avg = sum_of_vals / len(players)  #average fitness
        file = open('learning_curve.txt', 'a')  #write to file
        file.writelines(str(fitness_avg) + " " + str(fittest) + " " + str(least_fit) + "\n")
        file.close()
        return next_population
        # return players[: num_players]

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """
        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
        
            new_players_q = self.q_tournament(prev_players, num_players, 5)
            new_players = []
            for player in range(len(new_players_q), step=2):
                # new_player = self.clone_player(player)
                # self.mutate(new_player)
                # new_players.append(new_player)
                parent_1 = new_players[player]
                parent_2 = new_players[player + 1]
                
                clone_child_1 = self.clone_player(parent_1)
                clone_child_2 = self.clone_player(parent_2)
                
                clone_child_1.nn.w1, clone_child_2.nn.w1 = self.crossover(parent_1.nn.w1, parent_2.nn.w1)
                clone_child_1.nn.w2, clone_child_2.nn.w2 = self.crossover(parent_1.nn.w2, parent_2.nn.w2)
                clone_child_1.nn.b1, clone_child_2.nn.b1 = self.crossover(parent_1.nn.b1, parent_2.nn.b1)
                clone_child_1.nn.b2, clone_child_2.nn.b2 = self.crossover(parent_1.nn.b2, parent_2.nn.b2)
                
                clone_child_1 = self.mutation(clone_child_1)
                clone_child_2 = self.mutation(clone_child_2)
                
                new_players.append(clone_child_1)
                new_players.append(clone_child_2)
            return new_players

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player

    def crossover(self , array1 , array2):
        crossover_place = math.floor(array1.shape[0]/2)
        random_number = np.random.uniform(0, 1, 1)
        if(random_number > 0.8):      #crossover_probability = 0.8
            return array1 , array2
        else:
            return np.concatenate((array1[:crossover_place], array2[crossover_place:]), axis=0), np.concatenate((array2[:crossover_place], array1[crossover_place:]), axis=0)


    def mutate(self, child):
        global MUTATION_PROB
        for i, x in enumerate(child.nn.biases):
            if(random.random() < MUTATION_PROB):
                child.nn.biases[i] += np.random.randn(*np.shape(x))

        for i, x in enumerate(child.nn.weights):
            if(random.random() < MUTATION_PROB):
                child.nn.weights[i] += np.random.randn(*np.shape(x))

    def q_tournament(self, players, num_players, q):
        result = []
        for i in range(num_players):
            batch = []
            for j in range(q):
                batch.append(np.random.choice(players))

            tmp = sorted(players, key=lambda x: x.fitness, reverse=True)
            result.append(self.clone_player(tmp[0]))

        return result