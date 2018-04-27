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

addonID = 'plugin.video.kodiyoutubers'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "UCuSdObYHdjize3ziP951org"
YOUTUBE_CHANNEL_ID_2 = "UCZuZ4D4WGmyCLlWkgXvqqEg"
YOUTUBE_CHANNEL_ID_3 = "UCb5DkdbEOBNoOY7RGkGN4pg"
YOUTUBE_CHANNEL_ID_4 = "UCr_wSx5sZh5ydPzf7jOS7ZQ"
YOUTUBE_CHANNEL_ID_5 = "UCgRxR05Lmy_KVVW5I0PcTDA"
YOUTUBE_CHANNEL_ID_6 = "UC9cSIEYg1sU5kpeCKhm_FBA"
YOUTUBE_CHANNEL_ID_7 = "UCUY5BYXIaZoa4-HclwnNWDA"
YOUTUBE_CHANNEL_ID_8 = "UClCRMB8kKz_-7funCdGdWLg"
YOUTUBE_CHANNEL_ID_9 = "UCGd9srwfA7kn4GuKfMqWbMQ"
YOUTUBE_CHANNEL_ID_10 = "UCx55aM88WDVMS-AR_q_VKUg"
YOUTUBE_CHANNEL_ID_11 = "UC18WQbNSfrqxlIjKeIW3bGQ"
YOUTUBE_CHANNEL_ID_12 = "UC0QRG-gMqHhF5-BPdmJfs1w"
YOUTUBE_CHANNEL_ID_13 = "UCIXdDyP0vUfFowI9n9M2WFg"
YOUTUBE_CHANNEL_ID_14 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_15 = "UCYl26CDTQ4yGPr768C8LtFQ"
YOUTUBE_CHANNEL_ID_16 = "UCgYI_a85B2wYm6CPH56a77g" 
YOUTUBE_CHANNEL_ID_17 = "UC00Jx1zkJloh2Ow0ubv4mfQ"
YOUTUBE_CHANNEL_ID_18 = "UCNO939DaqD5o-8Y2KWIWZXg"
YOUTUBE_CHANNEL_ID_19 = "UCWJ3sjHCtaO240IYKueqkNw"
YOUTUBE_CHANNEL_ID_20 = "UCOQVoYzsSlRnDNIBWe2dY4g"
YOUTUBE_CHANNEL_ID_21 = "UCTcmpCCEk6q0ovCrHANZoUw"
YOUTUBE_CHANNEL_ID_22 = "UC4unx6bvKRXP8EZ4LQvtT8g"
YOUTUBE_CHANNEL_ID_23 = "UC8Vs1m9YmDBQHGMicqzg9OA"
YOUTUBE_CHANNEL_ID_24 = "UCrS-4eNHy0t5Ud_IDipurmg"
YOUTUBE_CHANNEL_ID_25 = "UCFzeyifP-7nbeq4e6X1x5vw"
YOUTUBE_CHANNEL_ID_26 = "UC8IdNL6nD0UVJ82RzfMwjWQ"
YOUTUBE_CHANNEL_ID_27 = "UCvXiYqrB6P30yGpqMjFqExQ"
YOUTUBE_CHANNEL_ID_28 = "UC4aBkc35BUp_XR4J3TtRgtA"
YOUTUBE_CHANNEL_ID_29 = "UCOjHrylJ3-y-D0h9JUM-vLQ"
YOUTUBE_CHANNEL_ID_30 = "UC_RuE2MikI2QF4qYnUPr09g"
YOUTUBE_CHANNEL_ID_31 = "UCBuW46qJ0vOlzGheIyqK2xg"
YOUTUBE_CHANNEL_ID_32 = "UC1m4Spt5zrKpz77F1WuD2nQ"
YOUTUBE_CHANNEL_ID_33 = "UCK5sxkF-peyiVHO_ltHjipg"
YOUTUBE_CHANNEL_ID_34 = "UC-IyE0ceB6COHSGd_ItcWiA"
YOUTUBE_CHANNEL_ID_35 = "UCypHJluApWqOtke0HY28gDQ"
YOUTUBE_CHANNEL_ID_36 = "UCQZcmkkx7hc0ik4wjaAtINQ"
YOUTUBE_CHANNEL_ID_37 = "UCpEeeUjodpy2DnID-wdDY-w"
YOUTUBE_CHANNEL_ID_38 = "UCoMOQDEEBECQ81CdojuEqfg"
YOUTUBE_CHANNEL_ID_39 = "UCNpGTnUm6xVUWxfOe3GEBVQ"
YOUTUBE_CHANNEL_ID_40 = "UCKRic5GN63gWXc2MsWaRUHA"
YOUTUBE_CHANNEL_ID_41 = "UCVyBXMQLmUT77OHCVg52UdA"
YOUTUBE_CHANNEL_ID_42 = "UCFOStcorp34JSwYTaTZB1oQ"
YOUTUBE_CHANNEL_ID_43 = "UCTSfSNhVOXAHtvBTCcUzJAA"
YOUTUBE_CHANNEL_ID_44 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_45 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_46 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_47 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_48 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_49 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_50 = "UCvdVr9UCntCxe--bSroEeBQ"
YOUTUBE_CHANNEL_ID_51 = "UCvdVr9UCntCxe--bSroEeBQ"








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
        title="Solo Man",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-YUHW44PfRLU/AAAAAAAAAAI/AAAAAAAAAAA/TMK9xizbGJU/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JoeNobody010101",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-yyi7bfBAFdM/AAAAAAAAAAI/AAAAAAAAAAA/YZtjGJ9XsYo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Husham Memar",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-7MqMXmT3DR8/AAAAAAAAAAI/AAAAAAAAAAA/bfs3l0wg6u4/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Simply Caz",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-swGWsXGqbbA/AAAAAAAAAAI/AAAAAAAAAAA/GnwcHOLcYfo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Touchtone",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-PZf6tIaQqC4/AAAAAAAAAAI/AAAAAAAAAAA/LWrigWjcmcE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pro N Cons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-m901ribHIZ4/AAAAAAAAAAI/AAAAAAAAAAA/uNxYAVowRDU/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Dimitrology",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-gc8RvvduE-E/AAAAAAAAAAI/AAAAAAAAAAA/7YIGzK1cPME/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Lee TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-FnE4cQB7d-o/AAAAAAAAAAI/AAAAAAAAAAA/nHsRjgm55CY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="Kodi Heaven",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-Le-Q_Ny4ulU/AAAAAAAAAAI/AAAAAAAAAAA/3LqlYCWMdP4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
		folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="MeacePeace -Kodi Tutorials-",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-FJG-6RzIfqY/AAAAAAAAAAI/AAAAAAAAAAA/Va7CqtdjKgA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ASBYT",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-OMUC1O8NtyI/AAAAAAAAAAI/AAAAAAAAAAA/cPrpjgnjkdE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Top Tutorials",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-Qko8gm9_ncI/AAAAAAAAAAI/AAAAAAAAAAA/rDkvFqRYVUs/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )			

    plugintools.add_item( 
        #action="", 
        title="TARGETin1080P",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-BbCESrp7T_g/AAAAAAAAAAI/AAAAAAAAAAA/vYLUjXW1d2A/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="TARGETin1080P (Original)",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-wCgQEzXoRCc/AAAAAAAAAAI/AAAAAAAAAAA/uAY_iWuNosk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dexter Tv",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-UCQeDgi7HOc/AAAAAAAAAAI/AAAAAAAAAAA/emdw4Gam1IU/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="My Kodi",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-XZ4B4MqoYdo/AAAAAAAAAAI/AAAAAAAAAAA/zAXSx2gBOFA/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Gen TeC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-W0BrnKYJ-bA/AAAAAAAAAAI/AAAAAAAAAAA/XJ8P9GXM4tc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="GAM3RDS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-I0CSDReNHGE/AAAAAAAAAAI/AAAAAAAAAAA/IeJjaggdC-c/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="KODI SOLUTIONS",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-EuxUdKKs8xI/AAAAAAAAAAI/AAAAAAAAAAA/NghEpit0kAk/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="newtechevolution",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-Rn4z3ys8mIs/AAAAAAAAAAI/AAAAAAAAAAA/yPQtOUwwQKw/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="KRAZ inabox",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-cRThFqx7f4s/AAAAAAAAAAI/AAAAAAAAAAA/gEQAOW5hXPQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Kodi Latino",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-_hA6h23QE0c/AAAAAAAAAAI/AAAAAAAAAAA/ub6BUSWtzXQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Acosta XBMC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-r8WbLIryyAU/AAAAAAAAAAI/AAAAAAAAAAA/0KWNwqjB8yM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Freeworld Entertaiment",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-INUL15rMSa0/AAAAAAAAAAI/AAAAAAAAAAA/bExtHCNbrus/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Ariel Cintron",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-l3Vw3rxLNuo/AAAAAAAAAAI/AAAAAAAAAAA/XTbfqg2HjjQ/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="DaHenchmen Soulless",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-T5R891izvqc/AAAAAAAAAAI/AAAAAAAAAAA/yj2lp7_d1rs/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Savy Techgirl",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-4njccu-t--I/AAAAAAAAAAI/AAAAAAAAAAA/c6Enzfl1DkM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	
	
    plugintools.add_item( 
        #action="", 
        title="Mari's Review Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-Il4L8s9hUzg/AAAAAAAAAAI/AAAAAAAAAAA/jtgMLCZX9bE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		
		
		
    plugintools.add_item( 
        #action="", 
        title="XK MC",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-MO6brQ3gbCw/AAAAAAAAAAI/AAAAAAAAAAA/LTV3CPPI8U4/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	
		
    plugintools.add_item( 
        #action="", 
        title="KODI PRO",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-J1vHQwzPccc/AAAAAAAAAAI/AAAAAAAAAAA/QnhsbFhfPqo/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="KRATOS002",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-iBJF_OMuGU0/AAAAAAAAAAI/AAAAAAAAAAA/OeyeFdfVUME/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="XKMC Sin Music",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-H5pmS5w_E6s/AAAAAAAAAAI/AAAAAAAAAAA/tJRJG0b5Sas/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="elchispaartista",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-K7Y2OuJX6lU/AAAAAAAAAAI/AAAAAAAAAAA/cix9zelpcos/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Kodiline 007",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-DQJA3XUuDTE/AAAAAAAAAAI/AAAAAAAAAAA/5v8qeIkY6vc/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="CW",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-aoUNR6TihRQ/AAAAAAAAAAI/AAAAAAAAAAA/WtycToVTka8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Peter Carcione",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-ILSynlg95ME/AAAAAAAAAAI/AAAAAAAAAAA/NUXKGDZ9LA8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="The5thAvenueProject",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-jh9z8wAJlEY/AAAAAAAAAAI/AAAAAAAAAAA/PDbeXRAOqco/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Tech Timeruuu",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-xrpSGZutUms/AAAAAAAAAAI/AAAAAAAAAAA/WoCkFC1pt8Q/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="CSSC0DER",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-3roPe7rO4bU/AAAAAAAAAAI/AAAAAAAAAAA/kb_I0Ga4gaM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Chris Blower",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-cHYQjzYx_3k/AAAAAAAAAAI/AAAAAAAAAAA/4U46z5I0vyM/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	


    plugintools.add_item( 
        #action="", 
        title="Hackelodeon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-XhfQrXxyvAs/AAAAAAAAAAI/AAAAAAAAAAA/llQdScQrAsE/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Doc Squiffy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-nYgh3GLcdyc/AAAAAAAAAAI/AAAAAAAAAAA/eseha30N5uY/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )	

    plugintools.add_item( 
        #action="", 
        title="Jasonmoore85",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-rzWOMM2Ols4/AAAAAAAAAAI/AAAAAAAAAAA/88W2kITY5o8/s100-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )						
run()