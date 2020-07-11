SELECT DayofMonth, DestAirportID, DestCityName, WeatherDelay
FROM benchmark
WHERE DepDel15 = 1
    AND DayofMonth IN (7, 13) 
    AND DestAirportID > 11000 AND DestAirportID < 12000
    AND Distance > 500 AND Distance < 1000
    AND Diverted = 0
    AND WeatherDelay > 10