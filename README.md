# python-flask-mongoDB
## Small example project

1. The script pulls json data from the following url: http://api.coincap.io/v2/assets/bitcoin/history?interval=d1
The Json file contains the price of Bitcoin in USD and the corresponding timestamps.
2. The script can make very basic (avg, sum, std) async calculations on the downloaded data
3. The results of these calculations are returned by a flask server

The script can also create basic visualizations:

![polinom](/pictures/polynomial_analysis.png)
![regplot](/pictures/regplot.png)
