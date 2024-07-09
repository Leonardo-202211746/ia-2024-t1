def read_graph(filename: str) -> (dict, dict):
    """Lê a estrutura do grafo a partir de um arquivo."""
    with open(filename, 'r') as file:
        # Ler número de nós
        num_nos = int(file.readline().strip())
        
        # Ler nós com suas coordenadas
        coordenadas = {}
        for _ in range(num_nos):
            linha = file.readline().strip().split()
            no, lat, lon = int(linha[0]), float(linha[1]), float(linha[2])
            coordenadas[no] = (lat, lon)
        
        # Ler número de arestas
        num_arestas = int(file.readline().strip())
        
        # Ler arestas com seus custos
        grafo = {no: [] for no in coordenadas}
        for _ in range(num_arestas):
            linha = file.readline().strip().split()
            origem, destino, custo = int(linha[0]), int(linha[1]), float(linha[2])
            grafo[origem].append((destino, custo))
            grafo[destino].append((origem, custo))  # Se o grafo for não-direcionado
        
    return grafo, coordenadas
