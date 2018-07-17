from time import time

from .addon import Addon
from .view import View
from .router import Router
from .util import log

from .exceptions import InputError, ServiceError

class Controller(object):
    def __init__(self, base_url, handle):
        self._addon    = Addon()
        self._router   = Router(base_url, self, default=self.home)
        self._view     = View(self._addon, handle)

    def run(self, route):
        _start = time()

        try:
            self._router(route)
        except InputError:
            pass
        except ServiceError as e:
            log.exception(e)
        except Exception as e:
            log.exception(e)
            self._view.dialog(str(e), type(e).__name__)
        finally:
            self._close()
            log.debug("Time Taken: {}".format(time() - _start))

    def _close(self):
        #need to work out way to close addon before any view stuff
        self._view.close()
        self._addon.close()

    def service(self, params):
        try:
            log.debug('SERVICE!')
        except Exception as e:
            raise ServiceError(e)

    def home(self, params):
        items = [
            {'title':'Home', 'url': self._router.get(self.home)},
            {'title':'Clear Data', 'url': self._router.get(self.clear)},
            {'title':'Service', 'url': self._router.get(self.service)},
        ]

        # count = self._addon.cache.get('count', 0)

        # count += 1
        # self._addon.cache.set('count', count, 0)
        # self._addon.cache.set('count2', count+1)
        # self._addon.cache.set('count3', count+2)
        # print(self._addon.cache['count'])
        # print(self._addon.cache['count2'])
        # print(self._addon.cache['count3'])

        # items.append(
        #     {'title': self._addon.cache['test']},
        # )

        # key = 'test'
        # checksum = count

        # if self._addon.db.check(key, checksum=checksum):
        #     print("OK!")
        # else:
        #     print("NO!")
        #     self._addon.db.set(key, checksum=checksum)
        #     if self._addon.db.check(key, checksum=checksum):
        #         print("NOW OK")

    #    count = 1
   #     checksum = 2
       # db = self._addon.db

        # count = db.get('count', default=0, checksum=checksum)
        # db.set('count', value=count+1, checksum=checksum)
        # print(count)

        # count = self._addon.data.get('count', 0)
        # print(count)

     #   self._addon.clear()

        # count = self._addon.data.get('count', 0)
        # print(count)
        # self._addon.data['count'] = count + 1
        
        cache = self._addon.cache
      #  print(cache['10000'])
        # for i in range(10000):
        #     cache[str(i)] = i
 
       # print(count)
        # print(count)
        count = cache.get('count', 0)
        count += 1
        cache.set('count', count)
        print(count)
        # count = cache.get('count2', 0)
        # count += 1
      #  cache.set('count', count)
        # print(count)


        # data = self._addon.data
        # if not data.get('100000'):
        #     print("GENERATE!")
        #     for i in range(100001):
        #         data[str(i)] = i

        # print(data['100000'])


     #   count = self._addon.db.get('count', 0)
       # db.set('count', blob=count+1)
       # self._addon.db.set('blob2', value='test5')
        #print(self._addon.db.pop('count', None))
       # del self._addon.db['count']
        
        #count = self._addon.data.get('count', 0) + 1
        # self._addon.data['count'] = count
        # self._addon.data['new'] = 'HELLO!!'

        # print(self._addon.data['new'])

        # items.append(
        #     {'title': count},
        # )

      #  self._view.items(items, title='Home', cache=False)

        self._view.play({'url':'test', 'vid_type': 'widevine',  'vid_key': '123'})
        # if self._view.dialog_yes_no("Play?", heading=self._addon.name, yeslabel="Play", nolabel="Cancel"):
        #     log("PLAY!")

        # if self._view.dialog("OK?", heading=self._addon.name):
        #     log("OK!")

    def settings(self, params):
        self._addon.close()
        self._addon.settings.open()

    def clear(self, params):
        self._addon.clear()
        self._view.notification('Data cleared')

    def dialog(self, params):
        self._view.dialog(params.get('message'), heading=params.get('heading'))