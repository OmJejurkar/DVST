import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
# Replace 'your_data.csv' with the path to your dataset
data = pd.read_csv('your_data.csv')

# Example 1: Bar chart - Count of work types
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='work_type', palette='viridis')
plt.title('Count of Work Types')
plt.xlabel('Work Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Example 2: Scatter plot - BMI vs Average Glucose Level
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='bmi', y='avg_glucose_level', hue='heart_disease', palette='cool')
plt.title('BMI vs Average Glucose Level (Colored by Heart Disease)')
plt.xlabel('BMI')
plt.ylabel('Average Glucose Level')
plt.legend(title='Heart Disease')
plt.show()

# Example 3: Histogram - Distribution of Age
plt.figure(figsize=(10, 6))
plt.hist(data['age'], bins=20, color='steelblue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Example 4: Boxplot - BMI by Smoking Status
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='smoking_status', y='bmi', palette='Set2')
plt.title('BMI by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('BMI')
plt.xticks(rotation=45)
plt.show()
