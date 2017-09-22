# -*- coding: utf-8 -*-

import sys, re, argparse
import numpy as np


def main():
	# 1. traitement des arguments
	tf = sys.argv[1] or None
	algo = sys.argv[2] or None
	encodage = sys.argv[3] or None
	textes = sys.argv[4:] or None
	# TODO: remplacer par argparse

	texte = ""

	# 2. parser les textes
	print("Parsage en cours...")
	for chemin in textes:
		with open(chemin, "r", encoding=encodage) as f:
			texte += f.read()

	if texte[0] == "\ufeff":
		texte = texte[1:]

	p = re.compile("[\\' .,;:\n\-0123456789\[\]+*()`~«»!?/]+")
	corpus = p.split(texte)
	corpus = [i.lower() for i in corpus if len(i) > 0]

	vocabulaire = {}
	i = 0
	for mot in corpus:
		if mot not in vocabulaire:
			vocabulaire[mot] = i
			i += 1

	print("Entrainement en cours...")

	# 3. entrainement donnees
	matrice = np.zeros((i, i))


	# 4. demander mot utilisateur
	while True:
		rep = input("Entrez un mot pour avoir une liste de synonymes: ")

		if rep == "-1":
			break

		# 5. trouver liste des synonymes
		print(rep)

	return 0


if __name__ == '__main__':
	sys.exit(main())
