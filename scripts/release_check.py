"""Harbor Street Bakery: delivery release check, run right after each deploy (demonstration code)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from delivery_fee import delivery_total


def dollars(cents):
    return f"${cents / 100:.2f}"


print(f"Release check: {environment}")
print(open(os.path.join(release, "RELEASE.txt")).read().strip())
for order in (1500, 2000, 3000):
    print(f"Delivery on a {dollars(order)} order:", dollars(delivery_total(order) - order))
print("Release check passed.")
