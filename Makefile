PY=python
POP=10
GEN=100
SRC=traveling_saleman_problem.py
INPUT=cities.txt

# By default, the population size is 10 and the number of generations is 100.
# To change the population size and number of generations to, let say 100 and 100, respectively, run:
# make  run POP=100  GEN=100
run:
	$(PY)	$(SRC)	$(POP)	$(GEN)	<	$(INPUT)

