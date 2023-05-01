import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('C:\\Users\\uttka\\Desktop\\data science\\covid19_tweets.csv')

# Group the data by user_location and count the number of tweets from each location
location_counts = df.groupby('user_location')['text'].count().sort_values(ascending=False).head(10)

# Create a horizontal bar chart of the location counts
fig, ax = plt.subplots()
ax.barh(location_counts.index, location_counts.values)
ax.set_xlabel('Number of Tweets')
ax.set_ylabel('Location')
ax.set_title('Top 10 Tweeting Locations')
plt.show()
