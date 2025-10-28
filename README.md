#  Sistema de Gestión Hospitalaria

Este proyecto implementa un **sistema de gestión hospitalaria** en Python, utilizando **estructuras de datos avanzadas** como **colas con prioridad**, **colas circulares** y **arreglos dinámicos** para simular el proceso de atención de pacientes en un hospital.

---

##  Descripción General

El sistema permite:
- Registrar pacientes y agregarlos a una **cola con prioridad**, donde los más urgentes son atendidos primero.
- Asignar doctores disponibles para atender pacientes.
- Simular el proceso de atención de cada paciente (con una pausa de 3 segundos por atención).
- Guardar el **historial de atenciones** en un **arreglo dinámico**.
- Mostrar los registros históricos de atención.


---

##  Estructuras de Datos Usadas

### 1.  Arreglo Dinámico (`list`)
- Se utiliza para almacenar el **historial de atenciones**.
- Permite que el tamaño crezca automáticamente a medida que se registran nuevas atenciones.
- Ejemplo de uso:
  ```python
  self.history.append((doctor_name, patient_name, symptom))
  ```
### 2.  Cola Circular
- Se usa para administrar doctores disponibles.
- Cuando un doctor termina de atender a un paciente, se coloca nuevamente al final de la cola, garantizando una rotación equitativa entre los doctores.
### 3.  Cola con Prioridad (heapq)
- Se usa para manejar los pacientes según su nivel de urgencia.
- Cada paciente tiene una prioridad (por ejemplo, 1 = urgente, 3 = leve).
- Los pacientes con menor valor de prioridad son atendidos primero.
- Ejemplo:
  ```python
  heapq.heappush(self.priority_queue, (priority, patient))
  ```

##  Lógica del Sistema

1. **Ingreso de pacientes:**  
   Se insertan en una **cola con prioridad**, asignándoles un nivel de urgencia.

2. **Atención de pacientes:**  
   - El sistema toma al paciente con **mayor prioridad (menor número)**.  
   - Se asigna un **doctor de la cola circular**.  
   - Se **simula la atención durante 3 segundos**.  
   - Se **registra la atención** en el **arreglo dinámico (historial)**.

3. **Rotación de doctores:**  
   El doctor atendido vuelve al **final de la cola circular**.

4. **Visualización:**  
   Se puede **imprimir el historial completo** de atenciones realizadas.

## Instalación

Para instalar y ejecutar este proyecto, siga estos pasos:

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/abellol/Hospital-Management-System.git
   cd Hospital-Management-System/
   ```

2. **Crear y activar un entorno virtual (recomendado)**  
   - En Windows:  
     ```bash
     python -m venv my_venv
     venv\Scripts\activate
     ```
   - En macOS/Linux:  
     ```bash
     python -m venv my_venv
     source venv/bin/activate
     ```

3. **Instalar dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Ejecutar el código principal con:

```bash
python main.py
```

## Uso de las estructuras
---

| Estructura             | Propósito                                    | Ventajas                                     |
| ---------------------- | -------------------------------------------- | -------------------------------------------- |
| **Arreglo dinámico**   | Guardar historial de atenciones              | Crece automáticamente sin límite predefinido |
| **Cola circular**      | Rotar doctores disponibles                   | Asegura uso equilibrado de recursos          |
| **Cola con prioridad** | Atender primero a los pacientes más urgentes | Mejora la eficiencia del sistema             |



