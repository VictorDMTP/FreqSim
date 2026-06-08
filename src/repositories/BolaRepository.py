import json
import os

class BolaRepository:
    def __init__(self, caminho_arquivo="assets/save_bolas.json"):
        self.caminho = caminho_arquivo

    def salvar(self, lista_bolas):
        dados = []
        for b in lista_bolas:
            dados.append({
                "x": float(b._position_x),
                "y": float(b._position_y),
                "vel_x": float(b._vel_x),
                "vel_y": float(b._vel_y),
                "matiz": int(b._matiz_base),
                "raio": int(b._raio_base)
            })
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)
            
    def carregar(self):
        if not os.path.exists(self.caminho):
            return None
            
        try:
            with open(self.caminho, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Aviso: Arquivo de save vazio ou corrompido. Gerando bolinhas novas...")
            return None