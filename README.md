# book-repository

# Overview:

Required course textbooks can be a significant expense for students, and students are often presented with several purchasing options for the same book. Online marketplaces often offer better deals than campus stores, but comparing these options manually is time consuming, especially since students need several books per semester. Book Repository is a command-line tool that helps students find the best deals on textbooks. The program searches multiple online stores (via Barcode Lookup) using an ISBN and displays the prices. To make the project useful for international students, currency conversion is included in the functionality.

# Project Status:

This project is currently in active development. The initial prototype was built using the Barcode Lookup API during its free trial, which was used to validate the ISBN lookup and price-comparison concept. The free trial has since ended, so the current version cannot make live API requests without valid credentials.

The next development stage is to integrate additional book-marketplace data sources, including AbeBooks' Search Web Services API, followed by development of a web-based user interface.

# Key Features:

1. Search for books using ISBN numbers
2. Fetch real-time prices from various stores using Barcode Lookup API
3. Convert prices to the preferred currency
4. Open links directly from terminal
5. Calculate total price of books

# Tools Used:

1. Python 3.11, including the third-party library requests
2. Barcode Lookup API for price data. Please note that the free version, which I used, has limited access.
3. Open Exchange Rates API for currency conversions. Again, the free version has limitations; specifically it doesn't allow a base currency other than USD. As a workaround, the program will perform an additional conversion from USD to the preferred currency.

## Configuration:

This project requires API keys for the external services used by the application. The following must be set:
BARCODE_LOOKUP_API_KEY
OPEN_EXCHANGE_RATES_API_KEY

# Example Workflow:
1. The user will be asked how many books they want, as well as the currency.
2. For each book, the user will be asked to enter an ISBN number.
3. The program fetches store and price data for the ISBN number and displays it. Prices will be converted to the preferred currency.
4. The user can select a store, which will open the link. The user can also add the book to a cart.
5. The program will display the total price of all the books in the cart.

# Future Improvements:
1. Allow search by title instead of limiting it to ISBN
2. Develop a GUI version
