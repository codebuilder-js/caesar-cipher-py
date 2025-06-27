```markdown
# Simple Caesar Cipher Encryptor/Decryptor

Este é um programa simples em Python que permite criptografar ou descriptografar mensagens usando a **Cifra de César**, uma técnica clássica de criptografia baseada em substituição de letras.

---

## 🔐 Funcionalidades

- Criptografa mensagens com uma chave numérica simples.
- Descriptografa mensagens previamente codificadas.
- Aceita letras do alfabeto (A–Z) e ignora pontuação e espaços.
- Copia automaticamente o resultado final para a área de transferência (se o módulo `pyperclip` estiver instalado).

---

## 💡 Como funciona

A Cifra de César funciona deslocando cada letra da mensagem original por um número fixo de posições no alfabeto. Por exemplo, com chave 3:

```

Mensagem:     HELLO
Criptografado: KHOOR

````

---

## ▶️ Como usar

1. Execute o script Python:

```bash
python caesar_cipher.py
````

2. Escolha entre:

   * `(e)` para **encrypt** (criptografar)
   * `(d)` para **decrypt** (descriptografar)

3. Insira uma **chave** (de 0 a 25) — ela determina o quanto as letras serão deslocadas.

4. Digite a **mensagem** que deseja codificar ou decodificar.

5. O resultado será exibido e, se possível, copiado para sua área de transferência.

---

## ✅ Requisitos

* Python 3.x
* (Opcional) Módulo `pyperclip` para copiar o resultado automaticamente:

```bash
pip install pyperclip
```

---

## 📄 Exemplo

```text
Do you want do (e)ncrypt or (d)ecrypt?
> e
Please, enter the key (0 to 25) to use
> 3
Enter the message to encrypt.
> HELLO WORLD
KHOOR ZRUOG
Full encrypted text copied to clipboard
```

---

## 📁 Arquivo

Este projeto contém apenas um arquivo principal:

* `caesar_cipher.py`: o script principal com toda a lógica de criptografia e descriptografia.

---

## 🧠 Observação

Este script só funciona com letras do alfabeto latino maiúsculo (A-Z). Letras minúsculas são convertidas automaticamente para maiúsculas, e qualquer símbolo especial ou número é mantido inalterado na saída.
