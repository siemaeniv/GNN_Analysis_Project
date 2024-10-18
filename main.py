from data_loader import load_data
from train import train
from models import GCN

# Parametry
library = "PyG"  # Możliwe wartości: "PyG", "DGL"
matrix_format = "COO"  # Możliwe wartości: "COO", "CSR", "CSC"

# Ładujemy dane w odpowiednim formacie i bibliotece
data, dataset = load_data(library, matrix_format)

# Inicjalizacja modelu
if library == "PyG":
    model = GCN(input_dim=data.num_node_features, hidden_dim=16, output_dim=dataset.num_classes)
else:
    model = GCN(input_dim=data.ndata['feat'].shape[1], hidden_dim=16, output_dim=dataset.ndata['label'].max().item() + 1)

# Trenowanie i pomiary wydajności
train_time, mem_usage = train(model, data)