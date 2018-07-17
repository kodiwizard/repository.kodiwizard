import os
import sqlite3
import _strptime

try:
    import cPickle as pickle
except:
    import pickle 

from . import peewee
from .util import hash_6

db = peewee.SqliteDatabase(None, pragmas={'foreign_keys': 'on'})
MAX_INSERTS = 100

class HashField(peewee.TextField):
    def db_value(self, value):
        return hash_6(value)

class PickledField(peewee.BlobField):
    def db_value(self, value):
        if value != None:
            return sqlite3.Binary(pickle.dumps(value, pickle.HIGHEST_PROTOCOL))

    def python_value(self, value):
        if value != None:
            return pickle.loads(str(value))

class Model(peewee.Model):
    def __str__(self):
        return str(self.__data__)

    def __repr__(self):
        return str(self.id)

    @classmethod
    def schema(cls):
        _schema = []

        for field in cls._meta.sorted_fields:
            _schema.append(field.__dict__)

        return str(_schema)

    @classmethod
    def delete(cls, *args, **kwargs):
        super(Model, cls).delete().where(*args, **kwargs).execute()

    @classmethod
    def exists(cls, *args, **kwargs):
        try:
            return cls.select().where(*args, **kwargs).exists()
        except peewee.OperationalError:
            return False

    @classmethod
    def set(cls, *args, **kwargs):
        return super(Model, cls).replace(*args, **kwargs).execute()

    @classmethod
    def name(cls):
        return cls._meta.table_name

    def to_dict(self):
        data = {}

        for field in self._meta.sorted_fields:
            field_data = self.__data__.get(field.name)
            data[field.name] = field_data

        return data

    @classmethod
    def replace_many(cls, data):
        with db.atomic():
            for idx in range(0, len(data), MAX_INSERTS):
                super(Model, cls).replace_many(data[idx:idx+MAX_INSERTS]).execute()

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return self.__str__

    class Meta:
        database = db
        only_save_dirty = True

class App(Model):
    key       = HashField(primary_key=True)
    value     = PickledField(null=True)
    checksum  = HashField(null=True, index=True)
    group     = HashField(null=True, index=True)

    @classmethod
    def get(cls, *args, **kwargs):
        try:
            return super(App, cls).get(*args, **kwargs).value
        except App.DoesNotExist:
            return None

    def __str__(self):
        return str(self.__data__)

    def __repr__(self):
        return str(self.key)

    class Meta:
        table_name = '_app'

class Database(object):
    def __init__(self, db_path):
        self._db_path = db_path

    def connect(self):
        db.init(self._db_path)

        if self.is_open:
            return

        db.connect(reuse_if_open=True)

        self.check_table(App)
        self._connected = True

    @property
    def is_open(self):
        return not db.is_closed()

    def check_table(self, table):
        key       = 'tbl_{}'.format(table.name())
        checksum  = table.schema()

        if App.exists(App.key == key, App.checksum == checksum):
            return

        self.create_table(table)
        App.set(key=key, checksum=checksum)

    def clear(self):
        reconnect = self.is_open
        self.close()

        try:
            os.remove(self._db_path)
        except:
            pass

        if reconnect:
            self.connect()

    def create_table(self, table):
        db.drop_tables([table])
        db.create_tables([table])

    def close(self):
        if self.is_open:
            db.close()