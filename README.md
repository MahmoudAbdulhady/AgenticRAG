Self-Study Agentic RAG Project

A small experimental project I built while learning LangChain, LangGraph, RAG, Chroma Cloud, Gemini, and LangSmith.

The goal was not to build a production-ready assistant, but to understand how the individual pieces of an agentic RAG workflow fit together and how state moves through a LangGraph.

What I was experimenting with

This project explores a workflow where an AI system:

Retrieves relevant context from a Chroma Cloud vector database

Uses Google Gemini to generate an initial answer

Uses a second LLM role to evaluate / reflect on that answer

Decides whether the retrieved knowledge is enough

If needed, performs a web search

Regenerates the answer using both the retrieved context and the new web research

Workflow

flowchart TD
    A[User Question] --> B[Retrieve Documents]
    B --> C[Generate Answer - LLM #1]
    C --> D[Evaluate / Reflect - LLM #2]

    D -->|Accept| E[Final Answer]
    D -->|Needs Research| F[Web Search]

    F --> G[Regenerate Answer]
    G --> E

Main concepts explored

RAG ingestion pipeline

Load web documents

Combine parsed content

Split content into chunks

Generate embeddings

Store vectors in Chroma Cloud

Semantic retrieval

Query Chroma using the user question

Return the most relevant document chunks

LangGraph state

Pass the question, retrieved documents, answer, evaluation result, research query, and web context between nodes

Structured LLM evaluation

The evaluator returns structured fields such as:

evaluation_reason

needs_research

research_query

Conditional routing

If the answer is sufficient → finish

If more information is required → search the web and regenerate

Observability

Use LangSmith to inspect prompts, model calls, outputs, and graph behavior

Tech stack

Python

LangChain

LangGraph

LangSmith

Google Gemini

Chroma Cloud

Hugging Face embeddings

Tavily Search

Unstructured

uv

Project structure

selfstudyproject/
│
├── nodes/
│   ├── retrieve.py
│   ├── generate_answer.py
│   ├── evaluate_answer.py
│   ├── web_search.py
│   └── regenerate_answer.py
│
├── scripts/
│   ├── ingest.py
│   └── run_agent.py
│
├── chroma_store.py
├── config.py
├── embeddings.py
├── graph.py
├── ingestion.py
├── llm.py
├── routing.py
├── sources.py
└── state.py

Quick start

To run the project locally:

Install the dependencies

uv sync

Add your API keys and Chroma Cloud configuration

Create a .env file in the project root:

CHROMA_API_KEY=...
CHROMA_TENANT=...
CHROMA_DATABASE=...
CHROMA_COLLECTION=...

GOOGLE_API_KEY=...
TAVILY_API_KEY=...

Run the agent

uv run python -m selfstudyproject.scripts.run_agent

Enter your question when prompted.

Note: The repository expects the Chroma collection to already contain the documents you want to retrieve from. If you want to ingest or refresh your own sources, run the ingestion script first:

uv run python -m selfstudyproject.scripts.ingest

Why I built it

I wanted to move beyond basic RAG and understand how an agent can make a decision about the quality of its own answer.

The most interesting part for me was separating the workflow into clear responsibilities:

retrieval finds evidence

generation creates an answer

evaluation decides whether that answer is good enough

routing determines the next step

web search adds missing information

regeneration creates the final answer

This project is part of my ongoing hands-on learning in Agentic AI and AI Engineering.

Status

Experimental / learning project.

I will continue improving it as I explore better retrieval strategies, evaluation, tracing, testing, and more advanced LangGraph patterns.
