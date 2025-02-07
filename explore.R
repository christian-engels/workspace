# Load necessary libraries
library(ggplot2)
library(dplyr)

# Load dataset
data <- mtcars

# Summary of the dataset
summary(data)

# Plotting
ggplot(data, aes(x=wt, y=mpg)) +
  geom_point() +
  labs(title="Weight vs MPG",
       x="Weight",
       y="Miles per Gallon")

       