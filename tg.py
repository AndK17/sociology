from telethon import TelegramClient, types
import config
from openpyxl import Workbook
import time
import random

api_id = config.API_ID
api_hash = config.API_HASH

client = TelegramClient('session_name', api_id, api_hash)
client.start()


def get_comments_by_link(link):
    slink = link.split('/')
    print(slink)
    
    book = Workbook()
    sheet = book.active
    sheet['F1'] = link
    
    c = 2
    for message in client.iter_messages(slink[-2], reply_to=int(slink[-1]), reverse=True):
        print(message)
        if isinstance(message.sender, types.User):
            print(message.date, message.sender.first_name, ':', message.text)
            sheet[f'A{c}'] = message.date
            sheet[f'B{c}'] = message.from_id.user_id
            sheet[f'C{c}'] = message.sender.first_name
            sheet[f'D{c}'] = message.text
        else:
            if message.from_id == None:
                sheet[f'A{c}'] = message.date
                sheet[f'B{c}'] = None
                sheet[f'C{c}'] = 'Author'
                sheet[f'D{c}'] = message.text
            else:
                print(message.date, message.sender.title, ':', message.text)
                sheet[f'A{c}'] = message.date
                sheet[f'B{c}'] = message.from_id.user_id
                sheet[f'C{c}'] = message.sender.title
                sheet[f'D{c}'] = message.text
        c += 1
            
    book.save(slink[-2]+'_'+slink[-1]+".xlsx")
    
        
def get_comments(channel, post_id, sheet):
    c = 2
    for message in client.iter_messages(channel, reply_to=int(post_id), reverse=True):
        if isinstance(message.sender, types.User):
            sheet[f'A{c}'] = message.date
            sheet[f'B{c}'] = message.from_id.user_id
            sheet[f'C{c}'] = message.sender.first_name
            sheet[f'D{c}'] = message.text
        else:
            if message.from_id == None:
                sheet[f'A{c}'] = message.date
                sheet[f'B{c}'] = None
                sheet[f'C{c}'] = 'Author'
                sheet[f'D{c}'] = message.text
            else:
                sheet[f'A{c}'] = message.date
                sheet[f'B{c}'] = message.from_id.user_id
                sheet[f'C{c}'] = message.sender.title
                sheet[f'D{c}'] = message.text
        c += 1
            
    
def get_posts(channel, count):
    i = 1
    for message in client.iter_messages(channel):
        print(message.id, message.message)
        
        book = Workbook()
        sheet = book.active
        sheet['F1'] = f'https://t.me/{channel}/{message.id}'
        sheet['G1'] = message.message
        get_comments(channel, message.id, sheet)
        book.save(f'{channel}/{channel}_{message.id}.xlsx')
        print(f'{i}/{count} OK')
        
        i += 1
        if i>= count:
            break
        
        time.sleep(random.randint(3, 7))
        
# get_posts('nemorgenshtern', 100)

get_comments_by_link('https://t.me/nemorgenshtern/13336')
# for message in client.iter_messages(chat):
#     print(message.sender_id, ':', message.text) https://t.me/nemorgenshtern/13337