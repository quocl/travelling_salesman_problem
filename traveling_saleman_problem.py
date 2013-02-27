import sys
import random

class Population:
	def __init__(self, graph, size):
		self. graph = graph
		self.population = []
		self.size = size

	def generate(self, length):
		"""
		Generate the first random population.
		length: length of a chromosome.
		"""
		sample_chromosome = [i for i in xrange(length)]
		for i in xrange(self.size):
			random.shuffle(sample_chromosome)
			new_c = Chromosome(self.graph, sample_chromosome)
			self.population.append(new_c)

class Chromosome:
	def __init__(self, graph, chromo ):
		self.graph = graph
		self.chromosome = chromo		
		self.cost = self.__compute_cost()

	def __str__(self):
		return str(self.chromosome)

	def __compute_cost(self):
		cost = 0
		for i in xrange(len(self.chromosome) - 1):
			src = self.chromosome[i]
			dest = self.chromosome[i+1]
			cost += self.graph[src][dest]
		return cost	

class GeneticAlgorithm:
	@staticmethod		
	def permutation(graph, chromosome):
		"return population by doing permutation"
		chromo = chromosome.chromosome
		random.shuffle(chromo)
		return Chromosome(graph, chromo)
	
	@staticmethod
	def crossover(graph,chromosome1, chromosome2):
		"return population by doing crossover"
		l = len(chromosome1.chromosome)
		child = [-1 for i in xrange(l)]
		start = int(random.random()*l)		
		end = int(random.random()*l)
		if start > end:
			start, end = end, start
		for i in xrange(start, end):
			child[i] = chromosome1.chromosome[i]
		for i in xrange(l):
			if chromosome2.chromosome[i] not in child:
				for j in xrange(l):
					if child[j] == -1:
						child[j] = chromosome2.chromosome[i]
						break
		return Chromosome(graph, child)

	@staticmethod
	def evolution(p):
		"make the input population evolve"
		l = len(p.population)
		for i in xrange(l):
			choice = random.randint(0, 1) 
			if choice == 0:
				chromosome = p.population[i]
				p.population.append(GeneticAlgorithm.permutation(p.graph, chromosome))
			else:
				first = random.randint(0, l-1)
				if first == l - 1:
					second = first - 1
				else:
					second = first + 1
				p1 = p.population[first]
				p2 = p.population[second]
				p.population.append(GeneticAlgorithm.crossover(p.graph, p1, p2)) 
		l = sorted(p.population, key=lambda x: x.cost)
		p.population = l[0:len(l)/2]
		return p	

def __main__():
	if len(sys.argv) != 3:
		print "Wrong usage. Exit..."
		sys.exit()
	T = int(raw_input())
	no_link = int(raw_input())
	graph = []
	for i in xrange(T):
		row = map(int, raw_input().strip().split())
		graph.append(row)

	p = Population(graph, int(sys.argv[1]))
	p.generate(len(graph))

	for i in xrange(int(sys.argv[2])):
		p = GeneticAlgorithm.evolution(p)
	print "Solution:", p.population[0], "with distance = ", p.population[0].cost

__main__()

