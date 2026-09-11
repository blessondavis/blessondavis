# Hi, I'm Blesson 👋

I build AI agents that do real work on messy data, and I publish the code.

Most of my projects start the same way. Some job that people do by hand looks like it should be automatable. I build the smallest version that actually works, measure it honestly, and write down where it falls over.

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

## Other things I've built

| project | what it is |
| --- | --- |
| [shopping-agent](https://github.com/blessondavis/shopping-agent) | A ReAct / chain-of-tools shopping agent built with smolagents and Claude on Amazon Bedrock |
| [optimize-pytorch-models-using-awsneuronsdk](https://github.com/blessondavis/optimize-pytorch-models-using-awsneuronsdk) | Compiling a Hugging Face BERT with the AWS Neuron SDK and serving it on Inferentia through SageMaker |
| [all-about-LLMs](https://github.com/blessondavis/all-about-LLMs) | Notebooks exploring what you can build on top of foundation models |
| [Artifical-Intelligence](https://github.com/blessondavis/Artifical-Intelligence) · [Natural-Language-Processing](https://github.com/blessondavis/Natural-Language-Processing) | Where it started: ML, DL and NLP projects |

## A bit about me

- I work across the stack of an ML system: data, training, inference on real hardware, and the agent on top that decides what to run.
- I've spent a lot of time in the AWS ML ecosystem, including SageMaker, Bedrock and Inferentia.
- My current favourite problem is making agents **reliable**: evals, budgets, stop conditions, and all the other less exciting parts that decide whether an agent can run unattended.

If you're working on agents, geospatial AI, or getting models to run well in production, feel free to reach out on X at [@BlessonDavis](https://x.com/BlessonDavis).

Or clone [gis-agent](https://github.com/blessondavis/gis-agent) and point it at a city it has never seen. That's usually the fun part.
