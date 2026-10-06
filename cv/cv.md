# Luca Romagnoli

Senior Software Engineer -- Distributed Backend Systems, Agentic AI, Polyglot (Python · Go · TypeScript · C++)

## Contact

- Location: London, UK
- Email: ${CV_EMAIL}
- Phone: ${CV_PHONE}
- GitHub: [github.com/lucaromagnoli](https://github.com/lucaromagnoli)
- LinkedIn: [linkedin.com/in/lucaromagnoli79](https://www.linkedin.com/in/lucaromagnoli79/)

## Summary

Senior software engineer with over ten years of experience building backend and distributed systems. Works mainly in Python, Go and TypeScript, with production experience in Ruby and JavaScript and substantial C++ in open-source work. Has carried out several system migrations: a high-throughput Rails service to Go at Deliveroo, a monolith to microservices at Sainsbury's, and legacy services to event-driven AWS Lambda at Siemens. Has also built Kafka-based asynchronous pipelines. Currently builds production AI-agent infrastructure (multi-agent orchestration, A2A, MCP) at NearForm. Creator of MAGDA, an open-source, cross-platform digital audio workstation (DAW) with built-in AI agents. It spans a C++ desktop application and audio engine, a React/Next.js web front end, and AWS infrastructure managed with Terraform.

## Technical Skills

- **Languages:** Python, Go, TypeScript (primary); C++20/23, Ruby, JavaScript, Java, SQL, Bash
- **Backend / APIs:** FastAPI, Flask, Django, Ruby on Rails, Node.js; REST, gRPC, GraphQL, WebSocket JSON-RPC
- **Frontend:** React, Next.js, Vite, Tailwind CSS, Zustand
- **Data / Messaging:** Kafka, AWS RDS, SQLite (FTS5)
- **Cloud / Infrastructure:** AWS (Lambda, ECS, EventBridge, RDS, S3, CloudFront), Terraform, Docker, Kubernetes, Helm, GitHub Actions
- **Native / Desktop:** C++ with JUCE, CMake, WebAssembly (Emscripten), Catch2; macOS, Windows and Linux builds
- **Observability:** Langfuse, DataDog, Sentry
- **AI / Agentic Systems:** Multi-agent orchestration, tool-using agents, A2A, MCP servers and integrations, RAG pipelines, Claude SDK, OpenAI, Anthropic, Gemini, Hugging Face, local inference with llama.cpp
- **LLM Infrastructure:** Prompt orchestration, structured output (JSON Schema, Pydantic), context-window optimisation, token and cost tracking
- **Practices:** Distributed and event-driven systems, async programming, API design, system migrations, TDD, integration testing, CI/CD

## Experience

### NearForm

**Senior Software Engineer**
2025 -- Present

- Contributing to Agents-at-Scale ARK, an open-source framework for building and running production AI agents.
- Designing multi-agent orchestration workflows and agent-to-agent (A2A) communication.
- Building backend services and tooling in Python, Go and TypeScript.
- Building agent tooling with the Claude SDK and LLM APIs, including Model Context Protocol (MCP) integrations for tool-using agents.
- Integrating LLM observability and tracing with Langfuse.

### Deliveroo

**Senior Software Engineer**
December 2024 -- 2025

- Led the migration of a high-throughput backend service from Ruby on Rails to Go.
- Built automation systems using LLM workflows to improve developer productivity.
- Implemented infrastructure as code with Terraform.
- Improved service observability with DataDog and Sentry.

### Citi

**Senior Software Engineer (Contract)**
October 2023 -- July 2024

- Developed proof-of-concept systems with Python and FastAPI for certifying internal IT solutions.
- Built automation tools that generate PowerPoint and Word reports programmatically.
- Implemented automated screen-capture scraping pipelines.

### Siemens

**Senior Software Engineer (Contract)**
March 2023 -- September 2023

- Migrated legacy services to an event-driven AWS Lambda architecture.
- Built distributed file-processing pipelines.
- Rewrote services from JavaScript to Python.

### Zaizi (National Archives)

**Senior Software Engineer (Contract)**
November 2022 -- February 2023

- Developed a Django backend integrated with Keycloak authentication.
- Built Docker images and deployed services to AWS ECS.

### Wayfair

**Senior Software Engineer (Contract)**
March 2022 -- October 2022

- Developed internal logistics and order-management tools.
- Implemented asynchronous processing pipelines with Kafka.

### Just Eat

**Senior Software Engineer**
September 2021 -- February 2022

- Automated AWS RDS infrastructure deployments.
- Improved infrastructure reliability through automation and monitoring.

### Sainsbury's

**Senior Software Engineer**
January 2020 -- August 2021

- Led the migration from monolithic systems to microservices.
- Built ETL pipelines with Kafka and asynchronous Python services.

### Mavens of London

**Software Developer**
February 2017 -- December 2019

- Built large-scale web-scraping systems.
- Contributed to machine-learning and NLP projects.

### Empello

**Junior Developer**
March 2015 -- January 2017

- Built web-scraping infrastructure that monitored mobile advertising networks.

## Projects

### MAGDA -- Open-source DAW with built-in AI agents

Creator and principal author. GPL-3.0. Links: [github.com/Conceptual-Machines/magda-core](https://github.com/Conceptual-Machines/magda-core) · [magda.land](https://magda.land)

- Built a cross-platform desktop application for macOS, Windows and Linux in C++23 and JUCE. It has Catch2 test suites, and CI builds and releases it on all three platforms.
- Designed and built a native audio engine to replace Tracktion Engine, with module boundaries enforced at build time. It hosts VST3, AU and LV2 plugins.
- Extracted the core into a host-independent C++ SDK (MIT licence) that compiles both natively and to WebAssembly, so the same code runs in the browser.
- Built the agent layer: an orchestrator that coordinates specialist agents and a custom domain-specific language (DSL) for DAW commands. It runs on a provider-agnostic LLM module (OpenAI, Anthropic, Gemini, local llama.cpp), and an embedded SQLite (FTS5) media and preset database supports search.
- Exposed the application through an embedded MCP server and a WebSocket JSON-RPC API. These are used by AI assistants and by a TypeScript Stream Deck plugin.
- Built magda.land with Next.js, React and TypeScript, plus an in-progress browser DAW (Faust compiled to WebAssembly). The site is served from S3 and CloudFront with Lambda functions, provisioned in Terraform and deployed with GitHub Actions.

### grammar-school

A framework for building small, LLM-friendly domain-specific languages, with Python and Go implementations.
[grammar-school](https://github.com/Conceptual-Machines/grammar-school) · [Python](https://github.com/Conceptual-Machines/grammar-school-python) · [Go](https://github.com/Conceptual-Machines/grammar-school-go)

### DataService

A Python library for scalable data gathering.
[github.com/lucaromagnoli/dataservice](https://github.com/lucaromagnoli/dataservice)

## Education

**BSc Computer Science** -- Open University

Final-year project: a machine-learning fashion search engine built with TensorFlow and Annoy.
[github.com/lucaromagnoli/open-uni-final-project](https://github.com/lucaromagnoli/open-uni-final-project)

## Interests

### Electronic Music Production

Produces electronic music and builds tools that connect AI with digital audio workstations.
