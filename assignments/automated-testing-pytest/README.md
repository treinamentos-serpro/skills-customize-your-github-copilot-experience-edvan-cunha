# 📘 Atividade: Testes Automatizados com pytest

## 🎯 Objetivo

Aprenda a escrever e executar testes automatizados para funções Python usando pytest. Você verificará resultados esperados, casos-limite e erros previstos.

## 📝 Tarefas

### 🛠️ Escrever os primeiros testes

#### Descrição

Baixe o código inicial e renomeie `starter-code.py` para `calculator.py`. Crie `test_calculator.py` na mesma pasta e escreva testes para a função `add()`.

#### Requisitos

Os testes devem:

- Importar `add()` de `calculator.py`.
- Usar `assert` para verificar a soma de pelo menos dois pares de números.
- Ser executados com `python -m pytest -q` e passar.

### 🛠️ Testar casos variados

#### Descrição

Adicione testes para a função `is_even()`, incluindo valores pares, ímpares e casos-limite.

#### Requisitos

Os testes devem:

- Verificar que `is_even()` retorna `True` para um número par e `False` para um ímpar.
- Incluir zero e um número negativo entre os casos testados.
- Usar nomes de teste que indiquem o comportamento verificado.

### 🛠️ Verificar erros esperados

#### Descrição

Teste o comportamento de `divide()` quando o divisor é zero, usando `pytest.raises` para confirmar que a função sinaliza o erro previsto.

#### Requisitos

Os testes devem:

- Verificar que uma divisão comum retorna o resultado esperado.
- Confirmar que dividir por zero levanta `ValueError`.
- Executar todos os testes com `python -m pytest -q` sem falhas.