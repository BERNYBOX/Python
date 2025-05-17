
AFP = 0.0287  
SFS = 0.0304  
SEGURIDAD_SOCIAL = AFP + SFS  
ISR = 0.15  
BONIFICACION = 0.0833  
def main():
    print("Calculadora de Sueldo - República Dominicana")
    
    sueldo_bruto = float(input("Ingrese el sueldo bruto: RD$"))
    if sueldo_bruto <= 0:
        print("Error: El sueldo bruto debe ser positivo")
        return
        
    otros_descuentos = float(input("Ingrese otros descuentos (0 si no hay): RD$"))
    if otros_descuentos < 0:
        print("Error: Los descuentos no pueden ser negativos")
        return
    
    descuento_ss = sueldo_bruto * SEGURIDAD_SOCIAL
    descuento_isr = sueldo_bruto * ISR
    bonificacion = sueldo_bruto * BONIFICACION
    
    sueldo_neto = sueldo_bruto - descuento_ss - descuento_isr - otros_descuentos + bonificacion
    
    print("\nResultados:")
    print(f"Sueldo Bruto: RD${sueldo_bruto:.2f}")
    print(f"Descuento por Seguridad Social: RD${descuento_ss:.2f}")
    print(f"Retención ISR: RD${descuento_isr:.2f}")
    print(f"Otros Descuentos: RD${otros_descuentos:.2f}")
    print(f"Bonificación: RD${bonificacion:.2f}")
    print(f"Sueldo Neto: RD${sueldo_neto:.2f}")

if __name__ == "__main__":
    main()