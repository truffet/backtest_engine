# backtest_engine
Building a backtest engine for financial models based on OmniSci

# install requirements
Git  
python3 (should already be installed on ubuntu)  
OmniSci for Ubuntu (define first superuser as 'truffet' with password 'bodyboard' along with 'bitmex' database)  
pymapd  
cuDF  
requests(python)  

# Quick launch guide
1- start server -> "start_server.sh"  
2- launch omnisci CLI -> "omnisci_cli.sh"  

# Launch Backtest on bitcoin/bitmex_perps
- start server -> "start_server.sh"
- create or update trades history data in database with 'init.sh'  

# Issues to be fixed
- find a way to handle max-rows in a database if needed (2^62 default limit)
