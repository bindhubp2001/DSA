# Input: ops = ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "-2" - Add -2 to the record, record is now [5, -2].
# "4" - Add 4 to the record, record is now [5, -2, 4].
# "C" - Invalidate and remove the previous score, record is now [5, -2].
# "D" - Add 2 \* -2 = -4 to the record, record is now [5, -2, -4].
# "9" - Add 9 to the record, record is now [5, -2, -4, 9].
# "+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
# "+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
# The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.


class BaseBallGame():
  def baseBall(self, operations):

    record = []

    for op in operations:
      if op == "C":
        record.pop()

      elif op == "D":
        record.append(2 * record[-1])

      elif op == "+":
        record.append(record[-1] + record[-2])
      
      else:
        record.append(int(op))

    return sum(record)
  
object = BaseBallGame()

result = object.baseBall(["10","20","C","D","+"])
print(result)
