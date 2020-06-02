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
	def fromString(cls, string):
		lst = string.split('-')
		kind, name, sound = lst
		return cls(kind, name, sound)


string = 'Dog-Lucky-GauGau'
Lucky = Pet.fromString(string)

print(Lucky.kind)
print(Lucky.name)
print(Lucky.sound)