# -*- coding: utf-8 -*-

'''
    Exodus Add-on
    Copyright (C) 2016 Exodus

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import re,urllib,urlparse,json,base64

from resources.lib.modules import cleantitle
from resources.lib.modules import cloudflare
from resources.lib.modules import client


class source:
    def __init__(self):
        self.domains = ['123movies.to', '123movies.ru']
        self.base_link = 'http://123movies.ru'
        self.info_link = '/ajax/movie_load_info/%s'
        self.search_link = 'aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vY3VzdG9tc2VhcmNoL3YxZWxlbWVudD9rZXk9QUl6YVN5Q1ZBWGlVelJZc01MMVB2NlJ3U0cxZ3VubU1pa1R6UXFZJnJzej1maWx0ZXJlZF9jc2UmbnVtPTEwJmhsPWVuJmN4PTAwMDc0NjAzOTU3ODI1MDQ0NTkzNTp1a2lqdGJvbm1jNCZnb29nbGVob3N0PXd3dy5nb29nbGUuY29tJnE9JXM='
        self.search2_link = '/movie/search/%s'


    def movie(self, imdb, title, year):
        try:
            t = cleantitle.get(title)

            try:
                query = '%s %s' % (title, year)
                query = base64.b64decode(self.search_link) % urllib.quote_plus(query)

                result = client.source(query)
                result = json.loads(result)['results']

                r = [(i['url'], i['titleNoFormatting']) for i in result]
                r = [(i[0], re.findall('(?:^Watch Full "|^Watch |)(.+?)(?:For Free On 123Movies|On 123Movies|$)', i[1])) for i in r]
                r = [(i[0], i[1][0]) for i in r if len(i[1]) > 0]
                r = [(re.sub('http.+?//.+?/','', i[0]), i[1]) for i in r]
                r = [('/'.join(i[0].split('/')[:2]), i[1]) for i in r]
                r = [x for y,x in enumerate(r) if x not in r[:y]]
                r = [i[0] for i in r if t == cleantitle.get(i[1])]

                for i in r:
                    url = self._info(i, year)
                    if not url == None: return url
            except:
                pass

            try:
                query = self.search2_link % urllib.quote_plus(title)
                query = urlparse.urljoin(self.base_link, query)

                result = cloudflare.source(query)

                r = client.parseDOM(result, 'div', attrs = {'class': 'ml-item'})
                r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r]
                r = [(i[0][0], i[1][-1]) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
                r = [(re.sub('http.+?//.+?/','', i[0]), i[1]) for i in r]
                r = [('/'.join(i[0].split('/')[:2]), i[1]) for i in r]
                r = [x for y,x in enumerate(r) if x not in r[:y]]
                r = [i[0] for i in r if t == cleantitle.get(i[1])]

                for i in r:
                    url = self._info(i, year)
                    if not url == None: return url
            except:
                pass

        except:
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            tvshowtitle = cleantitle.get(data['tvshowtitle'])
            year = re.findall('(\d{4})', premiered)[0]
            season = '%01d' % int(season)
            episode = '%01d' % int(episode)

            try:
                query = '%s season %01d' % (data['tvshowtitle'], int(season))
                query = base64.b64decode(self.search_link) % urllib.quote_plus(query)

                result = client.source(query)
                result = json.loads(result)['results']

                r = [(i['url'], i['titleNoFormatting']) for i in result]
                r = [(i[0], re.findall('(?:^Watch Full "|^Watch |)(.+)', i[1])) for i in r]
                r = [(i[0], i[1][0]) for i in r if len(i[1]) > 0]
                r = [(i[0], re.findall('(.+?) - Season (\d*)', i[1])) for i in r]
                r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if len(i[1]) > 0]
                r = [(re.sub('http.+?//.+?/','', i[0]), i[1], i[2]) for i in r]
                r = [('/'.join(i[0].split('/')[:2]), i[1], i[2]) for i in r]
                r = [x for y,x in enumerate(r) if x not in r[:y]]
                r = [i for i in r if tvshowtitle == cleantitle.get(i[1])]
                r = [i[0] for i in r if season == '%01d' % int(i[2])]

                for i in r:
                    url = self._info(i, year)
                    if not url == None: return '%s?episode=%01d' % (url, int(episode))
            except:
                pass

            try:
                query = self.search2_link % urllib.quote_plus(data['tvshowtitle'])
                query = urlparse.urljoin(self.base_link, query)

                result = cloudflare.source(query)

                r = client.parseDOM(result, 'div', attrs = {'class': 'ml-item'})
                r = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r]
                r = [(i[0][0], i[1][-1]) for i in r if len(i[0]) > 0 and len(i[1]) > 0]
                r = [(i[0], re.findall('(.+?) - Season (\d*)', i[1])) for i in r]
                r = [(i[0], i[1][0][0], i[1][0][1]) for i in r if len(i[1]) > 0]
                r = [(re.sub('http.+?//.+?/','', i[0]), i[1], i[2]) for i in r]
                r = [('/'.join(i[0].split('/')[:2]), i[1], i[2]) for i in r]
                r = [x for y,x in enumerate(r) if x not in r[:y]]
                r = [i for i in r if tvshowtitle == cleantitle.get(i[1])]
                r = [i[0] for i in r if season == '%01d' % int(i[2])]

                for i in r:
                    url = self._info(i, year)
                    if not url == None: return '%s?episode=%01d' % (url, int(episode))
            except:
                pass

        except:
            return


    def _info(self, url, year):
        try:
            url = urlparse.urljoin(self.base_link, url)
            url = urlparse.urlparse(url).path
            url = client.replaceHTMLCodes(url)
            url = url.encode('utf-8')

            u = urlparse.urljoin(self.base_link, self.info_link)
            u = u % re.findall('(\d+)', url)[-1]
            u = cloudflare.source(u)
            u = client.parseDOM(u, 'div', attrs = {'class': 'jt-info'})[0]
            if year == u: return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            url = urlparse.urljoin(self.base_link, url)
            url = referer = url.replace('/watching.html', '')

            content = re.compile('(.+?)\?episode=\d*$').findall(url)
            content = 'movie' if len(content) == 0 else 'episode'

            try: url, episode = re.compile('(.+?)\?episode=(\d*)$').findall(url)[0]
            except: pass

            url = urlparse.urljoin(self.base_link, url) + '/watching.html'

            result = cloudflare.source(url)
            movie = client.parseDOM(result, 'div', ret='movie-id', attrs = {'id': 'media-player'})[0]

            try: quality = client.parseDOM(result, 'span', attrs = {'class': 'quality'})[0].lower()
            except: quality = 'hd'
            if quality == 'cam' or quality == 'ts': quality = 'CAM'
            elif quality == 'hd': quality = 'HD'
            else: quality = 'SD'

            url = '/movie/loadepisodes/%s' % movie
            url = urlparse.urljoin(self.base_link, url)

            result = cloudflare.source(url)

            r = client.parseDOM(result, 'div', attrs = {'class': 'les-content'})
            r = zip(client.parseDOM(r, 'a', ret='onclick'), client.parseDOM(r, 'a', ret='episode-id'), client.parseDOM(r, 'a'))
            r = [(re.sub('[^0-9]', '', i[0].split(',')[0]), re.sub('[^0-9]', '', i[0].split(',')[-1]), i[1], ''.join(re.findall('(\d+)', i[2])[:1])) for i in r]
            r = [(i[0], i[1], i[2], i[3]) for i in r]

            if content == 'episode':
                r = [i for i in r if i[3] == '%01d' % int(episode)]
            else: 
                b = client.parseDOM(result, 'div', ret='data-episodes', attrs = {'id': 'server-backup'})
                b = [re.findall('(.+?)-(.+)', i) for i in b]
                r += [('99', i[0][1], i[0][0], '720') for i in b if len(i) > 0]


            direct_link = '/ajax/load_episode/%s/%s'

            embed_link = '/ajax/load_embed/%s/%s'

            links = []
            links += [{'source': 'gvideo', 'url': direct_link % (i[2], i[1]), 'direct': True} for i in r if 2 <= int(i[0]) <= 11]
            links += [{'source': 'cdn', 'url': direct_link % (i[2], i[1]), 'direct': True} for i in r if i[0] == '99']
            links += [{'source': 'openload.co', 'url': embed_link % (i[2], i[1]), 'direct': False} for i in r if i[0] == '14']
            links += [{'source': 'videomega.tv', 'url': embed_link % (i[2], i[1]), 'direct': False} for i in r if i[0] == '13']
            links += [{'source': 'videowood.tv', 'url': embed_link % (i[2], i[1]), 'direct': False} for i in r if i[0] == '12']

            for i in links: sources.append({'source': i['source'], 'quality': quality, 'provider': 'Onemovies', 'url': i['url'], 'direct': i['direct'], 'debridonly': False})

            return sources
        except:
            return sources


    def resolve(self, url):
        try:
            url = urlparse.urljoin(self.base_link, url)
            result = cloudflare.source(url)
        except:
            pass

        try:
            url = re.compile('"?file"?\s*=\s*"(.+?)"\s+"?label"?\s*=\s*"(\d+)p?"').findall(result)
            url = [(int(i[1]), i[0]) for i in url]
            url = sorted(url, key=lambda k: k[0])
            url = url[-1][1]

            url = client.request(url, output='geturl')
            if 'requiressl=yes' in url: url = url.replace('http://', 'https://')
            else: url = url.replace('https://', 'http://')
            return url
        except:
            pass

        try:
            url = re.compile('file\s*=\s*"(.+?)"').findall(result)[0]
            if self.base_link in url: raise Exception()
            url = client.replaceHTMLCodes(url)
            return url
        except:
            pass

        try:
            url = json.loads(result)['embed_url']
            return url
        except:
            pass


