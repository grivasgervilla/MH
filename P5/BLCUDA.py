import numpy as np
from knnLooGPU import *

def flip(s,i):
	new_s = np.array(s)
	new_s[i] = not new_s[i]
	return new_s


def BLCUDA(training_data, training_labels, knnGPU):
	print("Ejecutando BLCUDA")
	n = len(training_data[0]) #number of features
	s = np.random.choice([True, False], n)
	s_score = knnGPU.scoreSolution(training_data[:, s], training_labels)
	n_generated_sols = 0
	max_generated_sol = 15000

	while (True):
		idx = np.random.choice(range(0,n), n, False)
		found_better_sol = False

		for i in idx:
			s[i] = not s[i]
			s_i_score = knnGPU.scoreSolution(training_data[:, s], training_labels)
			n_generated_sols += 1

			if(s_i_score > s_score):
				found_better_sol = True
				#s = s_i
				s_score = s_i_score
			else:
				s[i] = not s[i] #revert change

			if n_generated_sols == max_generated_sol:
				return s, s_score

			if found_better_sol:
				break

		if not found_better_sol:
			return s, s_score
