SELECT weekend.DestCityName,
    weekend.DesCnt,
    weekdays.DesCnt,
    weekend.OriCnt,
    weekdays.OriCnt
FROM (
        SELECT DestCityName,
            DesCnt,
            OriCnt
        FROM (
                SELECT DestCityName,
                    COUNT(*) as DesCnt
                From benchmark
                WHERE DayOfWeek >= 6
                GROUP BY DestCityName
            ) AS Des
            INNER JOIN (
                SELECT OriginCityName,
                    COUNT(*) as OriCnt
                From benchmark
                WHERE DayOfWeek >= 6
                GROUP BY OriginCityName
            ) as Ori ON Des.DestCityName = Ori.OriginCityName
    ) AS weekend
    INNER JOIN (
        SELECT DestCityName,
            DesCnt,
            OriCnt
        FROM (
                SELECT DestCityName,
                    COUNT(*) as DesCnt
                From benchmark
                WHERE DayOfWeek <= 5
                GROUP BY DestCityName
            ) AS Des
            INNER JOIN (
                SELECT OriginCityName,
                    COUNT(*) as OriCnt
                From benchmark
                WHERE DayOfWeek <= 5
                GROUP BY OriginCityName
            ) as Ori ON Des.DestCityName = Ori.OriginCityName
    ) AS weekdays ON weekend.DestCityName = weekdays.DestCityName
WHERE weekdays.DesCnt <= weekend.DesCnt
ORDER BY weekend.DesCnt DESC