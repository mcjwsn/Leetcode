with t1 as(
    select stock_name, operation, sum(price) as 'suma' from Stocks
    where operation = 'Buy'
group by stock_name, operation),
t2 as(select stock_name, operation, sum(price) as 'suma' from Stocks
    where operation = 'Sell'
group by stock_name, operation)
select t1.stock_name, t2.suma - t1.suma 'capital_gain_loss' from t2
join t1 on t1.stock_name = t2.stock_name