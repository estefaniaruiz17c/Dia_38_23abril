# Estefanía Ruiz Cuartas
# Lenguaje de programación: Python
# Tema: Programación orientada a objetos. Herencia
# Fuentes de consulta: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#poo-atributos-clase-instancia  https://www.discoduroderoer.es/herencia-python-3-poo/  https://docs.hektorprofe.net/python/herencia-en-la-poo/ejercicios/

# Herencia: La herencia consiste en la creación de clases a partir de otras ya existentes. Tenemos lo que llamamos una clase padre (superclase) y clases hijas (clases derivadas), que heredan los métodos y atributos de su clase padre
print("Herencia\n")

# Ejercicio 1: Class Cubiertos
print("\n- Ejercicio 1: Class Cubiertos\n","\n")

# Creación de la clase padre Cubiertos, donde incluiremos algunas características de los cubiertos. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Cubiertos'.
class Cubiertos():
  '''
    Clase padre usada para representar algunas características de los cubiertos

    ...

    Atributos
    ------------------
    material : str (atributo de instancia)
        indica el material del cubierto
    color : str (atributo de instancia)
        indica el color de la fruta
  
    Métodos
    ------------------
    __init__(self, material, color)
        inicializa los artibutos del objeto
  '''
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: material,color
  def __init__(self, material, color):
    
    '''Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
    ...
    
    Parametros
    -------------------
    material : str (atributo de instancia)
        indica el material del cubierto
    color : str (atributo de instancia)
        indica el color de la fruta'''
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.material = material
    self.color = color

# Creación de la clase hija Cuchara, donde incluiremos características extra de este cubierto Para esto usamos la palabra clave 'class', la acompañamos con el nombre elegido 'Cuchara' y entre paréntesis(), la clase padre 'Cubiertos'.
class Cuchara(Cubiertos):
  '''
    Clase hija usada para representar características de una cuchara

    ...

    Atributos
    ------------------
    nombre : str (atributo de clase)
        indica el nombre  del cubierto de la clase
    material : str (atributo de instancia)
        indica el material del cubierto de la clase
    color : str (atributo de instancia)
        indica el color del cubierto de la clase
    uso : str (atributo de instancia)
        indica en qué se utiliza el cubierto de la clase
    tamano : str (atributo de instancia)
        indica el tamaño del cubierto de la clase

  
    Métodos
    ------------------
    __init__(self, material, color, uso, tamano)
        inicializa los artibutos del objeto
  '''
  nombre = "cuchara"
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: material,color,uso,tamano
  def __init__(self, material, color, uso, tamano):
    '''
     Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
     Para invocar un método de una clase padre desde una clase hija, podemos utilizar el nombre de la clase padre, seguida de un '.' y luego incluimos el método que queremos invocar 
    ...
    
    Parametros
    -------------------
    material : str (atributo de instancia)
        indica el material del cubierto de la clase
    color : str (atributo de instancia)
        indica el color del cubierto de la clase
    uso : str (atributo de instancia)
        indica en qué se utiliza el cubierto de la clase
    tamano : str (atributo de instancia)
        indica el tamaño del cubierto de la clase
  '''

    Cubiertos.__init__(self, material, color)
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.uso = uso
    self.tamano = tamano

