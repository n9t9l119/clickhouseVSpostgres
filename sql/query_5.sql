SELECT
    WeekendsAllMonth.Origin,
    WeekendsAllMonthCount * 100 / AllMounthCount as AllMonthCoef,
    WeekendsEndOfMonthCount * 100 / EndOfMonthCoef as EndOfMonthCoef,
    WeekendsStartOfMonthCount * 100 / StartOfMonthCoef as StartOfMonthCoef
FROM
    (
        SELECT
            Origin,
            count(*) AS WeekendsAllMonthCount
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND Year >= 1997
        GROUP BY
            Origin
    ) WeekendsAllMonth
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS AllMounthCount
        FROM
            benchmark
        WHERE
            Year >= 1997
        GROUP BY
            Origin
    ) AllMounth on WeekendsAllMonth.Origin = AllMounth.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS WeekendsEndOfMonthCount
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND DayofMonth > 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) WeekendsEndOfMonth on WeekendsAllMonth.Origin = WeekendsEndOfMonth.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS EndOfMonthCoef
        FROM
            benchmark
        WHERE
            DayofMonth > 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) EndOfMonth on EndOfMonth.Origin = WeekendsEndOfMonth.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS WeekendsStartOfMonthCount
        FROM
            benchmark
        WHERE
            DayOfWeek in (6, 7)
            AND DayofMonth <= 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) WeekendsStartOfMonth on WeekendsStartOfMonth.Origin = WeekendsEndOfMonth.Origin
    INNER JOIN (
        SELECT
            Origin,
            count(*) AS StartOfMonthCoef
        FROM
            benchmark
        WHERE
            DayofMonth <= 15
            AND Year >= 1997
        GROUP BY
            Origin
    ) StartOfMonth on WeekendsStartOfMonth.Origin = StartOfMonth.Origin
ORDER BY
    WeekendsAllMonth.Origin