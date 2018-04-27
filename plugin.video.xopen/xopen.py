

import os,requests,urllib,urllib2,re,xbmcplugin,xbmcaddon,xbmc,xbmcgui

api_url = 'http://www.xopenload.com'
arrow = 'http://www.clker.com/cliparts/Z/T/D/Z/J/X/gray-last-button-md.png'
r = requests.get(api_url)
r_text = r.content

find_cats = re.compile('<li id="menu-item-.+?" class=".+?"><a href="http://www.xopenload.com/(.+?)">(.+?)</a></li>').findall(r_text)

#find_cats = re.compile('<li id="menu-item-(.+?)".+?"><a href="(.+?)">(.+?)</a></li>').findall(r_text)

pluginhandle = int(sys.argv[1])

def CATEGORIES():

	page = re.compile('<span class="current">1</span><a class="inactive" href="(.+?)">(.+?)<').findall(r_text)
	for ident, name in find_cats:
		url = ('http://www.xopenload.com/' + ident)
	#for ident, url, name in find_cats[1:]:
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
	ident = url[25:]
	num = ident.split('/')
	if num[0] == 'category':
		cat = num[1]
	
		if cat == '1':
			xbmc.log('\n**\n****\n1 selected,  ' + cat + ' fetched')
			find_movies = re.compile('\n<div class="poster">\n<a href="(.+?)"><img src="(.+?).".+?alt="(.+?)"></a>',re.DOTALL).findall(links.content)
			for url, img, title in find_movies:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass
			
		if cat == '2':
			xbmc.log('\n**\n****\n2 selected,  ' + cat + ' fetched')
			find_clips = re.compile('<img src="(.+?)" alt="(.+?)">\n.+?\n<a href="(.+?)">').findall(links.content)
			for img, title, url in find_clips:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass

		if cat == '3':
			xbmc.log('\n**\n****\n3 selected,  ' + cat + ' fetched')
			find_packs = re.compile('\n<div class="poster">\n<a href="(.+?)"><img src="(.+?).".+?alt="(.+?)"></a>',re.DOTALL).findall(links.content)
			for url, img, title in find_packs:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass
	
		if cat == '4':
			xbmc.log('\n**\n****\n4 selected,  ' + cat + ' fetched')
			find_jav = re.compile('<img src="(.+?)" alt="(.+?)">.+?<a href="(.+?)">',re.DOTALL).findall(links.content)
			xbmc.log(str(links.content))
			xbmc.log(str(find_jav))
			for img, title, url in find_jav[1:]:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass
	
	if num[0] == 'tags' or  url.startswith('http://www.xopenload.com/search.php'):
		
		find_tags = re.compile('\n<div class="poster">\n<a href="(.+?)"><img src="(.+?).".+?alt="(.+?)"></a>',re.DOTALL).findall(links.content)
		for url, img, title in find_tags:
			if img.endswith('.jp'):
				img = img.replace('.jp','.jpg')
			if img.endswith('.jpg\r'):
				img = img.replace('.jpg\r','.jpg')
			if img.endswith('.png\r'):
				img = img.replace('.png\r','.png')
			if img.endswith('.pn'):
				img = img.replace('.pn','.png')
			if img.endswith('.jpeg\r'):
				img = img.replace('.jpeg\r','.jpg')
			addDir3(title,url,5,img,'','')
	else:
		pass
	
	if num[0] != 'category':
		cat =num[0]
	
		if cat == 'recent':
			xbmc.log('\n**\n****\nrecent selected,  ' + cat + ' fetched')
			find_recent = re.compile('\n<div class="poster">\n<a href="(.+?)"><img src="(.+?).".+?alt="(.+?)"></a>',re.DOTALL).findall(links.content)
			for url, img, title in find_recent:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass
		
		if cat == 'list':
			xbmc.log('\n**\n****\nlist selected,  ' + cat + ' fetched')
			find_list = re.compile(".+?onmouseover=\"loadimg\('.+?','(.+?)'\)\"><a href=\"(.+?)\">(.+?)<img").findall(links.content)
			for img, url, title in find_list:
				if img.endswith('.jp'):
					img = img.replace('.jp','.jpg')
				if img.endswith('.jpg\r'):
					img = img.replace('.jpg\r','.jpg')
				if img.endswith('.png\r'):
					img = img.replace('.png\r','.png')
				if img.endswith('.pn'):
					img = img.replace('.pn','.png')
				if img.endswith('.jpeg\r'):
					img = img.replace('.jpeg\r','.jpg')
				addDir3(title,url,5,img,'','')
		else:
			pass

	page = re.compile('<span class="current">.+?</span><a class="inactive" href="(.+?)">').findall(links.content)

	for page_url in page:
		addDir3('[COLOR gold]Next Page >>[/COLOR]',page_url,3,arrow,'','')

		
def OPEN(url):
	c = 0
	addDir2('[COLOR green][B]Please go to olpair.com to load links[/B][/COLOR]','',5,'')
	playable_links = requests.get(url)
	find_links = re.compile("urlChange\('(.+?)'\)\">(.+?)<").findall(playable_links.content)
	for url, srvr in find_links[1:]:
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
					addDir2(name,url,1,'')
					
		
					

		
def OPEN_URL(url):
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
elif mode==3:
        MOVIES(url,name)
elif mode==4:
        LIST(url)
elif mode==5:
        OPEN(url)
elif mode==6:
        TAGS(r_text)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
