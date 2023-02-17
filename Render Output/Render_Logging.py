#Jangan edit kode ni

import logging
import time

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Log the message
logging.info("+ Bot Online Now")

# Get the start time
start_time = time.time()

# Main bot code here...

# Calculate the uptime
uptime = time.time() - start_time
hours, rem = divmod(uptime, 3600)
minutes, seconds = divmod(rem, 60)

# Log the uptime
logging.info(f"Uptime: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
