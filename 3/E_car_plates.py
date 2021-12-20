witnesses = int(input())
testimonies = [input().strip() for i in range(witnesses)]

suspects = int(input())
car_plates = [input().strip() for i in range(suspects)]

res = [0] * suspects
for plate_index in range(suspects):
    for testimony in testimonies:
        if all(ch in car_plates[plate_index] for ch in testimony):
            res[plate_index] += 1
max_intersection = max(res)
for i in range(suspects):
    if res[i] == max_intersection:
        print(car_plates[i])