
import string

chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}
#-----question 1-----
dict1={int(i):j for i,j in chest.items()}
sort1 = sorted(dict1.items())
chest = dict(sort1)
print(chest)

#-----question 2-----
a=(tuple(chest.items())[0])
b=(tuple(chest.items())[1])
c=(tuple(chest.items())[-1])
d=(tuple(chest.items())[-2])
list1=[a,b,c,d]
print(list1)
#------question 3----
variable2=dict(list1)
s=""
for i in variable2.values():
    s= s + str(i)
print (s)
#------question 4-----

def firstLast(string):
    str=""    
    for i in range(len(string)):
        if i == 0:
            str = str + string[i]
        if i == len(string) - 1:
            str = str + string[i]
        if string[i] == " ":
            str = str + string[i - 1] + string[i + 1]
    return str
occurance=firstLast(s)
print(occurance)

#------question 5-----
n=5
number_of_occurance=[]
c_dict={}
for i in occurance:
    if i not in c_dict:
        c_dict[i] = 1
    else:
        c_dict[i] +=1
sorted_dict = sorted(c_dict.items(),key=lambda x: (-x[1],x[0]))
soreted_dict = sorted_dict[:n]
print(dict(soreted_dict))
for key,value in soreted_dict:
    number_of_occurance.append(value)
print(number_of_occurance)
#--------question 6--------
key_list = []
for i in chest.keys():
    key_list.append(i)
print(key_list)
#-------question 7------
sum_list = [sum(value) for value in zip(number_of_occurance, key_list)]
print(sum_list)
#-------question 8-----
ascii_char =[]
for i in sum_list:
    ascii_char.append(chr(i))
print(ascii_char)







    