For this to import the necessary modules you must make sure you have the
modules4all repo source added into your very own repo. If you've already
the <a href="http://totalrevolution.tv/create_repo.php" target="_blank">repository creator</a> on this site then it will already be setup, if not
then use it to create a repo and copy the modules4all section into your own repo addon.xml.

If you just want to test locally by installing from zip without having to
commit to your repo then you can just install the noobsandnerds repo as
that has contains all the relevant modules, if you have that installed then
you'll be able to install from zip without missing dependency errors.
The source for the NaN repo is http://noobsandnerds.com/portal

<h3>ONCE ADD-ON IS INSTALLED:</h3>
Go through the default.py and read the comments for each section.
This is a very simple template to follow, all you need to do is add/edit the
YouTube ID's (lines 62-66) - these can be either playlist or channel ID's.

In the Main_Menu() function all you need to edit is the relevant Add_Dir command,
if using a playlist then the url must start with BASE and if it's a channel you need
to use BASE2. In these Add_Dir commands you can edit the title which shows as well as
the artwork.

Have a little play around, it's very fun and easy to do and you'll have
your very own YouTube based add-on up in no time and every time you update your YT
channel/playlist the changes will automatically show in your add-on!!!


<h3>Frequently Asked Questions:</h3>
I want to develop an add-on and make it publicly available, what are my options?
-- You really have 2 options...

   1: Create your own repository and host on somewhere like github (it's free). If you contact the team at noobsandnerds they will happily add your repository to the daily Add-on Portal scan so your add-on can be accessed by the whole Kodi community. If you want them to add your repository zip to their http://noobsandnerds.com/portal source then they will be happy to do so but they only add repos to this source on request (they don't randomly re-upload without consent) so you will have to ask a member of the team. They also offer a great support forum and if you choose to have your add-on officially supported on there you can also join the NaN developer telegram chat where great minds can share ideas and collaborate together on projects. Again if interested please contact a member of the team via the forum.

   2: Just upload this zip file to your own server and add details to the Add-on Portal at http://noobsandnerds.com/addons. Their system allows for standalone zips which do not reside on repositories. This will allow the add-on to be installed via Community Portal but we would recommend using option 1 rather than this method - if you want to be able to push updates then you're really going to want it on a repository. Dealing with support when you only have standalone zips can be extremely hard work as you're never quite sure which version the user has installed, this was a big problem the XBMC foundation resolved a decade ago when they created the repository framework in Kodi (or XBMC as it was then).

Can I use this code commercially?
-- Please look at our TRMC system for commercial options: http://totalrevolution.tv