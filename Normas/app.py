from flask import Flask, request, jsonify, render_template
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

@app.route('/')
def index():
    return render_template('index.html')

# Configurar a chave da OpenAI
openai.api_key = "SUA API OPENAI AQUI"

# Banco de dados simulado de normas
normDatabase = {
    "iso9001": {
        "name": "ISO 9001 - Gestão da Qualidade",
        "keyRequirements": [
            "Contexto organizacional", "Liderança", "Planejamento",
            "Suporte", "Operação", "Avaliação de desempenho", "Melhoria contínua"
        ]
    },
    "iso14001": {
        "name": "ISO 14001 - Gestão Ambiental",
        "keyRequirements": [
            "Planejamento ambiental", "Aspectos ambientais", "Requisitos legais",
            "Objetivos ambientais", "Competência e conscientização", "Monitoramento e medição"
        ]
    },
    "iso45001": {
        "name": "ISO 45001 - Segurança do Trabalho",
        "keyRequirements": [
            "Identificação de perigos", "Avaliação de riscos", "Requisitos legais",
            "Consulta e participação dos trabalhadores", "Controles operacionais", "Preparação e resposta a emergências"
        ]
    },
    "iso13485": {
        "name": "ISO 13485 - Dispositivos Médicos",
        "keyRequirements": [
            "Sistema de gestão da qualidade", "Gestão de riscos", "Projeto e desenvolvimento",
            "Avaliação de desempenho", "Auditorias internas", "Controle de não conformidades"
        ]
    },
    "iatf16949": {
        "name": "IATF 16949 - Automotiva",
        "keyRequirements": [
            "Gestão da qualidade", "Planejamento da qualidade", "Melhoria contínua",
            "Auditoria interna", "Análise crítica pela direção", "Controle de processos"
        ]
    },
    "iso50001": {
        "name": "ISO 50001 - Gestão de Energia",
        "keyRequirements": [
            "Política de gestão energética", "Planejamento energético", "Monitoramento de desempenho",
            "Melhoria contínua", "Auditoria e revisão energética"
        ]
    },
    "ohsas18001": {
        "name": "OHSAS 18001 - Saúde Ocupacional",
        "keyRequirements": [
            "Planejamento de segurança e saúde", "Identificação de riscos", "Avaliação e controle de riscos",
            "Auditoria interna", "Revisão pela gestão"
        ]
    },
    "iso27001": {
        "name": "ISO 27001 - Segurança da Informação",
        "keyRequirements": [
            "Política de segurança da informação", "Gestão de riscos", "Controle de acesso",
            "Gestão de incidentes de segurança", "Auditorias de segurança", "Melhoria contínua"
        ]
    },
    "iso22000": {
        "name": "ISO 22000 - Segurança de Alimentos",
        "keyRequirements": [
            "Gestão de segurança alimentar", "Plano de controle de perigos", "Auditoria interna",
            "Rastreamento e monitoramento de alimentos", "Melhoria contínua"
        ]
    },
    "iso31000": {
        "name": "ISO 31000 - Gestão de Riscos",
        "keyRequirements": [
            "Estabelecimento de contexto", "Identificação de riscos", "Avaliação de riscos",
            "Tratamento de riscos", "Monitoramento e revisão", "Comunicação de riscos"
        ]
    },
    "sa8000": {
        "name": "SA 8000 - Responsabilidade Social",
        "keyRequirements": [
            "Condições de trabalho", "Segurança e saúde ocupacional", "Direitos dos trabalhadores",
            "Gestão de não conformidades", "Responsabilidade social corporativa"
        ]
    },
    "iso26000": {
        "name": "ISO 26000 - Diretrizes de Responsabilidade Social",
        "keyRequirements": [
            "Governança organizacional", "Direitos humanos", "Práticas trabalhistas", "Ambiente",
            "Práticas operacionais justas", "Engajamento com consumidores"
        ]
    }
}

@app.route("/analyze", methods=["POST"])
def analyze_norm():
    data = request.json
    norm_key = data.get("norm")
    org_context = data.get("context")

    if not norm_key or not org_context:
        return jsonify({"error": "Norma e contexto são obrigatórios"}), 400

    norm = normDatabase.get(norm_key)
    if not norm:
        return jsonify({"error": "Norma não encontrada"}), 404

    # Chamar a API da OpenAI para análise inteligente
    prompt = f"""
    Você é um especialista em conformidade de normas. Avalie a norma {norm['name']} e os requisitos:
    {', '.join(norm['keyRequirements'])}.

    O contexto da organização informado pelo usuário é:
    "{org_context}"

    Identifique os requisitos já atendidos, lacunas de conformidade e sugira melhorias detalhadas.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Você é um especialista em normas e conformidade."},
                  {"role": "user", "content": prompt}]
    )

    analysis = response["choices"][0]["message"]["content"]

    return jsonify({"analysis": analysis})

if __name__ == "__main__":
    app.run(debug=True)