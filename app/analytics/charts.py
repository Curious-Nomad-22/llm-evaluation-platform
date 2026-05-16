import matplotlib.pyplot as plt


def latency_chart(df):

    fig, ax = plt.subplots(figsize=(10, 5))

    bars = ax.bar(
        df["Model"],
        df["Latency"]
    )

    ax.set_title(
        "Model Latency Comparison",
        fontsize=18,
        pad=20
    )

    ax.set_ylabel(
        "Latency (sec)",
        fontsize=12
    )

    ax.set_xlabel(
        "Models",
        fontsize=12
    )

    ax.grid(
        axis="y",
        linestyle="--",
        alpha=0.4
    )

    plt.xticks(
        rotation=10,
        ha="right"
    )

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    return fig