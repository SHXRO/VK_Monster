import pandas as pd
import vk_api
from auth import TOKEN
import xlrd
import xlwt
import os
import sys
from vk_api.utils import get_random_id



#авторизация
session = vk_api.VkApi(token=TOKEN)
vk = session.get_api()

#====================================================функции==================================================#
#Отменить все заявки
def deleteAllRequests():
     print ("Все заявки отклонены")
     delreq = session.method("friends.deleteAllRequests")
     menu()

#Кикнуть всех из чата по ID
def chatkick():
     chatid = input('ID чата?: ')
     excel_data_file = xlrd.open_workbook('./IDs.xls')
     sheet = excel_data_file.sheet_by_index(0)     
     list = []
     row_number = sheet.nrows
     if row_number > 0:
          for row in range(0, row_number):
               list.append(str(sheet.row(row)[0]).replace("number:", "").replace('.0',''))
          print ("Количество запрашиваемых id: ", len(list))
     else:
          print("Пусто")
     print(list) 
     for i in range (len(list)):
          try: 
               status = session.method("messages.removeChatUser",  {'chat_id': chatid,'user_id': list[i]} ) 
               print(status) 
               print ('Пользователь кикнут', list[i])
               menu()
          except vk_api.exceptions.ApiError:
               print ('___________________________Ошибка________________________________')
               print ('                 ID Пользователя: ',list[i])
               print ('1. Проверьте актуальность/наличие токена')
               print ('2. У вас нет прав на выполнение данной команды :c')
               print ('3. Вы не можете кикнуть администратора')
               print ('_________________________________________________________________')
               continue

#Добавить пользователей в чат по IDs
def addchat():
     excel_data_file = xlrd.open_workbook('./IDs.xls')
     sheet = excel_data_file.sheet_by_index(0)     
     list = []
     row_number = sheet.nrows
     if row_number > 0:
          for row in range(0, row_number):
               list.append(str(sheet.row(row)[0]).replace("number:", "").replace('.0',''))
          print ("Количество запрашиваемых id: ", len(list))
     else:
          print("Пусто")
     print(list) 

     chatid = input('Введите ID чата')
     for i in range (len(list)):
          try: 
               status = session.method("messages.addChatUser",  {'chat_id': chatid,'user_id': list[i]} ) 
               print(status)
               print ('Пользователь добален: ', list[i])
               menu() 
          except vk_api.exceptions.ApiError:
               print ('___________________________Ошибка________________________________')
               print ('                 ID Пользователя: ',list[i])
               print ('1. Проверьте актуальность/наличие токена')
               print ('2. Возможно, у вас нет прав в группе :c')
               print ('3. Возможно, у вас нет это пользователя в друзьях')
               print ('_________________________________________________________________')
               continue

#Бан по ID 
def banbyid():
     excel_data_file = xlrd.open_workbook('./IDs.xls')
     sheet = excel_data_file.sheet_by_index(0)     
     list = []
     row_number = sheet.nrows
     if row_number > 0:
          for row in range(0, row_number):
               list.append(str(sheet.row(row)[0]).replace("number:", "").replace('.0',''))
          print ("Количество запрашиваемых id: ", len(list))
     else:
          print("Пусто")
     print(list) 
     for i in range (len(list)):
          try: 
               status = session.method("account.ban",  {'owner_id': list[i]} ) 
               print(status)
               print ('Пользователь забанен: ',list[i])
               menu() 
          except vk_api.exceptions.ApiError:
               continue

#Flood
def spam():
     excel_data_file = xlrd.open_workbook('./IDs.xls')
     sheet = excel_data_file.sheet_by_index(0)     
     list = []
     row_number = sheet.nrows
     if row_number > 0:
          for row in range(0, row_number):
               list.append(str(sheet.row(row)[0]).replace("number:", "").replace('.0',''))
          print ("Количество запрашиваемых id: ", len(list))
     else:
          print("Пусто")
     print(list) 
     text = input('Введите текст')
     for i in range (len(list)):
          try: 
               status = session.method("messages.send",  {"peer_id": list[i], "message": text , "random_id":get_random_id()})
               print(status)
               print ('Сообщение отправленно')
               menu() 
          except vk_api.exceptions.ApiError:
               print ('___________________________Ошибка________________________________')
               print ('                 ID Пользователя: ',list[i])
               print ('1. Проверьте актуальность/наличие токена')
               print ('2. Возможно, у пользователя закрыта личка для вас или вы в ЧС :c')
               print ('_________________________________________________________________')
               continue

              



              









