from dotenv import load_dotenv
import os
from clubrunner import Clubrunner

# Load environment variables from .env file
load_dotenv()

# Access the BASE_URL environment variable
clubrunner_site = os.getenv('clubrunner_site')

def main():
    automation = Clubrunner(clubrunner_site)
    automation.send_meeting_reminder()

if __name__ == "__main__":
    main()