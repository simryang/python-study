# list_comprehension.py
bUseListComprehension = False
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
if not bUseListComprehension:
    starts_s = []

    for friend in friends:
        if friend.startswith("S"):
            starts_s.append(friend)
    print(starts_s)
else:
    starts_s = [f for f in friends if f.startswith("S")]
    print(starts_s)