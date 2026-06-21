import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# SAMPLE DATASET
# -----------------------
data = {
    "review": [
        "This product is amazing, I love it",
        "Worst experience ever, very bad service",
        "It is okay not too good not too bad",
        "Excellent quality and fast delivery",
        "I hate this product, waste of money",
        "Very nice and useful product",
        "Not satisfied with the product",
        "Pretty good experience overall"
    ]
}

df = pd.DataFrame(data)

# -----------------------
# SENTIMENT FUNCTION
# -----------------------
def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df["Sentiment"] = df["review"].apply(get_sentiment)

print(df)

# -----------------------
# VISUALIZATION
# -----------------------
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Analysis Result for Reviews")
plt.show()