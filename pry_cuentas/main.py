from grupo.controlador import ctrGrupo
from grupo.modelo import modGrupo
from plancuentas.controlador import ctrPlan
from plancuentas.modelo import modPlan
ctrg = ctrGrupo()
ctrp = ctrPlan()

opc = 0
try:
    while opc != 4:
        print("Menu")
        opc = int(input('1) Grupo de Cuentas' + '\n2) Plan de Cuentas' + '\n3) Salir' + '\n¿Opcion?: '))

        if opc == 0:
            pass

        elif opc == 1:
            print("Mantenimiento Grupos")
            opcG = 0
            while opcG != 6:
                opcG = int(input('1) Nuevo Grupos' + '\n2) Listar Grupo' + '\n3) Editar Grupo' + '\n4) Eliminar  Grupos' +  '\n5) Regresar' + '\n¿Opcion?: '))

                if opcG == 1:
                    descripcion = input('Ingrese una descripción: ')
                    grupoAdd = modGrupo(descripcion.upper())
                    if ctrg.ingresar(grupoAdd):
                        print("Registro grabado correctamente\n")
                    else:
                        print("Error")

                if opcG == 2:
                    print("\nListar Grupos\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0],r[1]))
                    print("\n")

                if opcG == 3:
                    print("\nListado Grupos\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0],r[1]))
                    print("\n")
                    id = int(input('Ingrese codigo id de grupo a editar: '))
                    descripcion = input('Ingrese una nueva descripción: ')
                    grupoEdit = modGrupo(descripcion)
                    if ctrg.modificar(grupoEdit,id):
                        print("Registro grabado correctamente\n")
                    else:
                        print("Error")

                if opcG == 4:
                    print("\nListado Grupos\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0],r[1]))
                    print("\n")
                    id = int(input('Ingrese codigo id de grupo a eliminar: '))
                    if ctrg.eliminar(id):
                        print("Registro eliminado correctamente\n")
                    else:
                        print("Error")

                if opcG == 5:
                    opcG = 6
                    opc = 0
                    pass

        elif opc == 2:
            print("Mantenimiento Plan de Cuentas")
            opcP = 0
            while opcP != 6:
                opcP = int(input('1) Nuevo Plan' + '\n2) Listar Plan' + '\n3) Editar Plan' + '\n4) Eliminar  Plan' +  '\n5) Regresar' + '\n¿Opcion?: '))

                if opcP == 1:
                    codigo = input('Ingrese una codigo: ')
                    print("\nListar Grupos\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0],r[1]))
                    print("\n")
                    grupoid = int(input('Ingrese la id del grupo: '))
                    descripcion = input('Ingrese una descripción: ')
                    print('D = Deudora \nA = Acredora')
                    naturaleza = input('Ingrese una naturaleza: ')
                    print('0 = Falso \n1 = True')
                    estado = int(input('Ingrese un estado: '))
                    add = modPlan(codigo,grupoid,descripcion.upper(),naturaleza.upper(),estado)
                    if ctrp.ingresar(add):
                        print("Registro grabado correctamente\n")
                    else:
                        print("Error")

                if opcP == 2:
                    print("\nListar Plan de Cuentas\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n")

                if opcP == 3:
                    print("\nListar Plan de Cuentas\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n")

                    id = int(input('Ingrese codigo id de grupo a editar: '))
                    codigo = input('Ingrese una codigo: ')
                    print("\nListado Grupos\n")
                    grupolist = ctrg.consulta()
                    print("Id - Descripción")
                    for r in grupolist:
                        print("{} - {}".format(r[0],r[1]))
                    print("\n")
                    grupoid = int(input('Ingrese la id del grupo: '))
                    descripcion = input('Ingrese una descripción: ')
                    print('D = Deudora \nA = Acredora')
                    naturaleza = input('Ingrese una naturaleza: ')
                    print('0 = Falso \n1 = True')
                    estado = int(input('Ingrese un estado: '))
                    edit = modPlan(codigo,grupoid,descripcion.upper(),naturaleza.upper(),estado)
                    if ctrp.modificar(edit,id):
                        print("Registro grabado correctamente\n")
                    else:
                        print("Error")

                if opcP == 4:
                    print("\nListar Plan de Cuentas\n")
                    lista = ctrp.consulta()
                    print("Id - Codigo - Grupo - Descripcion - Naturaleza - Estado")
                    for r in lista:
                        print("{} - {} - {} - {} - {} - {}".format(r[0], r[1], r[2], r[3], r[4], r[5]))
                    print("\n")
                    id = int(input('Ingrese codigo id de plan a eliminar: '))
                    if ctrp.eliminar(id):
                        print("Registro eliminado correctamente\n")
                    else:
                        print("Error")

                if opcP == 5:
                    opcP = 6
                    opc = 0
                    pass


        elif opc == 3:
            print('ADIOS')
            break

except Exception as ex:
    print(ex)