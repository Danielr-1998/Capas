from base import *

class CRUDDoctor:
	def __init__(self):
		self.doctors = []

	def addDoctor(self, ide, hoid, name, spec):
		new = Doctor(ide, hoid, name, spec)
		self.doctors.append(new)
		print("\n\nAñadido correctamente.")

	def deleteDoctor(self, ide):
		for x in self.doctors:
			if x.id == ide:
				self.doctors.remove(x)
		print("Eliminado.")

	def editDoctor(seld, ide, hoid, name, spec):
		for x in self.doctors:
			if x.id == ide:
				x.editDoctor(ide, hoid, name, spec)

		print("Editado correctamente.")

	def serchDoctor(self, name):
		ban=0
		for x in self.doctors:
			if x.name == name:
				print(x.id, x.hospital_id, x.name, x.speciality)
				ban = 1
		if ban == 0:
			print("No hubo resultados.")
