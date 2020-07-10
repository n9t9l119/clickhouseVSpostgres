SELECT a.Year,
    c1 / c2
FROM (
        select Year,
            count(*) as c1
        from benchmark
        WHERE DepDelay > 10
        GROUP BY Year
    ) a
    INNER JOIN (
        select Year,
            count(*) as c2
        from benchmark
        GROUP BY Year
    ) b on a.Year = b.Year
ORDER BY a.Year;