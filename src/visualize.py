import matplotlib.pyplot as plt
import seaborn as sns

def plot_query_trends(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df["timestamp"], bins=20, kde=True)
    plt.title("Query Frequency Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

def plot_error_rates(df):
    error_logs = df[df["message"].str.contains("error", case=False)]
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=error_logs["timestamp"], y=error_logs.index)
    plt.title("Error Log Trends")
    plt.xlabel("Time")
    plt.ylabel("Errors")
    plt.xticks(rotation=45)
    plt.show()
