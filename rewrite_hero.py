import sys

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# ── 1. HERO: de "IA" para "resultado" ──────────────────────────────────────
old_hero = '''<!-- HERO -->
<section class="hero">
  <div class="hero-eyebrow">Análise financeira com IA</div>
  <h1 class="hero-title">
    O seu negócio merece<br>
    análise <em>de nível CFO</em>.<br>
    <strong>Em 2 minutos.</strong>
  </h1>
  <p class="hero-sub">
    O SalesLab analisa os dados financeiros da sua PME e devolve KPIs, alertas, previsões e recomendações concretas — sem consultores, sem Excel, sem horas perdidas.
  </p>'''

new_hero = '''<!-- HERO -->
<section class="hero">
  <div class="hero-eyebrow">Para negócios com dados, mas sem analista</div>
  <h1 class="hero-title">
    Descubra onde a empresa<br>
    está a <em>perder dinheiro.</em><br>
    <strong>Antes que seja tarde.</strong>
  </h1>
  <p class="hero-sub">
    O SalesLab analisa os dados que já tem — vendas, custos, eficiência — e devolve o que mudou, porquê, e o que fazer a seguir. Sem consultores. Sem Excel. Em 2 minutos.
  </p>'''

if old_hero not in content:
    print("AVISO: bloco do hero não encontrado — nada foi alterado no hero. Verifica manualmente.")
else:
    content = content.replace(old_hero, new_hero, 1)
    print("OK: hero atualizado.")

# ── 2. Remover o "Exemplo de relatório" de dentro de "Como funciona" ───────
old_demo_in_place = '''
    <!-- Demo report -->
    <div class="demo-wrap reveal">
      <div class="demo-bar">
        <div class="demo-dot" style="background:#e74c3c"></div>
        <div class="demo-dot" style="background:#e67e22"></div>
        <div class="demo-dot" style="background:#2ecc71"></div>
        <span class="demo-bar-label">SalesLab · Exemplo ilustrativo — FisioAtiva (dados fictícios)</span>
      </div>
      <div class="demo-content">
        <div class="demo-kpis">
          <div class="demo-kpi">
            <div class="demo-kpi-label">Receita total</div>
            <div class="demo-kpi-value">€48.420</div>
            <div class="demo-kpi-change up">↑ +9,6% vs Fev</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Consultas</div>
            <div class="demo-kpi-value">1.247</div>
            <div class="demo-kpi-change up">↑ +109 consultas</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Novos pacientes</div>
            <div class="demo-kpi-value">84</div>
            <div class="demo-kpi-change up">↑ +18,3%</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Meta mensal</div>
            <div class="demo-kpi-value">105,3%</div>
            <div class="demo-kpi-change up">↑ +€2.420 acima</div>
          </div>
        </div>
        <div class="demo-alerts">
          <div class="demo-alert demo-alert-pos">✓ Fisioterapia Desportiva cresce 12,4% — capitalizar época primaveril</div>
          <div class="demo-alert demo-alert-warn">⚠ Dr. André Nunes 5,4% abaixo da meta — avaliar carga ou formação</div>
          <div class="demo-alert demo-alert-crit">! Reabilitação Pós-Cirurgia representa apenas 1,6% da receita — serviço premium subaproveitado</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PREÇOS -->'''

new_demo_removed = '''
  </div>
</section>

<!-- PREÇOS -->'''

if old_demo_in_place not in content:
    print("AVISO: bloco do demo-report (posição antiga) não encontrado — nada foi removido. Verifica manualmente.")
else:
    content = content.replace(old_demo_in_place, new_demo_removed, 1)
    print("OK: demo-report removido da posição antiga.")

# ── 3. Inserir o "Exemplo de relatório" logo a seguir ao ticker ────────────
ticker_end_marker = '''    <div class="ticker-item">Múltiplos perfis <span>→</span></div>
  </div>
</div>

<!-- PROBLEMA -->'''

new_proof_section = '''    <div class="ticker-item">Múltiplos perfis <span>→</span></div>
  </div>
</div>

<!-- PROVA: exemplo real do que o SalesLab devolve -->
<section id="exemplo" style="padding-top:60px">
  <div class="container">
    <div class="container-sm reveal" style="text-align:center; margin:0 auto 40px">
      <div class="section-label">Isto é o que recebe</div>
      <h2 class="section-title">Não gráficos.<br><em>Descobertas.</em></h2>
    </div>
    <div class="demo-wrap reveal">
      <div class="demo-bar">
        <div class="demo-dot" style="background:#e74c3c"></div>
        <div class="demo-dot" style="background:#e67e22"></div>
        <div class="demo-dot" style="background:#2ecc71"></div>
        <span class="demo-bar-label">SalesLab · Exemplo ilustrativo — FisioAtiva (dados fictícios)</span>
      </div>
      <div class="demo-content">
        <div class="demo-kpis">
          <div class="demo-kpi">
            <div class="demo-kpi-label">Receita total</div>
            <div class="demo-kpi-value">€48.420</div>
            <div class="demo-kpi-change up">↑ +9,6% vs Fev</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Consultas</div>
            <div class="demo-kpi-value">1.247</div>
            <div class="demo-kpi-change up">↑ +109 consultas</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Novos pacientes</div>
            <div class="demo-kpi-value">84</div>
            <div class="demo-kpi-change up">↑ +18,3%</div>
          </div>
          <div class="demo-kpi">
            <div class="demo-kpi-label">Meta mensal</div>
            <div class="demo-kpi-value">105,3%</div>
            <div class="demo-kpi-change up">↑ +€2.420 acima</div>
          </div>
        </div>
        <div class="demo-alerts">
          <div class="demo-alert demo-alert-pos">✓ Fisioterapia Desportiva cresce 12,4% — capitalizar época primaveril</div>
          <div class="demo-alert demo-alert-warn">⚠ Dr. André Nunes 5,4% abaixo da meta — avaliar carga ou formação</div>
          <div class="demo-alert demo-alert-crit">! Reabilitação Pós-Cirurgia representa apenas 1,6% da receita — serviço premium subaproveitado</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- PROBLEMA -->'''

if ticker_end_marker not in content:
    print("AVISO: fim do ticker não encontrado — nada foi inserido. Verifica manualmente.")
else:
    content = content.replace(ticker_end_marker, new_proof_section, 1)
    print("OK: nova secção de prova inserida a seguir ao ticker.")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Concluído.")
