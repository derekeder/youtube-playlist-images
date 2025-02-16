# get the video id's from a youtube playlist:
# https://developers.google.com/youtube/v3/docs/playlistItems/list?apix_params=%7B%22part%22%3A%22contentDetails%22%2C%22maxResults%22%3A35%2C%22playlistId%22%3A%22PL_dBjjdnIbKyQXLBrIn_LLHTnwR03baW0%22%7D#usage
# curl \
#   'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=35&playlistId=PL_dBjjdnIbKyQXLBrIn_LLHTnwR03baW0&key=[YOUR_API_KEY]' \
#   --header 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
#   --header 'Accept: application/json' \
#   --compressed

# https://img.youtube.com/vi/[YOUTUBE ID]/hqdefault.jpg


import requests

def main():
    print("Fetching images ...")
  
    # list of youtube videos
    videos = ['Y0qx3sKKoFI',
'sI8gzqmRF60',
'JQ_JXa_m7LA',
'anNZrv0jOhY',
'zSLdidnyQJQ',
'42f64RcEuhk',
'XekrMt5CybU',
'r0A9rwJzZg8',
'9lHVj_xc2GQ',
'aK1NMRpn4Vc',
'qE3UnbJWqko',
'xCOD6YjOGlM',
'GycVgfX-NmU',
'7RWyWE1wI8M',
'oXbdxDd_7IA',
'a0v-Eyf2xwg',
'-bKPEp2XWrc',
'Ir6j1WLeUhY',
'-5b2G81MKE0',
'i6pl-b-9pj4',
'beimme-kIFc',
'bCLb8flUHqk',
'duI534HGt2c',
'L2XY4fEGAlM',
'A1ycx-sATQY',
'RdASKfRoUDQ',
'WaAw5dLq3fA',
'_3iaveGz3OE',
'q-bs1Acjqcg',
'4wlZPOMK8GA',
'WwV9r_GfDPM',
'f222uUDvSWE',
'caqqkowV7T8',]

    for v in videos:
        
        url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(v)
     
        myfile = requests.get(url)
     
        open('images/{}.jpg'.format(v), 'wb').write(myfile.content)
        print('Saved {}.jpg'.format(v))

    print('done')

if __name__== "__main__":
    main()