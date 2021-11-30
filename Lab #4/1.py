from random import randint


#Words
Word1='Trees,Grass,Girls,Ghosts,Galaxy,Time'.split(',')
Word2='Are,is,Below,Get,Give,Was'.split(',')
Word3='Clown,Cool,Water,Free,Boy,Flower '.split(',')


#Phrase
Word4=''
Word4+=Word1[randint(0, len(Word1) - 1)]
Word4+=' '
Word4+=Word2[randint(0, len(Word2) - 1)]
Word4+=' '
Word4+=Word3[randint(0, len(Word3) - 1)]


#Final
print(Word4)