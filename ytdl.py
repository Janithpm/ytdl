
import os
try:
        import youtube_dl
        import ffmpeg
except:
        print('Trying to download and install requred module : youtube_dl')
        os.system('python -m pip install youtube_dl')
        os.system('python -m pip install ffmpeg')
        import youtube_dl
        import ffmpeg

url = input('Enter the URL : ')
path = './%(playlist_title)s/%(title)s.%(ext)s'

while True:
	vformat = input('Select video quality (720p/360p/audio) : ')

	if vformat == '720p':
		sub = input('Download auto genarated subtitle (y/n) : ')
		if sub == 'y':
			output = {'format':'best', 'writeautomaticsub':True, 'outtmpl':path}
			break
		elif sub == 'n':
			output = {'format':'best', 'writeautomaticsub':False, 'outtmpl':path}
			break
		else:
			print('Error : Invalied selection. Try again.')
			continue
	elif vformat == '360p':
		sub = input('Download auto genarated subtitle (y/n) : ')
		if sub == 'y':
			output = {'format':'worst', 'writeautomaticsub':True, 'outtmpl':path}
			break
		elif sub == 'n':
			output = {'format':'worst', 'writeautomaticsub':False, 'outtmpl':path}
			break
		else:
			print('Error : Invalied selection. Try again.')
			continue
	elif vformat == 'audio':
		output = {'format':'bestaudio/best', 'outtmpl':path}
		break
	else:
		print('Error : Invalied selection. Try again.')
		continue

if len(url) != 0:
	with youtube_dl.YoutubeDL(output) as y:
		y.download([url])

else:
	print('Invalied URL.')
