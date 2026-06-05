# Proyecto final - Calculadora con Tkinter y Python 
### Este proyecto es una calculadora interactiva desarrollada con Python y la libreria Tkinter para la interfaz grafica. Se hizo respetando el paradigma de programacion estructurada (sin POO) utilizando funciones, variables y estructuras de control claras y modulares.

## ¿QUE HACE EL PROGRAMA?
### El programa funciona como una calculadora capaz de resolver operaciones basicas e incluso largas respetando un poco la jerarquia de operaciones de numeros enteros, sus caracteristicas principales incluyen:

**1.-Operaciones Fundamentales:** Suma resta multiplicacion y division
**2.-Evaluacion de expresiones:** Capacidad de recibir cadenas largas como ejemplo (7*3+2-8/6) y resolverlas mediante un algoritmo hecho con manipulacion de listas 
**3.-Memoria inteligente(ANS):** Guarda automaticamente el resultado de la ultima operacion para que si el usuario desea usarla en un posterior calculo lo pueda hacer sin ningun problema
**4.-Sistema de borrad:** Incluye limpieza total de la pantalla con "C" y borrado digito por digito con "Borrar"
**5.-Persistencia de datos:** Genera automaticamente un historial con las operaciones hechas por el usuario ademas de que si el usuario quiere tiene la opcion de "Ver historial" para ver las operaciones que haya hecho con la calculadora a traves de un cuadro emergente 
**6.-Proteccion contra errores:** Implementacion de bloques try/except y validaciones logics para evitar que el programe de un error ya sea por divisiones entre cero o errores de sintaxis por parte del usuario

## ¿COMO EJECUTAR EL PROGRAMA Y USARLO?
## Para probar esta calculadora en tu computadora sigue los siguientes pasos

**1.-** Aegurate de tener **Python** instalado en tu sistema
**2.-** Desacarga el archivo "CALCULADORA.py" en una carpeta de tu preferencia
**3.-** Ejecuta el archivo desde un IDE de preferencia Visual Studio Code o dando doble click sobre el archivo
**4.-** USA LA CALCULADORA: Ingresa las operaciones matematicas y presiona el boton de **=** para obtener resultados, utiliza **C** para borrar todo lo que hay en la pantalla, utiliza **Borrar** para borra un digito ya sea un numero u operador que pusiste y no querias ponerlo, y tambien puedes usar el boton **ANS** para que la calculadora te muestre el resultado de una operacion anterior (cada que haces una operacion ANS se actualiza a ese resultado).
**5.-** Presiona el boton de **Ver Historial** en la parte de abajo para comprobar como el programa genera y lee el archivo "HISTORIAL.txt" automaticamente


## ¿QUE PARTES DEL CODIGO IMPLEMENTE ?
### Implemente la totalidad de la estructura del proyecto con ayuda de documentacion de paginas webs con los comandos de Tkinter para asi asegurarme de comprender cada linea de codigo y asi poder evitar usar funciones desconocidas por mi, complejas o no vistas durante las clases para favorecer una logica clara y amigable, especificamente desarrolle:

**1.-La logica Matematica:** Las funciones base de las cuatro operaciones y la validacion para bloquear la division entre cero
**2.-La interfaz grafica:** El diseño visual en tkinter, la cuadricula (grid) de los botones, la paleta de colores inspirandome en una calculadora que tengo desde la peparatoria y la integracion de alertas para los errores
**3.-El manejo de archivos:** Las funciones exclusivas de guardar_datos y cargar_datos para manejar el flujo de lectura y escritura del archivo tipo .txt de manera segura y asegurandome que no hubiera fallos al momento de la ejecucion
**4.-La modularidad:** la separacion del codigo en bloques de codigo como si fuesen "cajas" para mantener el archivo limpio y ordenado

## ¿QUE APRENDI DURANTE EL DESARROLLO?
### Durante el desarrollo de la calculadora aprendi mas sobre la logica de programacion el como se comportan los datos y un poquito mas sobre la recursividad de las funciones el como unas funciones pueden llamar a otras funciones para ejecutar con exito el programa, ademas aprendi sobre como la modularidad hace que nuestro codigo se vea un poco mas limpio y mas sencillo de entender, tambien cabe reslatar que comprendi como usar el manejo de persistencia de datos y para que nos puede servir en futuros programas hechos por mi, aprendi sobre el control de flujo y la jerarquia y el manejo de errores para que nuestro programa corra bien y atrape esos errores y sepa que hacer con ellos no afectando el codigo, una de las cosas que mas destacan en mi aprendizaje es que aprendi los comando basicos de git y github y el como tener un control de versiones es beneficioso para nosotros 

## DESPEDIDA Y AGRADECIMIENTO:
### Este proyecto representa la culminacion de todo el esfuerzo y el aprendizaje de este semestre, fue todo un reto lo eh de admitir pero me enorgullece haberlo terminado, quiero agradecer a mi maestra de Introduccion a la programacion por haberme dado estos conocimientos y poner los cimientos en mi futuro.

*(Notas adicionales: La calculadora utiliza enteros "int" es decir si por alguna razon en una division ejemplo se coloca 15 / 2 la calculadora mostarara como resultado 7 ya que esta construida con puros numreros enteros ya que se evito el uso de los decimales o "float")*