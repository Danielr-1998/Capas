class Hospital:
	def __init__(self, ide, name):
		self.id = ide
		self.name = name


	def editHospital(self, ide, name):
		self.name = name
		self.id = ide

class Doctor:
	def __init__(self, ide, hoid, name, speciality):
		self.doctor_id = id
		self.hospital_id = hoid
		self.doctor_name = name
		self.speciality = speciality

	def editDoctor(self, ide=None, hoid=None, name=None, speciality=None):
		self.doctor_id = ide
		self.hospital_id = hoid
		self.doctor_name = name
		self.speciality = speciality
