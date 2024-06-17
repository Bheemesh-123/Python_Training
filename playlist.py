from pytube import Playlist
import os

def download_youtube_playlist(playlist_url, download_path='.'):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)

        # Print the playlist title
        print(f'Downloading playlist: {playlist.title}')
        
        # Iterate through all videos in the playlist
        for video in playlist.videos:
            try:
                print(f'Downloading: {video.title}')
                # Get the highest resolution stream available
                video_stream = video.streams.get_highest_resolution()
                # Download the video to the specified path
                video_stream.download(download_path)
                print(f'Download completed: {video.title}')
            except Exception as e:
                print(f'Error downloading {video.title}: {e}')
        
        print('All videos have been downloaded successfully!')
    except Exception as e:
        print(f'Error accessing the playlist: {e}')

if __name__ == '__main__':
    # Replace with your playlist URL
    playlist_url = 'https://www.youtube.com/watch?v=Ez8F0nW6S-w&list=PLfqMhTWNBTe0PY9xunOzsP5kmYIz2Hu7i&index=4&pp=iAQB'
    
    # Replace with your desired download path
    download_path = 'D:\git_github'
    
    # Create the download directory if it does not exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download the playlist
    download_youtube_playlist(playlist_url, download_path)
