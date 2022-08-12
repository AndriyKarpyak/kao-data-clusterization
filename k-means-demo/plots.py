import random

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.metrics.pairwise import euclidean_distances

WIDTH = 2480
HEIGHT = 3508

DPI = 300.0

plt.rcParams.update({'figure.dpi': DPI})

COLORS = ['gold',
          'tab:red',
          'limegreen',
          'tab:pink',
          'tab:orange',
          'tab:cyan',
          'tab:purple',
          'tab:brown',
          'tab:green',
          'tab:olive']

MARKERS = ['o', 's', 'D', '^', '>', 'v', '<', '*', 'p', 'X']

COLORMAP = ['jet', 'gnuplot', 'gist_ncar']


def plot_jqhlp_scatter(file_name, x_label, y_label, data):
    MARKERS = ['D', 'o', 's', '>', '^']
    COLORS = ['gray', 'gray', 'gray', 'gray', 'gray']
    file_path = "output/{} {}.png".format(data['Prefix'], file_name.replace('.', '').replace("\n", ""))
    f_names = [
        # other
        'Viseven', 'Vector Software', 'Excited', 'Eastern Peak',
        'Ciklum', 'Capgemini Engineering', 'Jabil', 'Ubisoft', 'Infineon Technologies',
        #
        'Skelia', 'Apriorit', 'Aegas', 'Turum-Burum',
        'Inn4Science', 'ScienceSoft', 'NANOBOT Medical Communication',
        'EPAM ', 'SoftServe', 'GlobalLogic ', 'Luxoft ']

    clustered_names_mx = data['C_Names']
    clustered_points_mx = data['C_Points']

    # Build model
    scatters = list()
    point_labels = list()
    legend_elements = list()
    legend_elements_names = list()

    # Build clusters
    for index, clustered_points_row in enumerate(clustered_points_mx):

        xr = list()
        yr = list()

        clustered_names_row = clustered_names_mx[index]

        for i, p in enumerate(clustered_points_row):
            x = p[0]
            y = p[1]

            point_label = clustered_names_row[i]
            if point_label in f_names:
                if point_label in ['Capgemini Engineering', 'Infineon Technologies']:
                    point_label = point_label.replace(' ', '\n')

                point_labels.append((x, y, point_label))

            xr.append(x)
            yr.append(y)

        alpha = .9

        scatters.append((xr, yr, COLORS[index], MARKERS[index], alpha))

    # Build Legend
    for index in range(0, len(scatters)):
        legend_elements_names.append('Cluster {}'.format(index))
        legend_elements.append(Line2D([0], [0],
                                      marker=MARKERS[index], color='w',
                                      markerfacecolor=COLORS[index], markersize=14))

    # Set up plot
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'font.weight': 'medium'})

    px = 1 / plt.rcParams['figure.dpi']
    plt.figure(figsize=(WIDTH * px, HEIGHT * px))
    # {"linear", "log", "symlog", "logit", ...}
    plt.gca().set_xscale('linear')
    plt.gca().set_yscale('linear')

    # plt.xlabel(x_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})
    # plt.ylabel(y_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})

    # Plot clusters
    for xr, yr, color, marker, alpha in scatters:
        plt.scatter(xr, yr, c=color, s=60, marker=marker, alpha=alpha)

    # Plot marker labels
    for x, y, point_label in point_labels:
        plt.text(x, y, point_label)

    # Plot legend
    # plt.legend(legend_elements, legend_elements_names)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_btayaqaxazbs_scatter(file_name, x_label, y_label, data):
    MARKERS = ['D', 'o', 's', '>', '^']
    file_path = "output/{} {}.png".format(data['Prefix'], file_name.replace('.', '').replace("\n", ""))
    f_names = [
        # other
        'Viseven', 'Vector Software', 'Boosty Labs', 'Excited', 'Eastern Peak',
        #
        'Skelia', 'Apriorit', 'Raccoon Gang', 'Aegas', 'Turum-Burum',
        'Inn4Science', 'ScienceSoft', 'NANOBOT Medical Communication',
        'EPAM ', 'SoftServe', 'GlobalLogic ', 'Luxoft ']

    clustered_names_mx = data['C_Names']
    clustered_points_mx = data['C_Points']

    # Build model
    scatters = list()
    point_labels = list()
    legend_elements = list()
    legend_elements_names = list()

    # Build clusters
    for index, clustered_points_row in enumerate(clustered_points_mx):

        xr = list()
        yr = list()

        clustered_names_row = clustered_names_mx[index]

        for i, p in enumerate(clustered_points_row):
            x = p[0]
            y = p[1]

            point_label = clustered_names_row[i]
            if point_label in f_names:
                if point_label in ['Boosty Labs', 'Raccoon Gang']:
                    point_label = point_label.replace(' ', '\n')

                point_labels.append((x, y, point_label))

            xr.append(x)
            yr.append(y)

        alpha = .7

        scatters.append((xr, yr, COLORS[index], MARKERS[index], alpha))

    # Build Legend
    for index in range(0, len(scatters)):
        legend_elements_names.append('Cluster {}'.format(index))
        legend_elements.append(Line2D([0], [0],
                                      marker=MARKERS[index], color='w',
                                      markerfacecolor=COLORS[index], markersize=14))

    # Set up plot
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'font.weight': 'medium'})

    px = 1 / plt.rcParams['figure.dpi']
    plt.figure(figsize=(WIDTH * px, HEIGHT * px))
    # {"linear", "log", "symlog", "logit", ...}
    plt.gca().set_xscale('linear')
    plt.gca().set_yscale('linear')

    plt.xlabel(x_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})
    plt.ylabel(y_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})

    # Plot clusters
    for xr, yr, color, marker, alpha in scatters:
        plt.scatter(xr, yr, c=color, s=60, marker=marker, alpha=alpha)

    # Plot marker labels
    for x, y, point_label in point_labels:
        plt.text(x, y, point_label)

    # Plot legend
    # plt.legend(legend_elements, legend_elements_names)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_cpbxbubwbyco_scatter(file_name, x_label, y_label, data):
    MARKERS = ['D', '>', 's', 'o', '^']
    file_path = "output/{} {}.png".format(data['Prefix'], file_name.replace('.', '').replace("\n", ""))
    f_names = [
        # other
        'Viseven', 'Vector Software', 'Boosty Labs',
        #
        'Skelia', 'Apriorit', 'QATestLab', 'JatApp', 'Aegas',
        'Inn4Science', 'ScienceSoft', 'NANOBOT Medical Communication',
        'EPAM ', 'SoftServe', 'GlobalLogic ', 'Luxoft ']

    clustered_names_mx = data['C_Names']
    clustered_points_mx = data['C_Points']

    # Build model
    scatters = list()
    point_labels = list()
    legend_elements = list()
    legend_elements_names = list()

    # Build clusters
    for index, clustered_points_row in enumerate(clustered_points_mx):

        xr = list()
        yr = list()

        clustered_names_row = clustered_names_mx[index]

        for i, p in enumerate(clustered_points_row):
            x = p[0]
            y = p[1]

            point_label = clustered_names_row[i]
            if point_label in f_names:
                if point_label in ['Boosty Labs', 'Vector Software']:
                    point_label = point_label.replace(' ', '\n')

                point_labels.append((x, y, point_label))

            xr.append(x)
            yr.append(y)

        alpha = .7

        scatters.append((xr, yr, COLORS[index], MARKERS[index], alpha))

    # Build Legend
    for index in range(0, len(scatters)):
        legend_elements_names.append('Cluster {}'.format(index))
        legend_elements.append(Line2D([0], [0],
                                      marker=MARKERS[index], color='w',
                                      markerfacecolor=COLORS[index], markersize=14))

    # Set up plot
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'font.weight': 'medium'})

    px = 1 / plt.rcParams['figure.dpi']
    plt.figure(figsize=(WIDTH * px, HEIGHT * px))
    # {"linear", "log", "symlog", "logit", ...}
    plt.gca().set_xscale('linear')
    plt.gca().set_yscale('linear')

    plt.xlabel(x_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})
    plt.ylabel(y_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})

    # Plot clusters
    for xr, yr, color, marker, alpha in scatters:
        plt.scatter(xr, yr, c=color, s=60, marker=marker, alpha=alpha)

    # Plot marker labels
    for x, y, point_label in point_labels:
        plt.text(x, y, point_label)

    # Plot legend
    # plt.legend(legend_elements, legend_elements_names)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_hj_scatter(file_name, x_label, y_label, data):
    file_path = "output/{} {}.png".format(data['Prefix'], file_name.replace('.', '').replace("\n", ""))
    f_names = [
        # other
        'EPAM ', 'Capgemini Engineering', 'Ubisoft', 'Jabil', 'Infineon Technologies',
        # lime
        'SoftServe', 'GlobalLogic ', 'Luxoft ',
        # cyan
        'Plarium', 'N-iX', 'Intellias', 'Itransition', 'Wargaming', 'Valtech', 'Ciklum',
        # blue
        'Miratech', 'Levi9', 'Grammarly', 'ScienceSoft', 'Israel IT',
        'Roud Studio', 'Solvd Inc.']

    clustered_names_mx = data['C_Names']
    clustered_points_mx = data['C_Points']

    # Build model
    scatters = list()
    point_labels = list()
    legend_elements = list()
    legend_elements_names = list()

    # Build clusters
    for index, clustered_points_row in enumerate(clustered_points_mx):

        xr = list()
        yr = list()

        clustered_names_row = clustered_names_mx[index]

        for i, p in enumerate(clustered_points_row):
            x = p[0]
            y = p[1]

            point_label = clustered_names_row[i]
            if point_label in f_names:
                if 'Capgemini Engineering' == point_label:
                    point_label = point_label.replace(' ', '\n')

                point_labels.append((x, y, point_label))

            xr.append(x)
            yr.append(y)

        alpha = .7

        scatters.append((xr, yr, COLORS[index], MARKERS[index], alpha))

    # Build Legend
    for index in range(0, len(scatters)):
        legend_elements_names.append('Cluster {}'.format(index))
        legend_elements.append(Line2D([0], [0],
                                      marker=MARKERS[index], color='w',
                                      markerfacecolor=COLORS[index], markersize=14))
    # legend_elements.append(Line2D([0], [0], color='red', linestyle="dotted", lw=2))
    # legend_elements_names.append('The threshold of the 100% Ukraine Companies')

    # Set up plot
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'font.weight': 'medium'})

    px = 1 / plt.rcParams['figure.dpi']
    plt.figure(figsize=(WIDTH * px, HEIGHT * px))
    # {"linear", "log", "symlog", "logit", ...}
    plt.gca().set_xscale('linear')
    plt.gca().set_yscale('linear')

    plt.xlabel(x_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})
    plt.ylabel(y_label, fontdict={'family': 'Times New Roman', 'fontsize': 22, 'fontweight': 'medium'})

    # Plot clusters
    for xr, yr, color, marker, alpha in scatters:
        plt.scatter(xr, yr, c=color, s=60, marker=marker, alpha=alpha)

    # Plot marker labels
    for x, y, point_label in point_labels:
        plt.text(x, y, point_label)

    # Plot legend
    # plt.legend(legend_elements, legend_elements_names)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_hj_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette {}.png".format(n_clusters,
                                                         file_name.replace('.', '').replace("\n", ""),
                                                         "{}_{}_{}".format(algorithm, random_state, init))

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

    # plt.ylabel("Кластери")
    plt.ylabel("Clusters")
    plt.yticks([])  # Clear the yaxis labels / ticks
    # plt.xlabel("Міра несхожості")
    plt.xlabel("Silhouette value")
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


