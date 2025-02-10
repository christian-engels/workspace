import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a simple plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Show the plot
plt.show()
