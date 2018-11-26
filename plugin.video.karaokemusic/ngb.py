# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Sourced From Online Templates And Guides
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Thanks To: Google Search For This Template
# Modified: NGB
#
#
# to find url of channel view channel source then find data-channel-external-id=
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.karaokemusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "UCPNEsIoorK2GsBSJ4O4hlQw"
YOUTUBE_CHANNEL_ID_2 = "UCjCBQdXHbIJ_u2Wm-WMb9ow"
YOUTUBE_CHANNEL_ID_3 = "UCCNirCgrJmpONpinbBOiFog"
YOUTUBE_CHANNEL_ID_4 = "UCaPwSXblS8F0owlKHGc6huw"
YOUTUBE_CHANNEL_ID_5 = ""








# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="RLucra Karaoke TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAwn4RQvE3MSWAUFBsDkDy1g0t4gn4JTzOsa=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Karaoke Hits Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAyoKku1xmhMvq8FgCKeh8TdX2QVw5zLAMNLVw=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MyKaraoke Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAx3I7r6IbXjsbtKfVEI5ATrPDgTz30gDIIonQ=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CoversPH",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/a-/AN66SAw5d3ybi4EjvWJBi0fgVip9NEfhNcu1DFvtvw=s288-mo-c-c0xffffffff-rj-k-no",
        folder=True )

   
run()