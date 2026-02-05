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
litres_of_water = [1,2,3,4,5,6,7]
exercise_mins = [10,15,30,35,45,50,60]
 
# Now we are going to combine the separate lists into a pandas dataframe
data = {
    "Day": days,
    "Study Hours" : study_hours,
    "Water(litres)": litres_of_water,
    "Exercise(min)": exercise_mins
}
df = pd.DataFrame(data)
st.dataframe(df)


