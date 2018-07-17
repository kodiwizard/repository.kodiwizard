from time import time

from . import config
from .util import _NOARG
from .models import App

class Cache(object):
    def __init__(self, group='_cache', checksum=None):
        self._group    = group
        self._checksum = checksum

        self._cache = App.get(App.key == self._group, App.checksum == checksum)
        if self._cache == None:
            self.wipe()
        elif self._cache:
            self.clean()

    def wipe(self):
        self._cache = {}
        App.delete(App.group == self._group)
        try:
            App._meta.database.execute_sql('VACUUM FULL')
        except:
            pass

    def clean(self):
        _time = time()
        _deletes = []

        for key in self._cache.keys():
            expires = self._cache[key]
            if expires and _time > expires:
                _deletes.append(key)
                self._cache.pop(key)

        if _deletes:
            App.delete(App.key << _deletes)

    def get(self, key, default=None):
        try:
            if key not in self._cache:
                raise App.DoesNotExist

            # Used one shot. Set expiry to 1 second
            if self._cache[key] == 0:
                self._cache[key] = 1

            return App.get(App.key == key, App.group == self._group)
        except App.DoesNotExist:
            if default == _NOARG:
                raise

        return default

    #expires 0 = 1 shot, None = No expiry, int = seconds
    def set(self, key, value, expires=_NOARG):
        if expires == _NOARG:
            expires = config.DEFAULT_EXPIRY

        if expires:
            expires = int(time() + expires)

        self._cache[key] = expires
        App.set(key=key, value=value, group=self._group)

    def function(self, key, func, **kwargs):
        value = self.get(key, default=func)

        if value == func:
            value = func()
            self.set(key, value, **kwargs)

        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key, default=_NOARG)

    def save(self):
        App.set(key=self._group, value=self._cache, checksum=self._checksum)