def plot_hj_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} elbow {}.png".format(n_clusters,
                                                    file_name.replace('.', '').replace("\n", ""),
                                                    "{}_{}_{}".format(algorithm, random_state, init))

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

    plt.axvline(x=3, color="gray", linestyle="--", linewidth=1, alpha=.5)
    plt.axvline(x=4, color="red", linestyle="--", linewidth=1, alpha=1)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_gi_scatter(file_name, x_label, y_label, data):
    colors = COLORS.copy()
    # random.shuffle(colors)
    markers = MARKERS.copy()
    # random.shuffle(markers)
    file_path = "output/{} {}.png".format(data['Prefix'], file_name.replace('.', '').replace("\n", ""))
    f_names = [
        # other
        'EPAM ', 'Capgemini Engineering', 'Ubisoft',
        # lime
        'SoftServe', 'GlobalLogic ', 'Luxoft ',
        # cyan
        'Plarium', 'Intellias', 'Itransition', 'Wargaming', 'Ciklum',
        # blue
        'Miratech', 'Grammarly', 'ScienceSoft', 'Itera', 'Future Processing', 'Netpeak',
        'LookInAr', 'Roud Studio', 'Bambuk Studio', 'Solvd Inc.', 'Happy']

    f_names = [
        # other
        'EPAM ', 'Capgemini Engineering', 'Ubisoft',
        # lime
        'SoftServe', 'GlobalLogic ', 'Luxoft ',
        # cyan
        'Plarium', 'Intellias', 'Wargaming',
        # blue
        'Grammarly', 'ScienceSoft', 'Future Processing',
        'Roud Studio', 'Bambuk Studio', 'Solvd Inc.']

    clustered_names_mx = data['C_Names']
    clustered_points_mx = data['C_Points']

    # Build model
    scatters = list()
    point_labels = list()
    legend_elements = list()
    legend_elements_names = list()

    # Build clusters
    for index, clustered_points_row in enumerate(clustered_points_mx):

        xr = list()
        yr = list()

        clustered_names_row = clustered_names_mx[index]

        for i, p in enumerate(clustered_points_row):
            x = p[0]
            y = p[1]

            point_label = clustered_names_row[i]
            if point_label in f_names:
                if 'Capgemini Engineering' == point_label:
                    point_label = point_label.replace(' ', '\n')

                point_labels.append((x, y, point_label))

            xr.append(x)
            yr.append(y)

        alpha = .7

        scatters.append((xr, yr, colors[index], markers[index], alpha))

    # Build Legend
    for index in range(0, len(scatters)):
        # legend_elements_names.append('Кластер {}'.format(index))
        legend_elements_names.append('Cluster {}'.format(index))
        legend_elements.append(Line2D([0], [0],
                                      marker=markers[index], color='w',
                                      markerfacecolor=colors[index], markersize=14))
    legend_elements.append(Line2D([0], [0], color='red', linestyle="dotted", lw=2))
    # legend_elements_names.append('Межа компаній зі 100% Українських           \nпрацівників')
    legend_elements_names.append('Limit of companies with 100% Ukrainian           \nemployees')

    # Set up plot
    x_lim = 500_000
    y_lim = 500_000
    x_ticks = [10, 100, 500, 2000, 10_000, 50_000]
    y_ticks = [10, 100, 500, 2000, 10_000, 50_000]

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27 - 1.97), (8.27 - 1.97)]})

    plt.figure()
    # {"linear", "log", "symlog", "logit", ...}
    plt.gca().set_xscale('log')
    plt.gca().set_yscale('log')

    plt.xlabel(x_label, fontdict={'family': 'Times New Roman', 'fontsize': 12, 'fontweight': 'medium'})
    plt.ylabel(y_label, fontdict={'family': 'Times New Roman', 'fontsize': 12, 'fontweight': 'medium'})

    plt.xlim([1, x_lim])
    plt.ylim([1, y_lim])

    plt.xticks(x_ticks, list(map(lambda t: "{}".format(t), x_ticks)))
    plt.yticks(y_ticks, list(map(lambda t: "{}".format(t), y_ticks)))

    # Plot clusters
    for xr, yr, color, marker, alpha in scatters:
        plt.scatter(xr, yr, c=color, s=15, marker=marker, alpha=alpha)

    # # Plot threshold
    plt.plot([1, x_lim], [1, y_lim], color="red", linestyle="dotted", linewidth=1, alpha=.5)

    # Plot marker labels
    for x, y, point_label in point_labels:
        plt.text(x, y, point_label)

    # Plot legend
    plt.legend(legend_elements, legend_elements_names, ncol=2, bbox_to_anchor=(-0.032, -0.1), loc='upper left')

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_gi_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette {}.png".format(n_clusters,
                                                         file_name.replace('.', '').replace("\n", ""),
                                                         "{}_{}_{}".format(algorithm, random_state, init))

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

    # plt.ylabel("Кластери")
    plt.ylabel("Clusters")
    plt.yticks([])  # Clear the yaxis labels / ticks
    # plt.xlabel("Міра несхожості")
    plt.xlabel("Silhouette value")
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


