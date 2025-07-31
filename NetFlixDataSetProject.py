import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


netflixData=pd.read_csv("NetflixShows.csv",encoding="utf-8",encoding_errors="ignore")
print(netflixData["ratingLevel"].head())

# print(type(netflixData["ratingLevel"][0]))



# removing all the NaN values 

# For "ratingLevel"
netflixData["ratingLevel"].fillna("0",inplace=True)
netflixData.loc[netflixData["rating"]=="0","ratingLevel"]=="This has not been rated"
print(netflixData.isnull().sum())


# for "user rating score"
netflixData["user rating score"].fillna(0.0,inplace=True)
print(netflixData["user rating score"].head())
print(netflixData.isnull().sum())




# removing duplicate data
netflixData.drop_duplicates(inplace=True)





# making Pie Chart for rating 

fig,ax=plt.subplots(2,2)
ratingtypes=netflixData["rating"].value_counts()
ax[0][0].pie(ratingtypes.values,labels=ratingtypes.index,autopct="%1.1f%%")
ax[0][0].set_title("Types of Rating")
# plt.show()



# making bar chart for at which how many TV show released
releasingYear=netflixData["release year"].value_counts()
ax[0][1].bar(releasingYear.index,releasingYear.values,label="Number of Tv Shows")
ax[0][1].set_xlabel("Year")
ax[0][1].set_ylabel("Number of release")
ax[0][1].set_title("Year vs Number of Tv shows")





User_score=netflixData["user rating score"].value_counts()




# Making comparison Bar graph on user score and user size
NameofShow=netflixData["title"].value_counts()
User_size=netflixData["user rating size"].value_counts()
print(User_score.value_counts())

ax[1][0].bar(User_score.index,User_score.values,color="blue")
ax[1][0].set_title("user score vs number of user")
ax[1][0].set_xlabel("User rating")
ax[1][0].set_ylabel("Number of user")




ax[1][1].bar(User_size.index,User_size.values,color="orange")
ax[1][1].set_xlabel("User size")
ax[1][1].set_ylabel("Number of user size")
ax[1][1].set_title("User size vs Number of User size")





plt.suptitle("All The Detail of the  Netflix Dataset")
plt.tight_layout()
plt.show()





