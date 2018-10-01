# -*- coding: utf-8 -*-

""" ^ SECTION 1:
    This should be at the top of your code to declare the type of text
    format you're using. Without this you may find some text editors save
    it in an incompatible format and this can make bug tracking extremely
    confusing! More info here: https://www.python.org/dev/peps/pep-0263/
"""

#----------------------------------------------------------------

"""
    SECTION 2:
    This is where you'd put your license details, the GPL3 license 
    is the most common to use as it makes it easy for others to fork
    and improve upon your code. If you're re-using others code ALWAYS
    check the license first, removal of licenses is NOT allowed and you
    generally have to keep to the same license used in the original work
    (check license details as some do differ).

    Although not all licenses require it (some do, some don't),
    you should always give credit to the original author(s). Someone may have spent
    months if not years on the code so really it's the very least you can do if
    you choose to use their work as a base for your own.
"""
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Addon: My YouTube Add-on
# Author: Add your name here

#----------------------------------------------------------------

"""
    SECTION 3:
    This is your global imports, any modules you need to import code from
    are added here. You'll see a handful of the more common imports below.
"""
import os           # access operating system commands
import xbmc         # the base xbmc functions, pretty much every add-on is going to need at least one function from here
import xbmcaddon    # pull addon specific information such as settings, id, fanart etc.
import xbmcplugin   # contains functions required for creating directory structure style add-ons (plugins)

# The following are often used, we are not using them in this particular file so they are commented out

# import re           # allows use of regex commands, if you're intending on scraping you'll need this
# import xbmcgui      # gui based functions, contains things like creating dialog pop-up windows

from koding import route, Addon_Setting, Add_Dir, Find_In_Text, Open_URL, OK_Dialog
from koding import Open_Settings, Play_Video, Run, Text_File

ADDON = xbmcaddon.Addon()

#------------------------------------------------------------


def setView(content, viewType):
  # set content type so library shows more views and info
  if content:
    xbmcplugin.setContent(int(sys.argv[1]), content)
  if ADDON.getSetting('auto-view')=='true':
    xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )

"""
    SECTION 4:
    These are our global variables, anything we set here can be accessed by any of
    our functions later on. Please bare in mind though that if you change the value
    of a global variable from inside a function the value will revert back to the
    value set here once that function has completed.
"""
debug        = Addon_Setting(setting='debug')       # Grab the setting of our debug mode in add-on settings
addon_id     = xbmcaddon.Addon().getAddonInfo('id') # Grab our add-on id

# Set the base plugin url you want to hook into
BASE  = "plugin://plugin.video.youtube/playlist/"
BASE2 = "plugin://plugin.video.youtube/channel/"

