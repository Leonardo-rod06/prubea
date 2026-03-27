import hashlib
class manejoArchivos:
    # se manda el nombre de archivo en el constructor porque el objeto
    # siempre va a usar ese archivo
    def __init__(self, archivo):
        self.archivo=archivo
    # crea el archivo con la opción w del open
    # como no se hace nada le ponemos pass para que continue
    def creaArchivo(self):
        with open(self.archivo,"w") as f:
            pass
    # usamos la opción "a" de open para agregar datos al archivo
    def escribeDatos(self, linea):
        with open(self.archivo,"a") as f:
            f.write(linea)
    # usamos la opción "r" para leer el archivo
    # usamos un arreglo para guardar las líneas que contenga el archivo
    # agregamos al arreglo cada una de las líneas
    # devolvemos el arreglo como resultado del método
    def leerDatos(self):
        lineas=[]
        with open(self.archivo,"r") as f:
            for linea in f:
                lineas.append(linea.strip())
        return lineas

class usuarios:
    def __init__(self,nombre,apellidos,correo,matricula,contrasena,telefono):
        self.nombre=nombre
        self.apellidos=apellidos
        self.correo=correo
        self.matricula=matricula
        self.contrasena=contrasena
        self.telefono=telefono

    def cambiaDatos(self,nombre,apellidos,correo,matricula,contrasena,telefono):
        self.nombre=nombre
        self.apellidos=apellidos
        self.correo=correo
        self.contrasena=contrasena
        self.telefono=telefono

    def devuelveUsuario(self):
        password=self._encriptar_contrasena()
        return f"{self.nombre},{self.apellidos},{self.matricula},{self.correo},{self.telefono},{password}"

    def _encriptar_contrasena(self):
        return hashlib.sha256(self.contrasena.encode()).hexdigest()


usuario=usuarios("Juan Carlos","Olmos Luna","jcarlos.olmos@uvp.edu.mx","460","1234","2222222222")
archusua=manejoArchivos("usuarios.txt")
print(usuario.devuelveUsuario())
archusua.escribeDatos(usuario.devuelveUsuario())
