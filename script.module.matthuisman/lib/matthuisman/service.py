import xbmc, xbmcaddon

class Service(object):
    def run(self, poll_time):
        addon = xbmcaddon.Addon()
        monitor = xbmc.Monitor()
        cmd = 'XBMC.RunPlugin(plugin://{0}?_route=service)'.format(addon.getAddonInfo('id'))

        while not monitor.abortRequested():
            xbmc.executebuiltin(cmd)
            if monitor.waitForAbort(poll_time):
                break