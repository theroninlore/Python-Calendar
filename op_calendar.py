from colorama import Fore, Style
import os
import re 

c = Fore.LIGHTCYAN_EX # Definimos constantes para evitar funciones hardcodeadas.
y = Fore.LIGHTYELLOW_EX
w = Fore.LIGHTWHITE_EX
red = Fore.LIGHTRED_EX
r = Style.RESET_ALL

# Creamos esta lista para poder iterar usando el mes "nombre_meses[mes]", nos devolvera el nombre del mes.
nombres_meses = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                  "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Definimos función pedir fecha para optimizar y limpiar código, de esta forma no creamos código repetido.
def pedir_fecha(clst, max_dias):
    while True:
        try:
            mes = int(input(f"{c}\nPulse {r}"+ f"{w}0 {r}"+ f"{c}para salir al menu principal.\nMes (1-12): {r}")) # Indagamos el mes.
            if mes < 0 or mes > 12: # Validamos el rango del mes. El 0 esta incluido porque lo usaremos para salir al menu principal.                    
                print(f"{red}Mes inválido. Vuelve a intentarlo: {r}")   
                continue
            elif mes == 0:
                os.system(clst)
                return(None)
        except ValueError:  # Usamos try/except para validar la entrada de solo tipo int.
            print(f"{red}El valor ingresado no es valido.{r}")
            continue
        while True:
            try:
                dia = int(input(f"{c}\nPulse {r}"+ f"{w}0 {r}"+ f"{c}para salir al menu principal.\nDía: {r}")) # Indagamos día.
                if dia < 0 or dia > max_dias[mes]: # Validamos rango de días en el mes usando la lista max_dias con el indice [mes].
                    print(f"{red}Día inválido. Vuelve a intentarlo: {r}")
                    continue
                elif dia == 0:
                    os.system(clst)
                    return(None)
                else:
                    fecha = f"{mes}-{dia}" # Definimos fecha como un string que no debe ser tocado ni modificado.
                    return(fecha) # Devolvemos fecha para poder trabajar con la fecha ya estructurada como string.
            except ValueError: # Validamos la entrada de valor distinto a int.
                print(f"{red}El valor ingresado no es valido.{r}")
                continue

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

def añadir_evento(calendar, max_dias, patron, clst, Evento): 
    
    fecha = pedir_fecha(clst, max_dias) # LLamamos a la función pedir fecha.
    if fecha is None:
        return(None)
    if fecha not in calendar: # En el caso de que esa fecha no este en el calendario se crea el key (fecha) para el calendario.
        calendar[fecha] = [] # Al key (fecha) se le asigna un value (lista vacia).
        
    while True:
        nombre = str(input(f"{c}\nSi quieres salir pulsa" f"{w}'Enter'{r}" f"\n{c}Nombre evento: {r}")).strip() # Indagamos el nombre de el evento.
        if not nombre: # Comprobamos si el usuario a ingresado 'Enter'.
            os.system(clst)
            return(None)
        duplicado = False # Definimos variable como False.
        for evento in calendar[fecha]:  # Iniciamos bucle para que evento se transforme en cada objeto iterado dentro de calendar[fecha].
            if evento.nombre.lower() == nombre.lower(): #
                print(f"{red}Este evento ya existe. Intentalo de nuevo{r}")
                duplicado = True # en el caso de que los nombres coincidan asignamos como True a duplicado.
                break
        if duplicado: 
            continue
        elif not duplicado:
            break
                    
        descripcion = str(input(f"{c}\nSi quieres salir pulsa" f"{w}'Enter'{r}" f"\n{c}Descripción: {r}")).strip() # Indagamos la descripción del evento.
        if not descripcion: # Comprobamos si el usuario a ingresado 'Enter'.
            os.system(clst)
            return(None)
            
        while True: 
            hora = str(input(f"{c}\nSi quieres salir pulsa" f"{w}'Enter'{r}" f"\n{c}Hora (ej. 14:30): {r}")).strip() # Indagamos la hora del evento.
            if not hora: # Comprobamos si el usuario a ingresado 'Enter'.
                os.system(clst)
                return(None)
            if re.match(patron, hora): # Usamos regex para comprobar que la hora ingresa es valida.
                nuevo_evento = Evento(nombre, hora, descripcion) # La variable nuevo_evento se transforma en un objeto con los valores indagados arriba.
                calendar[fecha].append(nuevo_evento) # Añadimos el objeto al value (lista) que se asocia con key (fecha). Lo hemos definido antes.
                os.system(clst)
                return(calendar)
            else:
                print(f"{red}El formato ingresado no es valido. Ingrese un formato de hora valido.{r}")
                continue
            
            
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////// 
    
