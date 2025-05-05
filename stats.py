def word_count(content):
    count = content.split()
    return len(count)

def letter_count(content):
    letters = content.lower()
    dist_letters = {}
    
    for letter in letters:
        if letter in dist_letters:
            dist_letters[letter] += 1
        else:
            dist_letters[letter] = 1
    return dist_letters

def sort_results(dict_letters):
    results_list = []
    for char, count in dict_letters.items():
        results_list.append({"char": char, "num": count})
    results_list.sort(reverse=True, key=lambda dict_item: dict_item["num"])
    return results_list

