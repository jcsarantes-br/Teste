def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    return sum(notas) / len(notas) if notas else 0

def classificar(media):
    """Classifica o aluno com base na média."""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"

def main():
    alunos = {}  # dicionário: nome -> lista de notas
    
    while True:
        nome = input("Nome do aluno (ou 'sair'): ").strip()
        if nome.lower() == "sair":
            break
        try:
            notas = [float(n) for n in input("Notas (separadas por espaço): ").split()]
            alunos[nome] = notas
        except ValueError:
            print("⚠️  Digite apenas números válidos!")
    
    print("\n--- Resultados ---")
    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: média {media:.1f} → {classificar(media)}")

if __name__ == "__main__":
    main()