import pandas as pd
import vk_api
from auth import TOKEN
import xlrd
import xlwt
import os
import sys

#авторизация
session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()

#====================================================функции==================================================#
#Получить ID участниов конфы

def memberchat():
    try: 
        chatid= input('Введите ID чата: ')
        info = session.method("messages.getChatUsers",{'chat_id' :chatid}, {'fields': id})
        list_df = pd.DataFrame(info) 
        list_df.to_excel('ID_chat.xls',index=False)  
        os.system('cls')
        print ('Готово. Результат записан в ID_chat.xls')
        menu()
    except vk_api.exceptions.ApiError: 
        print ('___________________________Ошибка________________________________')
        print ('1. Проверьте актуальность/наличие токена')
        print ('2. Возможно, вы несостоите в чате или ввели не правильный ID :c')
        print ('_________________________________________________________________')
    except PermissionError:
        print ('Пожалуйста закройте таблицу Excel и повторите попытку')   

#Получить ID участинков группы

def groupid():
    try:
        groupid = input('Введите ID группы: ')
        info = session.method("groups.getMembers",{'group_id' : groupid})
        list_df = pd.DataFrame(info)
        list_df.to_excel('ID_groups.xls',index=False)
        os.system('cls')
        print ('Готово. Результат записан в ID_chat.xls')
        menu()
    except vk_api.exceptions.ApiError: 
        print ('_______________________Ошибка_________________________')
        print ('1. Проверьте актуальность/наличие токена')
        print ('2. Возможно, страница закрытая группа или вы в ЧС :c')
        print ('________________________________________________________')
    except PermissionError:
        print ('Пожалуйста закройте таблицу Excel и повторите попытку')      

#Получить ID друзей пользователей

def friendlistid():
    try:
        ID = input ('Введите ID пользователя: ')
        info = session.method("friends.get",{'user_id' : ID})
        print (info)
        list_df = pd.DataFrame(info['items'])
        list_df.to_excel('ID_friends.xls',index=False)
        os.system('cls')
        print ('Готово. Результат записан в ID_friends.xls')
        menu()
    except vk_api.exceptions.ApiError: 
        print ('_________________Ошибка______________________')
        print ('1. Проверьте актуальность/наличие токена')
        print ('2. Возможно, страница закрытая или вы в ЧС :c')
        print ('_____________________________________________')
    except PermissionError:
        print ('Пожалуйста закройте таблицу Excel и повторите попытку')     

def exit():
    print('''
.------.------.------.
|B.--. |Y.--. |E.--. |
| :(): | (\/) | (\/) |
| ()() | :\/: | :\/: |
| '--'B| '--'Y| '--'E|
`------`------`------' 
''')
    sys.exit        



#выбор функционала
def menu():
     print ('''
____   ________  __. __________  _____ __________  ____________________________  
\   \ /   |    |/ _| \______   \/  _  \\______   \/   _____\_   _____\______   \ 
 \   Y   /|      <    |     ___/  /_\  \|       _/\_____  \ |    __)_ |       _/ 
  \     / |    |  \   |    |  /    |    |    |   \/        \|        \|    |   \ 
   \___/  |____|__ \  |____|  \____|__  |____|_  /_______  /_______  /|____|_  / 
        ___.      \/          .__    .\/       \/        \/        \/        \/  
        \_ |__ ___.__.   _____|  |__ |_________  ____                            
         | __ <   |  |  /  ___|  |  \|  \_  __ \/  _ \                           
         | \_\ \___  |  \___ \|   Y  |  ||  | \(  <_> )                          
         |___  / ____| /____  |___|  |__||__|   \____/                           
             \/\/           \/     \/                                            ''')

     print('Вверсия v0.1')
     print('Новые версии будут публиковаться здесь - https://github.com/SHXRO')
     print()
     print()
     print('1 -- Получить ID участниов конфы' )
     print('2 -- Получить ID участинков группы' )
     print('3 -- Получить ID друзей пользователей' )
     print('4 -- Выход')
     print()
     print()
     print()
     print()
     print()
     print()
     
     sel = input('Введите номер функции: ')    

     if sel == '1':
        memberchat()
     if sel == '2':
        groupid()
     if sel == '3':
        friendlistid()    
     if sel == '4':
        exit()
menu()   