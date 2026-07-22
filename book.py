contacts=[]
while True:
    print("1:Add Contact")
    print("2:View Contact")
    print("3:Delete Contact")
    print("4:Exit")
    print("-------------------------")
    choice=int(input('Enter btw 1 and 4 :'))
    if choice==1:
        
        con=(input('Enter Contact number:'))
        con_n=input('Enter Contact Name:')
        con_a=input('Enter Contact Address:')
        contact=(con,con_n,con_a)
        contacts.append(contact)
        print("Contact's Information added successfully")
        print("---------------------")
        

    if choice==2:
       if contacts==[]:
           print('No contacts found')
       else:
        for contacts in contact:
           print('Contact Number:',contact[0])
           print('Contact Name:',contact[1])
           print('Contact Address:',contact[2])

    print("----------------")
        
           
            
        

    if choice==3:
        
        all_con.show()
        del(all_con)

    if choice==4:
        
        exit.main
        