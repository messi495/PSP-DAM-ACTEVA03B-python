# PSP-DAM-ACTEVA03B-python
Simulación de cocina con hilos en Python
Este proyecto simula el trabajo de una cocina de restaurante usando hilos en Python. Varios cocineros comparten una lista de pedidos, los van sacando de forma segura y registran el trabajo en un archivo de log.

## Descripción general
Cocina crea una lista de Pedido y arranca 3 hilos Cocinero.

Cada Cocinero toma pedidos de la lista compartida usando un Lock para evitar condiciones de carrera.

El cocinero “prepara” el pedido durante un tiempo aleatorio entre 1 y 3 segundos.

Cada pedido procesado se muestra por consola y se registra en el archivo log_pedidos.txt con marca de tiempo.

El programa termina cuando no quedan pedidos y todos los hilos han finalizado.

## Estructura de archivos
pedido.py

Clase Pedido:

Atributos: id, nombre_plato.

Métodos:

get_id()

get_nombre_plato()

__str__(): devuelve Pedido #id: nombre_plato.

Cocinero.py

Clase Cocinero que hereda de threading.Thread.

## Atributos:

nombre

lista_pedidos (lista compartida)

lock_lista (para proteger la lista)

Atributos de clase:

ARCHIVO_LOG = "log_pedidos.txt"

lock_archivo (para sincronizar escrituras en el log)

## Métodos principales:

run():

En bucle, intenta obtener un pedido de lista_pedidos dentro de un with lock_lista.

Si no quedan pedidos, sale del bucle.

Si obtiene uno, llama a preparar_pedido(pedido).

## preparar_pedido(pedido):

Imprime que está preparando el pedido.

Duerme entre 1 y 3 segundos (time.sleep con un número aleatorio).

Imprime que ha completado el pedido.

Llama a registrar_en_log(pedido).

## registrar_en_log(pedido):

Usa with Cocinero.lock_archivo para que solo un hilo escriba en el log a la vez.

Abre log_pedidos.txt en modo append.

Escribe una línea con fecha, hora, nombre del cocinero y pedido.

Cocina.py

Clase Cocina.

## Constante de clase:

ARCHIVO_LOG = "log_pedidos.txt".

Métodos estáticos:

inicializar_log():

Si el archivo existe, lo borra.

Crea uno nuevo con una cabecera y la fecha/hora de inicio.

main():

Llama a inicializar_log().

Crea la lista de pedidos (Pedido(1, "Paella Valenciana"), etc.).

Crea un Lock (lock_lista) para proteger la lista de pedidos.

Muestra por consola el inicio del servicio y el número total de pedidos.

Crea 3 cocineros (Cocinero 1, Cocinero 2, Cocinero 3) pasando la misma lista y el mismo lock.

Llama a start() en cada hilo.

Espera a que terminen con join().

Muestra un mensaje final indicando que todos los pedidos han sido procesados.

## Bloque principal:

Si el archivo se ejecuta directamente (if __name__ == "__main__":), llama a Cocina.main().

Requisitos
Python 3.x.

## Archivos:

Cocina.py

Cocinero.py

pedido.py

Todos en el mismo directorio o correctamente importables.

Ejecución
En la terminal, desde el directorio del proyecto:

bash
python Cocina.py
Verás en consola:

Inicio del servicio en la cocina.

Qué cocinero está preparando y completando cada pedido.

Mensaje final cuando no quedan pedidos.

En el archivo log_pedidos.txt se registran:

Marca de tiempo.

Nombre del cocinero.

Pedido procesado.
