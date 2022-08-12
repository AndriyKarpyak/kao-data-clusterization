# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from sklearn.cluster import KMeans

from xls_reader import get_data
from xls_writer import export_to_excel


def plot_elbow(excel_range, data, c, name=None):
    import plots.elbow
    try:
        plot_method = getattr(plots.elbow, 'plot_{}_elbow'.format(excel_range.replace(',', '').replace(':', '_')))
    except AttributeError:
        plot_method = getattr(plots.elbow, 'plot_default_elbow')

    plot_method(name if name else excel_range, data,
                n_clusters=c, algorithm='elkan', random_state=0, init='k-means++')


def fit_to_clusters(data, c=2, algorithm='elkan', random_state=0):
    ids = data["C_Ids"]
    names = data["C_Names"]
    points = data["C_Points"]
    columns = data["Columns"]

    clustered_ids = list()
    clustered_names = list()
    clustered_points = list()
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    _xls_range = 'z:af,ah'
    _c = 3
    _input_data = get_data(_xls_range)

    plot_elbow(_xls_range, _input_data, c=_c)
    export_to_excel(_xls_range, fit_to_clusters(_input_data, c=_c))

    # _xls_range = 'h,l,p'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=3)
    # export_to_excel(_xls_range, clustered_data)
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=4)
    # export_to_excel(_xls_range, clustered_data)

    # _xls_range = 'g,k,o'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=3)
    # export_to_excel(_xls_range, clustered_data)

    # _xls_range = 'j,n,r'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=4)
    # export_to_excel(_xls_range, clustered_data)

    # _xls_range = 'i,m,q'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=3)
    # export_to_excel(_xls_range, clustered_data)

    # _xls_range = 'ao,ap'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], C=4)
    # export_to_excel(_xls_range, clustered_data)

    # _xls_range = 'al:an'
    # _opts = ('elkan', 0, 7)
    # _input_data = get_data(_xls_range)
    #
    # plot_elbow(_xls_range, _input_data, n_clusters=_opts[2], algorithm=_opts[0], random_state=_opts[1], init='k-means++')
    # clustered_data = fit_to_clusters(_input_data, algorithm=_opts[0], random_state=_opts[1], c=4)
    # export_to_excel(_xls_range, clustered_data)


    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
