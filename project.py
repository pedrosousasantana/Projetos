import uuid
from datetime import datetime

class SoftwareFactorySystem:
    """Sistema genérico para gestão de fluxos em Fábricas de Software."""
    
    def __init__(self, nome_unidade="Matriz"):
        self.unidade = nome_unidade
        self.projetos = []

    def registrar_projeto(self, cliente, stack, categoria):
        """Adiciona um novo projeto ao backlog da fábrica"""
        projeto = {
            "id": str(uuid.uuid4())[:8].upper(),
            "cliente": cliente,
            "tecnologia": stack,
            "area": categoria,
            "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "status": "Backlog"
        }
        self.projetos.append(projeto)
        return f"✔️ [SISTEMA] Projeto '{cliente}' registrado com sucesso!"

    def dashboard_operacional(self):
        """Exibe o status atual de todos os squads/projetos"""
        print(f"\n{'='*15} DASHBOARD DE OPERAÇÕES {'='*15}")
        print(f"Unidade: {self.unidade} | Total de Projetos: {len(self.projetos)}")
        print("-" * 54)
        
        if not self.projetos:
            print("Aguardando novas demandas...")
        else:
            for p in self.projetos:
                print(f"ID: {p['id']} | {p['cliente']:<15} | {p['area']:<15} | {p['status']}")
        
        print(f"{'='*54}\n")


if __name__ == "__main__":
    fabrica = SoftwareFactorySystem("Divisão de Desenvolvimento")


    fabrica.registrar_projeto("E-commerce Alpha", "Node.js & React", "Web Full Stack")
    fabrica.registrar_projeto("Banco Digital", "Java & Spring Boot", "Fintech/Segurança")
    fabrica.registrar_projeto("IA de Diagnóstico", "Python & TensorFlow", "Data Science")

    fabrica.dashboard_operacional()

