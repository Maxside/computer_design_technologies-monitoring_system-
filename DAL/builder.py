from DAL.order import Order
from datetime import datetime

class OrderBuild:
    def __init__(self):
        self.order_id = None
        self.date_created = None
        self.date_shipped = False
        self.status = "Новий"
        self.oversized_cargo = "Габаритний"

    @staticmethod
    def item():
        return OrderBuild()
    
    def withOrderId(self, order_id):
        self.order_id = order_id
        return self
        
    def withDateCreated(self):
        self.date_created = datetime.now().strftime("%d/%m/%Y, %H:%M")
        return self

    def withDateShipped(self, date_shipped):
        self.date_shipped = date_shipped
        return self

    def withStatus(self, status):
        self.status = status
        return self
    
    def withOversizedCargo(self, oversized_cargo):
        self.oversized_cargo = oversized_cargo
        return self

    def build(self):
        return Order(self.order_id,
                     self.date_created,
                     self.date_shipped,
                     self.status,
                     self.oversized_cargo)           



