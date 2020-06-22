from DAL.sqlRequest import SqlRequest, get, db_session
from DAL.database_store import Product


class ProductRequest(SqlRequest):
    db_class = Product

    def Get(self, item_id):
        return get(i for i in self.db_class if i.product_id == item_id)

