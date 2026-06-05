import os
import matplotlib.pyplot as plt

# 1. Definir rutas relativas estrictas (Requerimiento de reproducibilidad de la rúbrica)
ruta_datos = os.path.join("datos", "sales_sample_2024.csv")
ruta_grafico = os.path.join("resultados", "grafico_resultados.png")

fechas = []
montos = []

# 2. Lectura del archivo CSV nativo
with open(ruta_datos, "r") as archivo:
    lineas = archivo.readlines()[1:] # Saltamos la primera fila (encabezado)
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) >= 3:
            fechas.append(partes[1])       # Columna sales_date
            montos.append(int(partes[2]))  # Columna sales_amount

# 3. Cálculos requeridos por el Escenario B
ventas_totales = sum(montos)
promedio_por_transaccion = ventas_totales / len(montos) if len(montos) > 0 else 0
venta_maxima = max(montos)

# Mostrar resultados técnicos en la consola
print("--- REPORTE DE GESTIÓN DE VENTAS (PROCESADO POR PACO) ---")
print(f"Monto Total de Ventas: ${ventas_totales}")
print(f"Venta Promedio por Operación: ${promedio_por_transaccion:.2f}")
print(f"Monto de la Mayor Venta Registrada: ${venta_maxima}")

# 4. Crear el gráfico solicitado (Evolución de ventas en el tiempo)
plt.figure(figsize=(8, 4))
plt.plot(fechas, montos, marker='o', color='mediumpurple', linestyle='-', linewidth=2)
plt.title("Evolución Temporal de Montos de Ventas")
plt.xlabel("Fecha de Venta")
plt.ylabel("Monto ($)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()

# 5. Guardar la imagen en la carpeta /resultados
plt.savefig(ruta_grafico)
print(f"\n[ÉXITO] Gráfico temporal generado y guardado en: {ruta_grafico}")
