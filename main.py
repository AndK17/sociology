import os
from dotenv import dotenv_values
from googleapiclient.discovery import build
import time
from datetime import datetime

config = dotenv_values(".env")
api_key = config['API_KEY']
service = build('youtube', 'v3', developerKey=api_key)

def get_comments(resource: str, id: str, maxResults = 100):
    parts = 'id,snippet'
    # мы будем брать только 10000 комментов для канала
    pages = 100
    args =  {'part':parts, 'maxResults': maxResults}
    if resource == "video":
        args['videoId'] = id
    elif resource == "channel":
        args['allThreadsRelatedToChannelId'] = id
    else:
        raise ValueError('Value of resource type must be "video" or "channel"!')
    
    comments = []
    for page in range(pages):
        r = service.commentThreads().list(**args).execute()
        # print(f"{page}/9 000 = {r['pageInfo']['totalResults']}")
        if page % 50 == 0: time.sleep(2)
        
        for item in r['items']:    
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        args['pageToken'] = r.get('nextPageToken')
        # print('nextPageToken = ', r.get('nextPageToken'))
        if not args['pageToken']: break
    
    return comments

def get_channel_title(id, maxResults = 100):
    parts = 'id,snippet'
    args = {'part':parts, 'id':id, 'maxResults': maxResults}
    r = service.channels().list(**args).execute()
    if r['items']:
        return r['items'][0]['snippet']['title']
    else:
        None

def get_channel_id_by_username(id, maxResults = 100):
    parts = 'id,snippet'
    args = {'part':parts, 'forUsername':id, 'maxResults': maxResults}
    r = service.channels().list(**args).execute()
    if r['items']:
        return r['items'][0]['id']
    else:
        None
    
    

def main():
    channels = {}
    with open('channels.txt', 'r', encoding='utf-8') as f:
        for line in f:
            channel_id = line.strip()
            print(channel_id)
            title = ''.join(filter(str.isalnum, get_channel_title(channel_id)))
            comments = get_comments('channel', channel_id)
            with open(f'lists/{title}_{str(datetime.now().date())}.txt', 'w', encoding='utf-8') as f:
                k = 0
                for comment in comments:
                    if comment:
                        f.write(comment + '\n')
            # comments = get_comments('video', 'tFS9Tep-qUg')
            print(len(comments))

if __name__ == '__main__':
    main()