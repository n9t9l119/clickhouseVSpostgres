SELECT
    a.Origin,
    num1 * 100 / num2 as all_month,
    num3 * 100 / num4 as end_of_month,
    num5 * 100 / num6 as start_of_month
FROM
    (
        SELECT
            Origin,
            count(*) AS num1
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND Year >= 1997
        GROUP BY
            Origin
    ) a
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS num2
        FROM
            benchmark
        WHERE
            Year >= 1997
        GROUP BY
            Origin
    ) a2 on a.Origin = a2.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS num3
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND DayofMonth > 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) b on a.Origin = b.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS num4
        FROM
            benchmark
        WHERE
            DayofMonth > 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) b2 on b.Origin = b2.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS num5
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND DayofMonth <= 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) c on c.Origin = b.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS num6
        FROM
            benchmark
        WHERE
            DayofMonth <= 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) c2 on c.Origin = c2.Origin
ORDER BY
    a.Origin