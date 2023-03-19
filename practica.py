class Casa:
    
	def __init__(self, precio):
		self._precio = precio

	@property
	def precio(self):
		return self._precio
	
	@precio.setter
	def precio(self, precio_nuevo):
		if precio_nuevo > 0 and isinstance(precio_nuevo, float):
			self._precio = precio_nuevo
		else:
			print("Por favor ingrese un precio valido.")

	@precio.deleter
	def precio(self):
		del self._precio
  
  
x=Casa(50000)
x.precio=20000.5

print(x.precio)