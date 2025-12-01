import threading
import time
import random
from datetime import datetime

class Cocinero(threading.Thread):
    ARCHIVO_LOG = "log_pedidos.txt"
    lock_archivo = threading.Lock()  # Lock para el archivo
    
    def __init__(self, nombre, lista_pedidos, lock_lista):
        super().__init__()
        self.nombre = nombre
        self.lista_pedidos = lista_pedidos
        self.lock_lista = lock_lista
    
    def run(self):
        while True:
            pedido = None
            
            # Sincronización para acceder a la lista de pedidos
            with self.lock_lista:
                if len(self.lista_pedidos) > 0:
                    pedido = self.lista_pedidos.pop(0)
                else:
                    break  # No hay más pedidos
            
            if pedido is not None:
                self.preparar_pedido(pedido)
    
    def preparar_pedido(self, pedido):
        # Mostrar en consola
        mensaje = f"{self.nombre} está preparando {pedido}"
        print(mensaje)
        
        # Simular tiempo de preparación (entre 1 y 3 segundos)
        tiempo_preparacion = random.random() * 2 + 1
        time.sleep(tiempo_preparacion)
        
        mensaje_completado = f"{self.nombre} ha completado {pedido}"
        print(mensaje_completado)
        
        # Registrar en el archivo (sincronizado)
        self.registrar_en_log(pedido)
    
    def registrar_en_log(self, pedido):
        # Sincronizar el acceso al archivo
        with Cocinero.lock_archivo:
            try:
                with open(Cocinero.ARCHIVO_LOG, 'a', encoding='utf-8') as archivo:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro = f"[{timestamp}] {self.nombre} procesó {pedido}\n"
                    archivo.write(registro)
            except IOError as e:
                print(f"Error al escribir en el log: {e}")