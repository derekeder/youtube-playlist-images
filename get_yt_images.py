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
    videos = [  
"M5cFfirSE8o",
"y64mJsE9e10",
"vwgnNTD5SLU",
"dteuCm8uEgE",
"Sx6j5slMz3o",
"4nqiD3I_k7o",
"WNeHEQnlohI",
"gee6dop3uJA",
"KuGdBSXA4UM",
"l6DxEOYnTtY",
"Jld4SJGlXsI",
"kyqsJNRaO8k",
"h0pwAr-WYxI",
"MgxCjvHgMl4",
"3_u81ZjGD24",
"tlxAmkG9DVs",
"2mUXMbpErmA",
"1158lO-dowQ",
"Gv0JCgyg1G0",
"NN7nk3xQ9dg",
"QwHigW4Y_Q0",
"DYnCRN-yYBo",
"nRiQBOVb3SE",
"0bslM63s9WE",
"aSfYpxg28u4",
"P8zAzDB4vAk",
"_qEfTalzfjc",
"AVBupIrafIg",
"7nog-T42p6w",
"rIwGclwfsrE",
"u8wbA49sHBU",
"oJs_7ZkqWHg",
"6D1jIxyIlTw",
"z5H_SWqmt9Q",
]

    for v in videos:
        
        url = 'https://img.youtube.com/vi/{}/hqdefault.jpg'.format(v)
     
        myfile = requests.get(url)
     
        open('images/{}.jpg'.format(v), 'wb').write(myfile.content)
        print('Saved {}.jpg'.format(v))

    print('done')

if __name__== "__main__":
    main()