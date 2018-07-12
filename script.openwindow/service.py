import xbmc
from default import WiFi_Check
if xbmc.getInfoLabel('Skin.String(Branding)') != 'off':
    WiFi_Check()