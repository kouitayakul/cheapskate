# cheapskate

A small python application that scraps a web page’s HTML. Currently this application is scrapping BestBuy’s website to check the price of a product on a weekly basis. Once a desired price is met, the script sends out both an email and a WhatsApp message using Twilio API. 

This application is deployed on Amazon Web Services (AWS) Lambda, which uses a cron schedule to execute the script twice a week. 

## NOTE:
 - Only websites that are allowed to be scrapped should be scrapped with this application
 - Check whether a website is scrapable by adding “robots.txt” at the end of the URL
 - A list of “Allow” and “Disallow” endpoints will show us which endpoints are scrapable
 
 - WhatsApp messaging functionality is not currently live because an approval by WhatsApp is needed to use the WhatsApp Twilio Number
 - WhatsApp Twilio Number can only be used in the WhatsApp Sandbox at the moment
