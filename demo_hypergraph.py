import pandas as pd
from cte_entropy import CTECalculator, plot_heatmap

# Example hypergraph
hypergraph = [
    {0,1}, {1,2,3}, {0,2,3}, {3,4}
]

cte = CTECalculator(log_base=2)

alphas = [0.1,0.5,1.0,1.5,2.0]
betas = [0.1,0.5,1.0,1.5,2.0]

results = cte.parameter_sweep(hypergraph, alphas, betas, structure_type='hypergraph')
df = pd.DataFrame(results)

print(df)
plot_heatmap(df, structure_name="small_hypergraph")
