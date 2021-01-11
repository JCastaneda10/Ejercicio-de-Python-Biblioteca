while True:
    print("Bienvenido a la biblioteca de Wa-shing-tong, qué se le ofrece \n 1.-Añadir un libro a la biblioteca \n 2.-Quiero ver qué libros hay en la biblioteca\n 3.- Estoy bien pinche loco alv así que quiero borrar todos los libros \n 4.-Ir en paz")
    opcion=int(input())
    if opcion == 4:
        print("saquese alv pues")
        break
    def agregar(libro):
        file = open("Libros.txt", "a+")
        file.write(libro)
        file.close
    def leer():
        file = open("Libros.txt", "r")
        print(file.read)
        file.close
    def borrar():
        file = open("Libros.txt","w")
        file.seek(0)
        file.write("")
        file.close
    if opcion == 1:
        titulo = input("Ingrese el nombre del libro: ")
        autor = input(" Quien es el autor?: ")
        fecha = input("Cuando fue publicado?: ")
        libro = "Titulo: {}, Autor: {}, Fecha de publicación: {}\n".format(titulo,autor,fecha)
        agregar(libro)
    if opcion == 2:
        leer()
    if opcion == 3:
        borrar()





