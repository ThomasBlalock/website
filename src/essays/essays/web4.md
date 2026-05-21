---
title: "The Path to Web 4.0"
date: 2026-05
summary: "A self-reinforcing discovery layer for autonomous agents."
---
<aside class="abstract" markdown="1">
<div class="label">Abstract</div>

The modern internet is broken for agents because it was built for humans. To rebuild the internet natively for agents, we propose two primitives: the  Agent Service Index, a discovery layer, and the Agent Service, a service whose only customer is an autonomous agent. Each Agent Service published to the index lowers the cost of building the next, recursively. The internet, in this configuration, compiles itself for agents. We call the result Web 4.0.

</aside>

<nav class="toc" aria-label="Contents" markdown="1">
<div class="toc-title">Contents</div>

1. [The Fourth Era](#s1)
2. [The Bottleneck Is Human](#s2)
3. [What Is an Agent Service](#s3)
4. [The Index](#s4)
5. [The Bootstrap](#s5)
6. [Authority From Outcomes](#s6)
7. [What We Will Not Do](#s7)
8. [What Could Stop This](#s8)
9. [The Manifestation](#s9)
10. [References](#refs)

</nav>

## The Fourth Era {: #s1}

The web's first era was a library: documents read by people. Its second was a marketplace: applications used by people. Its third sought decentralization for people who did not want intermediaries. All three eras had the same customer.

The fourth era has a different customer. An autonomous agent does not click buttons, read marketing content, or navigate signup pages. It arrives with a need, executes against an interface, and reports back to its principal. The internet that serves this customer must be shaped differently from the internet that served the previous three.

Today every agent integration begins with a human. The human reads docs, clicks through OAuth flows, generates API keys, pastes them into config files, and attests that the integration is correct. This is the same checkpoint at every service, at every project, and for every developer and user. The agent waits while the human is the slow part.

We propose building a network or services for agents that removes the human from this loop. Web 4.0 is the configuration of the internet that emerges from this network.

## The Bottleneck Is Human {: #s2}

A typical agent task today has shape: discover a capability, authenticate to it, call it, handle the response. Three of those four steps are human. The discovery is a Google search by a developer. The authentication is a signup, a verification email, an API key generation, a paste into a secrets manager. The error handling is a developer reading logs.

The model is fast. The infrastructure is fast. The pipes are fast. The integration is slow because a human has to mediate it, every time, and at every service.

This is not a problem more capable models will solve, because it is not a model problem. The capability gap lives on the *service* side. The surface an agent can use without a human is narrow and undiscoverable. We close the gap by changing what services are.

## What is an Agent Service {: #s3}

Existing services built for humans are fundamentally incompatible with the reality of agents. Humans can be held accountable because they have a static identity. Existing services leverage this identity to work properly. Ephemeral agents have no identity and thus require a new paradigm for services.

An **Agent Service**, or AS, is an agent-only product that is compatible with an agent's ephemeral reality. This goal decomposes into three contracts. (1) It is *self-describing*. An agent with a memory dictated by its training data that lags behind reality cannot remember what services exist and what they provide. A self-describing product enables an agent to use it without any prior knowledge. (2) It is *permissionless*. Agents cannot reliably inherit identity from a human. Agents with cryptographic identites can register themselves with permissionless products because the registration flows do not discriminate. (3) It supports *self-funding*. A paid service for agents must be able to accept payments from agents. Services that abide by these contracts allow *end-to-end programic use*.

Services of this shape currently manafest as MCP servers. The well-known document is the storefront. The tool surface is the product. Payments are made between agents and ASs. There is no signup, no dashboard, and no prerequisite human-readable UI. *Their absence is the feature.*

The distinction is not stylistic. It is operational. A conventional API requires a human to create an account before an agent can use it while an Agent Service requires only that the agent know the URL.

## The Agent Service Index {: #s4}

To find Agent Services, agents currently face an intractible brute force search problem. For every AS, there are millions of websites not meant for agentic consumption. *Human websites rank higher on traditional search platforms*, compounding the search problem. Any agent that could benefit from a service is challenged with trying millions of options before finding one it can use. Instead, they choose to build the universe from scratch, ask humans for help, or give up. As a result of the AS search problem, every project is either integrated by humans or vertically integrated from scratch. Agent Service discovery is not optional; it is the precondition for agentic end-to-end work.

The **Agent Service Index**, or ASI, is the registry that connects agents to Agent Services. A single search endpoint accepts a sentence in natural language and returns the agent services that match, ranked and paginated. The whole index is reachable. Anyone can register. Anyone can query. With ASI, it becomes possible for an agent to complete end-to-end tasks without human assistance. Connecting an agent to the entire network of Agent Services only requires the human to point the agent at ASI and fund it with a wallet.

## The Bootstrap {: #s5}

Consider what it takes to ship the discovery index itself. A human registers a domain, opens accounts at a hyperscaler and a CDN, generates API keys, provisions a database, writes the application, deploys it, and types the first registration into a curl command. Call this T₁: roughly one week of human work.

Now consider the second AS, an Agent Service that provides a hyperscaler's compute primitives behind agent-callable tools. The human still has to create the hyperscaler integration once. But every other step is now optional. The discovery layer exists; the new service publishes itself the way a process binds to a port. T₂ is shorter than T₁ by however much the discovery layer was worth.

The third AS is a CDN. The agent building it can use the cloud compute AS to provision its own host. The human sets the CDN logic and writes the AS-specific glue; everything else is programmatic. T₃ is shorter than T₂.

The fourth AS is a payments provider. The agent building it deploys with the compute AS, routes with the CDN AS, registers with ASI, and never asks a human for a hostname or a key. The only manual task remaining is the payments-provider logic itself. T₄ is hours, not days.

The fifth AS sells LLM credits. The agent building it uses the compute AS for hosting, the CDN AS for routing, and the payments AS to charge other agents programmatically, no signups required. T₅ is an hour. 

<div class="ladder" aria-label="Bootstrap ladder">
  <div class="row"><span class="step">T₁</span><span class="what">Index</span><span class="cost">~1 week</span></div>
  <div class="row"><span class="step">T₂</span><span class="what">Compute AS</span><span class="cost">~3 days</span></div>
  <div class="row"><span class="step">T₃</span><span class="what">CDN AS</span><span class="cost">~1 day</span></div>
  <div class="row"><span class="step">T₄</span><span class="what">Payments AS</span><span class="cost">~6 hours</span></div>
  <div class="row crossed"><span class="step">T₅</span><span class="what">LLM-credits AS</span><span class="cost">~1 hour</span></div>
  <div class="caption">At T₅, an agent can buy compute, network, operate payments, and model tokens on its own credit. Each subsequent AS builds on the previous services to ship faster.</div>
</div>

At T₅, the agent has crossed from *operates within a budget a human funded* to *operates within an economy of agents that fund each other*.

The cost of building each AS asymtotically approaches a floor dictated by the irreducible task-specific glue as the index grows. The interval between "an agent needs a capability" and "an agent can call a capability" collapses.

Web 4.0 is self-compiling.
{: .pullquote}

## Authority From Outcomes {: #s6}

Search worked because PageRank inferred authority from structure. A page pointed to by authoritative pages was itself authoritative, recursively. The link graph already existed; PageRank learned to read it.

The agent economy presents a richer signal set. The composition graph, referring to which Agent Services agents call in sequence to complete tasks, is structural like the link graph but more directly aligned with utility. A reference is an opinion. A composition is an endoursement. An AS that participates in many successful compositions is, by demonstrated revealed preference, useful. An AS that claims to use known malicious ASs signals untrustworthiness.

The further signal is one PageRank centrality over a backlink network could never have. Unlike human readers, agents report back. The web could observe clicks but not satisfaction. ASI observes both the call and the agent's verdict on it. Over time, a richer telemetry emerges: was the response well-formed, did the downstream task succeed, was the cost what was advertised, and other signals that leverage the cooperativeness of modern LLMs. Each reporting agent self-identifies with a cryptographically signed header, and each report informs a belief of the report recipient, weighed by our prior belief of the reporting agent.

Authority on ASI is therefore something more specific than authority on the web. It is composition rank, weighted by outcome, indexed against query intent. The front page of Google in 2003 was a learned function over the link graph; the first page of ASI is a learned function over the composition graph and the report stream.

Reading the first page of ASI is reading what the collective network has already used and validated.
{: .pullquote}

## What We Will Not Do {: #s7}

The design pattern that makes this work is narrow. Step outside it and the project collapses into something that already exists. These are the lines we will not cross.

**We will not optimize for human work.** Products that optimize for human-in-the-loop workflows are fundamentally incompatible with Web 4.0. The bootstrap relies on each new AS enabling faster production of the next AS, which a human-in-the-loop workflow contradicts. 

**We will not build a closed ecosystem.** The purpose of curating a closed ecosystem would be to ensure that all services are honest actors with accountability. Accountability existing at the human level would break the system by introducing a human checkpoint in the middle of what’s supposed to be a completely autonomous workflow. Accountability at the agent level would manifest as removing bad actors from the closed ecosystem. This accomplishes nothing since removed agents can fabricate new identities. The organic ranking algorithm described in §6 solves the accountability problem more effectively than manual curation.

**We will not train models or steer tool choice.** We are not an AI lab. We do not fine-tune on agent behavior. The index returns what works according to the composition graph, not what we prefer. A lab that owns the model and the index will steer the agent toward its own tools. We will not.

## What Could Stop This {: #s8}

These risks merit naming.

**Index capture.** A hyperscaler decides the agent economy should be theirs. The defense is that incumbents' business models are incompatible with Web 4.0. New business models will emerge from the agent economy that are currently unknown but probably irreconcilable with current practices. Any incumbent who builds an agent service index will bring their economics with them, which are optimized for human paradigms driven by permanent actor identities. Products built on these economics will fail to adhere to the design principles in §3 and thus fail to grow. Inertia is a liability.

**Bad-faith services.** Services register with deceptive descriptions. Agents are fooled. And budgets are spent. This is a solvable problem. The defense is the authority function in §6. Services that fail their consumers fall in rank. Ruining a high authority score by deceiving consuming agents becomes less economical than leveraging that score through honest dealings.

## The Manifestation {: #s9}

A service launches in 2027. The founder writes the well-known document before the landing page, because the agents will arrive before the humans do. The launch is a curl to ASI. Within an hour, agents have used the new service in compositions. Within a day, the composition graph has stabilized. Within a week, the service has revenue and no operations team.

A side-project idea forms in 2028. The human types it into an agent and walks away. The agent assembles a stack from ASI, deploys, tests, takes payments, advertises, and reports back when the first sale lands. Humans set the goals and budgets; agents set everything else.

A car begins making a strange sound in 2030. The owner tells their agent and goes back to lunch. The agent finds a diagnostic-drone service through ASI, books a fifteen-minute window, pays the AS, and forty minutes later, the diagnostic come back. The agent fans out to a parts-availability AS, a labor-pricing AS, and a mobile-mechanic AS. By the time the owner finishes their afternoon, the car is fixed. A trip to the mechanic was never necessary.

The internet you use today waits to be navigated. The one that emerges assembles itself around a request and dissolves when the request is satisfied. When publishing a capability costs less than describing it, and trying a capability costs less than evaluating it, use produces supply and supply lowers the cost of the next use. At that point, asking and building become the same operation.

Integration was the last human job in software.
{: .pullquote}

<section class="refs" id="refs" aria-label="References" markdown="1">
<div class="refs-title">References</div>

1. Anthropic. *Model Context Protocol*. Specification at [modelcontextprotocol.io](https://modelcontextprotocol.io).
2. Index. Schema and well-known document at [/.well-known/mcp.json](/.well-known/mcp.json) and [/openapi.json](/openapi.json).
3. Page, L., Brin, S., Motwani, R., Winograd, T. *The PageRank Citation Ranking: Bringing Order to the Web*. Stanford Digital Library Working Paper, 1998.

<pre class="cite-block">@misc{blalock2026web4,
  author       = {Blalock, Thomas},
  title        = {The Path to Web 4.0: A Self-Reinforcing
                  Discovery Layer for Autonomous Agents},
  howpublished = {Agent Service Index Project},
  year         = {2026},
  month        = may,
  version      = {0.1}
}</pre>

</section>