def plot_gi_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} elbow {}.png".format(n_clusters,
                                                    file_name.replace('.', '').replace("\n", ""),
                                                    "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters + 5)]
    for i in x_ticks:
        k_means = KMeans(n_clusters=i, algorithm=algorithm, random_state=random_state, init=init).fit(points)
        inertias.append(k_means.inertia_)

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27 - 1.97)/2, (6.27 - 1.97)/2]})

    y_ticks = [inertias[0], inertias[1], inertias[4]]
    plt.yticks(y_ticks, list(map(lambda c: '{:.1e}'.format(c), y_ticks)))

    plt.xticks(x_ticks, list(map(lambda c: '{0}'.format(c), x_ticks)))

    # plt.xlabel('Кількість кластерів')
    # plt.ylabel('Відстань')

    plt.xlabel('Clusters')
    plt.ylabel('Cumulative distance')

    for x_tick in x_ticks:
        plt.axvline(x=x_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)
    for y_tick in y_ticks:
        plt.axhline(y=y_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)

    plt.plot([x for x in range(2, n_clusters + 5)], inertias)

    plt.axvline(x=3, color="gray", linestyle="--", linewidth=1, alpha=.5)
    plt.axvline(x=6, color="red", linestyle="--", linewidth=1, alpha=1)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_buco_stacked_bar(file_name, x_label, y_label, in_data):
    category_names_en = [
        'Business services',
        'Consumer products & services',
        'Other industries',
        'Information technology',
        'Medical',
        'Retail',
        'Media',
        'Arts, entertainment & music',
        'Automotive',
        'Financial services',
        'Hospitality & leisure',
        'Gambling',
        'Telecomunications',
        'Advertising & marketing',
        'GPS, Navigation & GIS',
        'Supply Chain, logistics and Transport',
        'E-commerce',
        'Education',
        'Gaming',
        'Real Estate',
        'Manufacturing']

    category_names_ua = [
        'Бізнес - послуги',
        'Споживчі товари та послуги',
        'Інші галузі промисловості',
        'Інформаційні технології',
        'Медицина',
        'Роздрібна торгівля',
        'ЗМІ',
        'Мистецтво, розваги та музика',
        'Галузь автомобілебудування',
        'Фінансові послуги',
        'Гостинність і відпочинок',
        'Азартні ігри',
        'Телекомунікації',
        'Реклама та маркетинг',
        'GPS, навігація та ГІС',
        'Логістика та транспорт',
        'Електронна комерція',
        'Освіта',
        'Ігри',
        'Нерухомість',
        'Виробництво']

    category_names = category_names_en

    clustered_names_mx = in_data['C_Names']
    clustered_points_mx = in_data['C_Points']
    clustered_centers_mx = in_data['Centers']

    for cluster_index in range(0, len(clustered_names_mx)):

        file_path = "output/Cluster {} {} {}.png".format(cluster_index,
                                                         in_data['Prefix'],
                                                         file_name.replace('.', '').replace("\n", ""))

        cluster_names = clustered_names_mx[cluster_index]
        clustered_points = clustered_points_mx[cluster_index]
        clustered_centers_0 = clustered_centers_mx[cluster_index]

        cluster = []
        for index in range(0, len(cluster_names)):
            cluster.append([cluster_names[index], clustered_points[index],
                            euclidean_distances([clustered_points[index], clustered_centers_0])[0][1]])

        cluster = sorted(cluster, key=lambda r_: r_[len(r_) - 1], reverse=False)

        cluster_names = []
        clustered_points = []
        for row in cluster:
            cluster_names.append(row[0])
            clustered_points.append(row[1])

        labels = np.array(cluster_names)
        data = np.array(clustered_points)
        data_cum = data.cumsum(axis=1)
        category_colors = mpl.colormaps[COLORMAP[0]](np.linspace(0, 1, num=len(category_names)))

        plt.rcParams.update({'figure.dpi': DPI})
        plt.rcParams.update({'font.family': 'Times New Roman'})
        plt.rcParams.update({'font.size': 12})
        # plt.rcParams.update({'figure.figsize': [8.27 - 1.97, ((plt.rcParams['font.size'] + 4) * 1 / 72) * (len(cluster_names))]})
        plt.rcParams.update(
            {'figure.figsize': [8.27, ((plt.rcParams['font.size'] + 4) * 1 / 72) * (len(cluster_names))]})

        plt.figure()

        plt.gca().invert_yaxis()
        plt.gca().xaxis.set_visible(False)
        plt.gca().set_xlim(0, np.sum(data, axis=1).max())
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)

        for i, (col_name, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            plt.barh(labels, widths, left=starts, height=1, label=col_name, color=color)

        plt.legend(ncol=2, bbox_to_anchor=(0., 0., 1., 0.))

        plt.tight_layout(pad=0, rect=(0, 0, 0, 0))
        plt.savefig(file_path, dpi=DPI, format='png')
        plt.close()


def plot_buco_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette {}.png".format(n_clusters,
                                                         file_name.replace('.', '').replace("\n", ""),
                                                         "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data['C_Points']

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, 4.5]})
    # plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2]})
    plt.figure()

    # The silhouette coefficient can range from -1, 1
    plt.xlim([-0.1, 1])
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

    # plt.ylabel("Кластери")
    plt.ylabel("Clusters")
    plt.yticks([])  # Clear the yaxis labels / ticks
    # plt.xlabel("Міра несхожості")
    plt.xlabel("Silhouette value")
    plt.xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])

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

    plt.tight_layout(pad=0, rect=(0, 0, 0, 0))
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_buco_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} elbow {}.png".format(n_clusters,
                                                    file_name.replace('.', '').replace("\n", ""),
                                                    "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters + 5)]
    for i in x_ticks:
        k_means = KMeans(n_clusters=i, algorithm=algorithm, random_state=random_state, init=init).fit(points)
        inertias.append(k_means.inertia_)

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2.4]})

    y_ticks = [inertias[0], inertias[3], inertias[6], inertias[8]]
    plt.yticks(y_ticks, list(map(lambda c: '{:.1e}'.format(c), y_ticks)))

    plt.xticks(x_ticks, list(map(lambda c: '{0}'.format(c), x_ticks)))

    # plt.xlabel('Кількість кластерів')
    # plt.ylabel('Відстань')

    plt.xlabel('Clusters')
    plt.ylabel('Cumulative distance')

    for x_tick in x_ticks:
        plt.axvline(x=x_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)
    for y_tick in y_ticks:
        plt.axhline(y=y_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)

    plt.plot([x for x in range(2, n_clusters + 5)], inertias)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_aqbqbs_stacked_bar(file_name, x_label, y_label, in_data):
    category_names_en = [
        'Search Engine Optimization',
        'Web Design',
        'Advertising',
        'Branding',
        'Content marketing',
        'Public Relations',
        'Social Media Marketing',
        'BI & Big Data Consulting & SI',
        'Custom Software Development',
        'Enterprise App Modernization',
        'IT strategy consulting',
        'AR/VR Development',
        'Application testing',
        'Artificial Intelligence',
        'Blockchain',
        'Business consulting',
        'Cloud Consulting',
        'Cybersecurity',
        'E-comerce development',
        'IoT development',
        'Product design',
        'UX/UI Design',
        'Web development',
        'Digital Strategy',
        'IT Staff Augmentation',
        'IT managed services',
        'Mobile app Development',
        'CRM, ERP consulting and SI']

    category_names_ua = [
        'Пошукова оптимізація',
        'Веб дизайн',
        'Реклама',
        'Брендинг',
        'Контент-маркетинг',
        'Зв\'язки з громадськістю',
        'Маркетинг у соціальних мережах',
        'BI та BIG Data Consulting',
        'Розробка програмного забезпечення \nна замовлення',
        'Модернізація корпоративних додатків',
        'Консультації щодо ІТ-стратегії',
        'Розробка AR/VR',
        'Тестування програми',
        'Штучний інтелект',
        'Блокчейн',
        'Бізнес-консалтинг',
        'Хмарний консалтинг',
        'Кібербезпека',
        'Розвиток електронної комерції',
        'Розвиток IoT',
        'Дизайн виробу',
        'Дизайн UX/UI',
        'Веб-розробка',
        'Цифрова стратегія',
        'Збільшення штату ІТ',
        'Послуги, керовані ІТ',
        'Розробка мобільного додатка',
        'CRM, ERP-консалтинг і SI']

    category_names = category_names_en

    clustered_names_mx = in_data['C_Names']
    clustered_points_mx = in_data['C_Points']
    clustered_centers_mx = in_data['Centers']

    for cluster_index in range(0, len(clustered_names_mx)):

        file_path = "output/Cluster {} {} {}.png".format(cluster_index,
                                                         in_data['Prefix'],
                                                         file_name.replace('.', '').replace("\n", ""))

        cluster_names = clustered_names_mx[cluster_index]
        clustered_points = clustered_points_mx[cluster_index]
        clustered_centers = clustered_centers_mx[cluster_index]

        cluster = []
        for index in range(0, len(cluster_names)):
            cluster.append([cluster_names[index], clustered_points[index],
                            euclidean_distances([clustered_points[index], clustered_centers])[0][1]])

        cluster = sorted(cluster, key=lambda r_: r_[len(r_) - 1], reverse=False)

        cluster_names = []
        clustered_points = []
        for row in cluster:
            cluster_names.append(row[0])
            clustered_points.append(row[1])

        labels = np.array(cluster_names)
        data = np.array(clustered_points)
        data_cum = data.cumsum(axis=1)
        category_colors = mpl.colormaps[COLORMAP[1]](np.linspace(0, 1, num=len(category_names)))

        plt.rcParams.update({'figure.dpi': DPI})
        plt.rcParams.update({'font.family': 'Times New Roman'})
        plt.rcParams.update({'font.size': 12})
        # plt.rcParams.update({'figure.figsize': [8.27 - 1.97, ((plt.rcParams['font.size'] + 4) * 1 / 72) * (len(cluster_names))]})
        plt.rcParams.update(
            {'figure.figsize': [8.27, ((plt.rcParams['font.size'] + 4) * 1 / 72) * (len(cluster_names))]})

        plt.figure()

        plt.gca().invert_yaxis()
        plt.gca().xaxis.set_visible(False)
        plt.gca().set_xlim(0, np.sum(data, axis=1).max())
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)

        for i, (col_name, color) in enumerate(zip(category_names, category_colors)):
            widths = data[:, i]
            starts = data_cum[:, i] - widths
            plt.barh(labels, widths, left=starts, height=1, label=col_name, color=color)

        plt.legend(ncol=2, bbox_to_anchor=(0., 0., 1., 0.))

        plt.tight_layout(pad=0, rect=(0, 0, 0, 0))
        plt.savefig(file_path, dpi=DPI, format='png')
        plt.close()


