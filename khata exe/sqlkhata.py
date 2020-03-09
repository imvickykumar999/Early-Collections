import sqlite3
from datetime import date
conn = sqlite3.connect(r'C:\Users\Vicky Kumar\Desktop\face detection attendence file\Sqlite database\myshop.db')
c = conn.cursor()

def data_entry():

    customer_code = input('Enter Customer Code : ')
    price = float(input('Enter price : '))
    if price < 0:
        product = "...PAID..."
    else:
        product = input('Enter product : ')
    
    myDate = date.today()
    day = str(myDate.day)+ "/" + str(myDate.month) + "/" + str(myDate.year)
    
    c.execute("CREATE TABLE IF NOT EXISTS '" + str(customer_code) + "' (price REAL, product TEXT, day TEXT)") 
    c.execute("INSERT INTO '" + str(customer_code) + "' (price, product, day) VALUES(?, ?, ?)", (price, product, day)) 
    conn.commit()
    print('We have inserted', c.rowcount, 'records to the table.')

    
def show_table():
    
    customer_code = input('Enter Customer Code : ')
    c.execute("SELECT * FROM '" + str(customer_code) + "';") 
    rows = c.fetchall()
    print('\n1). PRICE 2). PRODUCT 3). DATE\n')
    for row in rows:
        print(row) 

def update_table():
        
    customer_code = input('Enter Customer Code : ')
    print('\n1). PRICE 2). PRODUCT 3). DATE\n')
    
    to_update = input('Enter column to_update : ')
    update_equal = input('Enter value of update_equal : ')
    something = input('Enter column something : ')
    is_something = input('Enter value of is_something : ')
    
    conn.execute("UPDATE '" + str(customer_code) + "' SET '" + str(to_update) + "' = '" + str(update_equal) + "' WHERE '" + str(something) + "' = '" + str(is_something) + "'") 
    
#     if to_update is 'price' and something is 'price':
#         conn.execute("UPDATE '" + str(customer_code) + "' SET '" + str(to_update) + "' = " + str(update_equal) + " WHERE '" + str(something) + "' = " + str(is_something)"") 
#     elif to_update is 'price' and something is not 'price':
#         conn.execute("UPDATE '" + str(customer_code) + "' SET '" + str(to_update) + "' = " + str(update_equal) + " WHERE '" + str(something) + "' = '" + str(is_something) + "'") 
#     elif to_update is not 'price' and something is 'price':
#         conn.execute("UPDATE '" + str(customer_code) + "' SET '" + str(to_update) + "' = '" + str(update_equal) + "' WHERE '" + str(something) + "' = " + str(is_something)"") 
#     elif to_update is not 'price' and something is not 'price':
#         conn.execute("UPDATE '" + str(customer_code) + "' SET '" + str(to_update) + "' = '" + str(update_equal) + "' WHERE '" + str(something) + "' = '" + str(is_something) + "'") 
#     else:
#         print('YOU ARE DEVELOPER...!!!')
                     
    conn.commit()
    print ("Total number of rows updated :", conn.total_changes) 

        
# def switch_menu(opt):
    
#     switcher = {
#         1: data_entry(), 
#         2: show_table(), 
#         3: update_table(to_update, update_equal, something, is_something)
#     }
#     return switcher.get(opt, "nothing")
        
def main():
    
    while True:
        print("\nMenu...\n")
        
        print('1: data_entry()')
        print('2: show_table()')
        print('3: update_table()')
        print('4: exit()\n')

        opt = int(input("Enter choice : "))
#         switch_menu(opt)

        if opt == 1:
            data_entry()
        elif opt == 2:
            show_table()
        elif opt == 3:
            update_table()
        elif opt == 4:
            break
        else:
            continue
        
    c.close()
    conn.close()
    
if __name__ == "__main__": 
    main()