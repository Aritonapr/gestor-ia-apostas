<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>GESTOR IA - PROTOCOLO GIAE-PRIME-V9</title>
    <style>
        /* CONFIGURAÇÕES GLOBAIS - DARK MODE PROFISSIONAL */
        :root {
            --sidebar-width: 260px;
            --primary-orange: #f64d23;
            --bg-deep: #0a0a0a;
            --bg-card: #141414;
            --text-main: #e0e0e0;
            --laser-glow: rgba(246, 77, 35, 0.5);
        }

        body, html {
            margin: 0;
            padding: 0;
            background-color: var(--bg-deep);
            color: var(--text-main);
            font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
            overflow-x: hidden;
        }

        /* Efeito de Grade HUD ao Fundo */
        body {
            background-image: 
                linear-gradient(rgba(246, 77, 35, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(246, 77, 35, 0.02) 1px, transparent 1px);
            background-size: 40px 40px;
        }

        /* CONTAINER PRINCIPAL */
        .app-wrapper {
            display: flex;
            min-height: 100vh;
        }

        /* SIDEBAR - 260px */
        .sidebar {
            width: var(--sidebar-width);
            background: #000000;
            border-right: 1px solid var(--primary-orange);
            display: flex;
            flex-direction: column;
            padding: 20px;
            box-sizing: border-box;
            position: fixed;
            height: 100vh;
            z-index: 100;
        }

        /* CONTEÚDO PRINCIPAL - MARGIN TOP -35px */
        .main-content {
            margin-left: var(--sidebar-width);
            margin-top: -35px;
            padding: 40px;
            flex-grow: 1;
        }

        /* BOTÕES GÊMEOS CÁPSULA COM LASER SCAN */
        .button-group {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
        }

        .btn-prime {
            width: 200px;
            height: 48px;
            background-color: var(--primary-orange);
            color: white;
            border: none;
            border-radius: 50px; /* Formato Cápsula */
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            box-shadow: 0 0 15px var(--laser-glow);
            transition: transform 0.2s;
        }

        .btn-prime:hover {
            transform: scale(1.03);
        }

        /* Efeito Laser Scan */
        .btn-prime::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                90deg,
                transparent,
                rgba(255, 255, 255, 0.6),
                transparent
            );
        }

        .btn-prime:hover::after {
            animation: laserScan 1.5s infinite;
        }

        @keyframes laserScan {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        /* ÁREA DE ANÁLISE MÉTRICA */
        .card-analise {
            background: var(--bg-card);
            border: 1px solid rgba(246, 77, 35, 0.3);
            border-radius: 8px;
            padding: 25px;
            margin-top: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .metrica-header {
            border-left: 4px solid var(--primary-orange);
            padding-left: 15px;
            margin-bottom: 20px;
        }

        .metrica-header h2 {
            margin: 0;
            color: var(--primary-orange);
            font-size: 1.2rem;
        }

        .grid-dados {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }

        .dado-item {
            background: rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 4px;
            text-align: center;
        }

        .valor-dado {
            display: block;
            font-size: 1.5rem;
            font-weight: bold;
            color: #fff;
        }

        .label-dado {
            font-size: 0.8rem;
            color: #888;
            text-transform: uppercase;
        }

    </style>
</head>
<body>

    <div class="app-wrapper">
        <!-- Sidebar -->
        <aside class="sidebar">
            <h3 style="color: var(--primary-orange);">GIAE PRIME V9</h3>
            <p style="font-size: 0.7rem; color: #555;">SISTEMA OPERACIONAL ATIVO</p>
            <nav style="margin-top: 40px;">
                <div style="color: #888; margin-bottom: 10px;">LIGAS BRASIL</div>
                <div style="font-size: 0.9rem; line-height: 2;">
                    • Série A-D<br>
                    • Estaduais<br>
                    • Copa do Brasil
                </div>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <div class="button-group">
                <button class="btn-prime">Análise Ativa</button>
                <button class="btn-prime">Sincronizar Ligas</button>
            </div>

            <div class="card-analise">
                <div class="metrica-header">
                    <h2>ANÁLISE MÉTRICA DOS JOGOS: COPA DO BRASIL</h2>
                </div>
                
                <p>Status: <span style="color: #00ff00;">Aguardando Input de Confronto...</span></p>

                <div class="grid-dados">
                    <div class="dado-item">
                        <span class="label-dado">Média de Gols (Copa)</span>
                        <span class="valor-dado">--</span>
                    </div>
                    <div class="dado-item">
                        <span class="label-dado">Prob. Ambas Marcam</span>
                        <span class="valor-dado">--%</span>
                    </div>
                    <div class="dado-item">
                        <span class="label-dado">Fator Mandante</span>
                        <span class="valor-dado">--%</span>
                    </div>
                    <div class="dado-item">
                        <span class="label-dado">Tendência Over 2.5</span>
                        <span class="valor-dado">--</span>
                    </div>
                </div>
            </div>
        </main>
    </div>

</body>
</html>
