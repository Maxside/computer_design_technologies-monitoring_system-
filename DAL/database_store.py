from pony.orm import Database, PrimaryKey, Required, Optional, select, commit, db_session
from pony.orm.ormtypes import datetime

db = Database()
db.bind(provider='sqlite', filename='database_store.db')

# db.drop_table("Product", if_exists=True, with_all_data=True)

class Product(db.Entity):
    product_id = PrimaryKey(int, auto=True)
    name = Required(str, unique = True)
    quantity = Required(int)

    def __str__(self):
        return f"Product id[{self.product_id}] name: {self.name}"

    
    

db.generate_mapping(create_tables=True)


# @db_session
# def create_entities():
#     # temp = Product(name = "Ноутбук ASUS ROG X502", quantity = 20 )
#     # temp2 = Product(name = "Ноутбук LENOVO IdeaPad500s", quantity = 20 )
#     # for p in Product.select(lambda p: p.quantity > 4):
#     #     print(p.name, p.quantity)

    

# create_entities()



