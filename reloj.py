import datetime


def ver_hora_ny():
    """ Fecha y hora de NY"""
    print("fecha y hora en N.Y. EU:\n")
    print("2018/05/09 12:20:00")


def ver_fecha_hora():
    """:return Cadena de hora y fecha local (-6)"""
    formato  = "%B %d, %Y  %H:%M:%S"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=-6))
    fecha_actual =  datetime.datetime.now(zona_horaria)
    fecha_formateada = fecha_actual.strftime(formato)
    print("La fecha y la hora exacta son: {}".format(fecha_formateada))


def ver_hora_sf():
	###Ver hora en Sn. Fco.###

	
def ver_hora(time_zone):
    """
    :param time_zone:
    :return cadena de hora con el formato %H:%M:%S:
    """
    formato = '%H:%M:%S'
    time_zone = datetime.timezone(datetime.timedelta(hours=time_zone))
    hora_actual = datetime.datetime.now(time_zone).time()
    return hora_actual.strftime(formato)


def ver_fecha_hora_espana():
    """
    :param Nada
    :return Cadena con fecha y hora
    """
    formato = "%B %d, %Y  %H:%M"
    zonaHoraria = datetime.timezone(datetime.timedelta(hours=2))
    fechaActual = datetime.datetime.now(zonaHoraria).strftime(formato)
    print("La fecha en España es: {} ".format(fechaActual))


def menu():
    print('1 - Ver la hora')
    print('2 - Ver fecha y hora')
    print('3 - Ver hora en NY')
    print('4 - Ver hora en SF')
    print('5 - Ver hora en España')
    print('6 - Ver instrucciones')
    print('7 - salir')

# TODO agregar opciones para obtener la fecha y hora en:
# España
# Brasil
# Japón
# Alaska
def reloj():
    print('Bienvenido al reloj del mundo')
    print('Estas son las operaciones que puedes realizar')
    menu()
    while True:
        try:
            op = int(input('Seleccione la operación: '))
        except ValueError:
            print('Ingrese un valor del 1 al 6')
        else:
            now = datetime.datetime.now()
            if op == 1:
                print('La hora exacta es: %s ' % ver_hora(-6))
            elif op == 2:
                print(ver_fecha_hora())
            elif op == 3:
                print('La hora exacta en NY es: %s' % ver_hora(-5))
            elif op == 4:
                print('La hora exacta SF es: %s' % ver_hora(-8))
            elif op == 5:
                ver_fecha_hora_espana()
            elif op == 6:
                menu()
            elif op == 7:
                break


def ver_hora_japon():
    """japon"""
    formato  = "%H:%M:%S"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=9))
    hora_actual =  datetime.datetime.now(zona_horaria).time()
    hora_formateada = hora_actual.strftime(formato)
    print("La hora exacta en Japon es: {}".format(hora_formateada)

reloj()

-
