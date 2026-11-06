def search_by_title(items, keyword):
    return [disc for disc in items if keyword.lower() in disc.title.lower()]    