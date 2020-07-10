SELECT Month, DayofMonth 
FROM benchmark
WHERE ArrDelay - DepDelay < 10  OR Diverted = 0 OR Cancelled = 0 AND CarrierDelay = 0 
AND SecurityDelay = 0 AND DestStateName = 'California' OR OriginStateName = 'California' 
AND TailNum = '%5' OR FlightNum = '%0' AND AirTime > 300
ORDER BY Month
