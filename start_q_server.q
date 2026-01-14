.ai:use`kx.ai
.s.init[]
rows:10000;
trade:([]time:.z.d+asc rows?.z.t;sym:rows?`AAPL`GOOG`MSFT`TSLA`AMZN;price:rows?100f;size:rows?1000);
corrections: @[
    {("SSS";enlist",") 0: `$":/home/matthew/kdb-x-mcp-server/corrections.csv"}
    ;()
    ;{([]QUERY:();BAD:();GOOD:())}
 ];
.z.exit: {
  save `$":/home/matthew/kdb-x-mcp-server/corrections.csv"
 };
