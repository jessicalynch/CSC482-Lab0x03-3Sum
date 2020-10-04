#!/usr/bin/env python3

"""lab0x03.py: driver program"""
__author__ = "Jessica Lynch"

from time import perf_counter_ns
import three_sum as ts
import sys


def main():
    # Assign timer function to variable
    clock = perf_counter_ns

    # Determine max run time for each algorithm
    one_second = 1000000000  # 1 second in nanoseconds
    MAX_RUN_TIME = one_second * 60 * 10
    # MAX_RUN_TIME = one_second # small value for testing

    # Init string constants for table header
    t_str = "Time"
    dr_str = "DR"
    na_str = "na"
    expected_str = "Expected DR"

    # Build list with functions to test
    three_sum_funcs = [ts.three_sum_bruteforce, ts.three_sum_faster, ts.three_sum_fastest]

    # Test accuracy of functions
    valid = verification_tests(three_sum_funcs)
    print(f"Passed verification test: {valid}\n")

    # Init lists for storing timing data
    results = [1] * 3  # clock time
    doubling_ratio = [0.0] * 3  # how much faster than previous run
    expected_dr = [1.0] * 3  # expected doubling ratio

    # Print heading (alg names)
    print(f"{'Brute 3 Sum':>30}{'Faster 3 Sum':>45}{'Fastest 3 Sum':>45}\n")

    # Print secondary heading
    print(f"{'N':>15}", end="")
    for i in range(3):
        print(f"{t_str:>15}{dr_str:>15}{expected_str:>15}", end="")
    print()

    # Init flag to track when
    # table is complete
    timed_out = False
    timed_out_algs = [False] * 3

    # Start with list length 4
    N = 4

    timed_out_algs[0] = True # bypass brute force

    # Test algorithm on larger lists as N increases
    while N < sys.maxsize and timed_out is False:

        # Assume all algorithms timed out
        timed_out = True

        # Create an N-sized list of random integers
        rand_ints = ts.generate_test_list(N, -N, N)

        # Print current N value
        print(f"{N:>15}", end="")

        # Calculate expected doubling ratios
        prev_N = (N // 2)
        expected_dr[0] = N ** 3 / prev_N ** 3  # brute force - O(N^3)
        expected_dr[1] = N ** 2 / prev_N ** 2  # one nested loop - O(N^2)
        expected_dr[2] = expected_dr[1]

        # Time each algorithm
        for i in range(3):

            # Skip to next alg if current is timed out
            if timed_out_algs[i]:
                # Print filler values to maintain table structure
                print(f"{na_str:>15}{na_str:>15}{na_str:>15}", end="")
                if i == 2:
                    print()
                continue

            # Start clock
            t0 = clock()

            # Run algorithm
            three_sum_funcs[i](rand_ints)

            # Stop clock and calculate time
            t1 = clock() - t0

            # Calculate doubling ratio
            # by dividing current and previous run
            if N > 4:
                doubling_ratio[i] = t1 / results[i]
            else:
                doubling_ratio[i] = na_str

            # Save current run
            results[i] = t1

            # Print results row for current N value
            print(f"{results[i]:>15}{doubling_ratio[i]:>15.3}{expected_dr[i]:>15.3}", end="")
            if i == 2:
                print()

            # Check if current run time is less than
            # the max time allowed
            if t1 < MAX_RUN_TIME:
                # Change flag if at least one sort is still going
                timed_out = False
            else:
                # Current algorithm timed out
                timed_out_algs[i] = True

        N *= 2


def verification_tests(funcs, print_tests=False):
    """Verify consistent results from each algorithm"""

    # Increase confidence by running the tests
    # multiple times
    for _ in range(10):

        # Start with a small list
        N = 4

        # Double list length each run
        while N < 2 ** 8:

            # Create an N-sized list of random integers
            rand_ints = ts.generate_test_list(N, -N, N)

            check = [[]] * 3
            for i in range(3):
                check[i] = funcs[i](rand_ints)
                check[i].sort()

            # Check if all three lists are equal
            valid = check[0] == check[1] == check[2]

            # Print tests
            if print_tests:
                print(f"===== N = {N} =====")
                for i in range(3):
                    print(f"List {i + 1} length:\t{len(check[i])}")

            # Return False as soon as any inconsistency is found
            if not valid:
                return False

            N *= 2

    # Return True if all tests are passed
    return True


if __name__ == '__main__':
    main()
