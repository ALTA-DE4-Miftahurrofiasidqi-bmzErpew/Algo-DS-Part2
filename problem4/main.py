def count_item_and_sort(items):
    items = sorted(items)

    frequensi = {}
    for item in items:
        if item in frequensi:
            frequensi[item] += 1
        else:
            frequensi[item] = 1

    shortted_freq = sorted(frequensi.items(), key=lambda x: x[1])
    result = " ".join([f"{key}->{value}" for key, value in shortted_freq])
    return result


if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"
