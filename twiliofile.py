from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from twilio.rest import Client
import time
import schedule
# Replace with relevant info where needed
account_sid = "twilio account sid"
auth_token = "twilio auth token"
twilio_phone_number = '+twilio phone num'
your_phone_number = 'enter your phone number'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_sms(message):
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )
    print(f"Sent message: {message.body}")

def scrape_news():
	driver = webdriver.Chrome()
	url = "https://news.sky.com/uk"
	driver.get(url)

	# Random delay between 2 to 5 seconds
	driver.implicitly_wait(10)

	headline_store = []

	# Scrape headlines and store them in the headline_store list
	search = driver.find_elements(By.CLASS_NAME, 'sdc-site-tile__headline-link')
	for i in search:
	    headlines = i.text
	    link = i.get_attribute('href')
	    headline_store.append([headlines, link])

	# Concatenate all headlines into one message
	message_body = "\n".join([f"{headline}: {link}" for headline, link in headline_store])

	# Split message into chunks of 1500 characters or less because of twilio character limit per sms message
	chunk_size = 1500
	chunks = [message_body[i:i+chunk_size] for i in range(0, len(message_body), chunk_size)]

	# Send each chunk as a separate message
	for chunk in chunks:
	    send_sms(chunk)

	print("Sent all headlines as separate messages.")  # Indicate success

	# Close the WebDriver
	driver.quit()



# Schedule the task to run daily at a specific time (adjust the time as needed)
schedule.every().day.at("09:00").do(scrape_news)

# Keep the script running to allow scheduling
while True:
    schedule.run_pending()
    time.sleep(1)









	 
