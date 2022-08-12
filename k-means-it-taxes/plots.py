
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from const import COLORS, MARKERS, WIDTH, HEIGHT





def plot_default_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette.png".format(n_clusters, file_name.replace('.', '').replace("\n", "").replace(":", "-"))

    points = input_data['C_Points']

    px = 1 / plt.rcParams['figure.dpi']
    plt.figure(figsize=(WIDTH * px, HEIGHT * px))
    # The silhouette coefficient can range from -1, 1
    plt.xlim([-0.2, 1])
    # The (n_clusters+1)*10 is for inserting blank space between silhouette
    # plots of individual clusters, to demarcate them clearly.
    plt.ylim([-5, len(points) + (n_clusters + 1) * 10])

    # Initialize the clusterer with n_clusters value and a random generator
    # seed of 10 for reproducibility.
    clusterer = KMeans(n_clusters=n_clusters, algorithm=algorithm, random_state=random_state, init=init)
    cluster_labels = clusterer.fit_predict(points)

    # The silhouette_score gives the average value for all the samples.
    # This gives a perspective into the density and separation of the formed
    # clusters
    silhouette_avg = silhouette_score(points, cluster_labels)

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(points, cluster_labels)

    plt.ylabel("Cluster id's")
    plt.yticks([])  # Clear the yaxis labels / ticks
    plt.xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

    y_lower = 0
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]

        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = COLORS[i]  # cm.nipy_spectral(float(i) / n_clusters)
        plt.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_silhouette_values,
            facecolor=color,
            edgecolor=color,
            alpha=1,
        )

        # Label the silhouette plots with their cluster numbers at the middle
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples

    # The vertical line for average silhouette score of all the values
    plt.axvline(x=silhouette_avg, color="red", linestyle="--")

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_cde_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} [{}] elbow.png".format(n_clusters, file_name.replace('.', '').replace("\n", ""))

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters + 5)]
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

    plt.plot([x for x in range(2, n_clusters + 5)], inertias)

    plt.axvline(x=4, color="gray", linestyle="--", linewidth=1, alpha=.5)
    plt.axvline(x=3, color="red", linestyle="--", linewidth=1, alpha=1)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()
