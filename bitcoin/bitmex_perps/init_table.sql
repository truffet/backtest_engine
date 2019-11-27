CREATE TABLE IF NOT EXISTS tradesHistory (
tradeTime TIMESTAMP NOT NULL,
symbol TEXT,
side TEXT,
size INTEGER,
price FLOAT, 
tickDirection TEXT,
trdMatchID TEXT,
grossValue FLOAT,
homeNotional FLOAT,
foreignNotional FLOAT
);