SELECT TaxiOut,
    NASDelay,
    CRSElapsedTime,
    DepartureDelayGroups,
    ActualElapsedTime
FROM benchmark
WHERE TaxiOut < 10
    AND NASDelay > 0
    AND CRSElapsedTime > 200 OR CRSElapsedTime < 100
    AND DepartureDelayGroups = '5'OR DepartureDelayGroups = '4'
    AND ActualElapsedTime > 500 AND ActualElapsedTime < 600