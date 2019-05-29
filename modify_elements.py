guest_list = ["Kelsey", "Nate", "Serge"]

print("Hi " + guest_list[0] + "!")
print("Good to see you " + guest_list[2] + ".")
print("You are late, " + guest_list[1] + "!")

print("Unfortunately, " + guest_list[2] + " can no longer make it.")

guest_list.remove("Serge")
guest_list.append("Wes")

print("Well hello again " + guest_list[0] + ".")
print("Glad you could make it, " + guest_list[1] + "!")
print(guest_list[2] + " you were our second choice.")

print("For some reason we found a bigger table, adding more guests.")

guest_list.insert(0, "Korrie")
guest_list.insert(2, "MC")
guest_list.append("Serge")

print(guest_list)

print("Now only two guests, removing the rest.")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print("Later " + removed_guest)

print(guest_list)
