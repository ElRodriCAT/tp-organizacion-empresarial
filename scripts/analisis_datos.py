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

# 4. Limpieza absoluta de memoria gráfica previa
plt.clf()
plt.close('all')

# 5. Crear el gráfico solicitado (Evolución de ventas en el tiempo)
fig, ax = plt.subplots(figsize=(12, 6)) # Un poco más grande para dar aire
ax.plot(fechas, montos, marker='o', color='mediumpurple', linestyle='-', linewidth=1, markersize=4)

# --- CONFIGURACIÓN CRÍTICA DE LECTURA PARA EL EJE X ---
# Seleccionamos un índice cada 30 registros para que el texto respire
paso = 30
indices_visibles = list(range(0, len(fechas), paso))
fechas_visibles = [fechas[i] for i in indices_visibles]

ax.set_xticks(indices_visibles)
ax.set_xticklabels(fechas_visibles, rotation=45, ha='right', fontsize=9)
# ------------------------------------------------------

ax.set_title("Evolución Temporal de Montos de Ventas", fontsize=12, fontweight='bold')
ax.set_xlabel("Fecha de Venta", fontsize=10)
ax.set_ylabel("Monto ($)", fontsize=10)
ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

# 6. Guardar la imagen en la carpeta /resultados
os.makedirs("resultados", exist_ok=True)
plt.savefig(ruta_grafico, dpi=300)
print(f"\n[ÉXITO DE QA] Gráfico temporal generado de forma limpia en: {ruta_grafico}")
