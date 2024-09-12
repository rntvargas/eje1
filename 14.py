precio = input("Introduce el precio en euros con dos decimales (ej. 4.56): ")  
euros, centimos = precio.split('.')  # Separamos euros y céntimos
print(f"Euros: {euros}, Céntimos: {centimos}")