#меню
def exit():
     print('''
.------.------.------.
|B.--. |Y.--. |E.--. |
| :(): | (\/) | (\/) |
| ()() | :\/: | :\/: |
| '--'B| '--'Y| '--'E|
`------`------`------' ''')
     sys.exit 


def back():
     menu()


def menu_chat():
     os.system('cls')
     print('---------Функции с чатом---------')
     print()
     print ('1 -- Добавить участников по IDs.xls')
     print ('2 -- Кикнуть участников по IDs.xls')
     print ('3 -- Назад')
     sel = input('Введите номер функции: ')    

     if sel == '1':
          os.system('cls') 
          addchat()
     if sel == '2':
          os.system('cls')
          chatkick()
     if sel == '3':
          os.system('cls') 
          menu()   
     


     

def menu_profile():
     os.system('cls')
     print('---------Функции с профилем---------')
     print ('1 -- Отклонить все запросы в друзья')
     print ('2 -- Забанить людей по IDs.xls')
     print ('3 -- Назад')
     sel = input('Введите номер функции: ')    

     if sel == '1':
          os.system('cls') 
          deleteAllRequests()
     if sel == '2':
          banbyid()
          os.system('cls')
          
     if sel == '3':
          os.system('cls') 
          menu()   

def menu_groups(): 
     os.system('cls')
     print('---------Функции с ЛС---------')   
     print ('1 -- Написать IDs.xls')
     print ('2 -- *****************')
     print ('3 -- Назад')
     sel = input('Введите номер функции: ')    

     if sel == '1':
        os.system('cls') 
        spam()
     if sel == '2':
        os.system('cls')      
        menu()
     if sel == '3':
        os.system('cls') 
        menu()    



def menu():
     print (''' 
      ___      ___ ___  __            _____ ______   ________  ________   ________  _________  _______   ________     
|\  \    /  /|\  \|\  \         |\   _ \  _   \|\   __  \|\   ___  \|\   ____\|\___   ___|\  ___ \ |\   __  \    
\ \  \  /  / \ \  \/  /|_       \ \  \\\__\ \  \ \  \|\  \ \  \\ \  \ \  \___|\|___ \  \_\ \   __/|\ \  \|\  \   
 \ \  \/  / / \ \   ___  \       \ \  \\|__| \  \ \  \\\  \ \  \\ \  \ \_____  \   \ \  \ \ \  \_|/_\ \   _  _\  
  \ \    / /   \ \  \\ \  \       \ \  \    \ \  \ \  \\\  \ \  \\ \  \|____|\  \   \ \  \ \ \  \_|\ \ \  \\  \| 
   \ \__/ /     \ \__\\ \__\       \ \__\    \ \__\ \_______\ \__\\ \__\____\_\  \   \ \__\ \ \_______\ \__\\ _\ 
 ___\|__|/ ______\|__|_\|__|_  _____\|__|     \|__|\|_______|\|__| \|__|\_________\   \|__|  \|_______|\|__|\|__|
|\   __  \|\  ___ \|\___   ___|\   __  \                               \|_________|                              
\ \  \|\ /\ \   __/\|___ \  \_\ \  \|\  \                                                                        
 \ \   __  \ \  \_|/__  \ \  \ \ \   __  \                                                                       
  \ \  \|\  \ \  \_|\ \  \ \  \ \ \  \ \  \                                                                      
   \ \_______\ \_______\  \ \__\ \ \__\ \__\                                                                     
    \|_______|\|_______|   \|__|  \|__|\|__|   
     ''')
     print ()
     print ()
     print ()
     print ('1 -- Функции с профилем')
     print ('2 -- Функции с чатом')
     print ('3 -- Функции с ЛС')
     print ('4 -- Выход' )
     print()
     print()

     
     sel = input('Введите номер функции: ')    

     if sel == '1':
        os.system('cls') 
        menu_profile()
     if sel == '2':
        os.system('cls')      
        menu_chat()
     if sel == '3':
        os.system('cls') 
        menu_groups()    
     if sel == '4':
        exit()

menu()   

     