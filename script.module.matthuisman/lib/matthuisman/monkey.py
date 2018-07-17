import io, json, os
import traceback
from collections import defaultdict
import xml.etree.ElementTree as ET

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs

def _func_print(name, locals):
    locals.pop('self')
    print("{}: {}".format(name, locals))


## xbmc ##

def log(msg, level=xbmc.LOGDEBUG):
    print(msg)

def getInfoLabel(cline):
    return {
        'System.BuildVersion': '18.0.1',
    }.get(cline, "")

def executebuiltin(function, wait=False):
    print("XBMC Builtin: {}".format(function))

def translatePath(path):
    return path

def getCondVisibility(condition):
    print("Get visibility condition: {}".format(condition))
    return False

def Player_play(self, item="", listitem=None, windowed=False, startpos=-1):
    _func_print('Play', locals())

xbmc.log               = log
xbmc.getInfoLabel      = getInfoLabel
xbmc.executebuiltin    = executebuiltin
xbmc.translatePath     = translatePath
xbmc.getCondVisibility = getCondVisibility
xbmc.Player.play       = Player_play


## xbmcaddon ##

import sys

def Addon_init(self, id=None):
    if not id:
        id = os.path.basename(os.path.realpath('.'))

    path = os.path.realpath("../{0}/".format(id))

    self._info = {
        'id': id,
        'path': path,
        'name': id,
        'profile': os.path.join(path, '_tmp'),
        'version': 'X',
    }
    self._settings = {}

    try:
        tree = ET.parse(os.path.join(path, 'addon.xml'))
        root = tree.getroot()
        for key in root.attrib:
            self._info[key] = root.attrib[key]
    except:
        pass

    try:
        tree = ET.parse(os.path.join(path, 'resources', 'settings.xml'))
        root = tree.getroot()
        for child in root:
            if 'id' in child.attrib:
                self._settings[child.attrib['id']] = child.attrib.get('default')
    except:
        pass

    try:
        with io.open(os.path.join(self._info['profile'], 'settings.json'), 'r', encoding='utf-8') as f:
            self._settings.update(json.loads(f.read()))
    except:
        pass

    if id == 'inputstream.adaptive':
        self._info.update({
            'version': '2.1.0',
        })

        self._settings.update({
            'DECRYPTERPATH': self._info['profile'],
        })

def Addon_getSetting(self, id):
    return str(self._settings.get(id, ""))

def Addon_setSetting(self, id, value):
    self._settings[str(id)] = str(value)

    if not os.path.exists(self._info['profile']):
        os.mkdir(self._info['profile'])

    with io.open(os.path.join(self._info['profile'], 'settings.json'), 'w', encoding='utf8') as f:
        f.write(unicode(json.dumps(self._settings, separators=(',',':'), ensure_ascii=False)))

def Addon_getAddonInfo(self, id):
    return self._info.get(id, "")

xbmcaddon.Addon.__init__     = Addon_init
xbmcaddon.Addon.getSetting   = Addon_getSetting
xbmcaddon.Addon.setSetting   = Addon_setSetting
xbmcaddon.Addon.getAddonInfo = Addon_getAddonInfo


## xbmcgui ##

def Dialog_yesno(self, heading, line1, line2="", line3="", nolabel="N", yeslabel="Y", autoclose=0):
    return raw_input("{}: {} {} {}\n{}/({}): ".format(heading, line1, line2, line3, yeslabel, nolabel)).strip().lower() == yeslabel.strip().lower()

def Dialog_ok(self, heading, line1, line2="", line3=""):
    return (raw_input("{}: {} {} {}\n(OK): ".format(heading, line1, line2, line3)).strip().lower() or 'ok') == 'ok'

def Dialog_notification(self, heading, message, icon="", time=0, sound=True):
    _func_print('Notification', locals())

def Dialog_input(self, heading, defaultt="", type=0, option=0, autoclose=0):
    return raw_input('{0} ({1}): '.format(heading, defaultt)).strip() or defaultt

def DialogProgress_create(self, heading, line1="", line2="", line3=""):
    print('Progress: {} {} {} {}'.format(heading, line1, line2, line3))

def ListItem_init(self, label="", label2="", iconImage="", thumbnailImage="", path=""):
    self._data = defaultdict(dict)
    _locals = locals()
    _locals.pop('self')
    self._data.update(_locals)

def ListItem_setArt(self, dictionary):
    self._data['art'] = dictionary