# Set each of your YouTube playlist id's
YOUTUBE_CHANNEL_ID_1 = "UC5vVe2R4ucoMzJP53o38Yaw"
YOUTUBE_CHANNEL_ID_2 = "UCbCmjCuTUZos6Inko4u57UQ"
YOUTUBE_CHANNEL_ID_3 = "UC7Pq3Ko42YpkCB_Q4E981jw"
YOUTUBE_CHANNEL_ID_4 = "UClB5W7RGrG1QSTdS0jZ21Rg"
YOUTUBE_CHANNEL_ID_5 = "UCPdxa631-MvtSXGGJuhGuxw"
YOUTUBE_CHANNEL_ID_6 = "UCdF_AO4sEh80l6J7T_XTsRg"
YOUTUBE_CHANNEL_ID_7 = "UC-exISJxZ6hYgRSJVKshpeA"
YOUTUBE_CHANNEL_ID_8 = "UCpzYfBXbEHHQHU2e89jM9Tg"
YOUTUBE_CHANNEL_ID_9 = "UCeA2JrCAqRohEHHwAFJNY4Q"
YOUTUBE_CHANNEL_ID_10 = "UCaeCuyKgxngpD4DXoYwQRwQ"
YOUTUBE_CHANNEL_ID_11 = "UCviIx9YkgPfh3SFEEp5jvRQ"
YOUTUBE_CHANNEL_ID_12 = "UCfHiKU6BIcBfDbeb_ChRNEw"
YOUTUBE_CHANNEL_ID_13 = "UCelMeixAOTs2OQAAi9wU8-g"
YOUTUBE_CHANNEL_ID_14 = "UCJkWoS4RsldA1coEIot5yDA"
YOUTUBE_CHANNEL_ID_15 = "UC6zPzUJo8hu-5TzUk8IEC2Q"
YOUTUBE_CHANNEL_ID_16 = "UCyTcCCMxgmVF9-AjBX2n0PQ"
YOUTUBE_CHANNEL_ID_17 = "UCLsooMJoIpl_7ux2jvdPB-Q"
YOUTUBE_CHANNEL_ID_18 = "UCp5Nhw2YMCMUemXC1oWTkkA"
YOUTUBE_CHANNEL_ID_19 = "UCdIWg_E1ckuONPTsdvevYgg"
YOUTUBE_CHANNEL_ID_20 = "UC56cowXhoqRWHeqfSJkIQaA"
YOUTUBE_CHANNEL_ID_21 = "UCKAqou7V9FAWXpZd9xtOg3Q"
YOUTUBE_CHANNEL_ID_22 = "UCewxcWJd20P0dzo-Fk0xWdg"
YOUTUBE_CHANNEL_ID_23 = "UCqr8yqX8vkk63PMoZKA1WzA"
YOUTUBE_CHANNEL_ID_24 = "UC8MR0wSTbzs5Yo7DgP04P-w"
YOUTUBE_CHANNEL_ID_25 = "UC4NALVCmcmL5ntpV0thoH6w"
YOUTUBE_CHANNEL_ID_26 = "UC4Oevb0i629FblbJ664Xagg"
YOUTUBE_CHANNEL_ID_27 = "UCMwg6tc7GuEgY6wRmsj7FrQ"
YOUTUBE_CHANNEL_ID_28 = "UC7Gf2tZ8coTX2ckTPgn62iQ"
YOUTUBE_CHANNEL_ID_29 = "UCNcdbMyA59zE-Vk668bKWOg"
YOUTUBE_CHANNEL_ID_30 = "UCJ-Ociya7ri8MKx1O5jCIKQ"
YOUTUBE_CHANNEL_ID_31 = "UClkUrNgGC4BD6pWURJbM9MQ"
YOUTUBE_CHANNEL_ID_32 = "UCnw5-9L8krhCmrZAjO6wO3g"
YOUTUBE_CHANNEL_ID_33 = "UC4NALVCmcmL5ntpV0thoH6w"
YOUTUBE_CHANNEL_ID_34 = "UCtgpDqkeOToveUgh8igrvXQ"
#----------------------------------------------------------------

"""
    SECTION 5:
    Add our custom functions in here, it's VERY important these go in this section
    as the code in section 6 relies on these functions. If that code tries to run
    before these functions are declared the add-on will fail.

    You'll notice each function in here has a decorator above it (an @route() line of code),
    this assigns a mode to the function so it can be called with Add_Dir and it also tells
    the code what paramaters to send through. For example you'll notice the Main_Menu() function
    we've assigned to the mode "main" - this means if we ever want to get Add_Dir to open that
    function we just use the mode "main". This particular function does not require any extra
    params to be sent through but if you look at the Simple_Dialog() function you'll see we send through
    2 different paramaters (title and msg), if you look at the Add_Dir function in Main_Menu()
    on line 106 you'll see we've sent these through as a dictionary. Using that same format you can send
    through as many different params as you wish.
"""

#----------------------------------------------------------------
# This is the main menu we open into
@route(mode='main_menu')
def Main_Menu():

# If debug mode is enabled show the koding tutorials
    # if debug == 'true':
    #     Add_Dir ( '[COLOR=lime]Koding Tutorials[/COLOR]', '', "tutorials", True, '', '', '' )
    # else:
    #     Add_Dir ( '[COLOR=lime]Enable debug mode for some cool dev tools![/COLOR]', '', "koding_settings", False, '', '', '' )
    
