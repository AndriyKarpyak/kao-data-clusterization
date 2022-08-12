import math

import matplotlib.pyplot as plt
import numpy as np
import pandas
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics.pairwise import euclidean_distances

import alg
import xls_reader
from cfg import CFG
from plots import COLORS

CLUSTER_GRAYS = ['#717171', '#717171', '#717171', '#717171', '#717171']

CLUSTER_MARKERS = ['o', 's', 'D', '^', '>', 'v', '<', '*', 'p', 'X']

WIDTH = 1920
HEIGHT = 1024


# noinspection PyBroadException
def export_to_excel(file_name, data, markers=CLUSTER_MARKERS):
    linked_data = xls_reader.get_data('s,t,j,x')

    prefix = data['Prefix']
    centers = data['Centers']
    columns = data['Columns']
    clustered_ids = data['C_Ids']
    clustered_names = data['C_Names']
    clustered_points = data['C_Points']

    data_frame = list()
    for index_, cluster in enumerate(clustered_names):
        print("{} [{}]:\t{}".format(index_, ','.join(map(lambda c: "{}".format(c), centers[index_])), cluster))

        first = ["{} [{}] {}".format(index_, markers[index_], COLORS[index_])]
        first.extend(['', ''])
        first.extend(centers[index_])
        first.extend([''])
        first.append(math.nan)

        _sum = 0
        _length = 0
        for name in cluster:
            # noinspection PyBroadException
            try:
                linked_data_row = linked_data['C_Points'][linked_data['C_Names'].index(name)]
                _min = linked_data_row[0]
                _max = linked_data_row[1]
                if _min > 0 and _max > 0:
                    _sum = _sum + ((_min + _max) / 2)
                    _length = _length + 1
            except Exception:
                pass
        _avg = _sum / _length if _length > 0 else 1
        first.append(_avg)

        _sum = 0
        _length = 0
        for name in cluster:
            try:
                linked_data_row = linked_data['C_Points'][linked_data['C_Names'].index(name)]
                _c = linked_data_row[2]
                if _c > 0:
                    _sum = _sum + _c
                    _length = _length + 1
            except Exception:
                pass
        _avg = _sum / _length if _length > 0 else 1
        first.append(_avg)

        _sum = 0
        _length = 0
        for name in cluster:
            try:
                linked_data_row = linked_data['C_Points'][linked_data['C_Names'].index(name)]
                _c = linked_data_row[3]
                if _c > 0:
                    _sum = _sum + _c
                    _length = _length + 1
            except Exception:
                pass
        _avg = _sum / _length if _length > 0 else 1
        first.append(_avg)

        data_frame.append(first)

        info_columns = ['', 'Avg. hourly rate', '% of employees in Ukraine', 'Client focus on Enterprise, %']

        c_frame = list()
        c_ids = clustered_ids[index_]
        c_points = clustered_points[index_]
        for row_index, name in enumerate(cluster):
            next_row = [math.nan]
            next_row.extend([c_ids[row_index], cluster[row_index]])
            next_row.extend(c_points[row_index])
            next_row.append(euclidean_distances([c_points[row_index], centers[index_]])[0][1])
            next_row.append(math.nan)
            try:
                linked_data_row = linked_data['C_Points'][linked_data['C_Names'].index(name)]
                next_row.append((linked_data_row[0] + linked_data_row[1]) / 2)
                next_row.append(linked_data_row[2])
                next_row.append(linked_data_row[3])
            except Exception:
                next_row.extend([math.nan, math.nan])
            c_frame.append(next_row)

        c_frame = sorted(c_frame, key=lambda r_: r_[len(r_) - (len(info_columns) + 1)], reverse=False)
        data_frame.extend(c_frame)

        sep = [math.nan]
        sep.extend(['', ''])
        sep.extend([math.nan] * columns.__len__())
        data_frame.append(sep)

    column_names = ['Кластер', 'Порядковий номер компанії', 'Назва компанії']
    column_names.extend(columns)
    column_names.extend(['Відстань до центроїда'])
    column_names.extend(info_columns)
    df1 = pandas.DataFrame(data_frame, columns=column_names)
    df1.to_excel("output/{} {}.xlsx".format(prefix, file_name.replace('.', '').replace("\n", "")))


