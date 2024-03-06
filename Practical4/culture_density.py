#The first day's density is 0.05
d=0.05
#From day 0
day=0
while d<=0.9:
    d=d*2
    day+=1
print("I can leave the lab for "+str(day)+" days")
