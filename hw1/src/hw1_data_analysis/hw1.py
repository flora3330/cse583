import pandas as pd
bicycle = pd.read_csv('bicycle_data.csv')

print(bicycle.dtypes)
#I got Date     str
#Fremont Bridge Sidewalks, south of N 34th St Total                    float64
#Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk    float64
#Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk    float64
#the Date column records the date and hour of bicycle counts. It should be in datetime format
#instead of a string. The other 3 columns are the bicycle counts, and they should be 
#integer instead of float, since counts are whole numbers.
bicycle= bicycle.rename(columns={"Fremont Bridge Sidewalks, south of N 34th St Total": "total", 
                                 "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk": "west",
                                 "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk": "east"}
                                 )
print(bicycle.columns)
bicycle["Date"] = pd.to_datetime(bicycle["Date"], format="%m/%d/%Y %I:%M:%S %p")
bicycle['total'] = bicycle['total'].astype('Int64')
bicycle['west'] = bicycle['west'].astype('Int64')
bicycle['east'] = bicycle['east'].astype('Int64')
print(bicycle.dtypes)

#3
#total is already in total column
bicycle["hour"] = bicycle["Date"].dt.hour
bicycle["year"] = bicycle["Date"].dt.year
print(bicycle.head())   

#4
bicycle_2016 = bicycle[bicycle["year"] == 2016].copy()

#5
num_missing_rows = bicycle_2016.isna().any(axis=1).sum()
print(num_missing_rows)
# there is one point with missing data

bicycle_2016 = bicycle_2016.dropna(subset=["east", "west", "total"])

#6
import matplotlib.pyplot as plt

counts_by_hour = bicycle_2016.groupby("hour")["total"].sum()
 
fig, ax = plt.subplots(figsize=(9, 5))
counts_by_hour.plot(ax=ax, kind="line")
ax.set_title("Fremont Bridge bicycle counts by hour in 2016")
ax.set_xlabel("Hour of day")
ax.set_ylabel("total daily counts (East + West)")
#ax.tick_params(axis="x", rotation=0)
fig.tight_layout()
fig.savefig("counts_by_hour.png", dpi=150)
plt.close(fig)

#7
avg_by_hour = bicycle_2016.groupby("hour")["total"].mean()
print(avg_by_hour.idxmax())
#the busiest hour is 17 (5pm)