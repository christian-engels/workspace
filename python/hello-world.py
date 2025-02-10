import seaborn as sns
import pyfixest as pf
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")
tips.head()

# Create a simple plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Run a regression of tip on total bill
model = pf.feols('tip ~ total_bill', tips)
model.summary()
