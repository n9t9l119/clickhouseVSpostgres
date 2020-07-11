SELECT
    a.Carrier,
    num1 * 100 / num2 DepDelayCoef,
    num3 * 100 / num4 AirDelayCoef
FROM
    (
        SELECT
            Carrier,
            count(*) AS num1
        FROM
            benchmark
        WHERE
            DepDelay > 10
            AND Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) a
    INNER JOIN (
        SELECT
            Carrier,
            count(*) AS num2
        FROM
            benchmark
        WHERE
            Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) a2 on a.Carrier = a2.Carrier
    INNER JOIN(
        SELECT
            Carrier,
            count(*) AS num3
        FROM
            benchmark
        WHERE
            ArrDelay > 10
            AND Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) b on b.Carrier = a.Carrier
    INNER JOIN (
        SELECT
            Carrier,
            count(*) AS num4
        FROM
            benchmark
        WHERE
            Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) b2 on b.Carrier = b2.Carrier
ORDER BY
    a.Carrier DESC