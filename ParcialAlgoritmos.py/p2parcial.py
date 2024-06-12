# 2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
# a) Contar cuantas especies hay;
# b) Determinar cuantos descubridores distintos hay;
# c) Mostrar todos los dinosaurios que empiecen con T;
# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;


class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)


dinosaurios = [
    {
        "nombre": "Tyrannosaurus Rex",
        "especie": "Theropoda",
        "peso": "7000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1902
    },
    {
        "nombre": "Triceratops",
        "especie": "Ceratopsidae",
        "peso": "6000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1889
    },
    {
        "nombre": "Velociraptor",
        "especie": "Dromaeosauridae",
        "peso": "15 kg",
        "descubridor": "Henry Fairfield Osborn",
        "ano_descubrimiento": 1924
    },
    {
        "nombre": "Brachiosaurus",
        "especie": "Sauropoda",
        "peso": "56000 kg",
        "descubridor": "Elmer S. Riggs",
        "ano_descubrimiento": 1903
    },
    {
        "nombre": "Stegosaurus",
        "especie": "Stegosauridae",
        "peso": "5000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Spinosaurus",
        "especie": "Spinosauridae",
        "peso": "10000 kg",
        "descubridor": "Ernst Stromer",
        "ano_descubrimiento": 1912
    },
    {
        "nombre": "Allosaurus",
        "especie": "Theropoda",
        "peso": "2000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Apatosaurus",
        "especie": "Sauropoda",
        "peso": "23000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1877
    },
    {
        "nombre": "Diplodocus",
        "especie": "Sauropoda",
        "peso": "15000 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1878
    },
    {
        "nombre": "Ankylosaurus",
        "especie": "Ankylosauridae",
        "peso": "6000 kg",
        "descubridor": "Barnum Brown",
        "ano_descubrimiento": 1908
    },
    {
        "nombre": "Parasaurolophus",
        "especie": "Hadrosauridae",
        "peso": "2500 kg",
        "descubridor": "William Parks",
        "ano_descubrimiento": 1922
    },
    {
        "nombre": "Carnotaurus",
        "especie": "Theropoda",
        "peso": "1500 kg",
        "descubridor": "José Bonaparte",
        "ano_descubrimiento": 1985
    },
    {
        "nombre": "Styracosaurus",
        "especie": "Ceratopsidae",
        "peso": "2700 kg",
        "descubridor": "Lawrence Lambe",
        "ano_descubrimiento": 1913
    },
    {
        "nombre": "Therizinosaurus",
        "especie": "Therizinosauridae",
        "peso": "5000 kg",
        "descubridor": "Evgeny Maleev",
        "ano_descubrimiento": 1954
    },
    {
        "nombre": "Pteranodon",
        "especie": "Pterosauria",
        "peso": "25 kg",
        "descubridor": "Othniel Charles Marsh",
        "ano_descubrimiento": 1876
    },
    {
        "nombre": "Quetzalcoatlus",
        "especie": "Pterosauria",
        "peso": "200 kg",
        "descubridor": "Douglas A. Lawson",
        "ano_descubrimiento": 1971
    },
    {
        "nombre": "Plesiosaurus",
        "especie": "Plesiosauria",
        "peso": "450 kg",
        "descubridor": "Mary Anning",
        "ano_descubrimiento": 1824
    },
    {
        "nombre": "Mosasaurus",
        "especie": "Mosasauridae",
        "peso": "15000 kg",
        "descubridor": "William Conybeare",
        "ano_descubrimiento": 1829
    },

]

print("")
print("PA")


def Contar_Especies(lista):
    pila = Stack()
    for dinosaurio in lista:
        pila.push(dinosaurio)
    especies = set()
    while pila.size() > 0:
        dinosaurio = pila.pop()
        especies.add(dinosaurio["especie"])
    return len(especies)


numero_de_especies_unicas = Contar_Especies(dinosaurios)
print(f"Hay {numero_de_especies_unicas} especies dinosaurios en la lista.")

print("")
print("PB")


def Contar_Descubridores(lista):
    pila = Stack()
    for dinosaurio in lista:
        pila.push(dinosaurio)
    descubridores = set()
    while pila.size() > 0:
        dinosaurio = pila.pop()
        descubridores.add(dinosaurio["descubridor"])
    return len(descubridores)


numero_de_descubridores_unicos = Contar_Descubridores(dinosaurios)
print(f"Hay {numero_de_descubridores_unicos} descubridores dinosaurios en la lista.")

print("")
print("PC")


def Mostrar_DinosauriosT(lista):
    pila = Stack()
    for dinosaurio in lista:
        pila.push(dinosaurio)
    dinosaurios_con_t = []
    while pila.size() > 0:
        dinosaurio = pila.pop()
        if dinosaurio["nombre"].startswith("T"):
            dinosaurios_con_t.append(dinosaurio)
    return dinosaurios_con_t


dinosaurios_con_t = Mostrar_DinosauriosT(dinosaurios)
for dino in dinosaurios_con_t:
    print(dino)

print("")
print("PD")


def dinosaurios_275kg(lista):
    pila = Stack()
    for dinosaurio in lista:
        pila.push(dinosaurio)
    dinosauriosL = []
    while pila.size() > 0:
        dinosaurio = pila.pop()
        peso, unidad = dinosaurio["peso"].split(" ")
        peso_kg = int(peso)
        if peso_kg < 275:
            dinosauriosL.append(dinosaurio)
    return dinosauriosL


dinosaurios_ligeros = dinosaurios_275kg(dinosaurios)
for dino in dinosaurios_ligeros:
    print(dino)

print("")
print("PE")
dinosauriosAQS = Stack()
for dinosaurio in dinosaurios:
    nombre = dinosaurio['nombre']
    if nombre[0] in ('A', 'Q', 'S'):
        dinosauriosAQS.push(dinosaurio)

print("Dinosaurios que comienzann con A, Q, S: ")
while dinosauriosAQS.size() > 0:
    dino = dinosauriosAQS.pop()
    print(dino['nombre'])
