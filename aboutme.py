import os

os.system("clear")
name = input("Nome De Usuário: ")
password = os.getenv("PASSWD")
if name == "Fetoyu":
    favorite_color = input("Qual é a sua cor favorita? ")
    if favorite_color == "Azul" or "Amarelo" or "Verde" or "Vermelho":
        print(f"Bem-vindo de volta, {name}")
        print("")
        print("Deseja continuar? (s/n)")
        confirm = input("> ")
        if confirm == "s":
            # Configurações
                first_job = "Back-end / Front-end Developer"
                second_job = "Shell / Bash Scripter"
                third_job = "Website Developer"
                skills = ["Python: Newbie", "C++: Newbie", "Bash: Expert", "Html: Advanced","PHP: Newbie"]
                hobbies = ["Listen to EDM songs", "Code Something", "Play Casual Games"]
                favorite_artists = ["Alan Walker", "Marshmello", "TheFatRat", "Rain Man", "F-777","Ericovich", "Jax Jones"]
                most_used_programming_language = "Bash / Shell"
                learning_since = 2020
                nowadays = 2025
                started_with = nowadays - learning_since
                github_profile = "https://github.com/FetoyuDev"
                github_public_repos = ["https://github.com/FetoyuDev/Emoji-Extractor", "https://github.com/FetoyuDev/File-Converter"]
                github_pinned_repo = "https://github.com/FetoyuDev/Emoji-Extractor"

                print("")
                print("Seu Perfil - Sobre-mim")
                print(f"Nome: {name}")
                print("")
                print("Trabalhos: ")
                print(f"1: {first_job}")
                print(f"2: {second_job}")
                print(f"3: {third_job}")
                print("")
                print("Habilidades ")
                print(skills)
                print("")
                print("Hobbies: ")
                print(hobbies)
                print("")
                print("Artistas Favoritos: ")
                print(favorite_artists)
                print("")
                print(f"Linguagem De Programação Mais Usada: {most_used_programming_language}")
                print(f"Aprendendo Desde {learning_since} / {nowadays}")
                print(f"Já Se Passaram {started_with} Anos Que Comecei A Aprender Programação")
                print("")
                print("Github: ")
                print(f"Seu Perfil: {github_profile}")
                print(f"Repositórios Públicos: {github_public_repos}")
                print(f"Repositório Fixado: {github_pinned_repo}")
                print("")
                print("Deseja Sair? (s/n)")
                exit = input("> ")
                if exit == "s":
                    print("Saindo...")
                    os.system("clear")
                    exit
                else:
                    print("Você não digitou 's' para sair. Tente novamente.")
        else:
            exit("Saindo...")
    else:
        exit("Saindo...")
else:
    print("Senha ou nome de usuário incorreto")  # Aqui você pode adicionar uma opção para o usuário tentar novamente ou sair do programa
    print("Deseja tentar novamente? (s/n)")
    resposta = input().lower()
    if resposta == "s":
        print("Login")
        print("")
        name = input("Nome De Usuário: ")
        password = input("Senha: ")
    if name == "Fetoyu" and password == "PythonDeveloper2025@#$":
        favorite_color = input("Qual é a sua cor favorita? ")
        if favorite_color == "Azul" or "Amarelo" or "Verde" or "Vermelho":
            print(f"Bem-Vindo de volta, {name}")
            print("Deseja continuar? (s/n)")
            confirm = input("> ")
            if confirm == "s":
                # Configurações
                first_job = "Back-end / Front-end Developer"
                second_job = "Shell / Bash Scripter"
                third_job = "Website Developer"
                skills = ["Python: Newbie", "C++: Newbie", "Bash: Expert", "Html: Advanced","PHP: Newbie"]
                hobbies = ["Listen to EDM songs", "Code Something", "Play Casual Games"]
                favorite_artists = ["Alan Walker", "Marshmello", "TheFatRat", "Rain Man", "F-777","Ericovich", "Jax Jones"]
                most_used_programming_language = "Bash / Shell"
                learning_since = 2020
                nowadays = 2025
                started_with = nowadays - learning_since
                github_profile = "https://github.com/FetoyuDev"
                github_public_repos = ["https://github.com/FetoyuDev/Emoji-Extractor", "https://github.com/FetoyuDev/File-Converter"]
                github_pinned_repo = "https://github.com/FetoyuDev/Emoji-Extractor"

                print("Seu Perfil - Sobre-mim")
                print(f"Nome: {name}")
                print("Trabalhos: ")
                print(f"1: {first_job}")
                print(f"2: {second_job}")
                print(f"3: {third_job}")
                print("")
                print("Habilidades ")
                print(skills)
                print("")
                print("Hobbies: ")
                print(hobbies)
                print("")
                print("Artistas Favoritos: ")
                print(favorite_artists)
                print("")
                print(f"Linguagem De Programação Mais Usada: {most_used_programming_language}")
                print(f"Aprendendo Desde {learning_since} / {nowadays}")
                print(f"Já Se Passaram {started_with} Anos Que Comecei A Aprender Programação")
                print("")
                print("Github: ")
                print(f"Seu Perfil: {github_profile}")
                print(f"Repositórios Públicos: {github_public_repos}")
                print(f"Repositório Fixado: {github_pinned_repo}")
                print("")
                print("Deseja Sair? (s/n)")
                exit = input("> ")
                if exit == "s":
                    print("Saindo...")
                    os.system("clear")
                    exit
                else:
                    print("Você não digitou 's' para sair. Tente novamente.")
            else:
                exit("Saindo...")
        else:
            exit("Saindo...")
    else:
        exit("Saindo...")