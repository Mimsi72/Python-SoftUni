num = int(input())

reservation_lists = set()
for invitation in range(num):
    invitation = input()
    reservation_lists.add(invitation)

arrived_guests = input()
while not arrived_guests == "END":
    reservation_lists.remove(arrived_guests)
    arrived_guests = input()

print(len(reservation_lists))

for not_attended_reservation in sorted(reservation_lists):
    if not_attended_reservation[0].isdigit():
        print(not_attended_reservation)

for not_attended_reservation in sorted(reservation_lists):
    if not_attended_reservation[0].isalpha():
        print(not_attended_reservation)