def plot_aqbqbs_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette {}.png".format(n_clusters,
                                                         file_name.replace('.', '').replace("\n", ""),
                                                         "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data['C_Points']

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, 4.5]})
    # plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2]})
    plt.figure()

    # The silhouette coefficient can range from -1, 1
    plt.xlim([-0.1, 1])
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

    # plt.ylabel("Кластери")
    plt.ylabel("Clusters")
    plt.yticks([])  # Clear the yaxis labels / ticks
    # plt.xlabel("Міра несхожості")
    plt.xlabel("Silhouette value")
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


def plot_aqbqbs_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} elbow {}.png".format(n_clusters,
                                                    file_name.replace('.', '').replace("\n", ""),
                                                    "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters + 5)]
    for i in x_ticks:
        k_means = KMeans(n_clusters=i, algorithm=algorithm, random_state=random_state, init=init).fit(points)
        inertias.append(k_means.inertia_)

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2.4]})

    y_ticks = [inertias[0], inertias[3], inertias[6], inertias[8]]
    plt.yticks(y_ticks, list(map(lambda c: '{:.1e}'.format(c), y_ticks)))

    plt.xticks(x_ticks, list(map(lambda c: '{0}'.format(c), x_ticks)))

    # plt.xlabel('Кількість кластерів')
    # plt.ylabel('Відстань')

    plt.xlabel('Clusters')
    plt.ylabel('Cumulative distance')

    for x_tick in x_ticks:
        plt.axvline(x=x_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)
    for y_tick in y_ticks:
        plt.axhline(y=y_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)

    plt.plot([x for x in range(2, n_clusters + 5)], inertias)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_xyz_silhouette(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} silhouette {}.png".format(n_clusters,
                                                         file_name.replace('.', '').replace("\n", ""),
                                                         "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data['C_Points']

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, 4.5]})
    # plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2]})
    plt.figure()

    # The silhouette coefficient can range from -1, 1
    plt.xlim([-0.1, 1])
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

    # plt.ylabel("Кластери")
    plt.ylabel("Clusters")
    plt.yticks([])  # Clear the yaxis labels / ticks
    # plt.xlabel("Міра несхожості")
    plt.xlabel("Silhouette value")
    plt.xticks([-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])

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

    plt.tight_layout(pad=0, rect=(0, 0, 0, 0))
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()


