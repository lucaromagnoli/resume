# Luca Romagnoli

Senior Software Engineer -- Shipping AI Agents to Production · Evals & Observability · Distributed Backend Systems (Python · Go · TypeScript · C++)

## Contact

- Location: London, UK
- Email: ${CV_EMAIL}
- Phone: ${CV_PHONE}
- GitHub: [github.com/lucaromagnoli](https://github.com/lucaromagnoli)
- LinkedIn: [linkedin.com/in/lucaromagnoli79](https://www.linkedin.com/in/lucaromagnoli79/)
- Website: [conceptualmachines.co.uk](https://conceptualmachines.co.uk) -- Conceptual Machines, personal brand

## Summary

Senior software engineer with over ten years of experience in backend and distributed systems, now shipping AI agents to production. At NearForm, builds agent infrastructure for ARK, an open-source, Kubernetes-native agent framework, including an OpenAI Responses API executor used in a client pilot. Also owns the Kubernetes infrastructure, application architecture and React UI of SDLC, a greenfield agentic project. Has led system migrations at Deliveroo, Sainsbury's and Siemens. Creator of MAGDA, an open-source digital audio workstation (DAW) with built-in AI agents and a native C++23 audio engine, with over 10,000 downloads and 250+ GitHub stars.

## Technical Skills

- **Languages:** Python, Go, C++20/23 (primary); TypeScript/JavaScript, Ruby, Lua, Java, SQL, Bash
- **AI Infrastructure:** Multi-agent orchestration, A2A, MCP servers, OpenAI Responses API, Claude SDK, provider-agnostic LLM integration (OpenAI, Anthropic, Gemini, llama.cpp), structured output, evals, OpenTelemetry and Langfuse tracing
- **Distributed Systems:** Event-driven and microservice architectures, Kafka, system migrations; FastAPI, Django, Ruby on Rails; REST, gRPC, GraphQL
- **Cloud / Infrastructure:** Kubernetes, Helm, AWS (Lambda, ECS, EventBridge, RDS, S3, CloudFront), Terraform, Docker, GitHub Actions, DataDog, Sentry
- **Native / Real-time:** C++ with JUCE, CMake, WebAssembly (Emscripten), real-time audio, Catch2
- **Frontend:** React, Next.js, Tailwind CSS

## Experience

### NearForm

**Senior Software Engineer**
October 2025 -- Present

#### ARK (Agents-at-Scale)

An open-source, Kubernetes-native framework for running AI agents, where agents, models and tools are declared as Kubernetes custom resources.

- Built the OpenAI Responses API executor, which runs ARK agents on the Responses API. A client used it in a pilot project.
- Integrated the OpenAI Files API with the executor, so users can upload files that agents then reference as input.
- Built an MCP server with the Claude SDK that loads files in isolation, as part of the file-handling architecture.
- Worked with ARK's OpenTelemetry and Langfuse tracing across agent hand-offs, LLM calls and tool calls.
- Designing multi-agent orchestration workflows and agent-to-agent (A2A) communication.
- Contributed React front-end features.

#### SDLC

A greenfield agentic project that automates the software development lifecycle.

- Set up the Kubernetes cluster and the infrastructure the project runs on.
- Made the key design decisions for the application architecture, the agent workflow and the UI.
- Built the React UI.

#### Across projects

- Built evals that gate agent releases: golden-dataset regression suites in CI, tool-call and trajectory checks, and online evals on production traces, with failing cases turned into new tests.
- Deploying services to Kubernetes with Helm, and building backend services and tooling in Python, Go and TypeScript.

### Deliveroo

**Senior Software Engineer**
November 2024 -- October 2025

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

- Developed a Django backend integrated with Keycloak authentication, and contributed React front-end features.
- Built Docker images and deployed services to AWS ECS.

### Wayfair

**Senior Software Engineer (Contract)**
March 2022 -- October 2022

- Developed internal logistics and order-management tools, including React front-end work.
- Implemented asynchronous processing pipelines with Kafka.
- Deployed services to Kubernetes.

### Just Eat

**Senior Software Engineer**
September 2021 -- February 2022

- Automated AWS RDS infrastructure deployments.
- Improved infrastructure reliability through automation and monitoring.

### Sainsbury's

**Senior Software Engineer**
January 2020 -- August 2021

- Led the migration from monolithic systems to microservices on Kubernetes.
- Built ETL pipelines with Kafka and asynchronous Python services.

### Earlier Roles

- **Mavens of London**, Software Developer, February 2017 -- December 2019: built large-scale web-scraping systems and contributed to machine-learning and NLP projects.
- **Empello**, Junior Developer, March 2015 -- January 2017: built web-scraping infrastructure that monitored mobile advertising networks.

## Projects

### MAGDA -- Open-source DAW with built-in AI agents

Creator and principal author. GPL-3.0. Over 10,000 downloads and 250+ GitHub stars. Links: [github.com/Conceptual-Machines/magda-core](https://github.com/Conceptual-Machines/magda-core) · [magda.land](https://magda.land)

- Built a cross-platform desktop application for macOS, Windows and Linux in C++23 and JUCE. It has Catch2 test suites, and CI builds and releases it on all three platforms.
- Designed and built a native C++23 audio engine to replace Tracktion Engine. It processes events with sample accuracy and applies state changes in real time while audio plays. It hosts VST3, AU and LV2 plugins.
- Separated the engine from the UI, with module boundaries enforced at build time.
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
