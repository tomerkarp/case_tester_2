from task2 import *  # TODO: Change "task2" to the name of the main program

import random
import itertools

import itertools
import random


# Function from task2, assuming it is correct
def alt_sum(x, target):
    sums = {0}
    for num in x:
        sums |= {num + s for s in sums}
    return target in sums


def alt_ordered_subset(str1, str2):
    it = iter(str1)
    last_index = -1
    for char in str2:
        try:
            current_index = next(i for i, c in enumerate(it, start=last_index + 1) if c == char)
            if current_index == last_index + 1:  # Consecutive letters found
                return False
            last_index = current_index
        except StopIteration:
            return False
    return True


def linear_test():
    test_cases = [
        ([2, 3, 6, 7, 10], 15, True),
        ([5, 14, 7, 3], 20, False),
        ([1, 2, 3, 4, 5], 10, True),
        ([1, 2, 3, 4, 5], 11, True),
        ([1, 1, 1, 1, 1], 3, True),
        ([1, 1, 1, 1, 1], 6, False),
        ([10, 20, 30], 0, True),
        ([], 0, True),
        ([], 10, False),
        ([1, 2, 3, 4, 5], 9, True),
        ([1, 2, 3, 4, 5], 3, True),
        ([2, 4, 6, 8], 10, True),
        ([2, 4, 6, 8], 7, False),
        ([10, 20, 30, 40], 100, True),
        ([10, 20, 30, 40], 90, True)
    ]

    for lst, target, expected in test_cases:
        result = linear_sum(lst, target)
        assert result == expected, f"Test failed for list: {lst} and target: {target}. Expected {expected}, got {result}"
    print("All linear_sum tests passed!")


def ordered_subset_test():
    test_cases = [
        ("ladbcfe", "abc", False),
        ("ladbxcfe", "abc", True),
        ("abcdefghijklmnop", "acegikmoqrs", False),
        ("abcdefghijklmnop", "acegikmoy", False),
        ("abcdefgh", "ah", True),
        ("abcdefgh", "hf", False),
        ("abcdefghijklmnop", "aefhkmp", False),
        ("abcd", "aefhkmp", False),
        ("abcdefghijklmnop", "aefhkx", False),
        ("abcdef", "af", True),
        ("abcdef", "fa", False),
        ("abcdef", "abdf", False),
        ("abcdef", "aef", False),
        ("abcdefkg", "afg", True),
        ("abcdefgh", "bh", True),
        ("abcdef", "cf", True)
    ]

    for str1, str2, expected in test_cases:
        result = ordered_subset(str1, str2)
        assert result == expected, f"Test failed for str1: '{str1}' and str2: '{str2}'. Expected {expected}, got {result}"
    print("All ordered_subset tests passed!")


def test_solve_test():
    test_cases = [
        ([[20, 5], [40, 9], [30, 8]], 55, 13),
        ([[15, 10], [20, 5], [10, 3]], 25, 13),
        ([[10, 2], [20, 4], [30, 6]], 60, 12),
        ([[5, 2], [10, 4], [15, 6]], 20, 8),
        ([[25, 8], [35, 7], [45, 10]], 70, 18),
        ([[10, 1], [20, 2], [30, 3]], 40, 4),
        ([[5, 5], [10, 10], [20, 20]], 15, 15),
        ([[8, 3], [16, 6], [24, 9]], 30, 9),
        ([[12, 4], [24, 8], [36, 12]], 50, 16),
        ([[6, 2], [12, 4], [18, 6]], 20, 6),
        ([[9, 3], [18, 6], [27, 9]], 30, 9),
        ([[7, 3], [14, 6], [21, 9]], 35, 15),
        ([[11, 4], [22, 8], [33, 12]], 50, 16),
        ([[13, 5], [26, 10], [39, 15]], 55, 20),
        ([[17, 6], [34, 12], [51, 18]], 70, 24),
    ]

    for questions, total_time, expected in test_cases:
        result = solve_test(questions, total_time)
        assert result == expected, f"Test failed for questions: {questions} and total_time: {total_time}. Expected {expected}, got {result}"
    print("All solve_test tests passed!")


