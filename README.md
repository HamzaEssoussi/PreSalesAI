<div align="center">

# 🤖 PreSalesAI

### MS Project Plan Generator

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**PreSalesAI** is a fully local, AI-powered automation system that helps pre-sales teams generate Microsoft Project XML plans — in a fraction of the time.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Useful Commands](#-useful-commands)
- [Troubleshooting](#-troubleshooting)
- [Security & Privacy](#-security--privacy)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

**PreSalesAI** is an internal AI automation system designed for pre-sales teams. It automatically generates **Microsoft Project XML plans** from structured project data, leveraging a local RAG (Retrieval-Augmented Generation) pipeline for intelligent task and resource recommendations.

> 🔒 **Fully on-premise.** No cloud. No external API calls. All AI inference runs locally via Ollama — your data never leaves your infrastructure.

---

## ⚠️ Problem Statement

Pre-sales teams routinely spend hours on repetitive tasks:

- Manually creating project schedules from scratch
- Estimating task durations and dependencies
- Assigning resources to tasks
- Building MS Project files by hand

**PreSalesAI automates this entire workflow** by generating MS Project XML files in seconds, reducing response time by **50–70%**.

---

## ✨ Features

### 🧠 Local AI Engine
- **Mistral 7B** — high-performance open-source LLM
- **nomic-embed-text** — embedding model for semantic search
- **100% local execution** via Ollama
- **No fine-tuning needed**

### 🔍 RAG Pipeline
- Indexes historical project documents (PDF, DOCX, TXT)
- Semantic similarity search via vector embeddings
- Enriched context for intelligent task recommendations
- Persistent vector store with ChromaDB
- Orchestrated with LangChain

### 📊 MS Project XML Generator
- Converts project plans directly into MS Project-compatible XML
- Supports tasks, durations, dependencies, and resources
- Handles calendar and resource management
- Fully compliant with Microsoft Project schema
- One-click file download

### 🚀 REST API
- Interactive Swagger UI documentation
- Clean RESTful endpoints
- Pydantic-powered validation
- Robust error handling

### 🎨 Streamlit UI
- Intuitive, no-code interface
- Document upload with one click
- Real-time project plan preview
- Direct XML file download

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        PreSalesAI — Architecture                        │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │               📱 FRONTEND (Streamlit) — Port 8501               │   │
│  │  ├── Upload Documents (indexing)                                │   │
│  │  └── Project Plan (MS Project XML export)                       │   │
│  └────────────────────────────┬────────────────────────────────────┘   │
│                               │ HTTP                                    │
│  ┌────────────────────────────▼────────────────────────────────────┐   │
│  │               🔌 BACKEND API (FastAPI) — Port 8000              │   │
│  │  ├── /api/project/generate-xml  → Generate MS Project XML       │   │
│  │  └── /api/documents/upload      → Index a document              │   │
│  └──────────────┬──────────────────────────────┬───────────────────┘   │
│                 │                              │                        │
│                 ▼                              ▼                        │
│  ┌──────────────────────────┐   ┌─────────────────────────────────┐   │
│  │      🔍 RAG SERVICE      │   │       📊 XML GENERATOR          │   │
│  │  ├── ChromaDB            │   │  ├── lxml                       │   │
│  │  ├── nomic-embed-text    │   │  ├── MS Project Schema          │   │
│  │  └── Semantic Search     │   │  └── Tasks, Deps & Resources    │   │
│  └──────────────┬───────────┘   └─────────────────────────────────┘   │
│                 │                                                       │
│                 ▼                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │              🧠 AI ENGINE (Ollama) — Port 11434                 │   │
│  │  ├── Mistral 7B       (text generation, local inference)        │   │
│  │  └── nomic-embed-text (embeddings for semantic search)          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                          💾 STORAGE                             │   │
│  │  ├── data/chroma/           → Persistent vector store           │   │
│  │  ├── data/ollama/           → AI models (Mistral, nomic)        │   │
│  │  └── data/historical_docs/  → Source documents for indexing     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User uploads a historical document
        ↓
Document indexed into ChromaDB (embeddings via nomic-embed-text)
        ↓
User submits project tasks with durations and dependencies
        ↓
[Optional] RAG suggests similar tasks from historical projects
        ↓
User validates and finalizes project plan
        ↓
MS Project XML generated & downloaded
```

---

## 🛠️ Tech Stack

| Layer | Technology | Version | Role |
|---|---|---|---|
| **LLM Runtime** | Ollama | latest | Local inference server |
| **Language Model** | Mistral 7B | latest | Task/resource recommendations |
| **Embeddings** | nomic-embed-text | latest | Semantic search |
| **RAG Framework** | LangChain | 1.2.15 | RAG orchestration |
| **Vector Store** | ChromaDB | 1.5.8 | Vector database |
| **Backend API** | FastAPI | 0.136.0 | REST API |
| **XML Generation** | lxml | 6.1.0 | MS Project XML output |
| **Frontend** | Streamlit | 1.56.0 | User interface |
| **Orchestration** | Docker Compose | latest | Container management |
| **Language** | Python | 3.11+ | Primary language |

---

## 📋 Prerequisites

### Required Tools

| Tool | Min Version | Check Command |
|---|---|---|
| Docker Desktop | ≥ 24.0 | `docker --version` |
| Docker Compose | ≥ 2.20 | `docker compose version` |
| Git | ≥ 2.30 | `git --version` |

### System Requirements

| Resource | Minimum | Recommended |
|---|---|---|
| RAM | 8 GB | 16 GB |
| CPU | 4 cores | 8 cores |
| Disk space | 20 GB | 30 GB |
| Swap | 2 GB | 4 GB |

### Docker Configuration by OS

| OS | Notes |
|---|---|
| **Windows** | Enable WSL2 in Docker Desktop settings |
| **macOS** | Enable HyperKit (macOS 10.15+) |
| **Linux** | Standard installation |

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/your-username/PreSalesAI.git
cd PreSalesAI

# 2. Start all services
docker compose up -d

# 3. Pull AI models (first-time setup — may take a few minutes)
docker exec -it presales_ollama ollama pull mistral
docker exec -it presales_ollama ollama pull nomic-embed-text

# 4. Open the app
# Streamlit UI   → http://localhost:8501
# Swagger UI     → http://localhost:8000/docs
# API Health     → http://localhost:8000/health
```

---

## 🎮 Usage

### 1. Upload Historical Documents

1. Go to **📤 Upload Documents**
2. Select a file (`.txt`, `.pdf`, or `.docx`)
3. Click **"Index Document"**

The document will be embedded and stored in ChromaDB for future reference.

### 2. Generate an MS Project Plan

1. Go to **📋 Project Plan**
2. Enter project details:
   - Project name
   - Start date
3. Add tasks with:
   - Task name
   - Duration (days)
   - Assigned resources
   - Predecessor dependencies
4. Define available resources
5. Click **"Generate MS Project XML"**
6. Download the `.xml` file

---

## 📡 API Endpoints

| Method | Endpoint | Description | Body |
|---|---|---|---|
| `GET` | `/` | Root health check | — |
| `GET` | `/health` | Service status | — |
| `POST` | `/api/project/generate-xml` | Generate MS Project XML | `ProjectPlanRequest` |
| `POST` | `/api/documents/upload` | Index a document | Multipart file |
| `GET` | `/api/documents/list` | List indexed documents | — |

Full interactive documentation available at: **`http://localhost:8000/docs`**

### Example — Project Plan Request

```json
POST /api/project/generate-xml
{
  "project_name": "CRM Bank Project",
  "project_start_date": "2025-01-01",
  "tasks": [
    {
      "name": "Requirements Analysis",
      "duration_days": 10,
      "resources": ["Architect", "Project Manager"],
      "predecessors": []
    },
    {
      "name": "Development",
      "duration_days": 25,
      "resources": ["Developer", "Developer"],
      "predecessors": [1]
    }
  ],
  "resources": ["Project Manager", "Architect", "Developer", "Tester"]
}
```

### Example Response

```json
{
  "status": "success",
  "xml": "<?xml version=\"1.0\"?>\n<Project>\n  <Name>CRM Bank Project</Name>\n  ...",
  "task_count": 2,
  "resource_count": 4
}
```

---

## 📁 Project Structure

```
PreSalesAI/
│
├── docker-compose.yml           # Docker orchestration
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guide
│
├── backend/                     # FastAPI backend
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py                  # Entry point
│   ├── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py           # Pydantic models
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── rag_service.py       # RAG + ChromaDB
│   │   └── xml_generator.py     # XML generation
│   │
│   └── routers/
│       ├── __init__.py
│       ├── project_plan.py      # MS Project XML endpoint
│       └── documents.py         # Document upload endpoint
│
├── frontend/                    # Streamlit UI
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py                   # Streamlit application
│
└── data/                        # Persistent storage (gitignored)
    ├── chroma/                  # Vector store
    ├── ollama/                  # AI model weights
    └── historical_docs/         # Source documents for indexing
```

---

## 🛠️ Useful Commands

### Docker Management

```bash
# Start all services
docker compose up -d

# Stop all services
docker compose down

# Stream all logs
docker compose logs -f

# Stream logs for a specific service
docker compose logs backend -f
docker compose logs ollama -f

# Restart a service
docker compose restart backend

# Check service status
docker compose ps

# Full reset (removes all data volumes)
docker compose down -v

# Rebuild images from scratch
docker compose build --no-cache
```

### Ollama Model Management

```bash
# Pull a model
docker exec -it presales_ollama ollama pull mistral

# List downloaded models
docker exec -it presales_ollama ollama list

# Remove a model
docker exec -it presales_ollama ollama rm mistral

# Run a quick inference test
docker exec -it presales_ollama ollama run mistral "Hello!"

# Show model details
docker exec -it presales_ollama ollama show mistral
```

### API Testing with cURL

```bash
# Health check
curl http://localhost:8000/

# Test XML generation
curl -X POST http://localhost:8000/api/project/generate-xml \
  -H "Content-Type: application/json" \
  -d '{"project_name":"Test","project_start_date":"2025-01-01","tasks":[{"name":"Task 1","duration_days":5,"resources":["Dev"],"predecessors":[]}],"resources":["Dev"]}'
```

---

## 🔧 Troubleshooting

<details>
<summary><b>Docker won't start</b></summary>

```bash
# Check Docker daemon status
docker info

# Restart Docker Desktop
# Windows: Start Menu → Docker Desktop
# macOS:   Applications → Docker → Start
# Linux:   sudo systemctl restart docker
```
</details>

<details>
<summary><b>Ollama memory error</b></summary>

Increase Docker's memory allocation:

**Docker Desktop → Settings → Resources → Memory → set to 8 GB minimum**
</details>

<details>
<summary><b>ChromaDB connection error</b></summary>

```bash
# Check if ChromaDB is running
docker compose ps chromadb

# Restart it
docker compose restart chromadb

# Check logs
docker compose logs chromadb -f
```
</details>

<details>
<summary><b>Mistral model fails to download</b></summary>

```bash
# Check available disk space
df -h

# Retry the pull
docker exec -it presales_ollama ollama pull mistral

# Alternative: use a lighter model
docker exec -it presales_ollama ollama pull phi3:mini
```
</details>

<details>
<summary><b>Backend fails to start</b></summary>

```bash
# Check logs
docker compose logs backend -f

# Rebuild and restart
docker compose build backend --no-cache
docker compose up backend -d
```
</details>

---

## 🔒 Security & Privacy

PreSalesAI was built with data confidentiality as a first-class concern.

| Property | Status |
|---|---|
| 100% on-premise | ✅ No data leaves your infrastructure |
| No cloud dependency | ✅ No external API calls |
| No fine-tuning | ✅ Pre-trained models only |
| Data isolation | ✅ Documents stay inside local containers |
| PCI-DSS compatible | ✅ Designed for fintech constraints |
| No external logging | ✅ All logs remain local |
| Full infrastructure control | ✅ You own the entire stack |

---

## 🗺️ Roadmap

### ✅ v1.0 — MVP (Complete)
- Full Docker infrastructure
- FastAPI backend with core endpoints
- Streamlit frontend
- MS Project XML generator
- RAG service with ChromaDB
- Ollama + Mistral integration

### 🔄 v1.1 — In Progress
- Full Mistral 7B integration for task recommendations
- Improved prompt engineering
- Support for additional formats (Excel, PowerPoint)
- Unit and integration tests

### 📅 v2.0 — Planned
- JWT authentication for the API
- Professional React.js frontend
- Model comparison (Phi-3, Llama 3.2)
- Evaluation metrics
- Generation history & audit trail

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create a branch** — `git checkout -b feature/your-feature-name`
3. **Commit your changes** — `git commit -m 'Add: brief description of change'`
4. **Push the branch** — `git push origin feature/your-feature-name`
5. **Open a Pull Request**

### Code Standards

- **Python**: Follow [PEP 8](https://pep8.org/)
- **Documentation**: Docstrings on all public functions
- **Tests**: Use `pytest` for unit tests
- **Commits**: Clear, descriptive messages

---

---

## 📞 Contact

- 📧 **Email**: hamza.essoussi@etudiant-enit.utm.tn
- 💼 **LinkedIn**: http://www.linkedin.com/in/hamza-essoussi


---

## 🙏 Acknowledgements

- [Ollama](https://ollama.ai/) — local LLM runtime
- [Mistral AI](https://mistral.ai/) — Mistral 7B model
- [LangChain](https://www.langchain.com/) — RAG framework
- [FastAPI](https://fastapi.tiangolo.com/) — API framework
- [Streamlit](https://streamlit.io/) — frontend framework
- [ChromaDB](https://www.trychroma.com/) — vector database
- [Docker](https://www.docker.com/) — containerization

---

<div align="center">

*Hamza Essoussi*

</div>