def plot_xyz_elbow(file_name, input_data, n_clusters, algorithm, random_state, init):
    file_path = "output/C{} {} elbow {}.png".format(n_clusters,
                                                    file_name.replace('.', '').replace("\n", ""),
                                                    "{}_{}_{}".format(algorithm, random_state, init))

    points = input_data["C_Points"]
    inertias = list()
    x_ticks = [x for x in range(2, n_clusters + 5)]
    for i in x_ticks:
        k_means = KMeans(n_clusters=i, algorithm=algorithm, random_state=random_state, init=init).fit(points)
        inertias.append(k_means.inertia_)

    plt.rcParams.update({'figure.dpi': DPI})
    plt.rcParams.update({'font.family': 'Times New Roman'})
    plt.rcParams.update({'font.size': 12})
    plt.rcParams.update({'figure.figsize': [(8.27-1.97) / 2, (8.27-1.97) / 2.4]})

    y_ticks = [inertias[1], inertias[4]]
    plt.yticks(y_ticks, list(map(lambda c: '{:.1e}'.format(c), y_ticks)))

    plt.xticks(x_ticks, list(map(lambda c: '{0}'.format(c), x_ticks)))

    # plt.xlabel('Кількість кластерів')
    # plt.ylabel('Відстань')

    plt.xlabel('Clusters')
    plt.ylabel('Cumulative distance')

    for x_tick in x_ticks:
        plt.axvline(x=x_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)
    for y_tick in y_ticks:
        plt.axhline(y=y_tick, color="lightgray", linestyle="--", linewidth=1, alpha=0.7)

    plt.plot([x for x in range(2, n_clusters + 5)], inertias)

    plt.axvline(x=6, color="red", linestyle="--", linewidth=1, alpha=1)

    plt.tight_layout()
    plt.savefig(file_path, dpi=300.0, format='png')
    plt.close()
