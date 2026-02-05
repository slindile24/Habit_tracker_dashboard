import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

title = st.title("Habit Tracker")
description = st.write("This dashboard shows my weekly habit progress")


#Now I am going to create a small dataset 

#It will include Days, Study hours, Water and Exercise

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
   
# now creating a list for all the other columns 
study_hours = [1,2,3,4,5,6,7]
litres_of_water = [4,5,3,1,2,6,7]
exercise_mins = [10,5,30,35,45,50,60]
 
# Now we are going to combine the separate lists into a pandas dataframe
data = {
    "Day": days,
    "Study Hours" : study_hours,
    "Water(litres)": litres_of_water,
    "Exercise(min)": exercise_mins
}
df = pd.DataFrame(data)
st.dataframe(df)

fig, ax = plt.subplots()


#Plotting the data
ax.plot(df["Day"],df["Study Hours"],marker="o", label="Study Hours")
ax.plot(df["Day"], df["Water(litres)"], marker="o", label="Water")
ax.plot(df["Day"], df["Exercise(min)"], marker="o", label="Exercise")



#Label the chart
ax.set_xlabel("Day")
ax.set_ylabel("Amount")

# ax.set_ylabel("Water(litres)")
ax.set_title("Weekly Habit Tracker")

ax.legend()

st.pyplot(fig)

total_study_hours = df["Study Hours"].sum()
total_litres_of_water = df["Water(litres)"].sum()
total_exercise = df["Exercise(min)"].sum()

labels = ["Study Hours", "Water(litres)", "Exercise(min)"]
totals = [total_study_hours,total_litres_of_water,total_exercise]

fig2, ax2 = plt.subplots()
ax2.bar(labels, totals, color=["pink","red","green"])
ax2.set_ylabel("Weekly Total")

ax2.set_title("Total Habits This Week")
st.pyplot(fig2)