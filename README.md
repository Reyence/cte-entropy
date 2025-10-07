
# CTE Entropy: Combinatorial-Topological Entropy Framework

**CTE Entropy** is an open-source Python framework for computing *Combinatorial-Topological Entropy (CTE)*, a structural measure of complexity for simplicial complexes, hypergraphs, and general combinatorial topologies.

CTE extends classical entropy notions into the combinatorial-topological domain, quantifying intrinsic structural complexity without relying on probability distributions.

---

## 🚀 Features

- Compute **CTE** for:
  - Simplicial complexes (of arbitrary dimension)
  - Hypergraphs
  - Future extensions: CW-complexes, graphs, neural manifold representations

- Parameterized weighting:
  - `α` (alpha): controls influence of simplex/hyperedge size  
  - `β` (beta): controls influence of adjacency/hierarchy

- Supports:
  - Logarithm base specification
  - Normalized entropy values
  - Batch experiments and parameter sweeps
  - Automated heatmap visualization

---

## 🧩 Installation

```bash
git clone https://github.com/reyencechua/cte-entropy.git
cd cte-entropy
pip install -r requirements.txt
