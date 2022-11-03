# Team 2 Article Replication Project

## Data Acquisition
See `Macro_Data_Acquisition_Team_2.ipynb` for solution of this task.

The data was compiled into a pandas DataFrame and uploaded as a .csv file `macro.csv`.

The DataFrame contains all data points available on each time series. For futher analysis only relevant time period was utilized.

Contributors to this task: Yudaykin Kirill, Mikhailov Daniil, Matevosova Anastasia, Zudin Anton

#### Some details on the data
- GDP: U.S. Bureau of Economic Analysis, Gross Domestic Product [GDP], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/GDP, October 26, 2022.
- PCEC: U.S. Bureau of Economic Analysis, Personal Consumption Expenditures [PCEC], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PCEC, October 26, 2022.
- GDP: U.S. Bureau of Economic Analysis, Gross Domestic Product: Implicit Price Deflator [A191RI1Q225SBEA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/A191RI1Q225SBEA, October 26, 2022.
- CPI less food and energy: Federal Reserve Bank of Atlanta, Sticky Price Consumer Price Index less Food and Energy [CORESTICKM159SFRBATL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CORESTICKM159SFRBATL, October 26, 2022.
- Total CPI: Federal Reserve Bank of Atlanta, Sticky Price Consumer Price Index [STICKCPIM157SFRBATL], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/STICKCPIM157SFRBATL, October 26, 2022.
- Investments: U.S. Bureau of Economic Analysis, Gross Private Domestic Investment [GPDI], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/GPDI, October 26, 2022.
- Inventories: U.S. Bureau of Economic Analysis, Private inventories [A371RC1Q027SBEA], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/A371RC1Q027SBEA, October 27, 2022.
- Wilshire 5000 Full Cap Price Index: Wilshire Associates, Wilshire 5000 Full Cap Price Index [WILL5000PRFC], retrieved from FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/WILL5000PRFC, October 26, 2022.

## Data Filtering and Results Generation
See `Macro_Analysis_Team_2.ipynb` for solution.

We have filtered the data to obtain detrended time series using Baxter and King filter with the same parameters as in the suggested article.

After detrending the data, our team has prepared the table analogous to table (3.b) from the article in question.

Contributors to this task: Osipov Alexey, Titov Egor, Medvedev Vsevolod

## Cross Correlation for Different Filters
See `Macro_Filtered_Cross_Corr_Team_2.ipynb` for solution.

Several filters mentioned in the article in question were applied to gatherd data. Stationarity analysis with Dickey-fuller test was conducted.

Contributors to this task: Dorofeeva Anastasia, Kaplun Ivan, Titov Egor




