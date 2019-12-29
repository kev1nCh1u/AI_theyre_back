import os

#linux
def IEEE():
    os.system('google-chrome https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=ai')
    input('press to continue...')

def pdf():
    os.system('xdg-open ieee.pdf')
