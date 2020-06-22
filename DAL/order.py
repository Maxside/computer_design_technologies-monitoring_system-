class Order:
    def __init__(self, order_id, date_created, date_shipped, status,
                oversized_cargo):
        self.order_id = order_id
        self.date_created = date_created
        self.date_shipped = date_shipped
        self.status = status
        self.oversized_cargo = oversized_cargo
        
    def getOrderId(self):
        return self.order_id
    
    def setOrderId(self, order_id):
        self.order_id = order_id

    def getDateCreated(self):
        return self.date_created

    def setDateCreated(self, date_created):
        self.date_created = date_created

    def getDateShipped(self):
        return self.date_shipped

    def setDateShipped(self, date_shipped):
        self.date_shipped = date_shipped

    def getStatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    
    def getOversizedCargo(self):
        return self.oversized_cargo

    def setOversizedCargo(self, oversized_cargo):
        self.oversized_cargo = oversized_cargo
    
    def print(self):
        print("=====Order #{}=====".format(self.order_id))
        print("Дата замовлення:", self.date_created)
        if self.date_shipped:print("Дата доставлення:", self.date_shipped)
        print("Статус замовленяя:", self.status)
        print("Тип товару:", self.oversized_cargo)