def test_solve_test_with_factor():
    test_cases = [
        ([[20, 5], [40, 9], [30, 8], [35, 7]], 55, 17),
        ([[15, 10], [20, 5], [10, 3]], 25, 15),
        ([[10, 2], [20, 4], [30, 6]], 60, 12),
        ([[5, 2], [10, 4], [15, 6]], 20, 10),
        ([[25, 8], [35, 7], [45, 10]], 70, 21),
        ([[10, 1], [20, 2], [30, 3]], 40, 5),
        ([[5, 5], [10, 10], [20, 20]], 15, 25),
        ([[8, 3], [16, 6], [24, 9]], 30, 13),
        ([[12, 4], [24, 8], [36, 12]], 50, 20),
        ([[6, 2], [12, 4], [18, 6]], 20, 9),
        ([[9, 3], [18, 6], [27, 9]], 30, 13),
        ([[7, 3], [14, 6], [21, 9]], 35, 16),
        ([[11, 4], [22, 8], [33, 12]], 50, 20),
        ([[13, 5], [26, 10], [39, 15]], 55, 25),
        ([[17, 6], [34, 12], [51, 18]], 70, 30),
    ]

    for questions, total_time, expected in test_cases:
        result = solve_test_with_factor(questions, total_time)
        assert result == expected, f"Test failed for questions: {questions} and total_time: {total_time}. Expected {expected}, got {result}"
    print("All solve_test_with_factor tests passed!")


def test_directory_depth():
    test_cases = [
        ({"a": 1, "b": 2}, 0),
        ({"a": {"b": 2}}, 1),
        ({"a": 1, "b": {"c": 2, "d": {"e": 3}}}, 2),
        ({}, 0),
        ({"a": {"b": {"c": {"d": {"e": 5}}}}}, 4),
        ({"a": {"b": {"c": {"d": 4}}}, "x": 1}, 3),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": {"g": 7}}}}, 3),
        ({"a": {"b": {"c": 5}}}, 2),
        ({"a": {"b": 1, "c": {"d": 2}}, "e": 3}, 2),
        ({"a": {"b": {"c": {"d": 2}}}}, 3),
        ({"a": 1, "b": 2, "c": {"d": 3, "e": {"f": 4}}}, 2),
        ({"a": 1, "b": {"c": {"d": {"e": {"f": 6}}}}}, 4),
        ({"a": {"b": {"c": {"d": {"e": 5}}}}, "f": 1}, 4),
        ({"a": 1, "b": {"c": 2}, "d": {"e": 3, "f": {"g": 4}}}, 2),
        ({"a": {"b": {"c": 3, "d": {"e": 4}}}, "f": {"g": {"h": 3, "i": {"j": {"k": 4}}}}}, 4)
    ]

    for dir, expected in test_cases:
        result = directory_depth(dir)
        assert result == expected, f"Test failed for directory: {dir}. Expected {expected}, got {result}"
    print("All directory_depth tests passed!")


def test_directory_music_size():
    test_cases = [
        ({"my documents": 30, "music": {"zohar argov": 10, "avihu pinhasov": 20}}, 30),
        ({"more_music": 40, "music": {"zohar argov": 10, "avihu pinhasov": 20}}, 70),
        ({"more_music": 40, "music": {"zohar argov": 10, "avihu pinhasov": 20},
          "just a folder": {"new1": 5, "new2": 6, "new_last": 7, "new_music": 9}}, 79),
        ({"a": 1, "b": 2}, 0),
        ({"music": {"a": 1, "b": 2}}, 3),
        ({"music_files": {"song1": 5, "song2": 10}}, 15),
        ({"folder": {"music_folder": {"song": 7}}}, 7),
        ({"folder": {"another_folder": {"more_music": 10, "song": 20}}}, 10),
        ({"a": 1, "music": {"b": 2, "c": {"music": 3}}}, 5),
        ({"a": {"music_b": 5, "c": {"d": 6}}}, 5),
        ({"music": {"a": {"b": {"c": {"d": 10}}}}}, 10),
        ({"folder1": {"folder2": {"music_folder": {"song": 4}}}}, 4),
        ({"a": {"b": {"c": {"d": {"music": 12}}}}}, 12),
        ({"a": 1, "music_folder": {"b": 2, "c": {"d": {"song": 8}}}}, 10),
        ({"my documents": 20, "music_files": {"zohar argov": 10, "avihu pinhasov": 15}}, 25)
    ]

    for dir, expected in test_cases:
        result = directory_music_size(dir)
        assert result == expected, f"Test failed for directory: {dir}. Expected {expected}, got {result}"
    print("All directory_music_size tests passed!")


