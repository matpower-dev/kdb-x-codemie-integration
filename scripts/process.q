rows: 10000;
date: .z.d;
datetime: date+asc rows?.z.t;
trade:([]date: date;time:datetime;sym:rows?`AAPL`GOOG`MSFT`TSLA`AMZN;price:rows?100f;size:rows?1000);
quote:([]date: date;time:datetime;sym:rows?`AAPL`GOOG`MSFT`TSLA`AMZN;bid:rows?100f;ask:rows?100f;size:rows?1000);

/ Save partitioned tables with symbol enumeration

.Q.dpft[`$":/mnt/c/Users/MatthewPower/kdb-x-mcp-server/scripts/db";2025.12.03;`sym;`trade]
.Q.dpft[`$":/mnt/c/Users/MatthewPower/kdb-x-mcp-server/scripts/db";2025.12.03;`sym;`quote]
