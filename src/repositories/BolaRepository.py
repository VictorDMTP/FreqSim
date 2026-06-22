import json
import os

class BolaRepository:
    def __init__(self):
        self._historico = []

    def registrar_estado(self, lista_bolas):
        alturas_frame = [int(b._position_y) for b in lista_bolas]
        self._historico.append(alturas_frame)

    def salvar(self, nome_arquivo="historico_musica.json"):

        os.makedirs("data", exist_ok=True)
        caminho = os.path.join("data", nome_arquivo)
        
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(self._historico, f, indent=2)
            
        print(f"\n[SUCESSO] {len(self._historico)} frames da música foram salvos em: {caminho}")