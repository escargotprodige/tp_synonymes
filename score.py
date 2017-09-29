import numpy as np
import math

def produit_scalaire(u, v):
	return np.sum(u*v)


def least_squares(u, v):
	pass


def city_block(u, v):
	return np.sum(abs(u - v))