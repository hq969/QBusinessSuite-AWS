from ai_assistant.q_business import process_query
from dashboard.quicksight_dashboard import get_dashboard
from automation.q_apps import create_q_app

if __name__ == "__main__":
    query = input("Ask Q Business: ")
    print(process_query(query))
