# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 13:37:06 2021
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
    In this method we update readen pages and report the number of readen, 
    unreaden pages and progress for each book or magazine. progress is percentage 
    of pages which been read for each book.
    ''' 
    def read(self):
        current_read_pages=int(input('How many pages did you read? '))
        if current_read_pages>self.pages: print(f'You can not read/listen more than\
        pages/times of a media!')
        else:
            self.total_read_pages+=current_read_pages
            self.unread_pages=self.pages-self.total_read_pages
            print(f'You have read {current_read_pages} more pages '
                  f'from \"{self.title}\". There are {self.unread_pages} pages left.\n')
            self.progress=round((self.total_read_pages/self.pages)*100,3)
            print(f'your progress in \"{self.title}\" is {self.progress}%')
            
    '''
    This method return statues of  each books based on number of readen pages.
    '''    
    def get_status(self):
        if self.total_read_pages==0:print('Satatus of this media is: Unreaded')
        elif self.total_read_pages<self.pages:print('Satatus of this media is: Reading')
        else:print('Satatus of this media is: Finished') 
    
    '''This method is for presenting of books '''  
    def __str__(self):
        return f'Title:{self.title}, Author(s):{self.authors},Publish_year:{self.publish_year}, Pages:{self.pages},Language:{self.language}, Price:{self.price}.\n'
#==============================================================================
#we consider Magazine as a child of Book.              
class Magazine(Book):
    def __init__(self,title,authors,publish_year,pages,language,price,issue,total_read_pages):
        self.issue=issue
        
#       in this section we call construcor of parent(Book)
        super().__init__(title,authors,publish_year,pages,language,price,total_read_pages)
        
#    This method is for presenting of magazines   
    def __str__(self): #Overriding
        return f'Title:{self.title}, Author(s):{self.authors}, '\
               f'Publish_year:{self.publish_year}, Pages:{self.pages}, '\
               f'Language:{self.language}, Price:{self.price}, Issue:{self.issue}\n'
#==============================================================================
#we consider PodcastEpizode as a child of Book.        
class PodcastEpizode(Book):
    def __init__(self,title,speaker,publish_year,time,language,price,total_listen_time):
        
#       in this section we call construcor of parent(Book)
        super().__init__(title,speaker,publish_year,time,language,price,total_listen_time)
        
        self.speaker=speaker
        self.time=int(time)
        self.total_listen_time=total_listen_time
     
    '''
    In this method we update listened times and report the times of listened, 
    unlistened times and progress for each podcast or audio book. progress is percentage 
    of pages which been listened for each podcast or audio book
    '''
    def listen(self): #Overriding
        current_listen_time=int(input('Enter the time that you have listened: '))
        if current_listen_time>self.time:print(f'You can not read/listen more than \
        pages/times of a media!')
        else:
            self.total_listen_time+=current_listen_time
            self.unlisten_time=self.time-self.total_listen_time
            print(f'\nYou have listened {current_listen_time} more times'
                  f'from \"{self.title}\". There are {self.unlisten_time} times left.\n')
            if self.total_listen_time==self.time: print(f'You have read {self.title} before.')
            self.progress=round ((self.total_listen_time/self.time)*100,3)
            print(f'your progress in \"{self.title}\" is {self.progress}%')
    
    '''
    This method returns statues of  each podcast or audiobook based on number of listened times.
    '''        
    def get_status(self):#Overriding
        if self.total_listen_time==0:print('Status of this media is: Unlistened')
        elif self.total_listen_time<self.pages:print ('Status of this media is: Listening')
        else:print ('Satatus of this media is: Finished')     
     
    def __str__(self):#Overriding
        return f'Title:{self.title}, Speaker:{self.speaker}, '\
               f'Publish_year:{self.publish_year}, Time:{self.time}, '\
               f'Language:{self.language}, Price:{self.price}.\n'
#===============================================================================              
#we consider AudioBook as a child of PodcastEpizode.            
class AudioBook(PodcastEpizode):
    def __init__(self,title,speaker,author,publish_year,pages,time,book_language,audio_language,price,total_listen_time):
        super().__init__(title,speaker,publish_year,time,audio_language,price,total_listen_time)
        self.audio_language=audio_language
        self.author=author
        self.pages=pages
        self.book_language=book_language
        
    def __str__(self):#Overriding
        return f'Title:{self.title}, Speaker:{self.speaker}, Author:{self.author}, '\
               f'Publish_year:{self.publish_year}, Pages:{self.pages}, Time:{self.time}, Book_language:{self.book_language}, '\
               f'Audio_language:{self.language}, Price:{self.price}.\n'

#==============================================================================
'''
This function gets datas from input and makes instances from that information.
We save instances in a dictionary such that, dictionary's key is the type of 
media and the value of each key is instances of that media.
'''                     
def get_data():
    command=input('What kind of media do you want to add to your library?\
    select the one of the \'book\'  \'magazine\', \'podcast\' and \'audiobook\' or enter \'quit\' to exit: ')
    dict_medias={'book':[],'magazine':[] ,'podcast':[], 'audiobook':[]}
    while command!='exit':
        if command=='book':
            info=input('\nPlz enter information of your media with specifing \',\'\
            (Title,author(s),publish_year,pages,language,price): ').split(',')
            dict_medias['book'].append(Book(info[0],info[1],info[2],info[3],info[4],info[5],0))
        elif command=='magazine':
            info=input('\nPlz enter information of your media with specifing \',\'\
            (Title,author(s),publish_year,pages,language,price,issue): ').split(',')
            dict_medias['magazine'].append(Magazine(info[0],info[1],info[2],info[3],info[4],info[5],info[6],0))
        elif command=='podcast':
            info=input('\nPlz enter information of your media with specifing \',\'\
            (Title,Speaker,Publish_year,time(min),Language,Price): ').split(',')
            dict_medias['podcast'].append(PodcastEpizode(info[0],info[1],info[2],info[3],info[4],info[5],0))
        elif command=='audiobook': 
            info=input('\nPlz enter information of your media with specifing \',\'\
            (Title,Speaker,Author,Publish_year,pages,time,book_language,audio_language,Price): ').split(',')
            dict_medias['audiobook'].append(AudioBook(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],0))
        command=input('What kind of media do you want to add to your library? \
        select the one of the \'book\' \'magazine\', \'podcast\' and \'audiobook\' or enter \'quit\' to exit: ')
           
    return dict_medias

dict_medias=get_data()
#==============================================================================
#this function prints all medias.Different types of medias are printed separately.
def show_all_medias(dict_medias):
    print(f'\nThe list of all items in your shelf is as follows:\n')
    for i in dict_medias.keys():
        ID=1
        if len(dict_medias[i])!=0:print(f'all {i}s:')
        for j in dict_medias[i]:
            print(f'ID:{ID} {j}')
            ID+=1

show_all_medias(dict_medias)
#==============================================================================
#This function prints a specific media.
def show_one_type(media):
    ID=1
    for i in dict_medias[media]:
        print(f'\nA list of all {media}s in your bookshelf is:\n\nID:{ID} {i}')
        ID+=1
#==============================================================================
''''
In this section we handle the operations of read, listen or get status based 
on recevied data from user.
'''           
media=input('Pleas specify the type of media that you want to get information about\
it:(book,magazine,podcast,audiobook) or exit to terminate: ')
while True:
    index=int(input(f'Which one of the {media}s? plz enter the ID of it: '))
    if media=='book' or media=='magazine':
        command=input('Plz select \'read\' or \'get_status\': ')
    elif media=='podcast' or media=='audiobook':
        command=input('Plz select \'listen\' or \'get_status\: ')
    dict_medias[media][index-1].__getattribute__(command)()
    media=input('Pleas specify the media that you want to get information about it:(book,magazine,podcast,audiobook) or exit to terminate: ')
    if media!='exit':show_one_type(media)
    else: break
#==============================================================================
''''
We saved medias in a dictionary (base on media type), so for sorting all medias  
we have to save all medias in a list.
'''    
lst_medias=[]
for i in dict_medias.keys():
    for j in range(len(dict_medias[i])):
        lst_medias.append(dict_medias[i][j])


#This function is for sorting all medias based on progress
def sorting_progress(lst_medias):
    lst_medias=sorted(lst_medias,key=lambda x:x.__getattribute__('progress'),reverse=True)
    return lst_medias

print('\n--------Sorted your medias basd on progress are:---------\n')
for i in sorting_progress(lst_medias):
#    i.__class__.__name__ returns the name of class of corresponding to i.
    print(f'media type:{i.__class__.__name__}, title:{i.title}, progress:{i.progress}%')
#==============================================================================
'''
This function is for sorting medias based on progress, but sorting is performed
local for each media type.
'''    
def sorting_progress(dict_medias):
    for i in dict_medias.keys():
        dict_medias[i]=sorted(dict_medias[i],key=lambda x:x.__getattribute__('progress'),reverse=True)
    return dict_medias

print('\n--------Local sorting of your medias basd on progress are:---------\n')
sorted_medias=sorting_progress(dict_medias)
show_all_medias(sorted_medias)
        
'''
Input samples:
A sample of magazine:
    Bukhara,[Ali Dehbashi and Darioush Ashoori],2020,768,persian,55,140
A sample of podcast:
    Ravaaq,Farzin Ranjbar,2020,50,persian,0
A sample of audio book:
    The Black Swan,Ali Bandari,Nassim Nicholas Taleb,2020,400,62,English,Persian,0
'''    

