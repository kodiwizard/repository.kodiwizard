import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys
import shutil
import urllib2,urllib
import re
import extract
import time


ADDON        =  xbmcaddon.Addon(id='plugin.video.usbwizard')
zip          =  ADDON.getSetting('zip')
dialog       =  xbmcgui.Dialog()
dp           =  xbmcgui.DialogProgress()
USERDATA     =  xbmc.translatePath(os.path.join('special://home/userdata',''))
ADDON_DATA   =  xbmc.translatePath(os.path.join(USERDATA,'addon_data'))
ADDONS       =  xbmc.translatePath(os.path.join('special://home','addons'))
GUI          =  xbmc.translatePath(os.path.join(USERDATA,'guisettings.xml'))
FAVS         =  xbmc.translatePath(os.path.join(USERDATA,'favourites.xml'))
SOURCE       =  xbmc.translatePath(os.path.join(USERDATA,'sources.xml'))
ADVANCED     =  xbmc.translatePath(os.path.join(USERDATA,'advancedsettings.xml'))
RSS          =  xbmc.translatePath(os.path.join(USERDATA,'RssFeeds.xml'))
KEYMAPS      =  xbmc.translatePath(os.path.join(USERDATA,'keymaps','keyboard.xml'))
USB          =  xbmc.translatePath(os.path.join(zip))
skin         =  xbmc.getSkinDir()


if zip=='':
    if dialog.yesno("USB BACKUP/RESTORE", "You Have Not Set Your Storage Path", 'Set The Storage Path Now ?',''):
        ADDON.openSettings()
        print '######### ZIP DIRECTORY #########'
        for filename in os.listdir(USB):
            print filename

def XfinityInstaller():
    path = os.path.join(xbmc.translatePath('special://home'),'userdata', 'sources.xml')
    if not os.path.exists(path):
        f = open(path, mode='w')
        f.write('<sources><files><source><name>.[COLOR blue]X[/COLOR]finity Installer</name><path pathversion="1">http://xfinity.xunitytalk.com</path></source></files></sources>')
        f.close()
        return
        
    f   = open(path, mode='r')
    str = f.read()
    f.close()
    if not'http://xfinity.xunitytalk.com' in str:
        if '</files>' in str:
            str = str.replace('</files>','<source><name>.[COLOR blue]X[/COLOR]finity Installer</name><path pathversion="1">http://xfinity.xunitytalk.com</path></source></files>')
            f = open(path, mode='w')
            f.write(str)
            f.close()
        else:
            str = str.replace('</sources>','<files><source><name>.[COLOR blue]X[/COLOR]finity Installer</name><path pathversion="1">http://xfinity.xunitytalk.com</path></source></files></sources>')
            f = open(path, mode='w')
            f.write(str)
            f.close()

    
