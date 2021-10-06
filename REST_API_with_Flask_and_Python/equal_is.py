friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(f"friends:{friends} == abroad:{abroad}? {friends == abroad}")
print(f"friends:{friends} is abroad:{abroad}? {friends is abroad}")
nn = friends
print(f"friends:{friends} == nn:{nn}? {friends == nn}")
print(f"friends:{friends} is nn:{nn}? {friends is nn}")
nn.append("hi")
print(f"nn:{nn}.append('hi')")
print(f"friends:{friends} == nn:{nn}? {friends == nn}")
print(f"friends:{friends} is nn:{nn}? {friends is nn}")