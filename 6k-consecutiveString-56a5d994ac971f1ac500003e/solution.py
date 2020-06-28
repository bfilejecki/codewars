def longest_consec(strarr, k):
    if k > len(strarr) or len(strarr) == 0 or k <= 0:
        return ''
    results = []
    for i in range(len(strarr)):
        current_string = ''
        for j in range(k):
            if i+j >= len(strarr):
                pass
            else:
                current_string += strarr[i+j]
        results.append(current_string)
    index_of_max_string = 0
    for string in results:
        if index_of_max_string is None or len(string) > len(results[index_of_max_string]):
            index_of_max_string = results.index(string)
    return results[index_of_max_string]

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))