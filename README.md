# Builder Guide — The Agent Toolkit Hack Day

**Event:** The Agent Toolkit — OpenClaw Hack Day
**Date:** March 25, 2026
**Audience:** Builders shipping OpenClaw skills during the event

---

## The Goal

Build an OpenClaw demo that solves a real problem and uses at least two sponsor tools in a meaningful way. The more sponsor tool consumption, the better — and the more likely you'll win a prize.

This is **not** a prompt contest and it is **not** a landing-page demo. The bar is:

- A real use case
- A working OpenClaw integration
- A clear reason your project should exist
- A believable path from hack-day prototype to something people would actually install

If your project could be described as *"we wrapped a model around a vague idea,"* the scope is probably wrong.

---

## What A Strong Project Looks Like

The best projects in the room will usually do four things well:

### 1. Solve a concrete problem

Start with a user, workflow, or pain point:

- "Developers need a safer way to install and inspect OpenClaw skills"
- "Teams need an agent that can pull live web data and turn it into action"
- "Users need a secure way to let agents act on their behalf"
- "OpenClaw needs better memory, routing, observability, or retrieval"

Good projects feel inevitable in hindsight.

### 2. Use sponsor tools as part of the core architecture

Do **not** bolt a sponsor logo onto the last mile of your demo.

A strong integration means the sponsor tool changes what your project can do:

- It unlocks data you could not easily get otherwise
- It makes the workflow faster, safer, or more reliable
- It enables a capability that would otherwise be too hard to build in one day
- It gives your OpenClaw skill a real production shape

### 3. Show a complete loop

The best demos show an actual system loop:

1. Input arrives
2. Your skill retrieves context or data
3. Your skill reasons or decides
4. Your skill takes action or produces a useful output
5. The result is visible and understandable

### 4. Make the project easy to explain

If someone cannot understand the value in 20 seconds, the project is not demo-ready yet.

Use this sentence:

> *We built **[thing]** for **[user]** so they can **[outcome]**, and we used **[sponsor tool(s)]** to make **[key capability]** possible.*

---

## How To Pick A Good Project In This Room

Pick something that fits at least one of these patterns:

- A skill that gives OpenClaw access to a valuable new system
- A skill that makes OpenClaw safer, faster, or more production-ready
- A workflow that combines live data, reasoning, and action
- A tool that another developer would realistically install from ClawHub

**Good scope for one day:**

- One user
- One sharp problem
- One primary workflow
- One or two sponsor tools used deeply

**Bad scope for one day:**

- A general AI assistant for everyone
- A big platform with no finished workflow
- Five shallow integrations with no core story
- Anything that depends on too much setup before you can show value

---

## Sponsor Directions

Exact keys, credits, SDKs, and docs will come from the sponsor teams. Use the notes below as directional prompts for what each tool can help you enable in an OpenClaw project.

### Contextual

Think about Contextual if your project needs better retrieval, grounded answers, document understanding, or reasoning over a large body of technical knowledge.

**Good uses:**

- Build a skill that ingests technical docs, support logs, specs, or policy files and lets OpenClaw answer with real context
- Build a domain-specific research or troubleshooting assistant
- Build a skill that turns messy documentation into structured context for downstream agent actions

**Strong demo angle:**

- Show the raw knowledge source
- Show how your skill retrieves the right context
- Show the action or answer that becomes possible because the agent is grounded in real material

### Redis

Think about Redis if your project needs memory, caching, queues, event streams, real-time state, vector search, or fast coordination between multiple components.

**Good uses:**

- Agent memory and retrieval
- Multi-agent task queues
- Semantic cache for repeated requests
- Live event stream for observability or workflow status
- Fast state layer for long-running or multi-step skills

**Strong demo angle:**

- Show the system state changing in real time
- Show lower latency, better coordination, or durable memory
- Show why your workflow would be brittle without Redis

### Civic

Think about Civic if your project needs authentication, user identity, permissions, approvals, or secure user-scoped actions.

**Good uses:**

- Build an OpenClaw skill that acts on behalf of a signed-in user
- Add identity or auth gates before sensitive tool use
- Create an approval flow for agent actions that should not run anonymously
- Add secure account linking or wallet-backed access to a workflow

**Strong demo angle:**

- Show who the user is
- Show what the agent is allowed to do for that user
- Show how Civic makes the workflow safer or more trustworthy

### Apify

Think about Apify if your project needs web data, browser automation, structured extraction, or repeatable workflows over public websites.

**Good uses:**

- Monitor the web for live information and feed it into OpenClaw
- Extract structured data from sites that matter to your workflow
- Build a research or automation skill that depends on browser actions
- Turn messy web pages into clean inputs for downstream reasoning

**Strong demo angle:**

- Show the live source on the web
- Show the extraction or automation step
- Show what OpenClaw can do now that it has current, usable data

### FriendliAI

Think about FriendliAI if your project needs fast inference, model serving, or a responsive model layer for a serious agent workflow.

**Good uses:**

- Route specific OpenClaw tasks to a fast model endpoint
- Build a skill that depends on low-latency generation or classification
- Prototype a multi-model workflow where speed and throughput actually matter
- Use model-serving performance to make an interaction feel real-time

**Strong demo angle:**

