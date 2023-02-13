import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
affordable = pd.read_csv("Affordable_Housing_Production_by_Building.csv")
print("Number of dataponts with null entry for each column:\n",affordable.isnull().sum())
affordable.fillna({'Building ID':0, 'Postcode':0,'BBL':0, 'BIN':0},inplace=True)
affordable.fillna({'Council District':0, 'Latitude':0, 'Longitude':0},inplace=True)
affordable.fillna({'Latitude (Internal)':0, 'Longitude (Internal)':0},inplace=True)

#affordable.fillna({'Project Completion Date':""}, inplace=True)
affordable.fillna({'Building Completion Date':""}, inplace=True)
affordable.fillna({'Census Tract':""}, inplace=True)
#affordable.fillna({'NTA - Neighborhood Tabulation Area':""},inplace=True)
affordable.drop(['Latitude (Internal)'], axis=1, inplace=True)
affordable.drop(['Longitude (Internal)'], axis=1, inplace=True)

grouped_zip = affordable.groupby("Postcode")
zipcodes = [11217,11238]
incomelist = ['Extremely Low Income Units','Very Low Income Units','Low Income Units','Moderate Income Units','Middle Income Units','Other Income Units']
print()
print("Key")
print("ELIU: Extremly Low Income Units")
print("VLIU: Very Low Income Units")
print("LIU: Low Income Units")
print("MoIU: Moderate Income Units")
print("MiIU: Middle Income Units")
print("OIU: Other Income Units are units reserved for building superintendents")
print("All Counted Units: total number of units in each building, both affordable and market rate.")
print() 
print("zipcode ELIU VLIU LIU MoIU  MiIU  OIU  Total Units")

for x in range(len(zipcodes)):
    mygroup = grouped_zip.get_group(zipcodes[x])
    print("%7i"%(zipcodes[x]), end=" ") 
    total = 0
    for i in range(len(incomelist)):
        value = mygroup[incomelist[i]].sum()
        print("%4i"%(value), end=" ")
        total += value 

    print("%11i"%(mygroup['All Counted Units'].sum()))

print()
print("Key")
print("Rent: Counted Rental Units")
print("Home: Counted Homeownership Units")
ownlist = ['Counted Rental Units', 'Counted Homeownership Units']
print("zipcode Rent Home Total Total Units")
for x in range(len(zipcodes)):
    mygroup = grouped_zip.get_group(zipcodes[x])
    print("%7i"%(zipcodes[x]), end=" ") 
    total = 0
    for i in range(len(ownlist)):
        value = mygroup[ownlist[i]].sum()
        print("%4i"%(value), end=" ")
        total += value 

    print("%5i"%(total), end=" ") 
    print("%11i"%(mygroup['All Counted Units'].sum()))

xval = ["Rental Units","Homeownership Units"]
xex = [4283,852]

x=np.arange(len(xval))
width = 0.3
fig, ax = plt.subplots()
shapetwo = ax.bar(x-width/2,xex,width,label = "Prospect Heights")
ax.set_ylabel("Number of Units in Prospect Heights")
ax.set_xticks(x,xval)
ax.legend()

ax.bar_label(shapetwo,padding=3)
fig.tight_layout()
plt.show
plt.savefig('RvsH')

prospecthome = grouped_zip.get_group(11217)
onelist = ['Counted Homeownership Units']
print("\nThe percentage of home-owned units in 11217 Prospect Heights: ")
for item in onelist:
    value = ((prospecthome[item].sum())/(prospecthome["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospectrent = grouped_zip.get_group(11217)
twolist = ['Counted Rental Units']
print("\nThe percentage of rental units in 11217 Prospect Heights: ")
for item in twolist:
    value = ((prospectrent[item].sum())/(prospectrent["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospecthome = grouped_zip.get_group(11238)
onelist = ['Counted Homeownership Units']
print("\nThe percentage of home-owned units in 11238 Prospect Heights: ")
for item in onelist:
    value = ((prospecthome[item].sum())/(prospecthome["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospectrent = grouped_zip.get_group(11238)
twolist = ['Counted Rental Units']
print("\nThe percentage of rental units in 11238 Prospect Heights: ")
for item in twolist:
    value = ((prospectrent[item].sum())/(prospectrent["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospect = grouped_zip.get_group(11217)
typelist = ['Studio Units', '1-BR Units', '2-BR Units', '3-BR Units', '4-BR Units', '5-BR Units', '6-BR+ Units', 'Unknown-BR Units']
print("\nThe percentage of studio units in 11217 Prospect Heights by type: ")
for item in typelist:
    #value = round(((prospect[item].sum()/prospect["All Counted Units"].sum())*100),2)
    value = ((prospect[item].sum())/(prospect["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospect2 = grouped_zip.get_group(11238)
typelist = ['Studio Units', '1-BR Units', '2-BR Units', '3-BR Units', '4-BR Units', '5-BR Units', '6-BR+ Units', 'Unknown-BR Units']
print("\nThe percentage of studio units in 11238 Prospect Heights by type: ")
for item in typelist:
    #value = round(((prospect[item].sum()/prospect["All Counted Units"].sum())*100),2)
    value = ((prospect2[item].sum())/(prospect2["All Counted Units"].sum())*100)
    valuerounded = round(value,2)
    print(item,":", valuerounded, "%")

prospectbk = grouped_zip.get_group(11217)
prospectbk.plot(x= "Project Start Date", y= "All Counted Units")
plt.gcf().subplots_adjust(bottom = 0.1)
plt.ylabel('Number of Units')
fig2 = plt.gcf()
fig2.savefig('unitsbydate.png')
plt.clf()

prospectbk = grouped_zip.get_group(11238)
prospectbk.plot(x= "Project Start Date", y= "All Counted Units")
plt.gcf().subplots_adjust(bottom = 0.1)
plt.ylabel('Number of Units')
fig2 = plt.gcf()
fig2.savefig('unitsbydate2.png')
plt.clf()
