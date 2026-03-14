/* Ajuste de Proteção da Sidebar - GESTOR IA V22 */
.sidebar-item, .menu-link {
    font-size: 11px; /* Mantendo o padrão do protocolo */
    white-space: normal; /* Permite que o texto quebre em duas linhas se necessário */
    word-wrap: break-word; /* Garante a quebra de palavras longas */
    padding-right: 15px; /* Espaçamento de segurança antes da linha vertical */
    display: flex;
    align-items: center;
    line-height: 1.4; /* Melhora a legibilidade em textos de duas linhas */
    max-width: 280px; /* Trava no limite da Sidebar */
}

/* Caso o senhor prefira que o texto NÃO quebre linha e sim use reticências: */
.sidebar-item-ellipsis {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
