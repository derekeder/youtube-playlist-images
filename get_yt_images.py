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
    videos = ['iRORcIdDF-g',
'efmZgEZsOCE',
'ekrbOwXgXUU',
'QsCRMzm4LX4',
'EpaZU_uKGTU',
'ao3_EA4Sac4',
'XgLdH6s-r8c',
'wofivGCqBTk',
'VFLcumbYvuE',
'7AkM3HATY5U',
'U-_BzpLAuWw',
'K3PogIoCpNY',
'Ibf10cGh2Xc',
'FjgR_M0qLpA',
'G-HR0KWgem8',
'incubFkdwls',
'zHjCP9jguSk',
'V_hYausllbU',
'd_AvOY9By94',
'M4D3h7lXeh8',
'kwz_4UtFv_w',
'zSXdgHVkvWc',
'NA8UyqrM0gI',
'ai8L9JaUsEI',
'z7GEStD6KdM',
'3jANRAGWbJU',
'ACtzJFyHsMQ',
'vePlebqCBq8',
'wA3jmdcu9aU',
'XNbWmQLH0rk',
'46u-apZmwBQ',
'_weWs0M7Tis',
'zp5dHWnk2NE',
'nkAQbKFTBoM']

    for v in videos:
        
        url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(v)
     
        myfile = requests.get(url)
     
        open('images/{}.jpg'.format(v), 'wb').write(myfile.content)
        print('Saved {}.jpg'.format(v))

    print('done')

if __name__== "__main__":
    main()