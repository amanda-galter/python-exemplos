#formatação de strings com varias linhas
escola = 'Senai'
curso= 'Desenvolvimento de Sistemas'
uc='Logica de Programação'
matricula=34
nota=8.999999
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}\n"
      f"Matricula: {matricula:03d}\n"
      f"nota: {nota:.2f}")
