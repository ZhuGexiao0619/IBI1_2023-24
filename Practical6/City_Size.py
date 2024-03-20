import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7]
China_cities=[0.58,8.4,29.9,22.2]
uk_names=["Edinburgh","Glsgow","Stirling","London"]
China_names=["Haning","Hangzhou","Shanghai","Beijing"]
plt.figure()
plt.bar(uk_names,uk_cities)
plt.show()
plt.clf()
plt.figure()
plt.bar(China_names,China_cities)
plt.show()