# An example title/message we're going to send through to a popup dialog in the first Add_Dir item
    my_message= "{'title' : 'Youtube Kids', 'msg' : \" If you click On Playlists in the sections within this addon you will get even more content\"}"

    Add_Dir(
        name="Important Infomation", url=my_message, mode="simple_dialog", folder=False,
        icon="https://cdn2.iconfinder.com/data/icons/picons-basic-2/57/basic2-087_info-512.png")
        
# Add some YT Playlists (see we're using BASE as the url)
    Add_Dir( 
        name="The Wiggles", url=BASE2+YOUTUBE_CHANNEL_ID_1+"/", folder=True,
        icon="https://yt3.ggpht.com/-m0-rgNGYBUo/AAAAAAAAAAI/AAAAAAAAAAA/pOL1ZD7ef5s/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="ABCkidTV - Nursery Rhymes ", url=BASE2+YOUTUBE_CHANNEL_ID_2+"/", folder=True,
        icon="https://yt3.ggpht.com/-gn0wGBOL4hE/AAAAAAAAAAI/AAAAAAAAAAA/RRCSsKhYNL8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Kids ABC TV - Kindergarten Songs & Nursery Rhymes", url=BASE2+YOUTUBE_CHANNEL_ID_10+"/", folder=True,
        icon="https://yt3.ggpht.com/-lmb7DtfTiRc/AAAAAAAAAAI/AAAAAAAAAAA/PU53XacjZYE/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Kids TV", url=BASE2+YOUTUBE_CHANNEL_ID_3+"/", folder=True,
        icon="https://yt3.ggpht.com/-Vas4UzOl0KE/AAAAAAAAAAI/AAAAAAAAAAA/_fWZBwq0qnA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Super Car Super Star", url=BASE2+YOUTUBE_CHANNEL_ID_4+"/", folder=True,
        icon="https://yt3.ggpht.com/-GhKj2aV_QYQ/AAAAAAAAAAI/AAAAAAAAAAA/z9LZSDN7xNU/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Road Rangers", url=BASE2+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
        icon="https://yt3.ggpht.com/-7aN80TWh5xA/AAAAAAAAAAI/AAAAAAAAAAA/PstSKoXZl3g/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Haunted House Monster Truck", url=BASE2+YOUTUBE_CHANNEL_ID_6+"/", folder=True,
        icon="https://yt3.ggpht.com/-2iVPeXEcrs8/AAAAAAAAAAI/AAAAAAAAAAA/s3I750wRY3U/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Baby Cars TV", url=BASE2+YOUTUBE_CHANNEL_ID_7+"/", folder=True,
        icon="https://yt3.ggpht.com/-HaiJISRArdc/AAAAAAAAAAI/AAAAAAAAAAA/m77-kxw9FKI/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Little Treehouse", url=BASE2+YOUTUBE_CHANNEL_ID_8+"/", folder=True,
        icon="https://yt3.ggpht.com/-GfhxHDqs2MQ/AAAAAAAAAAI/AAAAAAAAAAA/0ECyYx6tStU/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="ABC Heros", url=BASE2+YOUTUBE_CHANNEL_ID_9+"/", folder=True,
        icon="https://yt3.ggpht.com/-LZSyBktI1MA/AAAAAAAAAAI/AAAAAAAAAAA/i2lBdeBOcKI/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")


    Add_Dir( 
        name="Toys In Action", url=BASE2+YOUTUBE_CHANNEL_ID_11+"/", folder=True,
        icon="https://yt3.ggpht.com/-vgUxzVy4uro/AAAAAAAAAAI/AAAAAAAAAAA/wA4_ddGBiXc/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Toddlers Playroom", url=BASE2+YOUTUBE_CHANNEL_ID_12+"/", folder=True,
        icon="https://yt3.ggpht.com/-sfXMq3XDRyo/AAAAAAAAAAI/AAAAAAAAAAA/Rs1updH3GKg/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="CookieSwirlC", url=BASE2+YOUTUBE_CHANNEL_ID_13+"/", folder=True,
        icon="https://yt3.ggpht.com/-oX4t4rxK9ic/AAAAAAAAAAI/AAAAAAAAAAA/zpUPT1t2-Gs/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Mother Goose Club", url=BASE2+YOUTUBE_CHANNEL_ID_14+"/", folder=True,
        icon="https://yt3.ggpht.com/-CjtfMnhAf90/AAAAAAAAAAI/AAAAAAAAAAA/9x0cv1cw3-8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Mother Goose Club Playhouse", url=BASE2+YOUTUBE_CHANNEL_ID_15+"/", folder=True,
        icon="https://yt3.ggpht.com/-7EZ4R90FGWk/AAAAAAAAAAI/AAAAAAAAAAA/EGvKs_ccXVc/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Mother Goose Club: Minecraft", url=BASE2+YOUTUBE_CHANNEL_ID_16+"/", folder=True,
        icon="https://yt3.ggpht.com/-9OiKfoMRmB0/AAAAAAAAAAI/AAAAAAAAAAA/eA6f0c8PxDI/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Super Simple Songs - Kids Songs", url=BASE2+YOUTUBE_CHANNEL_ID_17+"/", folder=True,
        icon="https://yt3.ggpht.com/-nHzSx4QKfsY/AAAAAAAAAAI/AAAAAAAAAAA/o_0k7TejOiI/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Super Simple ABCs", url=BASE2+YOUTUBE_CHANNEL_ID_18+"/", folder=True,
        icon="https://yt3.ggpht.com/-OMmu0IzLnto/AAAAAAAAAAI/AAAAAAAAAAA/pjUOpBUHIik/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Super Simple TV - Kids Shows & Cartoons", url=BASE2+YOUTUBE_CHANNEL_ID_19+"/", folder=True,
        icon="https://yt3.ggpht.com/-6pW4f4RXkIE/AAAAAAAAAAI/AAAAAAAAAAA/L023NSeQw9Y/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Bounce Patrol Kids", url=BASE2+YOUTUBE_CHANNEL_ID_20+"/", folder=True,
        icon="https://yt3.ggpht.com/-P3GrO-qDn8c/AAAAAAAAAAI/AAAAAAAAAAA/WGyon47JL38/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="LittleBabyBum ®", url=BASE2+YOUTUBE_CHANNEL_ID_21+"/", folder=True,
        icon="https://yt3.ggpht.com/-KLfbkE3zovQ/AAAAAAAAAAI/AAAAAAAAAAA/gMZ_6qxvEXw/s176-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Listener Kids", url=BASE2+YOUTUBE_CHANNEL_ID_22+"/", folder=True,
        icon="https://yt3.ggpht.com/-rBViPDkWVZk/AAAAAAAAAAI/AAAAAAAAAAA/Uf3BvZ_rD4Y/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Storybook Nanny", url=BASE2+YOUTUBE_CHANNEL_ID_23+"/", folder=True,
        icon="https://yt3.ggpht.com/-7ff4XikFgBo/AAAAAAAAAAI/AAAAAAAAAAA/OwRaJPIhYiM/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Tic Tac Toy", url=BASE2+YOUTUBE_CHANNEL_ID_24+"/", folder=True,
        icon="https://yt3.ggpht.com/-AnJX1veayrc/AAAAAAAAAAI/AAAAAAAAAAA/ZRoPr61rg14/s100-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="LooLoo Kids - Nursery Rhymes and Children's Songs", url=BASE2+YOUTUBE_CHANNEL_ID_25+"/", folder=True,
        icon="https://yt3.ggpht.com/-5qCvnT93AYI/AAAAAAAAAAI/AAAAAAAAAAA/ehKNTtIwHSM/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Hello Mr. Freckles!", url=BASE2+YOUTUBE_CHANNEL_ID_26+"/", folder=True,
        icon="https://yt3.ggpht.com/-8Q3jgV1D6VU/AAAAAAAAAAI/AAAAAAAAAAA/7p-3COXvaZ4/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Ellen Toy Channel", url=BASE2+YOUTUBE_CHANNEL_ID_27+"/", folder=True,
        icon="https://yt3.ggpht.com/-viy5jTuCN40/AAAAAAAAAAI/AAAAAAAAAAA/p3W_1-VOPm8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Disney Junior UK ", url=BASE2+YOUTUBE_CHANNEL_ID_28+"/", folder=True,
        icon="https://yt3.ggpht.com/-e8lc2AnB-Z8/AAAAAAAAAAI/AAAAAAAAAAA/1kZk7GEiBxA/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Disney Junior", url=BASE2+YOUTUBE_CHANNEL_ID_29+"/", folder=True,
        icon="https://yt3.ggpht.com/-jguhAhy47vM/AAAAAAAAAAI/AAAAAAAAAAA/liAaBp31mDE/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="Radio Disney", url=BASE2+YOUTUBE_CHANNEL_ID_30+"/", folder=True,
        icon="https://yt3.ggpht.com/-uVJDTr6vVJw/AAAAAAAAAAI/AAAAAAAAAAA/_giNRoL37g8/s288-c-k-no-mo-rj-c0xffffff/photo.jpg")

    Add_Dir( 
        name="AWESMR kids", url=BASE2+YOUTUBE_CHANNEL_ID_31+"/", folder=True,
        icon="https://yt3.ggpht.com/-y4Ss2ZuRZwk/AAAAAAAAAAI/AAAAAAAAAAA/JzCUzgy3tfQ/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")

    Add_Dir( 
        name="AwesomeRainbowToys", url=BASE2+YOUTUBE_CHANNEL_ID_32+"/", folder=True,
        icon="https://yt3.ggpht.com/-gqxG9mkdJf4/AAAAAAAAAAI/AAAAAAAAAAA/sjvIpZJSfn8/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")

    Add_Dir( 
        name="LooLoo Kids - Nursery Rhymes and Children's Songs", url=BASE2+YOUTUBE_CHANNEL_ID_33+"/", folder=True,
        icon="https://yt3.ggpht.com/-5qCvnT93AYI/AAAAAAAAAAI/AAAAAAAAAAA/ehKNTtIwHSM/s288-mo-c-c0xffffffff-rj-k-no/photo.jpg")

    Add_Dir( 
        name="KidsTV123", url=BASE2+YOUTUBE_CHANNEL_ID_34+"/", folder=True,
        icon="https://lh3.googleusercontent.com/a-/AN66SAzwYopRgWJo3xy3ABodwRgKxBDJpm6Rdq7Hsg=s176-c-k-c0x00ffffff-no-rj-mo")    
    
    
    setView('movies', 'MAIN')    
    
    

# Add some YT channels (see we're using BASE2 as the url for this one)
#     Add_Dir( 
#         name="Bilderberg Coverage", url=BASE+YOUTUBE_CHANNEL_ID_5+"/", folder=True,
#         icon="https://i.ytimg.com/vi/k7pGPraw1Tc/hqdefault.jpg")
# #----------------------------------------------------------------
# A basic OK Dialog
@route(mode='koding_settings')
def Koding_Settings():
    Open_Settings()
#----------------------------------------------------------------
# A basic OK Dialog
@route(mode='simple_dialog', args=['title','msg'])
def Simple_Dialog(title,msg):
    OK_Dialog(title, msg)
#----------------------------------------------------------------

"""
    SECTION 6:
    Essential if creating list items, this tells kodi we're done creating our list items.
    The list will not populate without this. In the run command you need to set default to
    whatever route you want to open into, in this example the 'main_menu' route which opens the
    Main_Menu() function up at the top.
"""
if __name__ == "__main__":
    Run(default='main_menu')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))