import os

from matthuisman import plugin, gui, cache, settings, userdata, signals, inputstream
from matthuisman.constants import ADDON_PATH
from matthuisman.log import log

from .api import API
from .language import _

api = API()

@signals.on(signals.BEFORE_DISPATCH)
def before_dispatch():
    api.new_session()
    plugin.logged_in = api.logged_in

@plugin.route('')
def home():
    folder = plugin.Folder()

    if not api.logged_in:
        folder.add_item(label=_(_.LOGIN, _bold=True), path=plugin.url_for(login))
    else:
        folder.add_item(label=_(_.TRACKSIDE_1, _bold=True), path=plugin.url_for(play, type='channel', id='TS1', is_live=True), playable=True)
        folder.add_item(label=_(_.TRACKSIDE_2, _bold=True), path=plugin.url_for(play, type='channel', id='TS2', is_live=True), playable=True)
        folder.add_item(label=_(_.LIVE_NOW, _bold=True), path=plugin.url_for(live_now))
        folder.add_item(label=_.LOGOUT, path=plugin.url_for(logout))

    folder.add_item(label=_.SETTINGS, path=plugin.url_for(plugin.ROUTE_SETTINGS))

    return folder

@plugin.route()
def login():
    while not api.logged_in:
        username = gui.input(_.ASK_USERNAME, default=userdata.get('username', '')).strip()
        if not username:
            break

        userdata.set('username', username)

        password = gui.input(_.ASK_PASSWORD, default=cache.get('password', '')).strip()
        if not password:
            break

        cache.set('password', password, expires=60)

        try:
            api.login(username=username, password=password)
        except Exception as e:
            gui.ok(_(_.LOGIN_ERROR, error_msg=e))

    cache.delete('password')
    gui.refresh()

@plugin.route()
def logout():
    if not gui.yes_no(_.LOGOUT_YES_NO):
        return

    cache.empty()
    api.logout()
    gui.refresh()

@plugin.route()
def play(type, id):
    url = api.access(type, id)
    return plugin.Item(path=url, inputstream=inputstream.HLS(), art=False)

@plugin.route()
def live_now():
    folder = plugin.Folder(title=_.LIVE_NOW)

    events = api.live_now()
    for event in events:
        folder.add_item(
            label = event['name'],
            path  = plugin.url_for(play, type='event', id=event['id'], is_live=True),
            playable = True,
        )

    if not folder.items:
        folder.add_item(label=_(_.NO_GAMES, _label=True), is_folder=False)

    return folder