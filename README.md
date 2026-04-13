# University Exercises
Collection of university exercises, coding practices, and academic projects. Focused on improving programming skills, problem-solving, and understanding core concepts in software development.

# 🤖 Robô SVG Animado

Este projeto consiste em um robô estilizado construído inteiramente com **SVG (Scalable Vector Graphics)** e animado via **CSS**. Ele é leve, escalável para qualquer tamanho sem perda de qualidade e não requer arquivos externos.

## 🛠️ Como foi construído

O robô foi estruturado utilizando formas geométricas básicas definidas por tags XML. A hierarquia segue a ordem de empilhamento: elementos no topo do código ficam "atrás" dos elementos definidos no final.

### Elementos SVG utilizados:

- `<rect>`: Usado para criar o corpo principal, a tela do rosto e a boca. O atributo `rx` foi aplicado para arredondar os cantos.
- `<circle>`: Utilizado para os olhos e para a ponta da antena.
- `<line>`: Forma a haste da antena.
- `<style>`: Contém as regras CSS para cores e animação.

## 👁️ Animação de Piscar

A animação é controlada por `@keyframes` no CSS. Ela manipula a propriedade `transform: scaleY()` dos olhos.

- **Duração:** 4 segundos por ciclo.
- **Lógica:** Os olhos permanecem abertos em 90% do tempo. Nos 10% finais, eles encolhem verticalmente para simular o movimento das pálpebras.

## 🎨 Como Modificar

Você pode personalizar o robô editando o código diretamente em um editor de texto:

1. **Mudar a Cor do Corpo:** Localize a tag `<rect>` com o comentário `` e altere o valor de `fill` (ex: `fill="#00ffff"` para ciano).
2. **Velocidade do Piscar:** No CSS, altere o valor `4s` na classe `.eye` para um tempo menor (mais rápido) ou maior (mais devagar).
3. **Cor dos Olhos:** Altere o `fill` dentro da classe `.eye` no bloco de estilo.
4. **Tamanho:** Altere os valores de `width` e `height` na tag de abertura `<svg>`.

---

> **Dica:** Para usar este robô em um site, você pode copiar o código e colá-lo diretamente no HTML ou salvá-lo como um arquivo `.svg` e usá-lo dentro de uma tag `<img>`.
>