def BACKUP():  
    if zip == '':
        dialog.ok('USB BACKUP/RESTORE','You have not set your ZIP Folder.\nPlease update the addon settings and try again.','','')
        ADDON.openSettings(sys.argv[0])
    to_backup = xbmc.translatePath(os.path.join('special://','home'))
    backup_zip = xbmc.translatePath(os.path.join(USB,'backup.zip'))
    DeletePackages()    
    import zipfile
    
    dp.create("USB BACKUP/RESTORE","Backing Up",'', 'Please Wait')
    zipobj = zipfile.ZipFile(backup_zip , 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(to_backup)
    for_progress = []
    ITEM =[]
    for base, dirs, files in os.walk(to_backup):
        for file in files:
            ITEM.append(file)
    N_ITEM =len(ITEM)
    for base, dirs, files in os.walk(to_backup):
        for file in files:
            for_progress.append(file) 
            progress = len(for_progress) / float(N_ITEM) * 100  
            dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
            fn = os.path.join(base, file)
            if not 'temp' in dirs:
                if not 'plugin.video.usbwizard' in dirs:
                   import time
                   CUNT= '01/01/1980'
                   FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                   if FILE_DATE > CUNT:
                       zipobj.write(fn, fn[rootlen:])  
    zipobj.close()
    dp.close()
    dialog.ok("USB BACKUP/RESTORE", "You Are Now Backed Up", '','')
    
      
def READ_ZIP(url):

    import zipfile
    
    z = zipfile.ZipFile(url, "r")
    for filename in z.namelist():
        if 'guisettings.xml' in filename:
            a = z.read(filename)
            r='<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>'% skin
            
            match=re.compile(r).findall(a)
            print match
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&amp;','&') 
                xbmc.executebuiltin("Skin.Set%s(%s,%s)"%(type.title(),string,setting))  
                
        if 'favourites.xml' in filename:
            a = z.read(filename)
            f = open(FAVS, mode='w')
            f.write(a)
            f.close()  
			               
        if 'sources.xml' in filename:
            a = z.read(filename)
            f = open(SOURCE, mode='w')
            f.write(a)
            f.close()    
                         
        if 'advancedsettings.xml' in filename:
            a = z.read(filename)
            f = open(ADVANCED, mode='w')
            f.write(a)
            f.close()                 

        if 'RssFeeds.xml' in filename:
            a = z.read(filename)
            f = open(RSS, mode='w')
            f.write(a)
            f.close()                 
            
        if 'keyboard.xml' in filename:
            a = z.read(filename)
            f = open(KEYMAPS, mode='w')
            f.write(a)
            f.close()                 
              
def RESTORE():

    import time
    dialog = xbmcgui.Dialog()
    if zip == '':
        dialog.ok('USB BACKUP/RESTORE','You have not set your ZIP Folder.\nPlease update the addon settings and try again.','','')
        ADDON.openSettings(sys.argv[0])
        
    lib=xbmc.translatePath(os.path.join(zip,'backup.zip'))
    READ_ZIP(lib)
    dp.create("USB BACKUP/RESTORE","Checking ",'', 'Please Wait')
    HOME = xbmc.translatePath(os.path.join('special://','home'))
    
    dp.update(0,"", "Extracting Zip Please Wait")
    extract.all(lib,HOME,dp)
    time.sleep(1)
    XfinityInstaller()
    xbmc.executebuiltin('UpdateLocalAddons ')    
    xbmc.executebuiltin("UpdateAddonRepos")
    time.sleep(1)
    xbmc.executebuiltin('UnloadSkin()') 
    xbmc.executebuiltin('ReloadSkin()')    
    xbmc.executebuiltin("LoadProfile(Master user)")
    dialog.ok("USB BACKUP/RESTORE", "PLEASE REBOOT YOUR BOX IF HOMESCREEN HAS NOT CHANGED", "","")

    
    
def CATEGORIES():
    addDir('Backup','url',1,'','Back Up Your Full System')
    addDir('Restore','url',5,'','Restore Your Full System')


def BACKUP_OPTION():
    addDir('FULL BACKUP','url',3,'','Back Up Your Full System')
    addDir('Backup Just Your Addons','addons',6,'','Back Up Your Addons')
    addDir('Backup Just Your Addon UserData','addon_data',6,'','Back Up Your Addon Userdata')
    addDir('Backup Guisettings.xml',GUI,4,'','Back Up Your guisettings.xml')
    if os.path.exists(FAVS):
        addDir('Backup Favourites.xml',FAVS,4,'','Back Up Your favourites.xml')
    if os.path.exists(SOURCE):
        addDir('Backup Source.xml',SOURCE,4,'','Back Up Your sources.xml')
    if os.path.exists(ADVANCED):
        addDir('Backup Advancedsettings.xml',ADVANCED,4,'','Back Up Your advancedsettings.xml')
    if os.path.exists(KEYMAPS):
        addDir('Backup Advancedsettings.xml',KEYMAPS,4,'','Back Up Your keyboard.xml')
    if os.path.exists(RSS):
        addDir('Backup RssFeeds.xml',RSS,4,'','Back Up Your RssFeeds.xml')    


def RESTORE_OPTION():
    if os.path.exists(os.path.join(USB,'backup.zip')):   
        addDir('FULL RESTORE','url',2,'','Back Up Your Full System')
        
    if os.path.exists(os.path.join(USB,'addons.zip')):   
        addDir('Restore Your Addons','addons',6,'','Restore Your Addons')

        
    if os.path.exists(os.path.join(USB,'addon_data.zip')):   
        addDir('Restore Your Addon UserData','addon_data',6,'','Restore Your Addon UserData')           

    if os.path.exists(os.path.join(USB,'guisettings.xml')):
        addDir('Restore Guisettings.xml',GUI,4,'','Restore Your guisettings.xml')
    
    if os.path.exists(os.path.join(USB,'favourites.xml')):
        addDir('Restore Favourites.xml',FAVS,4,'','Restore Your favourites.xml')
        
    if os.path.exists(os.path.join(USB,'sources.xml')):
        addDir('Restore Source.xml',SOURCE,4,'','Restore Your sources.xml')
        
    if os.path.exists(os.path.join(USB,'advancedsettings.xml')):
        addDir('Restore Advancedsettings.xml',ADVANCED,4,'','Restore Your advancedsettings.xml')        

    if os.path.exists(os.path.join(USB,'keyboard.xml')):
        addDir('Restore Advancedsettings.xml',KEYMAPS,4,'','Restore Your keyboard.xml')
        
    if os.path.exists(os.path.join(USB,'RssFeeds.xml')):
        addDir('Restore RssFeeds.xml',RSS,4,'','Restore Your RssFeeds.xml')    


def RESTORE_ZIP_FILE(url):
    if zip == '':
        dialog.ok('USB BACKUP/RESTORE','You have not set your ZIP Folder.\nPlease update the addon settings and try again.','','')
        ADDON.openSettings(sys.argv[0])
        
    if 'addons' in url:
        ZIPFILE = xbmc.translatePath(os.path.join(USB,'addons.zip'))
        DIR = ADDONS
        to_backup = ADDONS
        
        backup_zip = xbmc.translatePath(os.path.join(USB,'addons.zip'))
    else:
        ZIPFILE = xbmc.translatePath(os.path.join(USB,'addon_data.zip'))
        DIR = ADDON_DATA

        
    if 'Backup' in name:
        DeletePackages() 
        import zipfile
        import sys
        dp.create("USB BACKUP/RESTORE","Backing Up",'', 'Please Wait')
        zipobj = zipfile.ZipFile(ZIPFILE , 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(DIR)
        for_progress = []
        ITEM =[]
        for base, dirs, files in os.walk(DIR):
            for file in files:
                ITEM.append(file)
        N_ITEM =len(ITEM)
        for base, dirs, files in os.walk(DIR):
            for file in files:
                for_progress.append(file) 
                progress = len(for_progress) / float(N_ITEM) * 100  
                dp.update(int(progress),"Backing Up",'[COLOR yellow]%s[/COLOR]'%file, 'Please Wait')
                fn = os.path.join(base, file)
                if not 'temp' in dirs:
                    if not 'plugin.video.usbwizard' in dirs:
                       import time
                       CUNT= '01/01/1980'
                       FILE_DATE=time.strftime('%d/%m/%Y', time.gmtime(os.path.getmtime(fn)))
                       if FILE_DATE > CUNT:
                           zipobj.write(fn, fn[rootlen:]) 
        zipobj.close()
        dp.close()
        dialog.ok("USB BACKUP/RESTORE", "You Are Now Backed Up", '','')   
    else:

        dp.create("USB BACKUP/RESTORE","Checking ",'', 'Please Wait')
        
        import time
        dp.update(0,"", "Extracting Zip Please Wait")
        extract.all(ZIPFILE,DIR,dp)
        
        time.sleep(1)
        XfinityInstaller()
        xbmc.executebuiltin('UpdateLocalAddons ')    
        xbmc.executebuiltin("UpdateAddonRepos")        
        dialog.ok("USB BACKUP/RESTORE", "You Are Now Restored", '','')        

def RESTORE_BACKUP_XML(name,url,description):
    if 'Backup' in name:
        TO_READ   = open(url).read()
        TO_WRITE  = os.path.join(USB,description.split('Your ')[1])
        
        f = open(TO_WRITE, mode='w')
        f.write(TO_READ)
        f.close() 
         
    else:
    
        if 'guisettings.xml' in description:
            a = open(os.path.join(USB,description.split('Your ')[1])).read()
            
            r='<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>'% skin
            
            match=re.compile(r).findall(a)
            print match
            for type,string,setting in match:
                setting=setting.replace('&quot;','') .replace('&amp;','&') 
                xbmc.executebuiltin("Skin.Set%s(%s,%s)"%(type.title(),string,setting))  
        else:    
            TO_WRITE   = os.path.join(url)
            TO_READ  = open(os.path.join(USB,description.split('Your ')[1])).read()
            
            f = open(TO_WRITE, mode='w')
            f.write(TO_READ)
            f.close()  
    dialog.ok("USB BACKUP/RESTORE", "", 'All Done !','')


def DeletePackages():
    print '############################################################       DELETING PACKAGES             ###############################################################'
    packages_cache_path = xbmc.translatePath(os.path.join('special://home/addons/packages', ''))
 
    for root, dirs, files in os.walk(packages_cache_path):
        file_count = 0
        file_count += len(files)
        
    # Count files and give option to delete
        if file_count > 0:
                        
            for f in files:
                os.unlink(os.path.join(root, f))
            for d in dirs:
                shutil.rmtree(os.path.join(root, d))

        
    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        if mode==None or mode==5 or mode==1 or mode==6 or url==None or len(url)<1:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        

                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass

        
if mode==None or url==None or len(url)<1:
        CATEGORIES()
       
elif mode==1:
        BACKUP_OPTION()
        
elif mode==2:
        print "############   RESTORE  #################"
        RESTORE()    
           
elif mode==3:
        print "############   BACKUP  #################"
        BACKUP()
              
elif mode==4:
        print "############   RESTORE_BACKUP_XML #################"
        RESTORE_BACKUP_XML(name,url,description)

elif mode==5:
        print "############   RESTORE_OPTION   #################"
        RESTORE_OPTION()

elif mode==6:
        print "############   RESTORE_ZIP_FILE   #################"
        RESTORE_ZIP_FILE(url)         
xbmcplugin.endOfDirectory(int(sys.argv[1]))

