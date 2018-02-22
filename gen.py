# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random,string
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 10:35:17 2017

@author: qiuying
"""

random.seed(0)
fp = open('source.csv','w')

chars = string.ascii_letters + string.digits
data = [0] * 11
#save data
most_v = 0
result = 0
for i in range(1,230):
    integer1 = random.randint(1,10)
    data[integer1] += 1
    #get string1 and 2
    string1 = "".join(random.sample(chars, random.randint(1,32)))
    string2 = "".join(random.sample(chars, random.randint(1,32)))
    temp_v = 0
    temp_s = string1 + string2
    for j in 'a,e,i,o,u':  #find aeiou
        temp_v += temp_s.count(j)
        
    if  temp_v > most_v:  #check most
        result = i
        most_v = temp_v
    fp.write('{},{},{},{}\n'.format(i, integer1, string1, string2)) #to file

print('{},{},{},{}\n'.format(i, integer1, string1, string2))
print(data)
print(result, most_v)  
  
fp.close()

