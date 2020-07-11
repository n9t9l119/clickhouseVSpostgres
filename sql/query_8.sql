SELECT AllFlights.AirlineID, CancelCnt * 100 / AllCnt
FROM (
        SELECT AirlineID,
            COUNT(*) As CancelCnt
        FROM benchmark
        WHERE Cancelled = 1
        GROUP BY AirlineID
    ) AS CancelFlights
    INNER JOIN (
        SELECT AirlineID,
            COUNT(*) As AllCnt
        FROM benchmark
        GROUP BY AirlineID
    ) AS AllFlights ON AllFlights.AirlineID = CancelFlights.AirlineID