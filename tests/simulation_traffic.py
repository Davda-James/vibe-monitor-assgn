import requests
import time
import logging
import signal
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration
TARGET_URL = "http://localhost:8000/api/serve"

# Global flag for graceful shutdown
running = True

def signal_handler(signum, frame):
    global running
    print("\nShutting down gracefully...")
    running = False

def make_request():
    try:
        response = requests.get(TARGET_URL)
        logging.info(f"Request made. Status: {response.status_code}")
        return response.status_code
    except Exception as e:
        logging.error(f"Error making request: {str(e)}")
        return None

def main():
    # Set up signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    logging.info("Starting requests")
    logging.info("Press Ctrl+C to stop")
    
    try:
        while running:
            make_request()
            # Small sleep to prevent overwhelming the server
            time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info("Stopping requests")
            
if __name__ == "__main__":
    main()
    sys.exit(0)
