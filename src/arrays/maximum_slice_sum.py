def get_max_slice_sum(A: []):
    max_ending_sum = max_slice_sum = A[0]
    for i in range(1, len(A)):
        if max_ending_sum < 0:
            max_ending_sum = max(max_ending_sum, A[i], max_ending_sum + A[i])
        else:
            max_ending_sum = max(0, max_ending_sum + A[i])

        max_slice_sum = max(max_slice_sum, max_ending_sum)
    return max_slice_sum
