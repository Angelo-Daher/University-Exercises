print('Robo SVG Animado!')

<svg width="300" height="300" viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="300" height="300" fill="#f4f4f4"/>

  <!-- Antena -->
  <line x1="150" y1="40" x2="150" y2="70" stroke="#444" stroke-width="4"/>
  <circle cx="150" cy="30" r="10" fill="#ff4d4d"/>

  <!-- Cabeça -->
  <rect x="75" y="70" width="150" height="110" rx="20" fill="#bfc9d1" stroke="#444" stroke-width="4"/>

  <!-- Olhos -->
  <rect x="105" y="105" width="25" height="14" rx="7" fill="#111">
    <animate attributeName="height" values="14;2;14" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="y" values="105;111;105" dur="3s" repeatCount="indefinite"/>
  </rect>

  <rect x="170" y="105" width="25" height="14" rx="7" fill="#111">
    <animate attributeName="height" values="14;2;14" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="y" values="105;111;105" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- Boca -->
  <rect x="120" y="140" width="60" height="12" rx="6" fill="#444"/>

  <!-- Corpo -->
  <rect x="95" y="185" width="110" height="70" rx="15" fill="#9aa7b1" stroke="#444" stroke-width="4"/>

  <!-- Botões -->
  <circle cx="125" cy="215" r="6" fill="#ff4d4d"/>
  <circle cx="150" cy="215" r="6" fill="#4dff88"/>
  <circle cx="175" cy="215" r="6" fill="#4da6ff"/>

  <!-- Braços -->
  <line x1="95" y1="205" x2="55" y2="225" stroke="#444" stroke-width="6" stroke-linecap="round"/>
  <line x1="205" y1="205" x2="245" y2="225" stroke="#444" stroke-width="6" stroke-linecap="round"/>

  <!-- Pernas -->
  <line x1="125" y1="255" x2="115" y2="285" stroke="#444" stroke-width="6" stroke-linecap="round"/>
  <line x1="175" y1="255" x2="185" y2="285" stroke="#444" stroke-width="6" stroke-linecap="round"/>
</svg>