def export_excel(excel_range, data, prefix="", markers=CLUSTER_MARKERS):
    # ua_cfg = CFG[excel_range]['UA']
    # export_to_excel("{}{}".format(prefix, ua_cfg["Name"]), data)

    eng_cfg = CFG[excel_range]['ENG']
    export_to_excel("{}{}".format(prefix, eng_cfg["Name"]), data, markers=markers)


def plot_scatter(excel_range: str, data, prefix=""):
    import plots
    plot_method = getattr(plots, 'plot_{}_scatter'.format(excel_range.replace(',', '').replace(':', '')))

    ua_cfg = CFG[excel_range]['UA']
    plot_method("{}{}".format(prefix, ua_cfg["Name"]), ua_cfg["XLabel"], ua_cfg["YLabel"], data)

    eng_cfg = CFG[excel_range]['ENG']
    plot_method("{}{}".format(prefix, eng_cfg["Name"]), eng_cfg["XLabel"], eng_cfg["YLabel"], data)


def plot_silhouette(excel_range, data, n_clusters, algorithm, random_state, init='k-means++', prefix=""):
    import plots
    plot_method = getattr(plots, 'plot_{}_silhouette'.format(excel_range.replace(',', '').replace(':', '')))

    eng_cfg = CFG[excel_range]['UA']
    plot_method("{}{}".format(prefix, eng_cfg["Name"]), data,
                n_clusters=n_clusters, algorithm=algorithm, random_state=random_state, init=init)


def plot_elbow(excel_range, data, n_clusters, algorithm, random_state, init='k-means++', prefix=""):
    import plots
    plot_method = getattr(plots, 'plot_{}_elbow'.format(excel_range.replace(',', '').replace(':', '')))

    eng_cfg = CFG[excel_range]['UA']
    plot_method("{}{}".format(prefix, eng_cfg["Name"]), data,
                n_clusters=n_clusters, algorithm=algorithm, random_state=random_state, init=init)


def plot_stacked_bar(excel_range: str, data, prefix=""):
    import plots
    plot_method = getattr(plots, 'plot_{}_stacked_bar'.format(excel_range.replace(',', '').replace(':', '')))

    # ua_cfg = CFG[excel_range]['UA']
    # plot_method("{}{}".format(prefix, ua_cfg["Name"]), ua_cfg["XLabel"], ua_cfg["YLabel"], data)

    eng_cfg = CFG[excel_range]['ENG']
    plot_method("{}{}".format(prefix, eng_cfg["Name"]), eng_cfg["XLabel"], eng_cfg["YLabel"], data)


def fit_to_clusters(data, c=2, algorithm='full', random_state=0):
    ids = data["C_Ids"]
    names = data["C_Names"]
    points = data["C_Points"]
    columns = data["Columns"]

    clustered_ids = list()
    clustered_names = list()
    clustered_points = list()
    # noinspection PyShadowingNames
    for i in range(c):
        clustered_ids.append(list())
        clustered_names.append(list())
        clustered_points.append(list())

    k_means = KMeans(n_clusters=c, algorithm=algorithm, random_state=random_state, init='k-means++').fit(points)
    for index, cluster in enumerate(k_means.labels_):
        clustered_ids[cluster].append(ids[index])
        clustered_names[cluster].append(names[index])
        clustered_points[cluster].append(points[index])

    return {
        "Prefix": 'C{}'.format(c),
        "C": c,
        "Centers": k_means.cluster_centers_,
        "Columns": columns,
        "C_Ids": clustered_ids,
        "C_Names": clustered_names,
        "C_Points": clustered_points
    }


def match_clusters(test_data):
    size = len(test_data)
    matched_names, matches = alg.match(test_data)

    data_frame = list()
    for match_key in matches.keys():
        match = matches[match_key]
        row = [match_key, round(len(match) / size, 2)]
        row.extend([math.nan] * len(matched_names))

        for match_point in match:
            split = match_point.split(';')
            index = int(split[0])
            row[index + 2] = int(split[1])
            pass

        data_frame.append(row)

    return matched_names, data_frame


def export_match(match_name, matched_names, data_frame):
    column_names = ['Компанії', 'Коефіцієнт']
    column_names.extend(matched_names)
    df1 = pandas.DataFrame(data_frame, columns=column_names)
    df1.to_excel("output/{}.xlsx".format(match_name))


