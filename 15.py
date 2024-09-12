fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")  
dia, mes, año = fecha.split('/')  # Separamos la fecha en día, mes y año
print(f"Día: {dia}, Mes: {mes}, Año: {año}")
