import threading
import os
from datetime import datetime
from Pedido import Pedido
from Cocinero import Cocinero

class Cocina:
    ARCHIVO_LOG = "log_pedidos.txt"
    
    @staticmethod
    def inicializar_log():
        try:
            # Eliminar archivo si existe
            if os.path.exists(Cocina.ARCHIVO_LOG):
                os.remove(Cocina.ARCHIVO_LOG)
            
            # Crear archivo con encabezado
            with open(Cocina.ARCHIVO_LOG, 'w', encoding='utf-8') as archivo:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                archivo.write(f"=== LOG DE PEDIDOS - INICIO: {timestamp} ===\n\n")
        except IOError as e:
            print(f"Error al inicializar el log: {e}")
    
    @staticmethod
    def main():
        # Inicializar el archivo log
        Cocina.inicializar_log()
        
        # Crear lista de pedidos compartida
        lista_pedidos = [
            Pedido(1, "Paella Valenciana"),
            Pedido(2, "Tortilla de Patatas"),
            Pedido(3, "Gazpacho Andaluz"),
            Pedido(4, "Pulpo a la Gallega"),
            Pedido(5, "Croquetas de Jamón"),
            Pedido(6, "Fabada Asturiana")
        ]
        
        # Lock para proteger la lista de pedidos
        lock_lista = threading.Lock()
        
        print("=== INICIO DEL SERVICIO EN LA COCINA ===")
        print(f"Total de pedidos: {len(lista_pedidos)}")
        print("=========================================\n")
        
        # Crear cocineros (hilos)
        cocinero1 = Cocinero("Cocinero 1", lista_pedidos, lock_lista)
        cocinero2 = Cocinero("Cocinero 2", lista_pedidos, lock_lista)
        cocinero3 = Cocinero("Cocinero 3", lista_pedidos, lock_lista)
        
        # Iniciar los hilos
        cocinero1.start()
        cocinero2.start()
        cocinero3.start()
        
        # Esperar a que todos los cocineros terminen
        cocinero1.join()
        cocinero2.join()
        cocinero3.join()
        
        # Mensaje final
        print("\n=========================================")
        print("Todos los pedidos han sido procesados.")
        print("=========================================")


if __name__ == "__main__":
    Cocina.main()
