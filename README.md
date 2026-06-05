# # Trabajo Práctico: Gestión Colaborativa y Control de Versiones

* **Institución:** Universidad Tecnológica Nacional (UTN - TUP)
* **Cátedra:** Organización Empresarial - 2026
* **Escenario Seleccionado:** Escenario B - Análisis de Ventas de una Pequeña Empresa

---

## 👥 Integrantes y Roles Simulados

> ⚠️ **NOTA ACLARATORIA DE AUTORIZACIÓN:** Por cuestiones de tiempos y retraso en la materia, y tras haber solicitado y recibido la debida autorización de la cátedra, procedo a realizar este Trabajo Práctico de forma **individual**. Dicho esto, se mantienen los nombres de ejemplo de la consigna para representar de forma clara las responsabilidades del flujo de trabajo ágil corporativo:

* **P1 - Líder, DevOps e Infraestructura (SRE):** Hugo
* **P2 - Desarrollador Técnico de Software:** Paco
* **P3 - Revisor de Código y Aseguramiento de Calidad (QA):** Luis

---

## ⚙️ Estructura del Proyecto

El repositorio está estructurado bajo las normativas estrictas de reproducibilidad técnica exigidas:
* `/datos`: Contiene el set de datos origen (`sales_sample_2024.csv`).
* `/scripts`: Aloja el backend analítico (`analisis_datos.py`).
* `/resultados`: Repositorio de salidas técnicas y reportes visuales (`grafico_resultados.png`).

---

## 🛠️ Ciclo de Vida del Desarrollo (SDLC)

El proyecto simula el ciclo completo de una célula de desarrollo profesional utilizando metodologías ágiles y control de versiones:

1. **Sprint Planning & DevOps (Hugo):** Configuración de repositorios, políticas estrictas de exclusión (`.gitignore`) para entornos de Google Colab y maquetado de infraestructura básica.
2. **Feature Development (Paco):** Implementación de la lógica nativa en Python (sin librerías de alto nivel como Pandas) para el cálculo de métricas financieras (Monto Total, Promedio de Operación y Máximo Histórico). Renderizado inicial de la curva visual de ventas comerciales.
3. **Control de Calidad & Peer Review (Luis):** Auditoría mediante Pull Request en GitHub, detección de errores de caja blanca (bloqueos de memoria interna de Matplotlib) y optimización crítica mediante submuestreo secuencial en el eje X para garantizar la legibilidad absoluta del informe gráfico final (**TP-3.1 - Hotfix**).

---

## ✅ Control de Calidad
* **Versión actual:** Auditada, corregida y aprobada de manera unánime por el rol de **Luis (QA)** bajo el ticket integrador de Jira.
