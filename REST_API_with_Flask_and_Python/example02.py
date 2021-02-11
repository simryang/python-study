# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [1, 2, 97]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (5,)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}


# =============================================
friends = {"sr", "jj", "faith", "love", "hope"}
asleep = {"faith", "love", "hope"}

# 차집합. difference A.difference(B) = A - B
awake = friends.difference(asleep)
print(f"friends={friends}")
print(f"asleeps={asleep}")
print(f"awakes=friends - asleeps={awake}")

# 합집합. union A.union(B) = A ⋃ B
all = asleep.union(awake)
print(f"union between asleep and awakes are = {all}")

# 교집합. intersection A.intersection(B) = A ⋂ B
both = friends.intersection(asleep)
print(f"intersection between friends and asleeps = {both}")