# Creación de la clase hija Tenedor, donde incluiremos características extra de este cubierto Para esto usamos la palabra clave 'class', la acompañamos con el nombre elegido 'Tenedor' y entre paréntesis(), la clase padre 'Cubiertos'.
class Tenedor(Cubiertos):
  '''
    Clase hija usada para representar características de un tenedor

    ...

    Atributos
    ------------------
    nombre : str (atributo de clase)
        indica el nombre  del cubierto de la clase
    material : str (atributo de instancia)
        indica el material del cubierto de la clase
    color : str (atributo de instancia)
        indica el color del cubierto de la clase
    longitud : str (atributo de instancia)
        indica la longitud del cubierto de la clase
    forma : str (atributo de instancia)
        indica la forma del cubierto de la clase

  
    Métodos
    ------------------
    __init__(self, material, color, longitud, forma)
        inicializa los artibutos del objeto
  '''
  nombre = "tenedor"
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: material,color,longitud,forma
  def __init__(self, material, color, longitud, forma):
    '''
     Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
     Para invocar un método de una clase padre desde una clase hija, podemos utilizar el nombre de la clase padre, seguida de un '.' y luego incluimos el método que queremos invocar
    ...
    
    Parametros
    -------------------
    material : str (atributo de instancia)
        indica el material del cubierto de la clase
    color : str (atributo de instancia)
        indica el color del cubierto de la clase
    longitud : str (atributo de instancia)
        indica la longitud del cubierto de la clase
    forma : str (atributo de instancia)
        indica la forma del cubierto de la clase
  '''
    Cubiertos.__init__(self, material, color)
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.longitud = longitud
    self.forma = forma

# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: Características de una cuchara
cubierto1 = Cuchara("acero", "plateado", "tomar sopa","mediano")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia
print("Color del cubierto:\n",cubierto1.color)
print("\nNombre del cubierto:\n",cubierto1.nombre)
print("\nTamaño del cubierto:\n",cubierto1.tamano)
print("\nUso del cubierto:\n",cubierto1.uso)
print("\nMaterial del cubierto:\n",cubierto1.material)

