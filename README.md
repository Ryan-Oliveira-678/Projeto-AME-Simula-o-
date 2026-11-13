# Projeto AME Hoje — MVP de Controle de Distribuição

Aplicação web desenvolvida como Produto Mínimo Viável (MVP) para o **Projeto AME Hoje**, uma organização social localizada no Jardim Benfica (zona leste de São Paulo) que atende famílias em situação de vulnerabilidade com a distribuição mensal de cestas básicas[cite: 6].

---

## 🎯 O Problema & A Solução
Tradicionalmente, o controle da distribuição de 50 a 80 cestas básicas por ação era descentralizado em planilhas e cadernos, gerando gargalos operacionais e entregas em duplicidade (famílias que recebiam duas vezes enquanto outras ficavam sem atendimento)[cite: 6, 8]. 

Este MVP centraliza o cadastro de famílias e o histórico de entregas, aplicando regras de negócio e restrições automatizadas no banco de dados para **bloquear logisticamente a duplicidade de atendimento no mês vigente**.

---

## 🛠️ Tecnologias Utilizadas
A stack foi escolhida para garantir simplicidade de desenvolvimento por desenvolvedor solo, alta performance e manutenibilidade:
* **Linguagem:** Python 3.12
* **Framework Web:** FastAPI (alta performance e validação automática via Pydantic)
* **Persistência / ORM:** SQLAlchemy
* **Template Engine:** Jinja2 (interfaces leves e responsivas para dispositivos móveis)
* **Banco de Dados:** PostgreSQL (hospedado em nuvem PaaS)
* **Testes Automatizados:** Pytest

---

## 📱 Funcionalidades Principais
1. **Autenticação Segura (RNF01):** Acesso restrito para coordenadores e voluntários, com senhas protegidas por hash robusto (`bcrypt`) e controle de sessão por tokens.
2. **Busca e Consulta Ágil (RF02):** Localização instantânea de cadastros por CPF ou nome, exibindo o status atual do beneficiário ("Liberada para entrega" ou "Atendida").
3. **Bloqueio de Duplicidade (RF04):** Restrição automática validada no servidor para impedir o registro de entregas duplicadas no mesmo ciclo mensal.
4. **Acessibilidade e Responsividade (RNF03):** Interface otimizada para uso em smartphones por voluntários em campo, com áreas de toque adequadas ($\ge 44\times44$ pixels), contraste WCAG AA e alertas multimodais (texto, ícone e cor).

---

## 🌍 Conexão com os ODS (ONU)
O projeto está alinhado ao **ODS 2 — Fome Zero e Agricultura Sustentável**, especificamente à **Meta 2.1**, contribuindo para garantir o acesso seguro e regular de pessoas em vulnerabilidade a alimentos por meio da otimização logística e justiça na distribuição[cite: 10].

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/ryanrichard-dev/projeto-ame-hoje-mvp.git](https://github.com/ryanrichard-dev/projeto-ame-hoje-mvp.git)
   cd projeto-ame-hoje-mvp
