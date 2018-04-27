################################################################
##  TeamX have built this addon from base code provided       ##
##  by pipcan and with help from whufclee (NoobsAndNerds)     ##
##  kiwiman has put in a few hours of work to find the links  ##
##  and build this code.  tdbnz has assisted where able and   ##
##  been a great sounding block for kiwiman while working     ##
##                         on this.  Enjoy                    ##
################################################################

import os,requests,urllib,urllib2,re,xbmcplugin,xbmcaddon,xbmc,xbmcgui

base_url = 'http://www.severestudios.com/livechase/'
r = requests.get(base_url)

pluginhandle = int(sys.argv[1])

def CATEGORIES():
    no_chasers_match = re.compile('<div id=".+?" class=".+?">\n.+?<div id="no-streams".+?class="cbp-item (.+?)">').findall(r.content)
    for item in no_chasers_match:
        if item == "no-streams":
			chaser = "**  No Storm Chasers Currently Streaming  **"
			chaser_stream = 'https://fpdl.vimeocdn.com/vimeo-prod-skyfire-std-us/01/3599/2/67995158/709472360.mp4?token=1497922266-0x23955caec376c6461ce453fe0adad2cdadbc304b'
			addDir2(chaser,chaser_stream,1,'')
    else:
        chaser_match = re.compile('.+?<a href="http://cdn(.+?)".+?data-title="(.+?)".+?\n.+?\n.+?<img src="(.+?)"').findall(r.content)
        for stream_url, chaser, image in chaser_match:
			stream_url = "http://cdn" + stream_url
			stream = requests.get(stream_url)
			match_stream = re.compile('.+?<source src="(.+?)"').findall(stream.content)
			for chaser_stream in match_stream:
				addDir2(chaser,chaser_stream,1,'')

def URL_SHOW(stream_url,chaser):
	stream = requests.get(stream_url)
	match_stream = re.compile('.+?<source src="(.+?)"').findall(stream.content)
	for chaser_stream in match_stream:
		addDir2(chaser+' - '+'',chaser_stream,1,'')
        
        
def OPEN_URL(chaser_stream,chaser):
	listitem = xbmcgui.ListItem(chaser_stream)
	xbmc.log(chaser_stream)
	listitem.setInfo('video', {'Title': name})
	play = xbmc.Player().play
	play(chaser_stream, listitem)
    
    
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
        OPEN_URL(url,name)
elif mode==3:
        URL_SHOW(url,name)
elif mode==4:
        mylist(url)

        
xbmcplugin.endOfDirectory(int(sys.argv[1]))