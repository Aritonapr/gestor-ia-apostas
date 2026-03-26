name: Sync Jarvis Data

on:
  schedule:
    - cron: '0 8 * * *' # Roda todo dia às 08:00 AM
  workflow_dispatch: # Permite rodar manualmente no botão "Run workflow"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install pandas

      - name: Run sync script
        run: python sync_data.py

      - name: Commit and push changes
        run: |
          git config --global user.name "Jarvis Bot"
          git config --global user.email "bot@jarvis.ia"
          git add data/database_diario.csv
          git commit -m "Auto-update jogos do dia [skip ci]" || echo "No changes to commit"
          git push
