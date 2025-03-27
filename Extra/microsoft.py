def create_diverse_word(A, B, C):
    # Initialize result and set the counts for 'a', 'b', and 'c'
    result = []
    counts = [['a', A], ['b', B], ['c', C]]
    
    total_chars = A + B + C  # Total number of characters to be used

    while len(result) < total_chars:
        # Sort counts lexicographically first, then by remaining count in descending order
        counts.sort(key=lambda x: (x[0]))  # Sort lexicographically 'a' -> 'b' -> 'c'
        
        added = False
        for i in range(3):
            char, count = counts[i]
            if count == 0:
                continue
            # Ensure no more than two consecutive characters are the same
            if len(result) >= 2 and result[-1] == result[-2] == char:
                continue
            # Append the character
            result.append(char)
            counts[i][1] -= 1  # Decrease the count
            added = True
            break
        
        # If no character was added (should not happen), break
        if not added:
            break
    
    return ''.join(result)

# Example usage
A = 1
B = 4
C = 4
print(create_diverse_word(A, B, C))  # Expected output: "abbcbcbcc"



