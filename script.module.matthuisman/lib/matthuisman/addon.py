import os

import xbmc, xbmcaddon

from .models import Database, App
from .cache import Cache

class Addon(object):
    _data_key = '_data'

    def __init__(self, addon_id=''):
        self.addon      = xbmcaddon.Addon(addon_id)
        self.id         = self.addon.getAddonInfo('id')
        self.name       = self.addon.getAddonInfo('name')
        self.version    = self.addon.getAddonInfo('version')

        self.path       = xbmc.translatePath(self.addon.getAddonInfo('path')).decode("utf-8")
        self.profile    = xbmc.translatePath(self.addon.getAddonInfo('profile')).decode("utf-8")   

        self._settings  = Settings(self.addon)
        self._first_run = False
        
        if not self._settings.getBool('_init'):
            self._first_run = True
            self._settings.setBool('_init', True)

        self._db        = Database(os.path.join(self.profile, 'data.db'))
        self._data      = None
        self._cache     = None

    def __str__(self):
        return self.id

    def save(self):
        if self._data:
            App.set(key=self._data_key, value=self._data)

        if self._cache:
            self._cache.save()

    def close(self):
        self.save()
        self._data = None
        self._cache = None
        self._db.close()

    def clear(self):
        if self._data:
            self._data.clear()
        self._db.clear()

    @property
    def first_run(self):
        return self._first_run

    @property
    def settings(self):
        return self._settings

    @property
    def db(self):
        self._db.connect()
        return self._db

    @property
    def data(self):
        if self._data == None:
            self._db.connect()
            self._data = App.get(key=self._data_key) or {}

        return self._data

    @property
    def cache(self):
        if not self._cache:
            self._db.connect()
            self._cache = Cache(checksum=self.version)

        return self._cache

class Settings(object):
    def __init__(self, addon):
        self._addon = addon

    def getInt(self, key):
        return int(self.get(key))

    def getBool(self, key):
        return self.get(key).lower() == 'true'

    def setBool(self, key, value=False):
        self.set(key, 'true' if value else 'false')

    def set(self, key, value):
        self._addon.setSetting(key, str(value))

    def get(self, key, default=''):
        return self._addon.getSetting(key) or default

    def open(self):
        self._addon.openSettings()