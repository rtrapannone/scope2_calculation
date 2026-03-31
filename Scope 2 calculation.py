import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
 
def scope2(electricity, ef_location, ef_market):
    location_based = electricity * ef_location / 1000
    market_based = electricity * ef_market / 1000
    print("Location-based scope 2 electricity emissions: " + str(location_based) + " tCO2eq")
    print("Market-based scope 2 electricity emissions: " + str(market_based) + " tCO2eq")
 
    # ── Chart styling ──────────────────────────────────────────────────────
    BLUE   = "#5B9BD5"
    ORANGE = "#E07B54"
 
    plt.rcParams.update({
        "font.family":      "sans-serif",
        "font.size":        14,
        "axes.titlesize":   18,
        "axes.titleweight": "bold",
        "axes.labelsize":   15,
        "xtick.labelsize":  14,
        "ytick.labelsize":  14,
        "legend.fontsize":  13,
    })
 
    fig, ax = plt.subplots(figsize=(11, 8))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
 
    bars_x     = [0, 1]
    bar_values = [location_based, market_based]
    bar_colors = [BLUE, ORANGE]
    bar_labels = ["Location-based", "Market-based"]
 
    bars = ax.bar(
        bars_x,
        bar_values,
        color=bar_colors,
        width=0.5,
        zorder=2,
    )
 
    # Value labels inside bars
    for bar, val in zip(bars, bar_values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2,
            f"{val:.2f} tCO₂eq",
            ha="center", va="center",
            fontsize=15, fontweight="bold", color="white",
        )
 
    # Value labels above bars
    for bar, val in zip(bars, bar_values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + max(bar_values) * 0.02,
            f"{val:.2f}",
            ha="center", va="bottom",
            fontsize=13, fontweight="bold", color="#333333",
        )
 
    # ── Axes formatting ────────────────────────────────────────────────────
    ax.set_xticks(bars_x)
    ax.set_xticklabels(bar_labels, fontfamily="DejaVu Sans")
    ax.set_ylabel("Emissions (tCO₂eq)", labelpad=12)
    ax.set_ylim(0, max(bar_values) * 1.30 if max(bar_values) > 0 else 1)
 
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(axis="y", colors="#555555")
    ax.tick_params(axis="x", bottom=False)
    ax.yaxis.grid(True, color="#eeeeee", zorder=0)
    ax.set_axisbelow(True)
 
    # ── Legend ─────────────────────────────────────────────────────────────
    legend_patches = [
        mpatches.Patch(color=BLUE,   label="Location-based"),
        mpatches.Patch(color=ORANGE, label="Market-based"),
    ]
    ax.legend(
        handles=legend_patches,
        loc="upper right",
        frameon=True,
        framealpha=0.9,
        edgecolor="#cccccc",
    )
 
    # ── Title ──────────────────────────────────────────────────────────────
    ax.set_title(
        "Scope 2 electricity emissions\n(location-based vs. market-based)",
        pad=18,
        fontfamily="DejaVu Sans",
    )
 
    plt.tight_layout(pad=2)
    plt.savefig("chart1_electricity_emissions.png", dpi=150, bbox_inches="tight")
    plt.show()
    
 
 
## For running the function call the function by inserting the electricity consumption expressed in kWh during the reporting year
## and the two emission factors expressed in kgCO2eq/kWh
## It returns the scope2 CO2eq related to electricity expressed in t
## Example: scope2(5000, 0.3, 0.2) -> Returns: Location-based: 1.5 tCO2eq; Market-based: 1.0 tCO2eq
