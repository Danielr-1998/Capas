from base import *


class CRUdHospital:
	def __init__(self):
		self.hospitals = []

	def addHospital(self, ide, name):
		new = Hospital(ide, name)
		self.hospitals.append(new)
		print("\n\nHospital Añadido.")

	def deleteHospital(self, ide):
		for x in self.hospitals:
			if x.id == ide:
				self.hospitals.remove(x)
		print("\nEliminado.")

	def editHospital(self, ide, name):
		for x in self.hospitals:
			if x.id == ide:
				x.editHospital(ide,name)
		print("\n\nEditado correctamente.")

	def searchHospital(self, name):
		ban=0
		for x in self.hospitals:
			if x.name == name:
				print(x.name, x.id)
				ban=1
		if ban == 0:
			print("No hubo resultados.")