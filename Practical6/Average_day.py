import matplotlib.pyplot as plt
dic1={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1}
dic1["other"]=24-dic1["Sleeping"]-dic1["Classes"]-dic1["Studying"]-dic1["TV"]-dic1["Music"]
Activity=["Sleeping","Classes","Studying","TV","Music","other"]
average=[dic1["Sleeping"],dic1["Classes"],dic1["Studying"],dic1["TV"],dic1["Music"],dic1["other"]]
plt.figure()
plt.pie(average,labels=Activity,startangle=90)
plt.show()