def eliminar_evento(calendar, max_dias, clst):
    
    fecha = pedir_fecha(clst, max_dias) # LLamamos a la función pedir fecha.
    if fecha is None: # Comprobamos si el usuario a ingresado 'Enter'.
        return(None)
    if fecha not in calendar or not calendar[fecha]: # Validamos si esa fecha existe en nuestro calendario.
        print(f"{red}No hay eventos en esa fecha{r}")
        return(None)
                
    while True:
        nombre_borrar = str(input(f"{c}\nSi quieres salir pulsa" f"{w}'Enter'{r}"f"\n{c}Que evento deseas eliminar: {r}")).strip() # Indagamos nombre evento.
        for evento in calendar[fecha]: # La variable evento va iterando por cada objeto en calendario[fecha] convirtiendose en cada objeto por el que pasa.
            # Cada vez que evento se combierte en un objeto distinto validamos que .nombre de ese objeto coincida con el nombre que queremos borrar.
            if evento.nombre.lower() == nombre_borrar.lower():  
                evento_encontrado = evento # evento_encontrado se transforma en un objeto, en el mismo objeto que era evento.
                calendar[fecha].remove(evento_encontrado) # Aquí eliminamos ese objeto de calendario.
                os.system(clst)
                return(calendar) # Devolvemos el calendario actualizado.
            elif not nombre_borrar: # Validamos que el usuario ponga 'Enter'.
                return(None)
        print(f"{red}El evento '{nombre_borrar}' no existe en esa fecha.{r}") # Validamos que el evento no exista.
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////// 

def mod_evento(calendar, max_dias, clst, patron):
    fecha = pedir_fecha(clst, max_dias) # LLamamos a la función pedir fecha.
    
    if fecha not in calendar or not calendar[fecha]: # Validamos si esa fecha existe en nuestro calendario.
        print(f"{red}No hay eventos en esa fecha{r}")
        return(None)
            
    while True:
        evento_mod = str(input(f"{c}\nSi quieres salir pulsa " f"{w}'Enter'{r}"f"\n{c}Que evento deseas modificar: {r}")).strip() # Indagamos el nombre del evento que va a ser buscado.
        if fecha not in calendar or not calendar[fecha]: # Validamos si esa fecha existe en nuestro calendario.
            print(f"{red}No hay eventos en esa fecha{r}")
            return(None)
        for evento in calendar[fecha]: # La variable evento va iterando por cada objeto en calendario[fecha] convirtiendose en cada objeto por el que pasa.
            # Cada vez que evento se combierte en un objeto distinto validamos que .nombre de ese objeto coincida con el nombre que queremos borrar.
            if evento.nombre.lower() == evento_mod.lower():  
                evento_encontrado = evento # evento_encontrado se transforma en un objeto, en el mismo objeto que era evento.
                os.system(clst)
                break
            elif not evento_mod: # Comprobamos si el usuario a ingresado 'Enter'.
                return(None)
            else:
                print(f"{red}El evento '{evento_mod}' no existe en esa fecha.{r}") # Validamos que el evento no exista.
                break
        while True: 
            print(  # Imprimimos un menu secundario.
f"""{Fore.LIGHTCYAN_EX}
1. Nombre
2. Hora
3. Descripción
4. Salir
{Style.RESET_ALL}"""
                )
            mod = int(input(f"{c}\nPulse "+ f"{w}0 "+ f"{c}Que quieres modificar: {r}")) # Indagamos que se desea modificar.
            if mod == 0: # Comprobamos si el usuario a ingresado '0'.
                return(None)
            elif mod == 1:
                nuevo_nombre = str(input(f"{c}\nSi quieres salir pulsa " f"{w}'Enter'" f"\n{c}Ingresa el nuevo nombre: {r}")).strip()  # Indagamos nuevo nombre.
                evento_encontrado.mod_nombre(nuevo_nombre) # Llamamos al método mod_nombre de el objeto en el que se ha convertido evento.
                return(None)
            elif mod == 2:
                while True: 
                    nueva_hora = str(input(f"{c}\nSi quieres salir pulsa " f"{w}'Enter'" f"\n{c}Hora (ej. 14:30): {r}")).strip() # Indagamos nueva hora.
                    if not nueva_hora:  # Comprobamos si el usuario a ingresado 'Enter'.
                        return(None)
                    if re.match(patron, nueva_hora): # Usamos regex para comprobar que la hora ingresa es valida.
                        evento_encontrado.mod_hora(nueva_hora) # Llamamos al método mod_hora de el objeto en el que se ha convertido evento.
                        return(None)
                    else:
                        print(f"{red}El formato ingresado no es valido. Ingrese un formato de hora valido.{r}")
                        continue
            elif mod == 3:
                nueva_descripcion = str(input(f"{c}\nSi quieres salir pulsa " f"{w}'Enter'" f"\n{c}Descripción: {r}")).strip() # Indagamos nueva descripcion
                evento_encontrado.mod_desc(nueva_descripcion) # Llamamos al método mod_desc de el objeto en el que se ha convertido evento.
                return(None)
            elif mod == 4:
                print(f"{y}Saliendo...{r}")
                return(None)
            else:
                print(f"{red}Entrada no valida, solo se permiten numeros del 1-4. Vuelve a intentarlo{r}")
                continue
                
                
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

