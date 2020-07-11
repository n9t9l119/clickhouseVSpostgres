SELECT
    a.OriginAirportID,
    num1,
    b.DestAirportID,
    num2
FROM
    (
        SELECT
            OriginAirportID,
            count(*) AS num1
        FROM
            benchmark
        WHERE
            Year = 2017
            AND DepDelayMinutes = 0
            AND ArrDelayMinutes = 0
            AND Cancelled = 0
            AND Diverted = 0
            AND CarrierDelay = 0
        GROUP BY
            OriginAirportID
    ) a
    INNER JOIN (
        SELECT
            DestAirportID,
            count(*) AS num2
        FROM
            benchmark
        WHERE
            Year = 2017
            AND DepDelayMinutes = 0
            AND ArrDelayMinutes = 0
            AND Cancelled = 0
            AND Diverted = 0
            AND CarrierDelay = 0
        GROUP BY
            DestAirportID
    ) b on a.OriginAirportID = b.DestAirportID
ORDER BY
    a.OriginAirportID