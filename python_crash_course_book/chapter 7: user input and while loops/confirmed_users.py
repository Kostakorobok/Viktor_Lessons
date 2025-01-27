unconfirmed_users = ["alice", "brain", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Veryfying user: {current_user.title()}")
    confirmed_users.append(current_user)

    prompt1 = input("(1) Continue (2) Stop\n")

    if prompt1 == "1":
        continue

    if prompt1 == "2":
        break

print("\nThe following users have been confirmed:")
for i in confirmed_users:
    print(i.title())

