import numpy as np
import random
import knn

def flip(s,i):
	new_s = np.array(s)
	new_s[i] = not new_s[i]
	return new_s


def BL(training_data, training_labels):
	n = len(training_data[0]) #number of features
	s = np.random.choice([True, False], n) #initial solution
	s_score = knn.getKNNClasiffierTrainingScore(training_data[:, s], training_labels)
	n_generated_sols = 0
	max_generated_sol = 5000
	
	while (True):
		idx = random.sample(range(0,n), n)
		found_better_sol = False

		for i in idx:
			s_i = flip(s, i)
			s_i_score = knn.getKNNClasiffierTrainingScore(training_data[:, s_i], training_labels)
			n_generated_sols += 1

			if(s_i_score > s_score):
				found_better_sol = True
				s = s_i
				s_score = s_i_score

			if n_generated_sols == max_generated_sol:
				return s, s_score

			if found_better_sol:
				break

		if not found_better_sol:
			return s, s_score
