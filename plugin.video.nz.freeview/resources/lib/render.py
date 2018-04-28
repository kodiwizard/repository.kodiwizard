import config

if config.KODI:
    import os, sys, xbmcgui, xbmc, xbmcplugin

class Render(object):
    @staticmethod
    def get_render():
        if config.KODI:
            return KodiRender()
        else:
            return Render()

    def play(self, data):
        print(data['url'])
        with open('out.strm', "w") as f:
            f.write(data['url'])

    def items(self, items):
        for item in items:
            print(item)

    def notifcation(self, message):
        print("NOTIFCATION: %S" % message)

class KodiRender(Render):
    def __init__(self):
        self._handle = int(sys.argv[1])

    def notifcation(self, message):
        dialog = xbmcgui.Dialog()
        dialog.notification(config.__addonname__, message, os.path.join(xbmc.translatePath(config.__addon__.getAddonInfo('path')).decode("utf-8"), 'icon.png'), 3000)

    def play(self, data):
        li = self._create_list_item(data)
        xbmcplugin.setResolvedUrl(self._handle, True, li)

    def _create_list_item(self, data):
        li = xbmcgui.ListItem(data.get('title'))
        li.setPath(data.get('url'))

        if data.get('playable', False):
            li.setProperty('IsPlayable', 'true')

        li.setArt(data.get('images', {}))
        li.setInfo('video', data.get('info',{}))
        li.addStreamInfo('video', data.get('video',{}))
        li.addStreamInfo('audio', data.get('audio',{}))

        contexts = []
        for context in data.get('context', []):
            contexts.append( (context[0], "XBMC.RunPlugin({0})".format(context[1]),) )

        li.addContextMenuItems(contexts)
        return li

    def items(self, items):
        listings = []
        for item in items:
            li = self._create_list_item(item)
            is_folder = item.get('is_folder', True) and not item.get('playable', False)
            xbmcplugin.addDirectoryItem(self._handle, item.get('url'), li, is_folder)

        xbmcplugin.endOfDirectory(self._handle)