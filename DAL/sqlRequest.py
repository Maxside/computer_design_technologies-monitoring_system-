from pony.orm import select, db_session, get


class SqlRequest:
    db_class = None

    def GetAll(self):
        return self.db_class.select()[:]

    def Get(self, item_id):
        return get(i for i in self.db_class if i.id == item_id)

    def Find(self, tag):
        return list(select(i for i in self.db_class).filter(tag))

    def Update(self, obj, **kwargs):
        for arg, value in kwargs.items():
            if hasattr(obj, arg):
                setattr(obj, arg, value)

    def Create(self, **kwargs):
        return self.db_class(**kwargs)

    def Delete(self, obj):
        obj.delete()