def test_distance():
    test_cases = [
        ((0, 0, 1, 1), 2),
        ((2, 3, 4, 5), 4),
        ((5, 5, 5, 5), 0),
        ((0, 0, 5, 5), 10),
        ((1, 2, 3, 4), 4),
        ((4, 4, 4, 7), 3),
        ((6, 2, 2, 6), 8),
        ((3, 3, 3, 3), 0),
        ((0, 0, 3, 4), 7),
        ((2, 1, 2, 3), 2),
        ((5, 5, 0, 0), 10),
        ((1, 1, 1, 4), 3),
        ((4, 2, 6, 5), 5),
        ((3, 3, 6, 6), 6),
        ((2, 2, 5, 5), 6)
    ]

    for (row1, col1, row2, col2), expected in test_cases:
        result = distance(row1, col1, row2, col2)
        assert result == expected, f"Test failed for distance({row1}, {col1}, {row2}, {col2}). Expected {expected}, got {result}"
    print("All distance tests passed!")


def test_add_tower():
    test_cases = [
        ([0, 0, 0, 0, 0], 2, 1, 1, False),
        ([0, 1, 0, 0, 0], 1, 2, 0, True),
        ([0, 3, 0, 0, 0], 2, 2, 4, False),
        ([0, 2, 0, 0, 4], 1, 4, 1, True),
        ([0, 3, 0, 5, 0], 2, 2, 1, True),
        ([1, 0, 3, 0, 0], 2, 4, 4, True),
        ([0, 2, 0, 0, 0], 2, 2, 4, True),
        ([0, 2, 4, 0, 0], 3, 3, 1, False),
        ([0, 0, 3, 0, 0], 2, 1, 4, True),
        ([1, 0, 0, 3, 0], 1, 3, 2, True),
        ([0, 0, 4, 0, 0], 3, 2, 3, True),
        ([0, 2, 0, 0, 0], 1, 3, 4, True),
        ([0, 3, 0, 0, 0], 2, 4, 4, True),
        ([1, 0, 0, 2, 0], 2, 2, 3, True),
        ([0, 0, 2, 0, 0], 3, 1, 4, True)
    ]

    for board, d, row, col, expected in test_cases:
        result = add_tower(board[:], d, row, col)  # use board[:] to avoid mutating the original board
        assert result == expected, f"Test failed for add_tower({board}, {d}, {row}, {col}). Expected {expected}, got {result}"
    print("All add_tower tests passed!")


def is_valid_tower_placement(board, d):
    delta = lambda row1, col1, row2, col2: abs(row1 - row2) + abs(col1 - col2)
    n = len(board)
    for i in range(n):
        for j in range(i+1,n):
            if delta(i, board[i], j, board[j]) <= d:
                return False
    return True

def test_n_towers():
    test_cases = [
        (6, 1, True),
        (4, 2, True),
        (3, 1, True),
        (5, 2, True),
        (2, 1, True),
        (4, 3, False),
        (5, 1, True),
        (3, 2, False),
        (4, 1, True),
        (6, 2, True),
        (3, 3, False),
        (5, 3, False),
        (6, 1, True),
        (4, 4, False),
        (2, 2, False),
        (4, 5, False),
        (3, 5, False)
    ]

    for n, d, expected in test_cases:
        result = n_towers(n, d)
        if expected:
            assert len(result) == n, f"Test failed for n_towers({n}, {d}). Expected length {n}, got {len(result)}"
            assert is_valid_tower_placement(result,
                                            d), f"Test failed for n_towers({n}, {d}). Invalid tower placement: {result}"
        else:
            assert result == [], f"Test failed for n_towers({n}, {d}). Expected [], got {result}"
    print("All n_towers tests passed!")



# Run the tests
linear_test()
ordered_subset_test()
test_solve_test()
test_solve_test_with_factor()
test_directory_depth()
test_directory_music_size()
test_distance()
test_add_tower()
test_n_towers()