#######################################################################
#Import Modules Section
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import os
import sys
import glob
import urllib
import urllib2
from urllib2 import urlopen
import downloader
import re
import time
import requests
import shutil
import glo_var
import time
from datetime import date, datetime, timedelta
#######################################################################

#######################################################################
#Global Variables
ADDON               = glo_var.ADDON
ADDONDATA           = glo_var.ADDONDATA
ADDONTITLE          = glo_var.ADDONTITLE
PACKAGES            = xbmc.translatePath(os.path.join('special://home/addons/' + 'packages'))
DIALOG              = glo_var.DIALOG
dialog              = glo_var.dialog
dp                  = glo_var.dp
FANART              = glo_var.FANART
ICON                = glo_var.ICON
skin                = xbmc.getSkinDir()
USER_AGENT          = glo_var.USER_AGENT
NEWSURL             = glo_var.NEWSURL

#######################################################################
# All add commands are listed below: These are used to add directories or items to the menus.
# In between the brackets you will find the information each add command is looking for.
def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==90 : ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else: ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir2(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        if not url == None: u += "&url="+urllib.quote_plus(url)        
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        if mode==90 : ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else: ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addItem(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty( "Fanart_Image", fanart )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def addFile(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
    u = sys.argv[0]
    if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
    if not name == None: u += "&name="+urllib.quote_plus(name)
    if not url == None: u += "&url="+urllib.quote_plus(url)
    ok=True
    if themeit: display = themeit % display
    liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
    liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
    liz.setProperty( "Fanart_Image", fanart )
    if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok    
	

#######################################################################

#######################################################################

def addonId(add):
    try:    return xbmcaddon.Addon(id=add)
    except: return False

def addonInfo(add, info):
    addon = addonId(add)
    if addon: return addon.getAddonInfo(info)
    else: return False

def ebi(proc):
    xbmc.executebuiltin(proc)

def percentage(part, whole):
    return 100 * float(part)/float(whole)

def LogNotify(title,message,times=2000,icon=ICON):
    xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % (title , message , times, icon))

def OPEN_URL(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link 

def workingURL(url):
    if url == 'http://': return False
    if url == 'url': return False
    try: 
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        response.close()
    except Exception, e:
        return e
    return True    
	
def addFile(display, mode=None, name=None, url=None, menu=None, description=ADDONTITLE, overwrite=True, fanart=FANART, icon=ICON, themeit=None):
	u = sys.argv[0]
	if not mode == None: u += "?mode=%s" % urllib.quote_plus(mode)
	if not name == None: u += "&name="+urllib.quote_plus(name)
	if not url == None: u += "&url="+urllib.quote_plus(url)
	ok=True
	if themeit: display = themeit % display
	liz=xbmcgui.ListItem(display, iconImage="DefaultFolder.png", thumbnailImage=icon)
	liz.setInfo( type="Video", infoLabels={ "Title": display, "Plot": description} )
	liz.setProperty( "Fanart_Image", fanart )
	if not menu == None: liz.addContextMenuItems(menu, replaceItems=overwrite)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok
#######################################################################

#######################################################################
# APK Download and Install Code
def apknotify(apk):
    class APKInstaller(xbmcgui.WindowXMLDialog):
        def __init__(self,*args,**kwargs):
            self.shut=kwargs['close_time']
            xbmc.executebuiltin("Skin.Reset(AnimeWindowXMLDialogClose)")
            xbmc.executebuiltin("Skin.SetBool(AnimeWindowXMLDialogClose)")

        def onFocus(self,controlID): pass

        def onClick(self,controlID): self.CloseWindow()

        def onAction(self,action):
            if action in [ACTION_PREVIOUS_MENU, ACTION_BACKSPACE, ACTION_NAV_BACK, ACTION_SELECT_ITEM, ACTION_MOUSE_LEFT_CLICK, ACTION_MOUSE_LONG_CLICK]: self.CloseWindow()

        def CloseWindow(self):
            xbmc.executebuiltin("Skin.Reset(AnimeWindowXMLDialogClose)")
            xbmc.sleep(400)
            self.close()
    
    xbmc.executebuiltin('Skin.SetString(apkinstaller, Now that %s has been downloaded[CR]Click install on the next window!)' % apk)

def apkInstaller(apk, url):
    if platform() == 'android':
        yes = DIALOG.yesno(ADDONTITLE, "[COLOR snow]Would you like to download and install:[/COLOR]", "[COLOR snow]%s[/COLOR]" % (apk))
        if not yes: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled'); return
        display = apk
        if yes:
            if not os.path.exists(PACKAGES): os.makedirs(PACKAGES)
            if not workingURL(url) == True: LogNotify(ADDONTITLE, 'APK Installer: [COLOR red]Invalid Apk Url![/COLOR]'); return
            dp.create(ADDONTITLE,'[COLOR springgreen][B]Downloading:[/B][/COLOR] [COLOR snow]%s[/COLOR]' % (display),'', 'Please Wait')
            lib=os.path.join(PACKAGES, "%s.apk" % apk)
            try: os.remove(lib)
            except: pass
            downloader.download(url, lib, dp)
            xbmc.sleep(500)
            dp.close()
            apknotify(apk)
            ebi('StartAndroidActivity("","android.intent.action.VIEW","application/vnd.android.package-archive","file:'+lib+'")')
        else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] Install Cancelled')
    else: LogNotify(ADDONTITLE, '[COLOR red]ERROR:[/COLOR] None Android Device')
	
#######################################################################
# News and Update Code
def Update_News():
        message=open_news_url(NEWSURL)
        path = xbmcaddon.Addon().getAddonInfo('path')
        newsfile = os.path.join(os.path.join(path,''), 'whatsnew.txt')
        r = open(newsfile)
        compfile = r.read()       
        if len(message)>1:
                if compfile == message:pass
                else:
                        text_file = open(newsfile, "w")
                        text_file.write(message)
                        text_file.close()
                        compfile = message
        showText('[B][COLOR springgreen]Latest Updates and Information[/COLOR][/B]', compfile)
        
def open_news_url(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'klopp')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        print link
        return link

def showText(heading, text):

    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except: pass
#######################################################################

#######################################################################
# The code below determines the platform of the device.
def platform():
    if xbmc.getCondVisibility('system.platform.android'):   return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):   return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'): return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):     return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):    return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):     return 'ios'
#######################################################################
