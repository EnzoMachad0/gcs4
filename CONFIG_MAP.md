# CONFIG_MAP — Mapa de Itens de Configuração

**Projeto:** TaskManager  
**Versão do documento:** 1.0.0  
**Data de criação:** 2026-05-07  
**Disciplina:** Gerência de Configuração de Software (GCS)

---

## 1. Política de Versionamento Semântico

Este projeto segue o padrão **SemVer 2.0.0** (https://semver.org/lang/pt-BR/), com o formato:

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

| Campo        | Quando incrementar                                                    |
|--------------|-----------------------------------------------------------------------|
| **MAJOR**    | Mudanças incompatíveis com versões anteriores (breaking changes)      |
| **MINOR**    | Novas funcionalidades compatíveis com versões anteriores              |
| **PATCH**    | Correções de bugs sem quebra de compatibilidade                       |
| **PRERELEASE** | Sufixo opcional: `-alpha`, `-beta`, `-rc.1` (versões de candidatos) |
| **BUILD**    | Metadados de build (ex: `+20260507`), ignorado na comparação         |

### Exemplos de progressão de versão

```
1.0.0          → lançamento inicial (baseline)
1.0.1          → correção de bug no módulo de tarefas
1.1.0          → nova funcionalidade: filtro por data
2.0.0          → refatoração com API incompatível
1.1.0-beta.1   → pré-lançamento da versão 1.1.0
```

### Regras de nomenclatura de tags Git

- Tags de release seguem o prefixo `v`: `v1.0.0`, `v1.1.0`, `v2.0.0`
- Tags de pré-lançamento: `v1.1.0-alpha.1`, `v1.1.0-rc.1`
- Nunca reutilizar ou mover uma tag já publicada

---

## 2. Inventário de Itens de Configuração (ICs)

### 2.1 Código-fonte

| ID    | Item de Configuração      | Caminho                        | Versão  | Tipo        | Descrição                              |
|-------|---------------------------|--------------------------------|---------|-------------|----------------------------------------|
| IC-01 | task_manager              | `src/task_manager.py`          | 1.0.0   | Módulo      | Lógica principal: Task e TaskManager   |
| IC-02 | settings                  | `config/settings.py`           | 1.0.0   | Módulo      | Carregamento de variáveis de ambiente  |
| IC-03 | test_task_manager         | `tests/test_task_manager.py`   | 1.0.0   | Teste       | Testes unitários da aplicação          |

### 2.2 Scripts e Automação

| ID    | Item de Configuração | Caminho              | Versão | Tipo   | Descrição                    |
|-------|----------------------|----------------------|--------|--------|------------------------------|
| IC-04 | run.sh               | `scripts/run.sh`     | 1.0.0  | Script | Script de execução da app    |

### 2.3 Configuração e Ambiente

| ID    | Item de Configuração | Caminho        | Versão | Tipo          | Descrição                                       |
|-------|----------------------|----------------|--------|---------------|-------------------------------------------------|
| IC-05 | config.env           | `config.env`   | 1.0.0  | Config        | Template de variáveis de ambiente               |

### 2.4 Documentação

| ID    | Item de Configuração | Caminho          | Versão | Tipo  | Descrição                                        |
|-------|----------------------|------------------|--------|-------|--------------------------------------------------|
| IC-06 | README               | `README.md`      | 1.0.0  | Docs  | Documentação geral do projeto                    |
| IC-07 | CONFIG_MAP           | `CONFIG_MAP.md`  | 1.0.0  | Docs  | Este documento — inventário e política de versão |

### 2.5 Linguagem e Runtime

| ID    | Item de Configuração | Versão  | Tipo     | Descrição                                  |
|-------|----------------------|---------|----------|--------------------------------------------|
| IC-08 | Python               | 3.11+   | Runtime  | Linguagem de programação da aplicação      |

### 2.6 Plataforma e Controle de Versão

| ID    | Item de Configuração | Versão | Tipo        | Descrição                              |
|-------|----------------------|--------|-------------|----------------------------------------|
| IC-09 | Git                  | 2.x    | Ferramenta  | Sistema de controle de versão          |

---

## 3. Baseline

| Tag      | Data       | Descrição                                    |
|----------|------------|----------------------------------------------|
| v1.0.0   | 2026-05-07 | Baseline inicial — estrutura e funcionalidades básicas definidas |

---

## 4. Controle de Mudanças

Toda alteração em um IC deve ser registrada via commit Git com mensagem seguindo o padrão:

```
<tipo>(<escopo>): <descrição curta>

Tipos: feat | fix | docs | refactor | test | chore
```

Exemplos:
```
feat(task): adiciona suporte a prazo (deadline) nas tarefas
fix(settings): corrige leitura de variáveis com espaços
docs(readme): atualiza instruções de instalação
```
