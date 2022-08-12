import math
import pandas
from const import MARKERS, COLORS

from sklearn.metrics.pairwise import euclidean_distances


def export_to_excel(file_name, data):

    prefix = data['Prefix']
    centers = data['Centers']
    columns = data['Columns']
    clustered_ids = data['C_Ids']
    clustered_names = data['C_Names']
    clustered_points = data['C_Points']

    data_frame = list()
    for index_, cluster in enumerate(clustered_names):
        print("{} [{}]:\t{}".format(index_, ','.join(map(lambda c: "{}".format(c), centers[index_])), cluster))

        first = ["{} [{}] {}".format(index_, MARKERS[index_], COLORS[index_])]
        first.extend(['', ''])
        first.extend(centers[index_])
        first.extend([''])
        first.append(math.nan)

        data_frame.append(first)

        c_frame = list()
        c_ids = clustered_ids[index_]
        c_points = clustered_points[index_]
        for row_index, name in enumerate(cluster):
            next_row = [math.nan]
            next_row.extend([c_ids[row_index], cluster[row_index]])
            next_row.extend(c_points[row_index])
            next_row.append(math.nan)
            next_row.append(euclidean_distances([c_points[row_index], centers[index_]])[0][1])

            c_frame.append(next_row)

        c_frame = sorted(c_frame, key=lambda r_: r_[len(r_) - 1], reverse=False)
        data_frame.extend(c_frame)

        sep = [math.nan]
        sep.extend(['', ''])
        sep.extend([math.nan] * columns.__len__())
        data_frame.append(sep)

    column_names = ['Кластер', 'Номер', 'Податкова']
    column_names.extend(columns)
    column_names.extend(['', 'Відстань до центроїда'])
    df1 = pandas.DataFrame(data_frame, columns=column_names)
    df1.to_excel("output/{} [{}].xlsx".format(prefix, file_name.replace('.', '').replace("\n", "").replace(":", "-")))