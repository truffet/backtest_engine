# backtest_engine
Building a backtest engine for financial models based on OmniSci

# install requirements
Git  
python3 (should already be installed on ubuntu)  
MySQL/MySQL server(root password bodyboard)  
requests(python)  
pip3  
MySQL Connector  
pyarrow  
pandas  
python3-matplotlib  
SQLAlchemy  
plotly

# Quick launch guide  

# Launch data update  

# Issues to be fixed / ideas  
- prepare for system or program unexpected shutdown by comparing data fetched and data stored  
- handle api rate limit properly(check allowance)  
- 'str' object has no attribute 'json' -> handle this error properly (occurs when fetching data from kraken api)
