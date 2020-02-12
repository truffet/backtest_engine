# backtest_engine
Building a backtest engine for financial models based on OmniSci

# install requirements
Git  
python3 (should already be installed on ubuntu)  
OmniSci for Ubuntu  
anaconda (https://www.anaconda.com/distribution/)  
-> conda-forge / pymapd / CUDA / requests  
cuDF  
requests(python)  

# Quick launch guide
1- start server -> "start_server.sh"  
2- launch omnisci CLI -> "omnisci_cli.sh"  

# Launch Backtest on bitcoin/bitmex_perps
- start server -> "start_server.sh" under init file at root
- to create or update trades history data in database, simply execute python file "update_db.py"  

# Issues to be fixed / ideas
- find a way to handle max-rows in a database if needed (2^62 default limit)  
- maybe create a default database that lists support exchanges and markets?
