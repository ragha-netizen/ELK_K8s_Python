from src.log_parser import fetch_logs
from src.analysis import log_error_rates, most_common_queries
from src.visualize import plot_query_trends, plot_error_rates

def main():
    print("\n🔹 Fetching logs from Elasticsearch...")
    
    # Fetch logs from Elasticsearch inside Kubernetes
    df = fetch_logs("logstash-*")

    if df.empty:
        print("❌ No logs found in Elasticsearch!")
        return

    # Display initial log data
    print("\n🔹 Sample Logs:")
    print(df.head())

    # Analyze Error Rates
    print("\n🔹 Log Error Rate:")
    print(log_error_rates(df))

    # Most common search queries
    print("\n🔹 Most Common Queries:")
    print(most_common_queries(df))

    # Generate Visualizations
    plot_query_trends(df)
    plot_error_rates(df)

if __name__ == "__main__":
    main()
