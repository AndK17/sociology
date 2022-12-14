from telethon import TelegramClient, types
import config
from openpyxl import Workbook
import time
import random
import json

api_id = config.API_ID
api_hash = config.API_HASH

client = TelegramClient('session_name', api_id, api_hash)
client.start()


def get_comments_by_link(link):
    slink = link.split('/')
    print(slink)
    
    # book = Workbook()
    # sheet = book.active
    # sheet['D1'] = link
    res = {'link': link,
           'comments': []}
    c = 2
    for message in client.iter_messages(slink[-2], reply_to=int(slink[-1]), reverse=True):
        # print(message)
        # sheet[f'A{c}'] = message.text
        res['comments'].append(message.text)
        c += 1
            
    # book.save(slink[-2]+'_'+slink[-1]+".xlsx")
    with open(slink[-2]+'_'+slink[-1]+".json", "w") as write_file:
        json.dump(res, write_file)
    
        
def get_comments_to_excel(channel, post_id, sheet):
    c = 2
    try:
        for message in client.iter_messages(channel, reply_to=int(post_id), reverse=True):
            sheet[f'A{c}'] = message.text
            c += 1
    except Exception as e:
        print(f'err: {e}')
        return 1
            
    
def get_posts_to_excel(channel, count):
    i = 0
    for message in client.iter_messages(channel):
        print(message.id, message.message)
        
        book = Workbook()
        sheet = book.active
        sheet['D1'] = f'https://t.me/{channel}/{message.id}'
        sheet['E1'] = message.message
        if get_comments(channel, message.id, sheet) != 1:
            book.save(f'{channel}/{channel}_{message.id}.xlsx')
            print(f'{i}/{count} OK')
            
            i += 1
            if i>= count:
                break
        else:
            print(f'{i}/{count} {message.id} error')
        time.sleep(random.randint(3, 7))


def get_comments(channel, message):
    c = 2
    res = {'link': f'https://t.me/{channel}/{message.id}',
           'text': message.message,
           'comments': []}
    
    try:
        for message in client.iter_messages(channel, reply_to=int(message.id), reverse=True):
            res['comments'].append(message.text)
            c += 1
            
        with open(channel+'/'+channel+'_'+str(message.id)+".json", "w", encoding="utf-8") as write_file:
            json.dump(res, write_file, ensure_ascii=False)
    except Exception as e:
        print(f'err: {e}')
        return 1
            
    
def get_posts(channel, count):
    i = 0
    for message in client.iter_messages(channel):
        # print(message.id, message.message)
        
        if get_comments(channel, message) != 1:
            print(f'{i+1}/{count} OK')
            
            i += 1
            if i>= count:
                break
        else:
            print(f'{i+1}/{count} {message.id} error')
        time.sleep(random.randint(3, 7))
        
# get_posts('nemorgenshtern', 100)
get_posts('bigpencil', 100)
# get_posts('postupashki', 100)