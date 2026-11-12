# Context Engineering for Claude Code

## Course Details

| Course detail | Value |
| --- | --- |
| Duration | 4 hours per cohort |
| Audience | Developers working in AI-assisted coding environments |
| Skill level | Intermediate |
| Format | Instructor-led course with demonstrations, a quiz, and two breakout labs |
| Primary tool | Claude Code |

## Delivery Model

| | Day 1 |
| --- | --- |
| **Morning Cohort** | Session 1 (AM) |
| **Afternoon Cohort** | Session 1 (PM, repeated) |

The instructor delivers the same four-hour session to both cohorts. The afternoon session repeats the morning instruction, demonstrations, quiz, labs, and outcomes without content changes.

## Course Overview

Participants learn how context engineering extends prompt design across the full information environment of an AI coding assistant. They examine how relevant project context is loaded or retrieved during a Claude Code session, including project instructions, scoped rules, auto memory, Skills, file-search tools, and MCP tool discovery. They practice managing long tasks with focused compaction, durable notes, fresh-session handoffs, and isolated subagents. The session also distinguishes RAG for external knowledge sources from direct project-file retrieval and introduces repeatable evaluation based on task correctness, instruction adherence, and context or usage cost.

## Main Topics Covered

- From prompt engineering to context engineering
- How Claude Code manages context at runtime
- Maintaining coherence across long tasks
- Context quality, evaluation, and iterative optimization

## Learning Outcomes

By the end of the session, participants will be able to:

- Explain how context engineering extends prompt design across instructions, files, tools, and memory.
- Describe how Claude Code combines startup context with information retrieved on demand.
- Configure concise project guidance and select appropriate retrieval, memory, and delegation strategies for a task.
- Manage long-running work with compaction, durable handoffs, and isolated subagents while checking for lost context.
- Evaluate context changes using task correctness, instruction adherence, and context or usage cost.

## Project Context and Tools

Participants use Claude Code, Git, and a multi-module sample repository with independent starter directories for each lab. The repository contains realistic application code, unconfigured build scripts, and test suites. Course materials provide reference prompt rules, task handoff templates, compaction runbooks, and context audit checklists. Each breakout lab starts from a verified standalone snapshot, allowing participants to complete each exercise without depending on outputs from earlier blocks.

## Prerequisites

Participants should have:

- Familiarity with core LLM concepts and prompt engineering terminology
- Basic experience using Claude Code or a comparable AI coding assistant
- Working knowledge of terminal commands, Git version control, and project navigation

## Session 1: Context Engineering for Claude Code

### 1. From Prompt Engineering to Context Engineering

#### Concept & Demo

The instructor explains how context engineering extends prompt design to the information available throughout an agentic workflow. Unlike a single-turn prompt, Claude Code can read files, run commands, inspect results, and take further actions; each step may add useful or distracting information to the working context. The demonstration compares a broad, noisy context with a focused set of relevant instructions and tool results. Participants discuss how larger or less relevant contexts can reduce recall and focus, without treating hallucination as an inevitable or uniquely caused result of context growth.

### 2. How Claude Code Manages Context

#### Concept & Demo

The instructor walks through the Claude Code context lifecycle, distinguishing instructions and other context available at session start from information loaded as work proceeds. The core demonstration uses `CLAUDE.md` or `AGENTS.md` project guidance, path-scoped rules in `.claude/rules/`, `/context`, and targeted file-search tools. It also shows how to structure task requests and keep tool output relevant. Auto memory, Skills, and MCP tool discovery, which can defer full tool schemas until needed, are introduced as additional mechanisms rather than explored in depth. The instructor explains that project instructions guide model behavior while permissions and hooks enforce tool-use constraints.

#### Breakout Lab 2.1: Structuring Project Context with CLAUDE.md

Participants inspect a multi-component codebase with ambiguous project guidance and conventions that should apply only to selected files. They create or refine a concise project-level `CLAUDE.md` and add a path-scoped rule for one component. They use Claude Code's file-search tools to retrieve relevant files and inspect `/context` to see what guidance is available.

Lab outcome: A tested project guidance configuration with verification commands, evidence that the relevant instructions are available for a repeatable task, and a before-and-after record of task results and context use. Token reduction is measured when observed, not assumed.

### 3. Maintaining Coherence Across Long Tasks

#### Concept & Demo

The instructor demonstrates strategies for extended development workflows. The class compares automatic compaction with a focused `/compact` request and discusses the limits of summaries: details may be lost even though some instructions and memory are re-injected or reloaded. The instructor shows how durable task notes and a fresh-session handoff provide another way to carry state forward. Subagents are introduced as isolated workers whose intermediate tool activity stays in their own context and whose findings are summarized for the parent. The class also compares direct project-file retrieval with RAG when relevant information lives in a large external corpus.

#### Breakout Lab 3.1: Context Compaction and State Handoffs

Participants inherit an ongoing debugging session with a long history of investigation and tool output. They use a focused compaction request, inspect the resulting summary, and write a concise handoff with the goal, current state, constraints, relevant files, failed approaches, and next verification steps. They continue in a fresh session and check the handoff against the repository and test results rather than assuming all prior context was preserved.

Lab outcome: A durable task handoff and evidence that a fresh session can resume the task, re-check relevant files, and run the required verification. Participants note any missing or incorrect state they discover.

### 4. Context Quality and Iteration

#### Concept & Demo

The instructor presents a repeatable way to evaluate context changes. Participants identify hazards such as verbose tool results, stale assumptions, redundant rules, context dilution, or instructions that conflict. The instructor compares the same task before and after a context change, using acceptance tests and instruction adherence as primary quality checks and recording context or usage cost and turns as supporting measures. The class discusses why fewer tokens or fewer turns alone do not prove that a result is better.

### Session Breakdown Table

| Topic | Duration |
| --- | ---: |
| Welcome, Course Intro & Setup | 15 min |
| 1. From Prompt Engineering to Context Engineering: Concept & Demo | 30 min |
| 2. How Claude Code Manages Context: Concept & Demo | 30 min |
| Lab 2.1: Structuring Project Context with CLAUDE.md | 25 min |
| Bio Break | 15 min |
| 3. Maintaining Coherence Across Long Tasks: Concept & Demo | 30 min |
| Lab 3.1: Context Compaction and State Handoffs | 25 min |
| Kahoot Quiz 1 | 15 min |
| Bio Break | 10 min |
| Mandatory Course Survey | 5 min |
| 4. Context Quality and Iteration: Concept & Demo | 25 min |
| Course Wrap-up | 15 min |
| **Total** | **4 hours** |

## Documentation Currency

Reviewed against Anthropic documentation on 2026-11-05. Claude Code changes over time; the instructor should verify command names and feature behavior against the current documentation before each delivery. This outline avoids pinning a Claude Code version unless a lab depends on a specific release.

- [Claude Code memory and project instructions](https://code.claude.com/docs/en/memory)
- [Claude Code context window](https://code.claude.com/docs/en/context-window)
- [Claude Code features overview](https://code.claude.com/docs/en/features-overview)
- [Claude Code permissions](https://code.claude.com/docs/en/permissions)
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
