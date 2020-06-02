class Pet:
	stt = sothutu = 1
	age = 1
	def __init__(self, kind, name, sound):
		self.kind = kind
		self.name = name
		self.sound = sound
		self.stt = Pet.sothutu
		Pet.sothutu += 1
	def eating(self):
		print('He is eating', self.name)
	@classmethod
	def update_age(cls, new_age):
		cls.age = new_age


john = Pet('Dog', 'John', 'GauGau')
mary = Pet('Cat', 'Mary', 'Meoaw')

print(john.age)

john.update_age(5)

print(john.age)


