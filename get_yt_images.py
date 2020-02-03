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
    videos = ['7UGx_s0Fpqo','WCiXUIDAh4U','SXGBxiAwABc','hBRkpR3DdbA','_ZM1xMqnJlE','RPlyRw3j_3M','w2iOAdE8sRE','h2Z09gOOOJg','UyPSJoMz0to','OtD017CUjz0','T7rnr0GQoCs','Qie7JSJUHRg','NamfsCgmYfo','eB2DuJaTPwU','A0ZIYlhf_k0','uLRIo8EIuY8','zHklYW13t5o','jbYse34ScmA','FMOaEfd5n8E','q6_GBf_US0M','bKgvjuhMJFY','-QOFOXw25P8','YndLXDVyV-g','O78jCdLCHsg','E8FiOwJO5sk','yITUudS1SX0','ZrT_4eEA2Iw','-LG2HoO9ZWo','vhuJrqT-9AY','osNs6vHU1ec','KeTAxbWX9VE','94zYRC16yVA','-iT4a2Mpf0M','xzbUuVoHRdI','6D_748NIlkE']

    for v in videos:
        
        url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(v)
     
        myfile = requests.get(url)
     
        open('images/{}.jpg'.format(v), 'wb').write(myfile.content)
        print('Saved {}.jpg'.format(v))

    print('done')

if __name__== "__main__":
    main()