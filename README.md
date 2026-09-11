# Hi, I'm Blesson 👋

I build AI agents that do real work on messy data, and I publish the code.

By day I build agentic systems for enterprises: multi-agent pipelines, knowledge graphs and MCP servers that run in production. On my own time I pick a job that people still do by hand, build the smallest version that actually works, measure it honestly, and write down where it falls over.

Right now that job is **tracing road networks off satellite imagery.**

<p align="center">
  <a href="https://github.com/blessondavis/gis-agent">
    <img src="https://raw.githubusercontent.com/blessondavis/gis-agent/main/docs/assets/hero.jpg" alt="gis-agent: road centrelines traced by the agent over Boston Back Bay" width="100%">
  </a>
</p>

**Lately, I've been working on**

- **[gis-agent](https://github.com/blessondavis/gis-agent)**: an LLM agent that drives a segmentation pipeline (SAM 3 or a trained U-Net, plus headless QGIS) through 23 MCP tools. It scores its own output and re-runs the areas it got wrong, and it gives you back a road network as GeoJSON.
- **Agent harnesses**: plan-first mode, a stop gate the agent can't talk its way past, rewind that restores files as well as chat, and task rules enforced in code rather than in the prompt
- **Judging output without labels**: vision-model critics, network topology and the model's own confidence, each tested against ground truth before I trust it. (Topology ranked the candidates backwards. The confidence-based judge picked the right one every time.)
- **Domain shift**: a road model trained on one US state and tested on six continents. Out of the box it found 21% of the roads in unseen cities. Ten minutes of fine-tuning took that to 54%.
- **Humans in the loop**: an in-map editor so a person can finish the last stretch, with edits that survive every re-run of the model

Everything is built to be cloned, run and pulled apart. The READMEs include the numbers, including the bad ones.

## What I build at work

I'm a **Senior Data Scientist at [Minfy Technologies](https://www.minfytech.com/)**, where I've spent the last four years putting AI systems into production on AWS, GCP and Azure. A few of them:

- **Agentic legacy modernization**: a platform for migrating 140+ legacy applications across 500+ repositories (COBOL → Java, old JDK → new). I built an AST-driven code-to-knowledge-graph pipeline and a custom Neptune MCP server so the agents can reason over the code. Choosing the graph store by benchmark cut query latency by 45%, and the agent skills cut manual code-comprehension work by 60%.
- **Knowledge graphs for operational resilience**: LLMs extract entities and relationships from business-impact documents into a continuously updated graph (FastAPI, Dapr, Bedrock). A LangGraph agent on top of it grades live simulation responses, which cut assessment turnaround by 85%. We benchmarked Neo4j, Memgraph and FalkorDB, and FalkorDB was 3× faster.
- **Multi-agent complaint resolution**: agents built with Google ADK that triage, route and quality-check customer-complaint emails through Outlook MCP servers. They handle thousands of emails a month, with 70% less manual effort.
- **Clinical documentation**: real-time transcription that drafts SOAP notes, referral letters and summaries, with a doctor in the loop, cutting documentation workload by 80%
- **Generative virtual try-on**: fine-tuned IDM-VTON and SDXL inpainting for full-body try-on, served on auto-scaling AWS infrastructure

## A bit about me

- 🎓 Postgraduate in **AI and Data Science** from Plaksha University (in partnership with UC Berkeley), after an undergraduate degree in Mechanical Engineering from IIIT Chennai
- 🛰️ GIS isn't new to me. Before Minfy I built geospatial ML at an agritech startup in Berlin, finding sites to grow avocados and olives from multi-terabyte GIS and weather data.
- ☁️ AWS Certified in **Machine Learning** (Specialty), **Data Analytics** (Specialty) and **Solutions Architecture** (Associate)
- 🧰 Tools I reach for: Python, PyTorch, LangGraph, Google ADK, MCP, Bedrock, Vertex AI, FastAPI, Kubernetes, and whichever graph database wins the benchmark
- 🔧 My current favourite problem is making agents **reliable**: evals, budgets, stop conditions, and all the other less exciting parts that decide whether an agent can run unattended.

## Other things on my GitHub

| project | what it is |
| --- | --- |
| [shopping-agent](https://github.com/blessondavis/shopping-agent) | A ReAct / chain-of-tools shopping agent built with smolagents and Claude on Amazon Bedrock |
| [optimize-pytorch-models-using-awsneuronsdk](https://github.com/blessondavis/optimize-pytorch-models-using-awsneuronsdk) | Compiling a Hugging Face BERT with the AWS Neuron SDK and serving it on Inferentia through SageMaker |
| [all-about-LLMs](https://github.com/blessondavis/all-about-LLMs) | Notebooks exploring what you can build on top of foundation models |
| [Artifical-Intelligence](https://github.com/blessondavis/Artifical-Intelligence) · [Natural-Language-Processing](https://github.com/blessondavis/Natural-Language-Processing) | Where it started: ML, DL and NLP projects |

If you're working on agents, knowledge graphs or geospatial AI, feel free to reach out on X at [@BlessonDavis](https://x.com/BlessonDavis).

Or clone [gis-agent](https://github.com/blessondavis/gis-agent) and point it at a city it has never seen. That's usually the fun part.
