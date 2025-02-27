def log_error_rates(df):
    error_logs = df[df["message"].str.contains("error", case=False)]
    error_rate = (len(error_logs) / len(df)) * 100
    return f"Error Rate: {error_rate:.2f}%"

def most_common_queries(df):
    return df["message"].value_counts().head(10)
