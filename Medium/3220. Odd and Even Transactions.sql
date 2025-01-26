with even as(select sum(amount)'even_sum', transaction_date from transactions
where amount % 2 = 0
group by transaction_date),
odd as(select sum(amount) 'odd_sum', transaction_date from transactions
where amount % 2 = 1
group by transaction_date)
select isnull(even.transaction_date,odd.transaction_date) 'transaction_date', isnull(odd_sum,0) 'odd_sum', isnull(even_sum,0) 'even_sum' from even
full join odd on even.transaction_date = odd.transaction_date