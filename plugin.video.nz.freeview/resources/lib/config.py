from matthuisman import globs as g
from matthuisman.config import Config as BaseConfig

class Config(BaseConfig):
    def __init__(self, addon_id=''):
        super(Config, self).__init__(addon_id)
        self.M3U8_FILE = 'http://iptv.matthuisman.nz/nz/tv.json'

g.config = Config()