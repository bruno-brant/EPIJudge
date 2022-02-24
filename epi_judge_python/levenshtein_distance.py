from test_framework import generic_test



def levenshtein_distance(A: str, B: str) -> int:
    cache = {}    
    return levenshtein_distance_impl(A, 0, B, 0, cache)


def levenshtein_distance_impl(A: str, a_idx: int, B: str, b_idx: int, cache: dict) -> int:
    key = (a_idx, b_idx)
    
    if key in cache:
        return cache[key]

    result = None
    
    if a_idx >= len(A):
        result = len(B) - b_idx
    elif b_idx >= len(B):
        result =  len(A) - a_idx
    elif A[a_idx] == B[b_idx]:
        result = levenshtein_distance_impl(A, a_idx + 1, B, b_idx + 1, cache)

    else:
        result = 1 + min(
            levenshtein_distance_impl(A, a_idx, B, b_idx + 1, cache),
            levenshtein_distance_impl(A, a_idx + 1, B, b_idx, cache),
            levenshtein_distance_impl(A, a_idx + 1, B, b_idx + 1, cache)
        )
    
    cache[key] = result

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
