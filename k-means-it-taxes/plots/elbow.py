import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def plot_default_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    __complete(__draw_base_plot(file_name, input_data, n_clusters, algorithm, random_state, init))


def plot_z_afah_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = __draw_base_plot(file_name, input_data, n_clusters, algorithm, random_state, init)

    plt.axvline(x=3, color="red", linestyle="--", linewidth=1, alpha=1)
    # plt.axvline(x=4, color="gray", linestyle="--", linewidth=1, alpha=.5)

    __complete(file_path)


def __draw_base_plot(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} [{}] elbow.png".format(n_clusters, file_name.replace('.', '').replace("\n", "").replace(":", "-"))

    n_clusters = 10 if n_clusters <= 10 else n_clusters + 5

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters)]
    for i in x_ticks:
        k_means = KMeans(n_clusters=i, algorithm=algorithm, random_state=random_state, init=init).fit(points)
        inertias.append(k_means.inertia_)

    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 17})
    plt.rcParams.update({'font.weight': 'medium'})

    y_ticks = [inertias[0], inertias[1], inertias[4]]
    plt.yticks(y_ticks, list(map(lambda c: '{:.1f}'.format(c), y_ticks)))

    plt.xticks(x_ticks, list(map(lambda c: '{0}'.format(c), x_ticks)))

    plt.ylabel('Cumulative distance')

    for x_tick in x_ticks:
        plt.axvline(x=x_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)
    for y_tick in y_ticks:
        plt.axhline(y=y_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)

    plt.plot([x for x in range(2, n_clusters)], inertias)

    return file_path


def __complete(file_path):
    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()