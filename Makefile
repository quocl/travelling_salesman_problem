PY=python
POP=10
GEN=100
TECH=0
SRC=traveling_saleman_problem.py
INPUT=cities.txt

# By default, the population size is 10, the number of generations is 100 and the evolution technique is permutation.
# To change the population size, number of generations and the evolution technique to, let say 100, 100 and crossover, respectively, run:
#	make  run POP=100  GEN=100	TECH=1

run:
	$(PY)	$(SRC)	$(POP)	$(GEN)	$(TECH) <	$(INPUT)