- Show the model-powered step inside the workflow
- Show why latency, throughput, or responsiveness matters for the user experience
- Show what becomes possible because the model layer is reliable enough to sit inside a working tool

---

## Good Multi-Sponsor Patterns

You do not need to use every sponsor. You should use **at least two** well.

**Strong combinations:**

| Combination | Pattern |
|---|---|
| **Apify + Contextual** | Pull live web data, structure it, ground answers or actions in it |
| **Redis + FriendliAI** | Build a fast, stateful, responsive agent workflow |
| **Civic + Apify** | Let authenticated users trigger high-trust web workflows safely |
| **Contextual + Redis** | Build memory-rich or retrieval-heavy skills that stay fast |
| **Civic + Redis** | Add user-scoped state and safe approvals to agent actions |

---

## A Good First 60 Minutes

If you are not sure where to start, do this:

### First 15 minutes

- Pick one user and one problem
- Choose one primary sponsor tool
- Write the one-sentence project pitch in HackerSquad

### Next 15 minutes

- Define the demo moment you want by the end of the day
- Decide what must be real and what can stay mocked
- Sketch the simplest end-to-end workflow

### Next 30 minutes

- Get one sponsor integration working
- Get one OpenClaw skill entry point working
- Prove the core loop before polishing anything

> If the core loop does not work by midday, **reduce scope.**

---

## Submission Requirements

Your project is not fully shipped until it is submitted on HackerSquad.

Every team should plan to do two things on **March 25, 2026** before live demo selection:

1. **Submit the project** on HackerSquad by **3:00 PM PT** before dinner begins
2. **Submit a video demo** of the project on HackerSquad by **4:00 PM PT** so judges can review projects

At **5:00 PM PT**, projects will be selected and the top demos will be chosen to present live.

Treat this as part of the build, not as cleanup at the very end.

### What To Submit On HackerSquad

Make your submission easy for judges, sponsors, and future builders to understand.

Include:

- Team name
- Team members
- Project title
- A short summary of what you built
- The problem you are solving
- Which sponsor tools you used
- Repo link, project link, or artifact link if available
- A demo-ready project description that matches what you will show live

### Video Demo Requirement

Every team must also submit a short video demo through HackerSquad.

This video matters because it preserves the project after the live demo block ends. It should make it possible for someone who was not in the room to understand what you built and why it matters.

HackerSquad makes this possible directly, so **do not skip it** even if you are already presenting live on stage.

Your video should clearly show:

- What you built
- What you are solving for
- How you used the tools
- What the tools enabled you to do

### Deadline Summary

| Time | Milestone |
|---|---|
| **3:00 PM PT** | Project submission due on HackerSquad |
| **4:00 PM PT** | Video demo submission due on HackerSquad |
| **5:00 PM PT** | Projects reviewed and top live demos selected |

---

## What To Ask Sponsor Teams

When talking to sponsors, do not ask for a generic product tour. Ask for the shortest path to a working build.

**Useful questions:**

- "What is the fastest thing we can ship with your tool today?"
- "What API or SDK should we start with?"
- "What kind of project tends to look especially strong with your product?"
- "What can your tool do that would be hard for us to recreate ourselves?"
- "What is the best demo-worthy workflow we can complete by tonight?"

---

## What We Want To Hear In Demos

Your demo should clearly answer these four questions:

### 1. What did you build?

Name the skill or workflow plainly.

- **Bad:** "We built an AI platform for the future of work"
- **Better:** "We built an OpenClaw skill that monitors target websites, extracts changes, and summarizes them into an action queue"

### 2. What problem are you solving?

Be specific about the user and the pain.

- **Bad:** "Knowledge work is broken"
- **Better:** "Developers waste time manually checking scattered docs and dashboards before making routine operational decisions"

### 3. How did you use the tools?

Do not just name-drop sponsors. Explain where each tool sits in the system.

- "Apify pulls the live source data"
- "Contextual grounds the agent on the right technical material"
- "Redis stores workflow state and retrieval context"
- "Civic handles user-scoped auth before the skill acts"
- "FriendliAI powers the low-latency model step"

### 4. What did the tools enable you to do?

This is the most important part. Tell us what became possible because of the integration.

- "Using Redis let us turn a stateless demo into a multi-step workflow with durable memory"
- "Using Civic let the agent act for a real user without turning the workflow into a security mess"
- "Using Apify let us work with live web data instead of fake sample data"
- "Using Contextual let the agent answer from technical material instead of hallucinating"
- "Using FriendliAI made the interaction fast enough to feel like a real product"

---

## Before You Call It Done

Before the event ends, make sure all of this is true:

- [ ] Your OpenClaw skill or workflow actually runs
- [ ] Your sponsor integration is visible and understandable
- [ ] Your live demo is ready
- [ ] Your project was submitted on HackerSquad by 3:00 PM PT
- [ ] Your video demo was submitted on HackerSquad by 4:00 PM PT

> If it is not on HackerSquad, it is not fully shipped yet.

---

## Final Build Heuristics

- Prefer a **finished narrow workflow** over a broad unfinished platform
- Prefer **real data** over canned screenshots
- Prefer **one strong sponsor integration** over several shallow ones
- Prefer **visible system behavior** over hidden architecture claims
- Prefer **"this works today"** over "this could be huge later"

> If you are deciding between making the project broader or making the demo clearer, **make the demo clearer.**
