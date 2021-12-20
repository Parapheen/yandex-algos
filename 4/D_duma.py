with open("input.txt") as f:
    lines = f.readlines()
    parties = []
    for line in lines:
        party = ' '.join(line.split()[:-1])
        voices = int(line.split()[-1])
        parties.append((party, voices))
    total_voices = sum(i[1] for i in parties)
    first_denominator = total_voices / 450
    seats = {i[0]: i[1] // first_denominator for i in parties}
    remainder = sorted([(i[0], i[1] % first_denominator) for i in parties], key=lambda x: -x[1])
    remaining_seats = int(450 - sum(seats.values()))
    for i in range(remaining_seats):
        target_party = remainder[i % len(remainder)][0]
        for party in seats:
            if party == target_party:
                seats[party] += 1
    for party in seats:
        print(party, int(seats[party]))