# Ejercicio 2: Class Cubiertos
print("\n","\n- Ejercicio 2: Class Cubiertos\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: Características de un tenedor
cubierto2 = Tenedor("plástico", "azul", "16 cm","cóncava hacia arriba con 4 dientes")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia
print("Forma del cubierto:\n",cubierto2.forma)
print("\nMaterial del cubierto:\n",cubierto2.material)
print("\nLongitud del cubierto:\n",cubierto2.longitud)
print("\nColor del cubierto:\n",cubierto2.color)
print("\nNombre del cubierto:\n",cubierto2.nombre)

print("\n","----------"*7,"\n")

# Ejercicio 1: Class Frutas
print("\n- Ejercicio 1: Class Frutas\n")

# Creación de la clase padre Fruta, donde incluiremos algunas características de las frutas. Para esto usamos la palabra clave 'class' y la acompañamos con el nombre elegido 'Frutas'.
class Fruta:
  '''
    Clase padre usada para representar algunas características de las frutas

    ...

    Atributos
    ------------------
    sabor : str (atributo de instancia)
        indica el sabor de la fruta
    color : str (atributo de instancia)
        indica el color de la fruta
  
    Métodos
    ------------------
    __init__(self, sabor, color)
        inicializa los artibutos del objeto
  '''
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: sabor,color
  def __init__(self, sabor, color):
    '''Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
    ...
    
    Parametros
    -------------------
    sabor : str (atributo de instancia)
        indica el sabor de la fruta
    color : str (atributo de instancia)
        indica el color de la fruta
    '''
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.sabor = sabor
    self.color = color

# Creación de la clase hija Cereza, donde incluiremos características extra de esta fruta. Para esto usamos la palabra clave 'class', la acompañamos con el nombre elegido 'Cereza' y entre paréntesis(), la clase padre 'Frutas'.
class Cereza(Fruta):
  '''
    Clase hija usada para representar características adicionales de las cerezas

    ...

    Atributos
    ------------------
    nombre : str (atributo de clase)
        indica el nombre de la fruta de la clase
    sabor : str (atributo de instancia)
        indica el sabor de la fruta de la clase
    color : str (atributo de instancia)
        indica el color de la fruta de la clase
    tamano : str (atributo de instancia)
        indica el tamaño promedio de la fruta de la clase
    propiedades : str (atributo de instancia)
        indica las propiedades en vitaminas de la fruta de la clase

  
    Métodos
    ------------------
    __init__(self, sabor, color,tamano,propiedades)
        inicializa los artibutos del objeto
  '''
  nombre = "cereza"
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: sabor,color,tamano,propiedades
  def __init__(self, sabor,color,tamano,propiedades):
    '''
     Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
     Hacemos uso de la función super() que permite invocar un método de una clase padre desde una clase hija
    ...
    
    Parametros
    -------------------
    sabor : str (atributo de instancia)
        indica el sabor de la fruta
    color : str (atributo de instancia)
        indica el color de la fruta
    tamano : str (atributo de instancia)
        indica el tamaño promedio de la fruta de la clase
    propiedades : str (atributo de instancia)
        indica las propiedades en vitaminas de la fruta de la clase
  '''
    super().__init__(sabor,color)
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.tamano = tamano
    self.propiedades = propiedades

# Creación de la clase hija Limon, donde incluiremos características extra de esta fruta. Para esto usamos la palabra clave 'class', la acompañamos con el nombre elegido 'Limon' y entre paréntesis(), la clase padre 'Frutas'.
class Limon(Fruta):
  '''
    Clase hija usada para representar características adicionales de los limones

    ...

    Atributos
    ------------------
    nombre : str (atributo de clase)
        indica el nombre de la fruta de la clase
    sabor : str (atributo de instancia)
        indica el sabor de la fruta de la clase
    color : str (atributo de instancia)
        indica el color de la fruta de la clase
    forma : str (atributo de instancia)
        indica la forma de la fruta de la clase
    especie : str (atributo de instancia)
        indica la especie de la fruta de la clase

  
    Métodos
    ------------------
    __init__(self, sabor, color,forma,especie)
        inicializa los artibutos del objeto
  '''
  nombre = "limon"
  # Uso del método constructor para definir e inicializar los atributos de la clase fiesta. Los parámetros que tendrá son: sabor,color,forma,especie
  def __init__(self, sabor,color,forma,especie):
    '''
     Permite inicializar los atributos de la clase. Se crean invocando self, a continuación un '.' y el atributo.
     Hacemos uso de la función super() que permite invocar un método de una clase padre desde una clase hija
    ...
    
    Parametros
    -------------------
    sabor : str (atributo de instancia)
        indica el sabor de la fruta
    color : str (atributo de instancia)
        indica el color de la fruta
    forma : str (atributo de instancia)
        indica la forma de la fruta de la clase
    especie : str (atributo de instancia)
        indica la especie de la fruta de la clase
  '''
    super().__init__(sabor,color)
    # Creación de los atributos de la instancia. Están igualados a los parametros del método constructor, esto para que al crear el objeto, capture la información que trae y se le asigne al atributo correspondiente 
    self.forma = forma
    self.especie = especie

# Instancia 1, crearemos el objeto a mostrar
# Objeto 1: Características del limon
fruta1 = Limon("ácido", "verde", "redondo y ligeramente alargado","cítricos")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia 
print("\nEspecie de la fruta:\n",fruta1.especie)
print("\nSabor de la fruta:\n",fruta1.sabor)
print("\nForma de la fruta:\n",fruta1.forma)
print("\nColor de la fruta:\n",fruta1.color)
print("\nNombre de la fruta:\n",fruta1.nombre)

# Ejercicio 2: Class Cubiertos
print("\n","\n- Ejercicio 2: Class Frutas\n")

# Instancia 2, crearemos el objeto a mostrar
# Objeto 2: Características de la cereza
fruta2 = Cereza("dulce", "rojo", "pequeño","vitaminas A y C")

# Mostrar los atributos del objeto 1. Para ello, llamamos la variable seguida de un '.' y el atributo que queremos ver. En este están incluidos, tanto atributos de clase como atributos de instancia 
print("Tamaño de la fruta:\n",fruta2.tamano)
print("\nPropiedades de la fruta:\n",fruta2.propiedades)
print("\nNombre de la fruta:\n",fruta2.nombre)
print("\nSabor de la fruta:\n",fruta2.sabor)
print("\nColor de la fruta:\n",fruta2.color)
