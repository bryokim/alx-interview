# 0x01-lockboxes

You have `n` number of locked boxes with each box numbered sequentially from `0` to `n - 1`
and each box may contain keys to the other boxes. The function `canUnlockAll` determines whether
all the boxes can be opened.

The first box is assumed to be unlocked.

```Python
boxes = [[1], [2], []]
          |     \  /
      Unlocked  Locked
```

A key with the same number as a box opens that box.
Also all keys are assumed to be positive integers. Keys that do not
have boxes are skipped and no error is raised.

```Python
boxes = [[1], [2, 3], [], [4], [5], [6, 7], [], []]
          |                           |
    Contains single key that        Contains two keys that
    unlocks the box at index 1      unlock boxes at index 6 and 7
```

## Usage

```Python
# Import function
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

---
Happy coding