def ListItem_setInfo(self, type, infoLabels):
    self._data['info'][type] = infoLabels

def ListItem_addStreamInfo(self, cType, dictionary):
    self._data['stream_info'][cType] = dictionary

def ListItem_addContextMenuItems(self, items, replaceItems=False):
    self._data['context'] = items

def ListItem_setProperty(self, key, value):
    self._data['property'][key] = value

def ListItem_setPath(self, path):
    self._data['path'] = path

def ListItem_getPath(self):
    return self._data.get('path', '')

def ListItem_str(self):
    return json.dumps(self._data)

def ListItem_repr(self):
    return self.__str__()

WINDOW_DATA = {}
def Window_init(self, existingWindowId=-1):
    global WINDOW_DATA
    self._window_id = existingWindowId
    if existingWindowId not in WINDOW_DATA:
        WINDOW_DATA[existingWindowId] = {}

def Window_getProperty(self, key):
    return WINDOW_DATA[self._window_id].get(key, "")

def Window_setProperty(self, key, value):
    global WINDOW_DATA
    WINDOW_DATA[self._window_id][key] = value

def Window_clearProperty(self, key):
    global WINDOW_DATA
    WINDOW_DATA[self._window_id].pop(key, None)

xbmcgui.Dialog.yesno                 = Dialog_yesno
xbmcgui.Dialog.ok                    = Dialog_ok
xbmcgui.Dialog.notification          = Dialog_notification
xbmcgui.Dialog.input                 = Dialog_input
xbmcgui.DialogProgress.create        = DialogProgress_create

xbmcgui.ListItem.__init__            = ListItem_init
xbmcgui.ListItem.setArt              = ListItem_setArt
xbmcgui.ListItem.setInfo             = ListItem_setInfo
xbmcgui.ListItem.addStreamInfo       = ListItem_addStreamInfo
xbmcgui.ListItem.addContextMenuItems = ListItem_addContextMenuItems
xbmcgui.ListItem.setProperty         = ListItem_setProperty
xbmcgui.ListItem.setPath             = ListItem_setPath
xbmcgui.ListItem.getPath             = ListItem_getPath
xbmcgui.ListItem.__str__             = ListItem_str
xbmcgui.ListItem.__repr__            = ListItem_repr

xbmcgui.Window.__init__              = Window_init
xbmcgui.Window.getProperty           = Window_getProperty
xbmcgui.Window.setProperty           = Window_setProperty
xbmcgui.Window.clearProperty         = Window_clearProperty

## xbmcplugin ##
def _init_data():
    return {'items': [], 'sort': [], 'content': '', 'category': ''}
    
DATA = _init_data()

def addDirectoryItem(handle, url, listitem, isFolder=False, totalItems=0):
    global DATA
    DATA['items'].append((url, listitem, isFolder))
    return True

def addDirectoryItems(handle, items, totalItems=0):
    global DATA
    for item in items:
        DATA['items'].append(item)
    return True

def endOfDirectory(handle, succeeded=True, updateListing=False, cacheToDisc=True):
    global DATA

    print('Title: {category}\nContent: {content}'.format(**DATA))
    for item in DATA['items']:
        print("\nUrl: {0}\nItem: {1}\nIs Folder: {2}".format(*item))

    DATA = _init_data()

def setResolvedUrl(handle, succeeded, listitem):
    print("Resolved: {0}".format(listitem))

def addSortMethod(handle, sortMethod, label2Mask=""):
    global DATA
    DATA['sort'].append(sortMethod)

def setContent(handle, content):
    global DATA
    DATA['content'] = content

def setPluginCategory(handle, category):
    global DATA
    DATA['category'] = category

xbmcplugin.addDirectoryItem  = addDirectoryItem
xbmcplugin.addDirectoryItems = addDirectoryItems
xbmcplugin.endOfDirectory    = endOfDirectory
xbmcplugin.setResolvedUrl    = setResolvedUrl
xbmcplugin.addSortMethod     = addSortMethod
xbmcplugin.setContent        = setContent
xbmcplugin.setPluginCategory = setPluginCategory


## xbmcvfs ##

def exists(path):
    return os.path.exists(path)

def mkdir(path):
    return os.mkdir(path)

def mkdirs(path):
    return os.makedirs(path)

def delete(file):
    return os.remove(file)

xbmcvfs.exists = exists
xbmcvfs.mkdir  = mkdir
xbmcvfs.mkdirs = mkdirs
xbmcvfs.delete = delete