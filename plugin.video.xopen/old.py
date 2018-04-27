

import os,requests,urllib,urllib2,re,xbmcplugin,xbmcaddon,xbmc,xbmcgui

api_url = 'http://www.xopenload.com'
arrow = 'https://cdn0.iconfinder.com/data/icons/simple-outlines-1/100/Next-512.png'
r = requests.get(api_url)
r_text = r.content

pluginhandle = int(sys.argv[1])

dialog = xbmcgui.Dialog()
dialog.notification('Please visit www.olpair.com','from another device to use this addon')


def CATEGORIES():
	find_cats = re.compile('<li id="menu-item.+?"><a href="(.+?)">(.+?)</a></li>').findall(r_text)
	page = re.compile('<span class="current">1</span><a class="inactive" href="(.+?)">(.+?)<').findall(r_text)
	for url, name in find_cats[1:]:
		addDir3(name,url,3,'','','')
	addDir3('Tags',url,6,'','','')
	for page_url, page_number in page:
		addDir3(page_number,page_url,3,'','','')
		
def TAGS(r_text):
	find_tags = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(r_text)
	for url, name in find_tags[8:]:
		addDir3(name,url,3,'','','')
    
def MOVIES(url,name):
	links = requests.get(url)
	find_movies = re.compile('\n<a href="(.+?)"><img src="(.+?)" alt="(.+?)"></a>').findall(links.content)
	find_clips = re.compile('<img src="(.+?)" alt="(.+?)">\n.+?\n<a href="(.+?)">').findall(links.content)
	find_jav = re.compile('<img src="(.+?)" alt="(.+?)">\n.+?\n.+?\n<a href="(.+?)">').findall(links.content)
	find_lists = re.compile(".+?onmouseover=\"loadimg\('.+?','(.+?)'\)\"><a href=\"(.+?)\">(.+?)<img").findall(links.content)
	page = re.compile('<span class="current">.+?</span><a class="inactive" href="(.+?)">').findall(links.content)

	for url, img, title in find_movies:
		addDir3(title,url,5,img,'','')
	for img, title, url in find_clips:
		addDir2(title,url,5,img)
	for img, title, url in find_jav:
		addDir2(title,url,5,img)
	for img, url, title in find_lists:
		addDir2(title,url,5,img)

	for page_url in page:
		addDir3('Next Page >>',page_url,3,arrow,'','')

		
def OPEN(url):
	playable_links = requests.get(url)
	find_links = re.compile("urlChange\('(.+?)'\)\">(.+?)<").findall(playable_links.content)
	for url, srvr in find_links:
		test = requests.get(url).content
		find = re.compile('<iframe src="(.+?)"').findall(test)
		for url in find:
			var1 = 'http://www.openload.co/embed/'
			var2 = 'https://api.openload.co/1/streaming/get?file='
			var3 = '"name":"(.+?)",.+?"url":"(.+)"'
			if url.startswith(var1):
				url = url.strip('/')
				url = url.replace (var1, var2)
				test1 = requests.get(url)
				regex = re.compile('"name":"(.+?)",.*"url":"(.+)"').findall(test1.content)
				for name,url in regex:
					playlink = var3 + url
					addDir2(name,playlink,1,'')

		
def OPEN_URL(playlink):
		listitem = xbmcgui.ListItem(playlink)
		listitem.setInfo('video', {'Title': name})
		play = xbmc.Player().play
		play(playlink, listitem)
    
    
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
elif mode==3:
        MOVIES(url,name)
elif mode==4:
        LIST(url)
elif mode==5:
        OPEN(url)
elif mode==6:
        TAGS(r_text)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
