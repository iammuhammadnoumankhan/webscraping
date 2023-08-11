This project is built to scrape chocolate data from the chocolate.co.uk website, including the Name, price, and URL for every item.
In this project, we scrape data using Scarpy by making chocolatespider. 
For running this project, first of all, install the dependencies by running "pip install -r requirements.txt".
Then, you need to put the username and password for your MySQL in the pipelines.py file.
The chocolate_scraping.sql file is given, you should first make a database for your PC.
Then run this command to scrape the data into the MySQL database.
"scrapy crawl chocolatespider"
If you want to scrape the data into csv file then run, "scrapy crawl chocolatespider -o data.csv"
If you want to scrape the data to json file then run, "scrapy crawl chocolatespider -o data.json"
