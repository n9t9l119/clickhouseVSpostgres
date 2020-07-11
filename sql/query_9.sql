SELECT Delayed.Month,
    Delayed.c1 * 100 / AllF.c2,
    Early.c3 * 100 / AllF.c2,
    OnTime.c4 * 100 / AllF.c2
FROM (
        SELECT Month,
            COUNT(*) AS c1
        FROM benchmark
        WHERE DepDelay > 10
        GROUP BY Month
    ) AS Delayed
    INNER JOIN (
        SELECT Month,
            COUNT(*) as c2
        FROM benchmark
        GROUP BY Month
    ) AS AllF ON Delayed.Month = AllF.Month
    INNER JOIN (
        SELECT Month,
            COUNT(*) AS c3
        FROM benchmark
        WHERE DepDelay < -10
        GROUP BY Month
    ) AS Early ON Delayed.Month = Early.Month
    INNER JOIN (
        SELECT Month,
            COUNT(*) AS c4
        FROM benchmark
        WHERE DepDelay = 0
        GROUP BY Month
    ) AS OnTime ON Early.Month = OnTime.Month