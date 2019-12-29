import os

def IEEE():
    os.system('google-chrome https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=ai')

def pdf():
    os.system('xdg-open ieee.pdf')

pdf()