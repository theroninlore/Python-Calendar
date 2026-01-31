# Python-Calendar

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)


```diff
+   ██████╗░░█████╗░██╗░░░░░███████╗███╗░░██╗██████╗░░█████╗░██████╗░██╗░█████╗░
+  ██╔════╝░██╔══██╗██║░░░░░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗
+  ██║░░░░░░███████║██║░░░░░█████╗░░██╔██╗██║██║░░██║███████║██████╔╝██║██║░░██║
+  ██║░░░░░░██╔══██║██║░░░░░██╔══╝░░██║╚████║██║░░██║██╔══██║██╔══██╗██║██║░░██║
+  ╚██████╗░██║░░██║███████╗███████╗██║░╚███║██████╔╝██║░░██║██║░░██║██║╚█████╔╝
+  ░╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░
```


Este proyecto es un sistema de gestión de eventos por terminal que contiene funciones como añadir evento, eliminar evento, modificar evento, consultar calendario y buscar evento. Para conseguir alcanzar mis objetivos del proyecto he tenido que usar diccionarios, listas, bucles, excepciones... Una de los mayores retos ha sido la **Programación Orientada a Objetos**.

>[!NOTE]
> Lo que ocupa casi todo el código son todas las excepciones y validaciones que hago a las entradas para poder evitar entradas inesperadas por parte del usuario.

###  **Conocimientos adquiridos**

En este proyecto he aprendido a como trabajar con **diccionarios y objetos**. También he aprendido a como realcionar **tipos de datos** y trabajar con **excepciones**.
Es mi primer proyecto en el que trabajo con diccionarios y objetos,  a esto se debe que el código este tan comentado.

---

### **Instalación**

1. **Clona el repositorio**
  ```bash
   git clone [https://github.com/theroninlore/Pytthon-Calendar.git](https://github.com/theroninlore/Python-Calendar.git)
  ```
2.  Instala las dependencias:
  ```bash
   pip install colorama
  ```

---

###  **Funcionalidades**

✅ **Añadir Eventos**: Validación de días según el mes y año bisiesto.

🔍 **Buscador Inteligente**: Encuentra eventos por coincidencia de nombre en todo el año.

📝 **Modificación Flexible**: Cambia nombre, hora o descripción usando métodos de clase.

💾 **Persistencia: Los datos** se guardan en calendario.json al salir.
