contacts=[]
while True:                                              #for continueing program untill user ends it
    print("--------------------------")
    print("--------------------------")
    print("    1:Add Contact         ")
    print("    2:View Contact        ")
    print("    3:Delete Contact      ")
    print("    4:Exit                ")
    print("--------------------------")
    print("--------------------------")
    choice=int(input('Enter btw 1 and 4 :'))          #taking input from user

               #For add contacts
    if choice==1:
        
        con=input('Enter Contact number:')
        con_n=input('Enter Contact Name:')
        con_a=input('Enter Contact Address:')
        contact=(con,con_n,con_a)                     #save contact infromation in contact
        contacts.append(contact)                      #for saving multiple contacts
        print("Contact's Information added successfully")
        
        
           #For View Contacts
    if choice==2:
       if contacts==[]:
           print('No contacts found')
       else:
        for contact in contacts:
           print('Contact Number:',contact[0])
           print('Contact Name:',contact[1])
           print('Contact Address:',contact[2])
           print(contact)

   
            #For Delete Contacts   
        
    if choice==3:
        print(contacts)
        if contacts==[]:
         print('No Contacts found')
        else:
           delete_contact=(input('Enter the Contact you want to delete:'))
           found=False

           for contact in contacts:
              if contact[1]==delete_contact:                     
                 contacts.remove(contact)                  #for deleting contact with thier name
                 print('Contact Deleted Successfully')
                 found=True
                 break
           if found==False:
            print('Contact Not Found')
           
           #For Exit
    if choice == 4:
       print('Thank you for chosing Contacts Books!')
       break                                               #for end the program 