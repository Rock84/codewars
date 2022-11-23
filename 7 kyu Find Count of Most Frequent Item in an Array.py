def most_frequent_item_count(collection):
    max = 0
    my_set = set(collection)
    for _ in my_set:
        item = collection.count(_)
        if item > max:
            max = item
    return max
