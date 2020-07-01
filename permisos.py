class Permiso:
    def __init__(self):
        self.codigo = []
        self.condutor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.fecha_solicitud = []
        self.motivo = []
        self.habilitado = []

    def menu(self):
        opcion="""
        ***** GESTION DE PERMISO DE VEHICULOS *****
                ( MENU DEL SISTEMA )  
                
        1.-GUARDAR REGISTRO DE PERMISO
        2.-MOSTRAR TODOS LOS PERMISOS SOLICITADOS
        3.-INABILITAR PERMISOS
        4.-MOSTRAR LOS PERMISOS HABILITADOS
        5.-MOSTRAR LOS PERMISOS NO HABILITADOS
        6.-SALIR
        """
        print(opcion)
        print('***********************************************************************')
        seleccion = int(input('DIGITE UNA OPCION:\n'))
        if (seleccion == 1):
           print(self.resgVehic())
           print(self.menu())
        elif (seleccion == 2):
           print(self.mostrarReg())
           print(self.menu())
        elif (seleccion == 3):
           print(self.cambiarHabilitar())
           print(self.menu())
        elif (seleccion == 4):
           print(self.mostrarReg())
           print(self.menu())
        elif (seleccion == 5):
           print(self.mostrarInab())
           print(self.menu())
        elif (seleccion == 6):
           print(self.salir())
    def resgVehic(self):
        codigo=int(input('Ingrese Codigo Por Favor: \n'))
        conductor=input('Ingrese nombre del solicitante:\n')
        modelo=input('Ingrese modelo del Vehiculo:\n ')
        marca=input('Ingrese marca del Vehiculo:\n')
        placa=input('Ingrese placa:\n')
        ciudad = input('Ingrese ciudad:\n')
        fecha_solic=input('Ingrese Fecha de solicitud (%): \n')
        motivo = input('ingresar descripcion del motivo:\n')

        print(self.guardarVehic(codigo,conductor.upper(),modelo.upper(),marca.upper(),placa.upper(),ciudad.upper(),fecha_solic,motivo.upper()))
        agregarmas=input('DESEA AGREGAR MAS SOLICITUD: y/n \n')
        if (agregarmas=='y' or agregarmas=='Y'):
            self.resgVehic()
        return'SE REGISTRO CORRECTAMENTE LA SOLICITUD DEL PERMISO'
    def guardarVehic(self, cd,cond,md,mc,pl,cdad,fech,mt):
        self.codigo.append(cd)
        self.condutor.append(cond)
        self.modelo.append(md)
        self.marca.append(mc)
        self.placa.append(pl)
        self.ciudad.append(cdad)
        self.fecha_solicitud.append(fech)
        self.motivo.append(mt)
        self.habilitado.append(1)
        return"SE REGISTRO LA PERSONA: {} **".format(cond)

    def mostrarReg(self):
        if (self.codigo):
            for i in range(len(self.codigo)):
                if (self.habilitado[i]== 1):
                    self.descripcionMenu(i)
        else:
            return 'ESTA VACIO EL REGISTRO'
    def mostrarInab(self):
        print('*****PERMISOS NO HABILITADOS******')
        if (self.codigo):
            for i in range(len(self.codigo)):
                if (self.habilitado[i]== 0):
                     self.descripcionMenu(i)
    def descripcionMenu(self,hb):
      # if (self.habilitado[hb] ==self.habil()):
            print('**SOLICITANTE  ***** {} *****'.format(self.condutor[hb]))
            print('CODIGO= {} '.format(self.codigo[hb]))
            print('MODELO = {} '.format(self.modelo[hb]))
            print('MARCA = ***{}***'.format(self.marca[hb]))
            print('PLACA=** {} **'.format(self.placa[hb]))
            print('CIUDAD= {}  '.format(self.ciudad[hb]))
            print('FECHA DE SOLICITUD = {}'.format(self.fecha_solicitud[hb]))
            print('MOTIVO= {}  '.format(self.motivo[hb]))
            print('HABILITADO= {}  '.format(self.habilitado[hb]))

            print('****************************************************')
    def habil(self,dc):
        inahabilitado=dc
        return inahabilitado
    def activo(self):
        self.mostrarReg()
        print('**************INABILITAR UN PERMISO**************')
        codServ = int(input('INGRESE CODIGO :\n '))
        posicion = self.codigo.index(codServ)
        return posicion

    def cambiarHabilitar(self):
        posicion = self.activo()
        return self.inabilitarServ(posicion)

    def inabilitarServ(self, posicion):
        self.habilitado[posicion] = 0
        return ' LA PERSONA *****{}***** SE INABILITADO CORRECTAMENTE'.format(self.condutor[posicion])

    def habilitarServ(self):
        posicion = self.activo()
        self.habilitado[posicion] = 1
        return ' LA PERSONA {} SE HABILITO CORRECTAMENTE'.format(self.condutor[posicion])

    def salir(self):
        return '*****GRACIAS POR UTILIZAR EL SISTEMA DE GESTION DE PERMISO VEHICULAR*****'


permisos = Permiso()
permisos.guardarVehic(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.guardarVehic(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '22/06/2020', 'PERMISO PARA IR AL TRABAJO')
permisos.menu()


