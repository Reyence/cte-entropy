import pandas as pd
from cte_entropy import CTECalculator, plot_heatmap

# Example simplicial complex (tetrahedron)
simplicial_complex = [
    (0,), (1,), (2,), (3,),
    (0,1), (0,2), (1,2), (2,3),
    (0,1,2)
]

cte = CTECalculator(log_base=2)

alphas = [0.1,0.5,1.0,1.5,2.0]
betas = [0.1,0.5,1.0,1.5,2.0]

results = cte.parameter_sweep(simplicial_complex, alphas, betas, structure_type='simplicial')
df = pd.DataFrame(results)

print(df)
plot_heatmap(df, structure_name="tetrahedron")
