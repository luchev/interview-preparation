SELECT name as NAME,
    balance as BALANCE
FROM(
        SELECT account,
            SUM(amount) as balance
        FROM Transactions
        GROUP BY account
        HAVING balance > 10000
    ) as acc_balance
    JOIN Users ON Users.account = acc_balance.account
