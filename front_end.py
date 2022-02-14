from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
import back_end
import re


def add_password():
    if back_end.select_password() == []:
        back_end.insert_password(password_text.get())
        list1.delete(0,END)
        list1.insert(END,("Password Created Successfully"))
        
    else:
        list1.delete(0,END)
        list1.insert(END,("A Password is already there"))

            

def get_selected(event):
   
    try:                     
        global selected_tuple                      
        index= list1.curselection()[0] # the curselection method will fetch the index of selected row from Listbox.
        selected_tuple= list1.get(index)
        e2.delete(0,END)
        e2.insert(END,selected_tuple[1])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[2])
    except IndexError:
        pass



def view_command():
    list1.delete(0,END)
    result = back_end.view()
    for x in result:
        list1.insert(END, x)



hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"


def add_command():
    back_end.insert(web_text.get(),e3.get())
    list1.delete(0,END)
    list1.insert(END,(web_text.get(),e3.get()))
       
    
    webdate_values = back_end.select_website_details()
    ans = webdate_values.pop(-1)

    site_to_block= ans[0]
    ending_date = ans[1]
    today_date = datetime.now().strftime("%m/%d/%y")

    if today_date < ending_date: 
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            if site_to_block not in hosts_content:
                hostfile.write(redirect + ' ' + site_to_block + '\n')
    
       

def delete_command():
    if back_end.select_password()!= []:
        
        if password_text.get() == back_end.select_password()[0][0]:
            back_end.delete(selected_tuple[0])
            list1.delete(0,END)
            list1.insert(END,("Website removed successfully"))
        elif password_text.get() == "":
            list1.delete(0,END)
            list1.insert(END,("Please enter your password in the Password section to remove this site"))
            
        else:
            list1.delete(0,END)
            list1.insert(END,("Password entered is wrong"))

    else:
        back_end.delete(selected_tuple[0])
    
    site_to_unblock = selected_tuple[1]    
    
    with open(hosts_path, 'r+') as hostfile:
        lines = hostfile.readlines()
        hostfile.seek(0)
        for line in lines:
            if site_to_unblock not in line:
                hostfile.write(line)
        hostfile.truncate()    
    
           

def removing_old_dates(i):
    try:
        values = back_end.select_address_id(i)
        
        site_to_unblock = values[0][0]
        back_end.delete(values[0][1])      
            
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if site_to_unblock not in line:
                    hostfile.write(line)
            hostfile.truncate()    
    
    except IndexError:
        pass
    
 
def refreshing():
 
    m = datetime.now().strftime("%m")
    d  = datetime.now().strftime("%d")
    y = datetime.now().strftime("%y")

    month_now= int(f"{int(m):01}")
    date_now = int(f"{int(d):01}")
    year_now = int(f"{int(y):01}")
   
    all_dates = back_end.date()

    for i in all_dates:
        splitting = re.split("/",i)
        mon = int(splitting[0])
        dat = int(splitting[1])
        year = int(splitting[2])      
        
        if mon<month_now or year<year_now:
            removing_old_dates(i)
        
        if mon==month_now and dat<date_now and year==year_now:
            removing_old_dates(i)
        


def password_change():
    try:
        old_password = back_end.select_password()[0][0]
        if e1.get() == old_password:
            back_end.delete_password(old_password)
            back_end.insert_password(e4.get())
            
            list1.delete(0,END)
            list1.insert(END,("Password updated successfully"))
        
        else:
            list1.delete(0,END)
            list1.insert(END,("Please mention your old password correctly and try again"))
            
    except IndexError:
        pass    
   
    
window= Tk()

window.wm_title("Website_blocker")

l1 = Label(window, text = "Password")
l1.grid(row= 0, column= 0)

l2 = Label(window, text = "Enter Web address")
l2.grid(row= 1, column= 0)

l3 = Label(window, text = "(e.g. www.youtube.com)")
l3.grid(row= 2, column= 0)

l4 = Label(window, text = "Block Website till")
l4.grid(row= 1, column= 2)

l5 = Label(window, text = "Created by Sriram",height=1,bg="grey")
l5.grid(row= 8, column= 0)

l6 = Label(window, text = "New Password")
l6.grid(row= 0, column= 2)


b1= Button(window, text = "Set Password",width= 12,command= add_password)
b1.grid(row=3, column= 3)

b2= Button(window, text = "View all",width= 12,command= view_command)
b2.grid(row=4, column= 3)

b3= Button(window, text = "Add Website",width= 12,command= add_command)
b3.grid(row=5, column= 3)

b4= Button(window, text = "Remove Website",width= 12,command= delete_command)
b4.grid(row=6, column= 3)

b5= Button(window, text = "Refresh",width= 12,command= refreshing)
b5.grid(row=7, column= 3)

b6= Button(window, text = "Change Password", command= password_change, width= 13)
b6.grid(row=8, column= 3)

b7= Button(window, text = "Close", command= window.destroy, width= 12)
b7.grid(row=9, column= 3)


password_text = StringVar()
e1= Entry(window, textvariable= password_text)
e1.grid(row=0, column= 1)

web_text = StringVar()
e2= Entry(window, textvariable= web_text)
e2.grid(row=1, column= 1)


e3 = DateEntry(window, width= 16,bd=2)
e3.grid(row=1, column= 3)

new_password_text = StringVar()
e4= Entry(window, textvariable= new_password_text)
e4.grid(row=0, column= 3)


list1 = Listbox(window,height= 8,width= 36)
list1.grid(row= 3,column= 0,rowspan= 10,columnspan= 2)

scroll = Scrollbar(window)
scroll.grid(row= 4,column= 2, rowspan= 7)

list1.configure(yscrollcommand= scroll.set)
scroll.configure(command= list1.yview)

list1.bind('<<ListboxSelect>>',get_selected) 
                                            


window.mainloop()