import xbmcaddon, base64

Decode = base64.decodestring
MainBase = (Decode('aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2tvZGl3aXphcmQvY2hyaXN0bWFzLWFkZG9uL21hc3Rlci9tZW51L21lbnUueG1s'))
addon = xbmcaddon.Addon('plugin.video.christmas01010')