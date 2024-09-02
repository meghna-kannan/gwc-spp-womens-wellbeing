# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd=pd.read_csv("livwell135.csv")

# Print out the number of rows and columns
print(lwd.shape)

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'


oneCountryBooleanList = lwd["country_name"]=="Nigeria"
oneCountryData = lwd.loc[oneCountryBooleanList]
print(oneCountryData)
# create a scatter plot
plt.scatter(oneCountryData["year"],oneCountryData["RH_contr_modern_know_p"],color="red")

# add a title to the plot
plt.title("Percent of Women Who Know Any Modern Method of Contraception Over Time")
plt.ylim(0, 100)
#Label the x-axis
plt.xlabel("Year")

# label the y-axis
plt.ylabel("Women who know any modern method of contraception (%)")


print("""Setting: Nigeria is located to the north of the equator in Africa.Nigeria is the most populated country in Africa and is the sixth most populated country in the world. 32% of Nigeria's population lives in extreme poverty (as of 2017)."""
)
print()
print("""Characters: 68% of Nigerians feel not safe in their country. 68% of the Nigerian population is literate, and the rate for men (75.7%) is higher than that for women (60.6%). Child marriage remains common in Northern Nigeria; 39% of girls are married before age 15, although the Marriage Rights Act banning marriage of girls under 18 was introduced on a federal level in 2008."""
)
print()
print("""Context: Life expectancy in Nigeria is 54.7 years on average, and 71% and 39% of the population have access to improved water sources and improved sanitation, respectively. As of 2019, the infant mortality is 74.2 deaths per 1,000 live births. Women face a large amount of inequality politically in Nigeria, being subjugated to a bias that is sexist and reinforced by socio-cultural, economic and oppressive ways.Nigeria is considered to be one of the most homophobic countries in the world."""
)
print()
print("Research Question: How does women's lack of knowledge of modern contraception methods impact child marriages and teen  pregnancies?")

# show the plot
plt.show()

