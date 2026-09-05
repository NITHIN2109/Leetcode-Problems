<h2>search-insert-position Notes</h2><hr>[ Time taken: 2d 1hr 15m 57s ]
# Pattern: Binary Search → Lower Bound

 ## Goal

 Find the first index where:

 `nums[i] >= target`

 ## Key Idea

 If `nums[mid] >= target`:

 - `mid` can be the answer.
- Store it: `ans = mid`
- Search left for an earlier valid position: `high = mid - 1`

 If `nums[mid] < target`:

 - `mid` is too small.
- Search right: `low = mid + 1`

 If no valid index is found, the answer is `n` (insert at the end).

 ## Algorithm

```
low = 0
high = n - 1
ans = n

while low <= high:
    mid = low + (high - low) / 2

    if nums[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

return ans
```

 ## Example

```
nums   = [1, 3, 3, 5, 7]
target = 3
```

 The first index where `nums[i] >= 3` is:

```
1
```

 Therefore:

```
lower_bound(nums, 3) = 1
```

 ## Complexity

 - **Time:** `O(log n)`
- **Space:** `O(1)`
