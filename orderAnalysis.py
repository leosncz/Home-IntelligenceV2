# Author: @leosncz
import config
import requests
import re

class orderAnalysis:
	def analyse(self, input):
		if input.isspace():
			print("Rien a analyser")
			return
		listDelimiter = config.separator_words
		finalInput = input
		for delimiter in listDelimiter:
			finalInput = finalInput.replace(" " + delimiter + " ", "|")
		finalInput = finalInput.split("|")
		
		orders = config.orders
		lastOrder = ""
		
		for session in finalInput:
			containsOrder = "NO"
			for order in orders:
				if order in session:
					lastOrder = order
					print("Présence de " + order)
					contextExists = "NO"
					for contexte in orders[order]:
						if contexte in session:
							print(contexte + " OK! (url: " + orders[order][contexte] + ")")
							requests.get(orders[order][contexte])
							contextExists = "OK"
					if contextExists == "NO":
						print("Ce contexte n'existe pas, veuillez l'enregistrer.")
					containsOrder = "OK"
			if containsOrder == "NO":
				if lastOrder != "":
					print("Pas d'ordre dans ce contexte, le dernier ordre était > " + lastOrder)
					contextExists = "NO"
					for contexte in orders[lastOrder]:
						if contexte in session:
							print(contexte + " OK! (url: " + orders[lastOrder][contexte] + ")")
							requests.get(orders[lastOrder][contexte])
							contextExists = "OK"
					if contextExists == "NO":
						print("Ce contexte n'existe pas, veuillez l'enregistrer.")

		