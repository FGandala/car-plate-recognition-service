class BoudingBox:
    """Representa uma caixa delimitadora (bounding box) em um sistema de coordenadas 2D."""
    def __init__(self,x1:int , y1:int , x2:int, y2:int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        pass