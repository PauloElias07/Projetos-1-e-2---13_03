# 📌 Factory Method em Python

## 👨‍💻 Autor

* **Paulo Roberto Santos Elias**
* **RA: 2171392511011**

---

## 📖 Descrição

Este projeto aplica o padrão **Factory Method** em Python para criar diferentes tipos de pessoas:

* Administrativo
* Aluno
* Professor
* Público

A criação dos objetos é feita por uma fábrica, sem instanciar diretamente as classes.

---

## 🧠 Estrutura

* `Pessoa` (classe abstrata com `abc`)
* Classes concretas: `Administrativo`, `Aluno`, `Professor`, `Publico`
* `PessoaFactory` (responsável pela criação dos objetos)

---

## ▶️ Execução

```bash
python factory_method.py
```

---

## 💡 Exemplo

```python
pessoa = PessoaFactory.criar_pessoa("aluno")
pessoa.mostrar_tipo()
```

**Saída:**

```
Tipo: Aluno
```

---

## ✅ Vantagem

Código mais organizado, flexível e fácil de manter.
