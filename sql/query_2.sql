SELECT
    Year,
    Month,
    DayofMonth,
    Origin,
    Dest
FROM
    benchmark
WHERE
    Flights > 5
    AND Distance > 100
    AND Diverted = 1
    AND DestCityName NOT IN ('New York', 'Texas')
    AND Quarter = 2
    OR Flights > 10
    AND Distance > 75
    AND Diverted = 0
    AND DestCityName != 'Texas'
    AND Quarter = 3
ORDER BY
    Carrier