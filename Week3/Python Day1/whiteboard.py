# Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
# The pipes connecting your level's stages together need to be fixed before you receive any more complaints.
# Pipes list is correct when each pipe after the first index is greater (+1) than the previous one, and that there is no duplicates.
# Task
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).
# Example
# Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8

def get_all_pipes(have_pipes):
    have_pipes = sorted(have_pipes)
    min_pipe = have_pipes[0]
    max_pipe = have_pipes[-1]
    all_pipes = [x for x in range(min_pipe, max_pipe)]
    return all_pipes

def get_all_pipes(have_pipes):
    return [x for x in range(min(have_pipes), max(have_pipes)+1)]