################################################################
##  this addon is from base code provided                     ##
##  by pipcan and with help from whufclee (NoobsAndNerds)     ##
##  lots of hours been put to find the links                  ##
##  and to build this code.   he assisted where able and      ##
##  been a great sounding block for us                        ##
################################################################

import os,requests,urllib,urllib2,re,xbmcplugin,xbmcaddon,xbmc,xbmcgui

api_url = 'https://now-api.mediaworks.nz/now-api/v3/shows/'
pluginhandle = int(sys.argv[1])

def CATEGORIES():
	r = requests.get(api_url)
	match = re.compile('"showId":"(.+?)".+?"name":"(.+?)".+?showTile":"(.+?)"').findall(r.content)
    # for item in match:
	for show_id, name, thumb in match:
		show_url = api_url.strip('s/') + '/' + show_id
		thumb = thumb.split('?width=')[0]
		name_no_space = name.replace(' ', '-')
		name_no_periods = name_no_space.replace('.','')
		addDir3(name,show_url,3,thumb,'','')
    
def URL_SHOW(show_url,name):
    a = requests.get(show_url)
    match = re.compile('"extId":".+?","name":"(.+?)".+?"once":{"url":"(.+?)".+?"videoTile":"(.+?)"}').findall(a.content)
    for episode, url_show, thumb in match:
		addDir2(name+' - '+episode,url_show,1,thumb)

		
def OPEN_URL(url_show):
	req = requests.get(url_show)
	match_show_url = re.compile('contenturi="(.+?)"').findall(req.content)
	url = str(match_show_url).strip('[, ], \'')
	listitem = xbmcgui.ListItem(url)
	listitem.setInfo('video', {'Title': name})
	play = xbmc.Player().play
	play(url, listitem)
    
    
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

		
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def addDir3(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok


def setView(content, viewType):
    # set content type so library shows more views and info
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if ADDON.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % Thumbnail )
 


              
params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
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
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
   
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        OPEN_URL(url)
elif mode==2:
        URL_EPISODE(url,name)
elif mode==3:
        URL_SHOW(url,name)
elif mode==4:
        mylist(url)

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