def consultar_evento(calendar, max_dias, clst):
    while True:
        try:
            mes = int(input(f"{c}\nPulse {r}"+ f"{w}0 {r}"+ f"{c}para salir al menu principal.\nMes (1-12): {r}")) # Indagamos el mes.
            if mes < 0 or mes > 12: # Validamos el rango del mes. El 0 esta incluido porque lo usaremos para salir al menu principal.      
                print(f"{red}Mes inválido. Vuelve a intentarlo: {r}")
                continue
            elif mes == 0:
                os.system(clst)
                return(None)
        except ValueError:   # Usamos try/except para validar la entrada de solo tipo int.
            print(f"{red}El valor ingresado no es valido.{r}")
            continue
        while True:
            try:
                dia = int(input(f"{c}\nPulse {r}"+ f"{w}0 {r}"+ f"{c}para salir al menu principal.\n\nDía: {r}")) # Indagamos día.
                if dia < 0 or dia > max_dias[mes]: # Validamos rango de días en el mes usando la lista max_dias con el indice [mes].
                    print(f"{red}Día inválido. Vuelve a intentarlo: {r}")
                elif dia == 0:
                    os.system(clst)
                    return(None)
                else:
                    fecha = f"{mes}-{dia}" # Definimos fecha como un string que no debe ser tocado ni modificado.
                    print(f"{c}Eventos para el {dia} de {nombres_meses[mes]}:{r}") # Imprimimos los eventos que hay en el dia y mes del calendario.
                    eventos = calendar.get(fecha, []) # Si la fecha existe obtiene la lista real de objetos, si la fecha no existe eventos se vuelve una lista vacia. Entones no se podra iterar.
                    for evento in eventos: # La variable evento va iterando por cada objeto en calendario[fecha] convirtiendose en cada objeto por el que pasa.
                        print(f"{w}- {evento}{r}") # Imprimimos el objeto evento.
                    while True:
                        salir = str(input(f"{c}Para salir pulsa {r}"+ f"{w}'Enter'{r}"))
                        if not salir:
                            os.system(clst)
                            return(None)
                        else:
                            print(f"{red}Valor no valido. Solo se puede ingresar Enter.{r}")
                            continue
            except ValueError: # Validamos la entrada de valor distinto a int.
                print(f"{red}El valor ingresado no es valido.{r}")
                continue
            
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

def buscar_evento(calendar):
    while True:
        nombre_buscar = str(input(f"{c}\nSi quieres salir pulsa " f"{w}'Enter'{r}"f"\n{c}Que evento deseas buscar: {r}")).strip() # Indagamos el nombre del evento que va a ser buscado.
        encontrado = False # Definimos una variable como 'False'. 
        # La función ".items()" devuelve el key por un lado y el value por otro.
        for fecha, lista_eventos in calendar.items(): # Creamos un bucle para que a fecha se le asigne el valor de la key y que a lista_objetos se le asigne el valor del value.
            for evento in lista_eventos: # La variable evento va iterando por cada objeto en lista_eventos convirtiendose en cada objeto por el que pasa.
                if nombre_buscar.lower() in evento.nombre.lower():
                    m, d = fecha.split("-") # Usamos ".split("-") para indicar que en el caracter "-" separe el string, y que le asigne un parte a "m" (mes) y la otra a "d" (dia).
                    print(f"El evento {evento.nombre} ha sido encontrado el {int(d)} de {nombres_meses[int(m)]}") # Imprimimos la ubicación del evento
                    encontrado = True # Si el evento ha sido encontrado la variable 'encontrado' se establece en 'True'.
                    break
            if encontrado: # Si encontrado es 'True' que salga del bucle.
                break
        if not encontrado: # Si encontrado es 'False' que imprima que el evento no se ha encontrado y salga del bucle.
            print(f"\n{red}El evento '{nombre_buscar}' no ha sido encontrado.{r}")
            break
    return(None)




