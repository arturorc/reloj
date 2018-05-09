import datetime

def ver_hora_ny():
    print("fecha y hora en N.Y. EU:\n")
    print("2018/05/09 12:20:00")


def menu():
    print('1 - Ver la hora')
    print('2 - Ver fecha y hora')
    print('3 - Ver hora en NY')
    print('4 - Ver hora en SF')
    print('5 - Ver instrucciones')
    print('6 - salir')

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
                menu()
            elif op == 6:
                break

reloj()

