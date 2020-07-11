SELECT
    FlightsWithDepDelayCount.Carrier,
    DepDelayCount * 100 / AllFlightsCount as DepDelayCoef,
    ArrDelayCount * 100 / AllFlightsCount as AirDelayCoef
FROM
    (
        SELECT
            Carrier,
            count(*) AS DepDelayCount
        FROM
            benchmark
        WHERE
            DepDelay > 10
            AND Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) FlightsWithDepDelayCount
    INNER JOIN (
        SELECT
            Carrier,
            count(*) AS AllFlightsCount
        FROM
            benchmark
        WHERE
            Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) Flights on FlightsWithDepDelayCount.Carrier = Flights.Carrier
    INNER JOIN(
        SELECT
            Carrier,
            count(*) AS ArrDelayCount
        FROM
            benchmark
        WHERE
            ArrDelay > 10
            AND Year >= 2000
            AND Year <= 2008
        GROUP BY
            Carrier
    ) FlightsWithArrDelayCount on FlightsWithArrDelayCount.Carrier = FlightsWithDepDelayCount.Carrier
ORDER BY
    FlightsWithDepDelayCount.Carrier DESC