import xbmcgui,xbmcplugin

plugin_handle = int(sys.argv[1])
_id = 'plugin.video.vodpass'
_icondir = "special://home/addons/" + _id + "/icons/"

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

# IPTV
add_video_item('http://tscstreaming-lh.akamaihd.net/i/TSCLiveStreaming_1@91031/index_3_av-p.m3u8',{ 'title': 'The Shopping Channel HD'}, '%s/tsc.png'% _icondir)
add_video_item('http://llnw.live.simplestream.com/coder5/coder.channels.channel2/hls/2/playlist.m3u8',{ 'title': 'truTVtruTV'}, '%s/tsc.png'% _icondir)
add_video_item('http://esioslive6-i.akamaihd.net/hls/live/202874/AL_P_ESP1_INTER_ENG/playlist_1800.m3u8',{ 'title': 'Eurosports'}, '%s/tsc.png'% _icondir)

# TV Shows
add_video_item('http://augrime.de/tv/BitMeTV/supergirl.106.hdtv-lol.mp4',{ 'title': 'Supergirl s01e06'}, '%s/cpac-english.png'% _icondir)
add_video_item('http://augrime.de/tv/BitMeTV/Ray.Donovan.S01.INTERNAL.HDTV.x264-BitMeTV/ray.donovan.s01e01.hdtv.x264.evolve.mp4',{ 'title': 'Ray Donovan S01SE1'}, '%s/cpac-english.png'% _icondir)

# Movies
add_video_item('http://178.162.214.232/vod/movies/english/The5thWave2016.mp4',{ 'title': 'The 5th Wave 2016'}, '%s/sportsnet_360.png'% _icondir)
add_video_item('http://178.162.214.232/vod/movies/english/TheTransporterRefueled.mp4',{ 'title': 'The Transporter Refueled'}, '%s/tsn_1.png'% _icondir)



xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

