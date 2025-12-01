# =====================================================
# ARCHIVO 1: pedido.py
# =====================================================

class Pedido:
    def __init__(self, id, nombre_plato):
        self.id = id
        self.nombre_plato = nombre_plato
    
    def get_id(self):
        return self.id
    
    def get_nombre_plato(self):
        return self.nombre_plato
    
    def __str__(self):
        return f"Pedido #{self.id}: {self.nombre_plato}"
