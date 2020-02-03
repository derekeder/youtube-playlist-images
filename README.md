# Youtube Playlist Images

Fetches vido preview images from all videos in a YouTube playlist.

I use this to make images like this for the Chi Hack Night year in review posts:

![Chi Hack Night 2017 year in review](https://chihacknight.org/images/blog/2017-12-28-2017-year-in-review/2017-speakers.jpg)

## Running locally

1. Make a virtual environment with python3 `mkvirtualenv yt-videos --python=/usr/local/bin/python3`
2. `pip install -r requirements.txt`
3. `python get_ty_images.py`

## Handy resources

Getting a list of YouTube video id's from a YouTube Playlist: https://developers.google.com/youtube/v3/docs/playlistItems/list?apix_params=%7B%22part%22%3A%22contentDetails%22%2C%22maxResults%22%3A35%2C%22playlistId%22%3A%22PL_dBjjdnIbKyQXLBrIn_LLHTnwR03baW0%22%7D#usage

Converting a JSON object to a CSV (to later convert into a python array): https://json-csv.com/