n_stations, in_station, out_station = map(int, input().split())
travel_stations = 0

dst1 = abs(in_station - out_station) - 1
dst2 = n_stations - 2 - dst1

print(min(dst1, dst2))