# Web Scraping and SMS News Alerts with Twilio API
This project automates the process of retrieving news headlines from a specified website and sending them as SMS alerts using the Twilio API. By running this Python script, you can receive daily news updates at a scheduled time without manual intervention.

# How It Works
-Web Scraping: The script employs the Selenium library to scrape news headlines from the Sky News website.

-Twilio API Integration: This project integrates with the Twilio API, a powerful cloud communications platform, to send SMS messages. To enable this functionality, you must provide your Twilio Account SID, Auth Token, Twilio phone number, and your own phone number.

-Message Splitting: Given that SMS messages have character limits, the script splits the news headlines into manageable chunks to ensure they fit within the message size constraints.

-Scheduling: You have the flexibility to schedule the script to run automatically at a specific time each day. This ensures you receive news updates consistently without needing manual interaction. In the provided example, the script is scheduled to run daily at 9:00 AM, but you can easily adjust the schedule to your preferred time.

-Continuous Execution: Thanks to the Schedule library, the script continues to run in the background, ensuring that the news scraping and SMS sending tasks occur as scheduled each day.



# Use case
This project is beneficial for individuals who want to stay informed about the latest news without actively checking news websites. By automating the process, you can receive daily news alerts on your mobile phone, making it a convenient solution for keeping up with current events.
