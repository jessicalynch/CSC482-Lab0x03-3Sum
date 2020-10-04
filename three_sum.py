#!/usr/bin/env python

"""three_sum.py: 3-sum algorithms"""
__author__ = "Jessica Lynch"

import sys
import random


def generate_test_list(N, min_v=None, max_v=None):
    """Generate a list of integers"""

    # If min/max not provided, set to system min/max
    if not min_v:
        min_v = sys.maxsize * -1
    if not max_v:
        max_v = sys.maxsize

    # Return N-sized list of random ints
    return [random.randint(min_v, max_v) for _ in range(N)]


def three_sum_bruteforce(arr):
    """Find all values that sum to zero using brute-force method"""

    # Remove duplicates
    arr = list(set(arr))

    # Get list size
    arr_size = len(arr)

    # Store valid tuples in list
    results = []

    # Start outer loop at beginning of list
    for i in range(arr_size):

        # Start middle loop after i
        for j in range(i + 1, arr_size):

            # Start inner loop after j
            for k in range(j + 1, arr_size):

                if arr[i] + arr[j] + arr[k] == 0:
                    # If all values sum to zero, append to results list
                    # results.append(tuple(sorted([arr[i], arr[j], arr[k]])))

                    # or simply return True
                    return True

    # Return list of 3-tuples
    # return results

    # or return False if no valid tuple exists
    return False

def three_sum_faster(arr):
    """Find all values that sum to zero by storing values previously seen
    in a set, reducing the amount of loops needed to two"""

    # Remove duplicates
    arr = list(set(arr))

    results = []

    # Start outer loop at beginning of list
    for i in range(len(arr) - 1):

        # Init a set to store all values previously seen
        vals_seen = set()

        # Start inner loop at i+1
        for j in range(i + 1, len(arr)):

            # The value needed to make zero is equal to
            # to negative (arr[i] + arr[j])
            val_needed = -(arr[i] + arr[j])

            # If we've seen the value previously (it is in the set),
            # then we know it exists in the list, and we're done searching
            if val_needed in vals_seen:

                # Append (arr[i], arr[j], -(arr[i] + arr[j])
                # results.append(tuple(sorted((arr[i], arr[j], val_needed))))

                # or simply return True
                return True

            # If we have not seen the value, then add arr[j] to the set
            # for future lookups
            vals_seen.add(arr[j])

    # Return tuples
    # return list(set(results))

    # or return False if no tuples exist
    return False

def three_sum_fastest(arr):
    """Find all values that sum to zero by iterating from both ends of list"""

    results = []

    # Remove duplicates and sort
    arr = list(set(arr))
    arr.sort()

    # Start iterating from the beginning of the list
    for i in range(len(arr) - 2):

        # Place left index after i and right index at end of list
        left_ind = i + 1
        right_ind = len(arr) - 1

        # Iterate from both ends of list
        # until left and right indices meet
        while left_ind < right_ind:

            # Sum values at all indices
            curr_sum = arr[i] + arr[left_ind] + arr[right_ind]

            if curr_sum == 0:
                # Append tuple to results list if it sums to zero
                # results.append((arr[i], arr[left_ind], arr[right_ind]))

                # Or simply return True (the list contains a triplet that sums zero)
                return True

                # Still increment left index to keep the list moving
                # and potentially find more values that work with arr[i]
                # Index choice is arbitrary-- could decrement the right index instead
                left_ind += 1

            elif curr_sum < 0:
                # Value is too low, increment from the left to increase current sum
                left_ind += 1
            else:
                # Value is too high, reduce the right index to lower the current sum
                right_ind -= 1

    # Return a list of tuples that sum to zero
    # return list(set(results))

    # or return False if none exist
    return False


