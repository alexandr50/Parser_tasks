def get_correct_data(content_without_solutions: list, content_with_solutions: list):
    for item_withouts in content_without_solutions:
        for _ in content_with_solutions:
            if _[0] in item_withouts:
                item_withouts.append(_[1])
    return content_without_solutions