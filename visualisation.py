import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_heatmap(df, structure_name="structure", save_dir="results/figures"):
    """
    df: DataFrame with columns ['alpha', 'beta', 'CTE']
    structure_name: name of the structure (for title and filename)
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Pivot for heatmap
    pivot_table = df.pivot(index='alpha', columns='beta', values='CTE')

    plt.figure(figsize=(8,6))
    plt.imshow(pivot_table, origin='lower', cmap='viridis', aspect='auto')
    plt.colorbar(label='CTE')
    plt.xticks(range(len(pivot_table.columns)), pivot_table.columns)
    plt.yticks(range(len(pivot_table.index)), pivot_table.index)
    plt.xlabel("beta")
    plt.ylabel("alpha")
    plt.title(f"CTE Heatmap: {structure_name}")
    
    filepath = os.path.join(save_dir, f"cte_heatmap_{structure_name}.png")
    plt.savefig(filepath, dpi=300)
    plt.close()
    print(f"Saved heatmap to {filepath}")
