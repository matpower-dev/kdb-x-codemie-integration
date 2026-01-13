getTrade:{[s;t] $[null t; 
    select from trade where sym = s;
    select from trade where sym = s, time >= t
    ]
 };
getQuote:{[s] 
    select from quote where sym = s
 };
getMaxPriceBySym:{
    select maxPrice:max price by sym from trade
 };



