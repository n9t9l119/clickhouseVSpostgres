SELECT
    AirportsWithNoDepDelays.OriginAirportID,
    NoDepDelays,
    AirportsWithNoArrDelays.DestAirportID,
    NoArrDelays
FROM
    (
        SELECT
            OriginAirportID,
            count(*) AS NoDepDelays
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
    ) AirportsWithNoDepDelays
    INNER JOIN (
        SELECT
            DestAirportID,
            count(*) AS NoArrDelays
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
    ) AirportsWithNoArrDelays on AirportsWithNoDepDelays.OriginAirportID = AirportsWithNoArrDelays.DestAirportID
ORDER BY
    AirportsWithNoDepDelays.OriginAirportID