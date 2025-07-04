import pandas as pd
import random

# Sample data generation
data = {
    'Date': pd.date_range(start='2024-06-01', periods=30),
    'Platform': random.choices(['Twitter', 'Instagram', 'Facebook'], k=30),
    'Posts': [random.randint(1, 5) for _ in range(30)],
    'Likes': [random.randint(50, 500) for _ in range(30)],
    'Comments': [random.randint(10, 100) for _ in range(30)],
    'Shares': [random.randint(5, 50) for _ in range(30)],
    'Followers': [random.randint(1000, 10000) for _ in range(30)]
}

df = pd.DataFrame(data)
df.to_csv('social_engagement.csv', index=False)
print("CSV generated successfully.")
