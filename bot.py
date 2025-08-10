import requests
import time
from datetime import datetime
import random

# ================= CONFIGURAÇÕES =================
TOKEN = "8031757993:AAFmkF-UutLiirkkXh_Rs7Kxfu73_iPFbYc"
CHAT_ID = "-4760999953"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# ================= FUNÇÕES =================
def send_message(text):
    """Envia mensagem para o grupo do Telegram."""
    try:
        payload = {
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }
        requests.post(URL, data=payload)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Mensagem enviada: {text}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def gerar_mensagem_faixa(valor):
    """Retorna a mensagem correta de acordo com o valor da vela."""
    if 2.50 <= valor <= 4.99:
        return f"{valor:.2f}x 🛡️🤑✈️ padrão de minutagem+repetição do viking\n*Confere lá bb, o viking tá na casa*\nhttps://go.aff.hanz.bet.br/hkd1ksx6\nPROTEÇÃO GARANTIDA"
    elif 5.00 <= valor <= 9.99:
        return f"{valor:.2f}x ⚔️🛡️🤑✈️ padrão de minutagem+repetição do viking\n*Confere lá bb, o viking tá na casa*\nhttps://go.aff.hanz.bet.br/hkd1ksx6\nLucro foi garantido."
    elif 10.00 <= valor <= 99.99:
        return f"{valor:.2f}x 🌹🤑✈️ padrão de minutagem+repetição do viking\nAquela rosinha não é segredo.\n*Confere lá bb, o viking tá na casa*\nhttps://go.aff.hanz.bet.br/hkd1ksx6"
    elif 100.00 <= valor <= 999.99:
        return f"{valor:.2f}x 🌹🤑✈️ pagaaa lindona vai padrão de minutagem+repetição do viking\n*Confere lá bb, o viking tá na casa*\nhttps://go.aff.hanz.bet.br/hkd1ksx6"
    elif valor >= 1000:
        return f"{valor:.2f}x 🚀🔥🌹🤑✈️ HISTÓRICO! padrão de minutagem+repetição do viking\n*Confere lá bb, o viking tá na casa*\nhttps://go.aff.hanz.bet.br/hkd1ksx6"
    return None

# ================= ESTRATÉGIAS =================
minutagem_alvo = [4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59]
gatilhos_rosa = [1.02, 1.04, 1.08, 1.22, 1.33, 1.44, 1.71]

historico_repeticao = []
ultima_vela_rosa = None

def analisar_minutagem(valor, horario):
    """Se vela >= 2.50 dentro da minutagem alvo (+/- 30s) envia alerta."""
    minuto_atual = horario.minute
    segundo_atual = horario.second
    for alvo in minutagem_alvo:
        if abs((minuto_atual * 60 + segundo_atual) - (alvo * 60)) <= 30:
            if valor >= 2.50:
                msg = gerar_mensagem_faixa(valor)
                if msg:
                    send_message(f"⏱ {horario.strftime('%H:%M')} ✈️💸\n{msg}")

def analisar_repeticao(valor):
    """Contagem de casas após última rosa (>= 10x). Reinicia no hit."""
    global ultima_vela_rosa, historico_repeticao
    if valor >= 10:
        ultima_vela_rosa = datetime.now()
        historico_repeticao = []
    elif ultima_vela_rosa:
        historico_repeticao.append(valor)
        if len(historico_repeticao) in [3, 5, 7, 9, 10, 12]:
            send_message(f"Padrão de repetição após última: 🌹✈️\n{len(historico_repeticao)} casas")
    
def analisar_gatilho(valor):
    """Se valor estiver na lista de gatilhos e próximo >= 2.50 envia Win."""
    if round(valor, 2) in gatilhos_rosa:
        send_message(f"Gatilhos para Rosas: 🌹✈️\nVela {valor:.2f}x detectada")

# ================= LOOP PRINCIPAL =================
def main():
    send_message("✅ Bot iniciado e conectado com sucesso!")
    
    # Simulação de resultados para teste
    valores_teste = [3.25, 8.88, 11.11, 1450.33, 1.04, 2.50]
    
    while True:
        valor = random.choice(valores_teste)
        agora = datetime.now()
        
        # Estratégias
        analisar_minutagem(valor, agora)
        analisar_repeticao(valor)
        analisar_gatilho(valor)
        
        time.sleep(5)  # intervalo de 5 segundos para simulação

if __name__ == "__main__":
    main()
