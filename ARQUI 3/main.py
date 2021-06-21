from CRUDHospital import CRUdHospital
from CRUDDoctor import CRUDDoctor

def main():
    CRUDH = CRUdHospital()
    CRUDD = CRUDDoctor()
    print("1.Agregar hospital.\n2.Eliminar Hospital.\n3.Editar Hospital\n4.Buscar Hospital.\n5.Agregar Doctor\n6.Eliminar Doctor\n7.Editar Doctor\n8.Buscar Doctor.")
    x = input()
    x = int(x)
    while x > 0 and x < 9:
    	if x == 1:
    		print("Ingrese id: ")
    		a = input()
    		print("Ingrese nombre:")
    		b = input()
    		CRUDH.addHospital(a,b)
    	if x == 2:
    		print("Ingrese id: ")
    		a = input()
    		CRUDH.deleteHospital(a)
    	if x == 3:
    		print("Ingrese id: ")
    		a = input()
    		print("Ingrese nombre:")
    		b = input()
    		CRUDH.editHospital(a,b)
    	if x == 4:
    		print("Ingrese nombre:")
    		b = input()
    		CRUDH.searchHospital(b)
    	if x == 5:
    		print("Ingrese id: ")
    		a = input()
    		print("Ingrese nombre:")
    		b = input()
    		print("Ingrese id del hospital:")
    		c = input()
    		print("Ingrese especialización: ")
    		d = input()
    		CRUDD.addDoctor(a,c,b,d)
    	if x == 6:
    		print("Ingrese id: ")
    		a = input()
    		CRUDD.deleteDoctor(a)
    	if x == 7:
    		print("Ingrese id: ")
    		a = input()
    		print("Ingrese nombre:")
    		b = input()
    		print("Ingrese id del hospital:")
    		c = input()
    		print("Ingrese especialización: ")
    		d = input()
    		CRUDD.editDoctor(a,c,b,d)
    	if x == 8:
    		print("Ingrese nombre:")
    		b = input()
    		CRUDD.serchDoctor(b)
    	print("\n\n\n1.Agregar hospital.\n2.Eliminar Hospital.\n3.Editar Hospital\n4.Buscar Hospital.\n5.Agregar Doctor\n6.Eliminar Doctor\n7.Editar Doctor\n8.Buscar Doctor.")
    	x = input()
    	x = int(x)

if __name__ == "__main__":
    main()
