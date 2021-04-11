# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:48:56 2021
This code suggested by Zahra Gholami for HW5 at maktab51.
In this code we use base sample (that are in the end of this code) for lists of book.
"""

class Book:
    def __init__(self,title,authors,publish_year,pages,language,price,total_read_pages):
        self.total_read_pages=total_read_pages
        self.title=title
        self.authors=authors
        self.publish_year=publish_year
        self.pages=int(pages)
        self.language=language
        self.price=price
    
    '''
    In this method we update readen pages and report the number of readen and 
    unreaden pages for each book.
    '''
    def read(self):
        current_read_pages=int(input('How many pages of this book did you read? '))
        if current_read_pages>self.pages: print(f'You can not read more than book’s pages!')
        else:
            self.total_read_pages+=current_read_pages
            self.unread_pages=self.pages-self.total_read_pages
            print(f'You have read {current_read_pages} more pages '
            f'from \"{self.title}\". There are {self.unread_pages} pages left.\n')
           
             
    '''
    This method return statues of  each books based on number of readen pages.
    '''
    def get_status(self):
        if self.total_read_pages==0:print('Satatus of this media is: Unreaded')
        elif self.total_read_pages<self.pages:print('Satatus of this media is: Reading')
        else:print('Satatus of this media is: Finished')
        
    '''This method is for presenting of books '''  
    def __str__(self):
        return f'Title:{self.title}, Author(s):{self.authors}, '\
               f'Publish_year:{self.publish_year}, pages:{self.pages}, '\
               f'Language:{self.language}, Price:{self.price}.\n'
#=============================================================================               
'''
This function gets data from input and make book instancee from that information.
'''      
def get_data():
    command=input('plz enter \'y\' to adding books or \'e\' to exit: ')
    lst_books=[] #for saving instances
    while command=='y':
        info=input('\nPlz enter information of your book with specifing \',\'\
        (Title,author(s),publish_year,num_pages,language,price): ').split(',')
        lst_books.append(Book(info[0],info[1],info[2],info[3],info[4],info[5],0))
        command=input('plz enter \'y\' to adding more books or \'e\' to exit: ')   
    return lst_books         

   
lst_books=get_data()

#this section is for printing all books
def show_medias(lst_books):
    ID=1
    print('\n----------A list of all books in your bookshelf is---------')
    for i in lst_books:
        print(f'\nID:{ID} {i}')
        ID+=1
    print('----------------------------------------------')

show_medias(lst_books)


''''
In this section we handle the operations of read or get satus based on recevied data from user.
'''   
index=int(input('Pleas specify ID of book that you want to get information about it or \'e\' to terminate: '))
command=input('Plz select \'read\' or \'get_status\: ')
while index!='e':
    lst_books[index-1].__getattribute__(command)()
    show_medias(lst_books)
    index=int(input('Pleas specify ID of book that you want to get information about it or \'e\' to terminate: '))
    command=input('Plz select \'read\' or \'get_status\: ')
    

'''samples for test code:
    No Friend But the Mountains, Behrouz Boochani, 2018, 374, English, 10$
    The Black Swan, Abbas Maroufi, 2007, 280, Persian, 20$
    Symphony of the Dead, Behrouz Boochani, 2018, 374, English, 12$
'''