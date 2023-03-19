class Persona:
    def __init__(self,pNombre,pEdad,pDni):
        self._nombre=pNombre
        self._edad=pEdad
        self._dni=pDni
        
        
    def mostrar(self):
        print(f"Mi nombre es {self._nombre} tengo {self._edad} y mi dni es {self._dni}")
    
    
    @property
    def nombre(self):
        print(f"Mi nombre es {self._nombre}")
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        if nuevoNombre!="" and  type(nuevoNombre)==str:
            self._nombre=nuevoNombre
        else:
            print("Ingrese su nombre Correctamente")
        
        
    @property
    def edad(self):
        print(f"Mi edad es {self._edad}")
        
    @edad.setter
    def edad(self,nuevaEdad):
        if type(nuevaEdad)==int and nuevaEdad>0:
            self._edad=nuevaEdad
        else:
            print("Ingrese su edad Correctamente y sin decimales")
    @property
    def dni(self):
        print(f"Mi Dni es {self._dni}")
    
    @dni.setter
    def dni(self,nuevoDni):
        if type(nuevoDni)!=str and type(nuevoDni)!=float and nuevoDni>0:
            self._dni=nuevoDni
        else:
            print("ingrese su dni Correctamente")
        
    def __str__(self):
       return f"Soy {self._nombre} tengo {self._edad} y mi dni es {self._dni}"
        
    def esMayor(self):
        if self.edad >=18:
            return True
        else:
            return False       
        


class Cuenta(Persona):
    _cantidad=0
    def __init__(self, pNombre, pEdad, pDni,pTitular):
        super().__init__(pNombre, pEdad, pDni)
        self._titular=pTitular
        
    @property
    def titular(self):
        print(f"El titular de la cuenta es {self._titular}")
    @titular.setter
    def titular(self,nuevotitular):
        self._titular=nuevotitular
        
    @property
    def cantidad(self):
        print(f"Esta cuenta posee ${self._cantidad}")
    # @cantidad.setter
    # def cantidad(self,nuevaCantidad):
    #     self._cantidad=nuevaCantidad
    
    def ingresar(self,cantidadIngresada):
        if cantidadIngresada<0:
            print("Debe ingresar un monto")
        else:
            self._cantidad+=cantidadIngresada
            print(f"Estado de Cuenta:${self._cantidad}")
    
    def retirar(self,retiro):
        if retiro<0:
            retiro*-1
            self._cantidad-=retiro
            print(f"Estado de Cuenta:${self._cantidad}")
        else:
            self._cantidad-=retiro
            print(f"Estado de Cuenta:${self._cantidad}")
            
    def mostrar(self):
        print(f"Titular de Cuenta {self._titular}, Saldo de la cuenta:$ {self._cantidad}")
    
    
x=Cuenta("juan",42,2855485,"Juan M")
# print(x)
# x.edad=55
# x.nombre="Artur"
# x.dni=88888888
# print(x)
# x.dni=0
# x.nombre="Fulano"
# print(x)
# print(x.esMayor)
y=Persona("Nuria",39,3025485)

#x.cantidad=150000   #asi no se deberia modificar la cantidad
x.ingresar(20000)
x.retirar(30000)
x.cantidad
x.mostrar()
y.mostrar()