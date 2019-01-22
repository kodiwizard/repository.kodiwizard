from matthuisman import userdata
from matthuisman.session import Session

from .constants import HEADERS

class API(object):
    def new_session(self):
        self.logged_in = False

        self._session = Session(HEADERS)
        self.set_authentication(userdata.get('authentication'))

    def set_authentication(self, authentication):
        if not authentication:
            return

        self._session.headers.update({'authentication': authentication, 'x-ob-channel': 'I', 'x-ob-session': self._session.cookies['OB-SESSION']})
        self.logged_in = True

    def login(self, username, password):
        data = {
            "username": username,
            "password": password
        }

        data = self._session.post('https://auth.tab.co.nz/identity-service/api/v1/assertion/by-credentials', json=data).json()
        authentication = data['data']['ticket']
        
        if not authentication:
            raise Exception('Failed to login')

        userdata.set('authentication', authentication)

        self._session.save_cookies()
        self.set_authentication(authentication)

    def reauthorise(self):
        data = self._session.post('https://auth.tab.co.nz/identity-service/api/v1/assertion/by-token').json()

        authentication = data['data']['ticket']
        userdata.set('authentication', authentication)

        self._session.save_cookies()
        self.set_authentication(authentication)

    def access(self, type, id):
        self.reauthorise()

        url = 'https://api.tab.co.nz/sports-service/api/v1/streams/access/{}/{}'.format(type, id)
        data = self._session.post(url).json()
        return data['data'][0]['streams'][0]['accessInfo']['contentUrl']

    def live_now(self):
        data = self._session.get('https://content.tab.co.nz/content-service/api/v1/q/event-list?liveNow=true&hasLiveStream=true').json()
        return data['data']['events']

    def logout(self):
        userdata.delete('authentication')
        self._session.clear_cookies()
        self.new_session()