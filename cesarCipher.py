
logo = '''
                                                                                               
                                                                                               
        CCCCCCCCCCCCC                                                                          
     CCC::::::::::::C                                                                          
   CC:::::::::::::::C                                                                          
  C:::::CCCCCCCC::::C                                                                          
 C:::::C       CCCCCC    eeeeeeeeeeee        ssssssssss     aaaaaaaaaaaaa  rrrrr   rrrrrrrrr   
C:::::C                ee::::::::::::ee    ss::::::::::s    a::::::::::::a r::::rrr:::::::::r  
C:::::C               e::::::eeeee:::::eess:::::::::::::s   aaaaaaaaa:::::ar:::::::::::::::::r 
C:::::C              e::::::e     e:::::es::::::ssss:::::s           a::::arr::::::rrrrr::::::r
C:::::C              e:::::::eeeee::::::e s:::::s  ssssss     aaaaaaa:::::a r:::::r     r:::::r
C:::::C              e:::::::::::::::::e    s::::::s        aa::::::::::::a r:::::r     rrrrrrr
C:::::C              e::::::eeeeeeeeeee        s::::::s    a::::aaaa::::::a r:::::r            
 C:::::C       CCCCCCe:::::::e           ssssss   s:::::s a::::a    a:::::a r:::::r            
  C:::::CCCCCCCC::::Ce::::::::e          s:::::ssss::::::sa::::a    a:::::a r:::::r            
   CC:::::::::::::::C e::::::::eeeeeeee  s::::::::::::::s a:::::aaaa::::::a r:::::r            
     CCC::::::::::::C  ee:::::::::::::e   s:::::::::::ss   a::::::::::aa:::ar:::::r            
        CCCCCCCCCCCCC    eeeeeeeeeeeeee    sssssssssss      aaaaaaaaaa  aaaarrrrrrr            
                                                                                               
                                                                                                                                         
                                                                                                                                         
                                      CCCCCCCCCCCCC  iiii                    hhhhhhh                                                     
                                   CCC::::::::::::C i::::i                   h:::::h                                                     
                                 CC:::::::::::::::C  iiii                    h:::::h                                                     
                                C:::::CCCCCCCC::::C                          h:::::h                                                     
                               C:::::C       CCCCCCiiiiiiippppp   ppppppppp   h::::h hhhhh           eeeeeeeeeeee    rrrrr   rrrrrrrrr   
                              C:::::C              i:::::ip::::ppp:::::::::p  h::::hh:::::hhh      ee::::::::::::ee  r::::rrr:::::::::r  
                              C:::::C               i::::ip:::::::::::::::::p h::::::::::::::hh   e::::::eeeee:::::eer:::::::::::::::::r 
                              C:::::C               i::::ipp::::::ppppp::::::ph:::::::hhh::::::h e::::::e     e:::::err::::::rrrrr::::::r
                              C:::::C               i::::i p:::::p     p:::::ph::::::h   h::::::he:::::::eeeee::::::e r:::::r     r:::::r
                              C:::::C               i::::i p:::::p     p:::::ph:::::h     h:::::he:::::::::::::::::e  r:::::r     rrrrrrr
                              C:::::C               i::::i p:::::p     p:::::ph:::::h     h:::::he::::::eeeeeeeeeee   r:::::r            
                               C:::::C       CCCCCC i::::i p:::::p    p::::::ph:::::h     h:::::he:::::::e            r:::::r            
                                C:::::CCCCCCCC::::Ci::::::ip:::::ppppp:::::::ph:::::h     h:::::he::::::::e           r:::::r            
                                 CC:::::::::::::::Ci::::::ip::::::::::::::::p h:::::h     h:::::h e::::::::eeeeeeee   r:::::r            
                                   CCC::::::::::::Ci::::::ip::::::::::::::pp  h:::::h     h:::::h  ee:::::::::::::e   r:::::r            
                                      CCCCCCCCCCCCCiiiiiiiip::::::pppppppp    hhhhhhh     hhhhhhh    eeeeeeeeeeeeee   rrrrrrr            
                                                           p:::::p                                                                       
                                                           p:::::p                                                                       
                                                          p:::::::p                                                                      
                                                          p:::::::p                                                                      
                                                          p:::::::p                                                                      
                                                          ppppppppp                                                                      
                                                                                                                                        
'''

def cesar(text,direction,shift):
    newText = ''
    for i in text:
        val = ord(i)
        if direction == 'encode':
            val = (val + shift)%127
        else:
            val -= shift
        newText += chr(val)
    print(f'Your {direction}ed text is : {newText}')



print(logo)
direction = str(input('Do You want to encode or decode?\n'))
text = str(input('Type the Text to Convert: '))
shift = int(input('How much shift Do you want: '))
cesar(text,direction,shift)