def calculate_silhouette(excel_range, cfg, range_n_clusters, algorithm, random_state, init):
    print("> Processing [{}]".format(excel_range))
    input_data = xls_reader.get_data(excel_range, [])
    points = input_data['C_Points']

    fig, axs = plt.subplots(len(range_n_clusters), 1)
    fig.set_size_inches(18, 8 * len(range_n_clusters))

    for index, n_clusters in enumerate(range_n_clusters):
        # Create a subplot with 1 row and 2 columns

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        axs[index].set_xlim([-0.2, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        axs[index].set_ylim([-5, len(points) + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, algorithm=algorithm, random_state=random_state, init=init)
        cluster_labels = clusterer.fit_predict(points)

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(points, cluster_labels)
        print(
            "For n_clusters =",
            n_clusters,
            "The average silhouette_score is :",
            silhouette_avg,
        )

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(points, cluster_labels)

        y_lower = 0
        # noinspection PyShadowingNames
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = COLORS[i]  # cm.nipy_spectral(float(i) / n_clusters)
            axs[index].fill_betweenx(
                np.arange(y_lower, y_upper),
                0,
                ith_cluster_silhouette_values,
                facecolor=color,
                edgecolor=color,
                alpha=1,
            )

            # Label the silhouette plots with their cluster numbers at the middle
            axs[index].text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        axs[index].set_title("The silhouette plot for the sample data with n_clusters = %d" % n_clusters)
        axs[index].set_xlabel("The silhouette coefficient values")
        axs[index].set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        axs[index].axvline(x=silhouette_avg, color="red", linestyle="--")

        axs[index].set_yticks([])  # Clear the yaxis labels / ticks
        axs[index].set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    plt.suptitle(
        "Silhouette analysis for KMeans clustering. [alg: {}, random: {}, init: {}]".format(algorithm, random_state,
                                                                                            init),
        fontsize=10,
        fontweight="bold",
    )

    plt.tight_layout()
    plt.savefig("output/Decision/{} {}.png".format(
        "{}_{}_{}".format(algorithm, random_state, init), cfg['Name'].replace('.', '').replace("\n", "")),
        dpi=300.0, format='png')
    plt.close()
    # plt.show()


def build_industry_focus_y_on_information_technology_metrics():
    """
    cp,bx,bu:bw,by:co   |   Industry focus %,\n X[Dispersion] Y[Information technology].

    :return:
    """
    _xls_range = 'cp,bx,bu:bw,by:co'
    _opts = ('auto', 0, 5)
    _input_data = xls_reader.get_data(_xls_range)

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    plot_scatter(_xls_range, CR[_xls_range])

    export_excel(_xls_range, CR[_xls_range], markers=['D', '>', 's', 'o', '^'])


def build_focus_service_lines_y_on_custom_software_development_metrics():
    """
    bt,ay,aq:ax,az:bs   |   Focus Service lines %, X[Dispersion] Y[Custom Software Development].

    :return:
    """
    _xls_range = 'bt,ay,aq:ax,az:bs'
    _opts = ('auto', 0, 5)
    _input_data = xls_reader.get_data(_xls_range)

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    plot_scatter(_xls_range, CR[_xls_range])

    export_excel(_xls_range, CR[_xls_range], markers=['D', 'o', 's', '>', '^'])


def build_total_size_to_ukraine_employees_percentage_metrics():
    """
    H,I   |   The size of the company and the percentage of Ukrainian employees.

    :return:
    """
    _xls_range = 'h,j'
    _opts = ('auto', 0, 5)
    _input_data = xls_reader.get_data(_xls_range)

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    plot_scatter(_xls_range, CR[_xls_range])

    export_excel(_xls_range, CR[_xls_range], markers=['o', 's', 'D', '^', '>'])


def build_total_size_to_ukraine_employees_metrics():
    """
    G,I   |   The size of the company and the amount of Ukrainian employees.

    :return:
    """
    _xls_range = 'g,i'
    _opts = ('elkan', 1, 6)
    _input_data = xls_reader.get_data(_xls_range)

    plot_silhouette(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])
    plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    plot_scatter(_xls_range, CR[_xls_range])

    export_excel(_xls_range, CR[_xls_range])


def build_industry_focus_metrics():
    """
    bu:co   |   Industry focus.

    :return:
    """
    _xls_range = 'bu:co'
    _opts = ('elkan', 8, 9)
    _input_data = xls_reader.get_data(_xls_range)

    plot_silhouette(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])
    plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    export_excel(_xls_range, CR[_xls_range])

    plot_stacked_bar(_xls_range, CR[_xls_range])


def build_focus_services_metrics():
    """
    aq:bq,bs   |   Focus Services Lines.

    :return:
    """
    _xls_range = 'aq:bq,bs'
    _opts = ('elkan', 0, 7)
    _input_data = xls_reader.get_data(_xls_range)

    plot_silhouette(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])
    plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1])

    CR[_xls_range] = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=_opts[2])
    export_excel(_xls_range, CR[_xls_range])

    plot_stacked_bar(_xls_range, CR[_xls_range])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for i in range(0, 10):
        # calculate_silhouette(
        #     'bu:co', CFG['bu:co']['UA'], [7, 8, 9],
        #     algorithm='elkan', random_state=i, init='k-means++')
        # calculate_silhouette(
        #     'bu:co', CFG['bu:co']['UA'], [7, 8, 9],
        #     algorithm='full', random_state=i, init='k-means++')

        # calculate_silhouette(
        #     'aq:bq,bs', CFG['aq:bq,bs']['UA'], [5, 6, 7, 8, 9, 10],
        #     algorithm='elkan', random_state=i, init='k-means++')
        # calculate_silhouette(
        #     'aq:bq,bs', CFG['aq:bq,bs']['UA'], [5, 6, 7, 8, 9, 10],
        #     algorithm='full', random_state=i, init='k-means++')

        # calculate_silhouette(
        #     'g,i', CFG['g,i']['UA'], [2, 3, 4, 5, 6],
        #     algorithm='elkan', random_state=i, init='k-means++')
        # calculate_silhouette(
        #     'g,i', CFG['g,i']['UA'], [9, 10],
        #     algorithm='full', random_state=i, init='k-means++')

        # calculate_silhouette(
        #     'x,y,z', CFG['x,y,z']['UA'], [3, 4, 5, 6],
        #     algorithm='elkan', random_state=i, init='k-means++')
        # calculate_silhouette(
        #     's,x,y,z', CFG['s,x,y,z']['UA'], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        #     algorithm='full', random_state=i, init='k-means++')
        pass

    reqs = {
        # 'bu:co': ('elkan', 8, 9),
        # 'aq:bq,bs': ('elkan', 0, 7)
        'x,y,z': ('elkan', 0, 6)
        # 'bt,ay,aq:ax,az:bs': ('auto', 0, 5),
        # 'j,q,h,l:p': ('auto', 0, 5),

    }

    # Вартість години праці середня avg. hourly rate
    # Розмір Client focus % / Enterprise
    # % працівників в Україні

    CR = dict()
    for item in reqs.items():
        xls_range = item[0]
        opts = item[1]
        input_data = xls_reader.get_data(xls_range)

        plot_silhouette(xls_range, input_data, n_clusters=opts[2], algorithm=opts[0], random_state=opts[1])
        plot_elbow(xls_range, input_data, n_clusters=opts[2], algorithm=opts[0], random_state=opts[1])

        CR[xls_range] = fit_to_clusters(input_data, algorithm=opts[0], random_state=opts[1], c=opts[2])
        export_excel(xls_range, CR[xls_range])
        # plot_scatter(xls_range, CR[xls_range])

    # ============================================================================================================
    # cp,bx,bu:bw,by:co   |   Industry focus %,\n X[Дисперсія] Y[Information technology]
    # ============================================================================================================
    # build_industry_focus_y_on_information_technology_metrics()

    # ============================================================================================================
    # bt,ay,aq:ax,az:bs   |   Focus Service lines %, X[Dispersion] Y[Custom Software Development].
    # ============================================================================================================
    # build_focus_service_lines_y_on_custom_software_development_metrics()

    # ============================================================================================================
    # h,j   |   The size of the company and the percentage of Ukrainian employees.
    # ============================================================================================================
    # build_total_size_to_ukraine_employees_percentage_metrics()

    # ============================================================================================================
    # g,i   |   The size of the company and the amount of Ukrainian employees.
    # ============================================================================================================
    build_total_size_to_ukraine_employees_metrics()

    # ============================================================================================================
    # bu:co   |   Industry focus.
    # ============================================================================================================
    build_industry_focus_metrics()

    # ============================================================================================================
    # aq:bq,bs   |   Focus Services Lines.
    # ============================================================================================================
    build_focus_services_metrics()

    # ============================================================================================================
    # Matches
    # ============================================================================================================

    avg_h_rates = xls_reader.get_data('s,t')

    # ============================================================================================================
    # Match salaries with client focus
    # ============================================================================================================
    # print("> Matching Company size and client focus")
    # matched_names, match_results = match_clusters({
    #     CFG['g,i']['ENG']["Name"]: CR['g,i']["C_Names"],
    #     CFG['x,y,z']['ENG']["Name"]: CR['x,y,z']["C_Names"]
    # })
    #
    # for match_index, match_result in enumerate(match_results):
    #     cluster_rates = []
    #     avg = 0
    #     length = 0
    #     for index, company in enumerate(avg_h_rates['C_Names']):
    #         if company in match_result[0]:
    #             avg_rate = avg_h_rates['C_Points'][index]
    #             cluster_rates.append((company, avg_rate))
    #
    #             avg_min = avg_rate[0]
    #             avg_max = avg_rate[1]
    #             if avg_min > 0 and avg_max > 0:
    #                 avg = avg + ((avg_min + avg_max) / 2)
    #                 length = length + 1
    #
    #     match_result.append(avg / (length if length > 0 else 1))
    #
    # column_names = ['Компанії', 'Коефіцієнт']
    # column_names.extend(matched_names)
    # column_names.extend(['Avg. hourly rate'])
    # df1 = pandas.DataFrame(match_results, columns=column_names)
    # df1.to_excel("output/{}.xlsx".format("Match salaries with client focus"))

    # ============================================================================================================
    # Matched Industry Focus and Focus Services
    # ============================================================================================================
    print("> Matching Industry Focus and Focus Services")
    matched_names, match_results = match_clusters({
        CFG['bu:co']['ENG']["Name"]: CR['bu:co']["C_Names"],
        CFG['aq:bq,bs']['ENG']["Name"]: CR['aq:bq,bs']["C_Names"]
    })

    for match_index, match_result in enumerate(match_results):
        cluster_rates = []
        avg = 0
        length = 0
        for index, company in enumerate(avg_h_rates['C_Names']):
            if company in match_result[0]:
                avg_rate = avg_h_rates['C_Points'][index]
                cluster_rates.append((company, avg_rate))

                avg_min = avg_rate[0]
                avg_max = avg_rate[1]
                if avg_min > 0 and avg_max > 0:
                    avg = avg + ((avg_min + avg_max) / 2)
                    length = length + 1

        match_result.append(avg / (length if length > 0 else 1))

    column_names = ['Компанії', 'Коефіцієнт']
    column_names.extend(matched_names)
    column_names.extend(['Avg. hourly rate'])
    df1 = pandas.DataFrame(match_results, columns=column_names)
    df1.to_excel("output/{}.xlsx".format("Matched Industry Focus and Focus Services"))

    # ============================================================================================================
    # Matched Company size with Industry Focus and Focus Services
    # ============================================================================================================
    # print("> Matching Company size with Industry Focus and Focus Services")
    # matched_names, match_results = match_clusters({
    #     CFG['g,i']['ENG']["Name"]: CR['g,i']["C_Names"],
    #     CFG['bu:co']['ENG']["Name"]: CR['bu:co']["C_Names"],
    #     CFG['aq:bq,bs']['ENG']["Name"]: CR['aq:bq,bs']["C_Names"]
    # })
    #
    # for match_index, match_result in enumerate(match_results):
    #     cluster_rates = []
    #     avg = 0
    #     length = 0
    #     for index, company in enumerate(avg_h_rates['C_Names']):
    #         if company in match_result[0]:
    #             avg_rate = avg_h_rates['C_Points'][index]
    #             cluster_rates.append((company, avg_rate))
    #
    #             avg_min = avg_rate[0]
    #             avg_max = avg_rate[1]
    #             if avg_min > 0 and avg_max > 0:
    #                 avg = avg + ((avg_min + avg_max) / 2)
    #                 length = length + 1
    #
    #     match_result.append(avg / (length if length > 0 else 1))
    #
    # column_names = ['Компанії', 'Коефіцієнт']
    # column_names.extend(matched_names)
    # column_names.extend(['Avg. hourly rate'])
    # df1 = pandas.DataFrame(match_results, columns=column_names)
    # df1.to_excel("output/{}.xlsx".format("Matched Company size with Industry Focus and Focus Services"))
