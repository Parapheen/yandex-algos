street_map = [int(i) for i in input().split()]

left_res = []
left_shop_pos = -20
dst_to_left_shop = 0
for i in range(len(street_map)):
    if street_map[i] == 2:
        left_shop_pos = i
    elif street_map[i] == 1:
        dst_to_left_shop = i - left_shop_pos
        left_res.append(dst_to_left_shop)

right_res = []
right_shop_pos = 20
dst_to_right_shop = 0
for i in range(len(street_map) - 1, -1, -1):
    if street_map[i] == 2:
        right_shop_pos = i
    elif street_map[i] == 1:
        dst_to_right_shop = right_shop_pos - i
        right_res.append(dst_to_right_shop)

closest_res = []
for i in range(len(left_res)):
    closest_res.append(min(left_res[i], right_res[::-1][i]))

print(max(closest_res))