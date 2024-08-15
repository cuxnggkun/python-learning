import matplotlib.pyplot as plt


def handle_chart(x_data, y_data, file_name):
    fig = plt.figure()
    plt.scatter(x_data, y_data, alpha=0.5)
    fig.savefig(file_name)
