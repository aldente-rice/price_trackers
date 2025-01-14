This project contains price trackers for various websites. The goal is to collect the prices
to track overtime to allow consumers to get the best prices for their products. Since there are many
e-commerce websites, it is important that users get the data from more than one place, and that may be
difficult with the different SKUs and other elements.

Features
- Track a product's price from select websites that will produce a graph of the price
    over a span of time
- Track the price across different websites to produce a graph that compares the prices
    for the websites. To do so, need to find the product from the other website(s) that
    most closely matches the product(s).
    Maybe a user wants to buy an Xbox controller from BestBuy, so then this program
    will search for other websites for this specific controller spec. and compare the prices.
- Create a website that visualizes this (similar to camelcamelcamel.com), except with multiple sources,
    rather than just amazon.com

Potential Features
- For searching for the product across websites, use a weight system
    with a database of things with the weights
    The brand name and model name could have a high weight,
    while things like color and things are lower weights
- A Chrome extension
- A web app
- An android app

Websites tracked includes:
- BestBuy
    https://www.bestbuy.com/
- Amazon
    https://www.amazon.com/ref=nav_logo

Documentation
Selenium: https://www.selenium.dev/documentation/

Other
'Fuzzy String Search' - approximate string matching
    https://stackoverflow.com/questions/5859561/getting-the-closest-string-match
    https://stackoverflow.com/questions/32337135/fuzzy-search-algorithm-approximate-string-matching-algorithm

