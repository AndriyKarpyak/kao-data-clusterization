from sortedcontainers import SortedSet


def match(mx: dict):

    size = len(mx)
    matches = dict()
    names = list()

    for BASE_X, BASE_Name in enumerate(mx.keys()):
        base_column = mx[BASE_Name]
        names.append(BASE_Name)
        for BASE_Y in range(0, len(base_column)):
            base_cluster = base_column[BASE_Y]

            for X, Name in enumerate(mx.keys()):
                if X > BASE_X:
                    column = mx[Name]
                    for Y in range(0, len(column)):
                        cluster = column[Y]
                        intersection = sorted(list(set(base_cluster) & set(cluster)))

                        if len(intersection) > 1:
                            match_name = ", ".join(intersection)
                            matches.setdefault(match_name, SortedSet()).add("{};{}".format(BASE_X, BASE_Y))
                            matches[match_name].add("{};{}".format(X, Y))

    for r in range(size):
        temp = matches.copy()
        for match_key in matches.keys():
            cluster = match_key.split(',')
            cluster_matches = matches[match_key]
            if len(cluster) > size:
                for BASE_X, BASE_Name in enumerate(mx.keys()):
                    base_column = mx[BASE_Name]
                    for BASE_Y in range(0, len(base_column)):
                        base_cluster = base_column[BASE_Y]
                        left = set(base_cluster)
                        right = set(cluster)
                        intersection = sorted(list(left & right))

                        if len(intersection) > 1:
                            match_name = ",".join(intersection)

                            if match_name in temp.keys():
                                temp[match_name] = temp[match_name].union(cluster_matches)
                                temp[match_name].add("{};{}".format(BASE_X, BASE_Y))
                            else:
                                temp.setdefault(match_name, SortedSet(cluster_matches)).add("{};{}".format(BASE_X, BASE_Y))

        matches = temp.copy()

    return names, matches

