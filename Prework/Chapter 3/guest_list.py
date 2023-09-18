guest_list = ['Muhammad', 'Asiya', 'Sawda']
message = "I would like to invite Prophet " + guest_list[0] + " to dinner because he is my role model."
message1 = " I would also like to invite " + guest_list[1] + " and " + guest_list[2] + "." + " However, Sawda cannot make it. So Aisha will come instead."
print(message + message1)

guest_list[2] = 'Aisha'
print(guest_list)


guest_list.insert(0, 'Shanzed')
guest_list.insert(2, 'Ariha')
guest_list.append('Mariam')
print(guest_list)

message2 = "I found a bigger table! I would like to invite " + guest_list[0] + ", " + guest_list[2] + ", and " + guest_list[5] + "."
print(message2)

popped_guest_list = guest_list.pop(-1)
print(popped_guest_list + " sorry love only have space for 2 guests.")

popped_guest_list = guest_list.pop(-2)
print(popped_guest_list + " sorry love only have space for 2 guests.")

popped_guest_list = guest_list.pop(-3)
print(popped_guest_list + " sorry love only have space for 2 guests.")

popped_guest_list = guest_list.pop(-4)
print(popped_guest_list + " sorry love only have space for 2 guests.")

print(guest_list[0] + " and " + guest_list[1] + " you are still invited.")
print(guest_list)

#WORK MORE