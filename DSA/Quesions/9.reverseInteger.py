# Input: x = 123
# Output: 321

x=-123
rev=0


sign = -1 if x < 0 else 1
x *= sign 

while x > 0:
  rem = x % 10;
  rev = rev * 10 + rem ;
  x = x // 10;

rev *= sign

if rev < -2**31 or rev > 2**31 - 1:
  rev = 0


# rev = str(x)[::-1]

print(rev)



