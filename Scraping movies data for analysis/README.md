
# Movie Data Scraping from "The Number.com"

## Overview
This project involves scraping data for approximately 300 movies from "The Number.com" website. The scraped data includes the following details for each movie:

- Rank
- Movie Name
- Genre
- Production Budget
- MPAA Rating
- Date
- Gross
- Theaters
- Number of Days in Box Office

The purpose of this project is to gather comprehensive movie data for analysis or any other research purposes.

## Technologies Used
- `Python`
- `Selenium (for web automation)`
- `BeautifulSoup (for web scraping)`

## Installation
To run this project on your local machine, follow these steps:

- Clone this repository
- Navigate to the project directory
- Install the required Python libraries using pip 
- Download the appropriate web driver for Selenium (e.g., ChromeDriver) and place it in the project directory or update the webdriver path in the code

## Blog
https://noumankhanonai.com/scraping-movie-data-for-analysis/

## Usage
- Run the Python script scrape_movies.py to start the scraping process:
`python scrape_movies.py`

- The script will automate the web browsing using Selenium and extract movie data from "The Number.com." It will store the data in a CSV file.

## Data Output
The scraped data will be saved in the .csv file with columns: Rank, Name, Genre, Production_Budget, MPAA, Date, Gross, Theaters, Days.

![alt text](https://noumankhanonai.com/wp-content/uploads/2023/09/data.png)

![alt text](https://noumankhanonai.com/wp-content/uploads/2023/09/info.png)

## Contributing
Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.



