# CONTEXT_TRANSFER.md

# Heroes

*A computational portraiture framework exploring semantic relationships between sound, memory, and image.*

---

# Current Status

**Iteration 2 Complete**

Iteration 1 asked:

> How does the portrait appear?

Iteration 2 asked:

> How does the portrait disappear?

Rather than implementing a fade-out effect, Iteration 2 introduced the concept of **STATE**.

The portrait no longer disappears because an animation tells it to.

It disappears because the artwork remembers previous luminosity and that memory naturally decays over time.

This distinction is foundational.

---

# Core Philosophy

Heroes is **not** being developed as a collection of visual effects.

Instead, each iteration asks a single artistic question.

The implementation exists only to answer that question.

Effects emerge from concepts—not the other way around.

Development therefore follows:

Question

↓

Discovery

↓

Architecture

↓

Implementation

↓

Observation

↓

Commit

Every Git commit should answer one artistic question.

---

# Development Methodology

An unexpected methodology emerged during development.

Most creative coding projects evolve by adding effects.

Heroes evolves by introducing concepts.

Example:

Iteration 1

Appearance

↓

Iteration 2

Memory

↓

Iteration 3

Recognition (planned)

↓

Iteration 4

Identity (possible)

Rather than asking

"What should we add?"

we ask

"What should the artwork understand?"

---

# Architectural Principles

## Components communicate only through semantic features.

Components never depend upon each other's implementation.

Each Base COMP publishes explicit semantic outputs.

For example:

AUDIO publishes

energy

REACTION publishes

luminosity

STATE publishes

memory

Consumers know only these semantic contracts.

---

## Python owns meaning.

TouchDesigner operators perform signal processing.

Python expresses semantic interpretation.

This distinction became one of the strongest architectural discoveries.

CHOPs answer

"What is happening?"

Python answers

"What does it mean?"

---

## Hidden state is technical debt.

Anything that advances the application's logic should become visible.

Every important semantic feature should bubble upward into STATE.

STATE functions as the artwork's "table of contents."

---

## Logging is architecture.

Logging is not merely debugging.

Logs describe the internal narrative of the artwork.

Similarly, the STATE dashboard represents the artwork's current understanding of itself.

---

# Current Runtime Architecture

Project Root

```
AUDIO
PORTRAIT
REACTION
STATE
RENDER
CONFIG
LOG
UI
```

---

## AUDIO

Responsibility

Acquire live guitar input.

Exports

```
energy
```

Internal network

```
Audio Device In

↓

Analyze

↓

Filter

↓

Math

↓

Rename

↓

OUT_energy
```

---

## PORTRAIT

Responsibility

Provide portrait imagery.

Current implementation

Movie File In TOP

↓

Level TOP

↓

OUT_portrait

Configuration determines which hero image is loaded.

---

## REACTION

Responsibility

Translate raw energy into visual luminosity.

Imports

```
energy
```

Exports

```
luminosity
```

Current implementation

```
IN_energy

↓

Math

↓

Rename

↓

OUT_luminosity
```

---

## STATE

Responsibility

Represent temporal memory.

STATE does **not** process audio.

STATE accumulates experience.

Imports

```
luminosity
```

Exports

```
memory
```

Current implementation

```
IN_luminosity

↓

Lag

↓

Math

↓

Rename

↓

OUT_memory

↓

CHOP Execute DAT

↓

StateExt.Publish(...)
```

Current semantic interpretation:

Memory is yesterday's luminosity.

The Lag CHOP is simply one implementation.

Memory itself is a semantic feature.

---

## RENDER

Responsibility

Render the final portrait.

Current implementation

Brightness driven by

```
STATE.memory
```

rather than instantaneous energy.

---

## CONFIG

Configuration is externalized into

```
config.py
```

Loaded during project startup.

Configuration stored using

```
root.store("CONFIG", ...)
```

Purpose

Separate project configuration from implementation.

---

## LOG

Simple Python logger.

Each application run creates its own log file.

Logging is treated as architectural infrastructure.

---

# State Dashboard

STATE maintains a live Table DAT.

Current columns

```
Feature

Value

Source
```

Example

| Feature | Value | Source |
|----------|-------|--------|
| memory | 0.62 | STATE |

The dashboard exists so every semantic feature remains observable.

---

# Important Architectural Discovery

Semantic features are not operators.

For example

```
memory
```

is **not** a Lag CHOP.

It is a semantic concept.

Possible implementations include

- Lag CHOP
- Feedback CHOP
- Python accumulator
- GLSL buffer

The implementation may change.

The meaning should not.

---

# SCHEMA Philosophy

SCHEMA.md is **not** documentation.

It is an expressive language.

Current layers include

Portal

↓

Lexicon

↓

Gestures

↓

Idioms

↓

Traversals

↓

Composition

↓

Semantic Features

The schema intentionally separates

structure

semantics

intention

These ideas are independent.

---

# Compiler Analogy

The project increasingly resembles a compiler pipeline.

```
TouchDesigner (.toe)

↓

Introspection

↓

graph.yaml

↓

Semantic Analysis

↓

architecture.yaml

↓

Pattern Language

↓

composition.yaml
```

Each pass adds meaning without destroying previous information.

---

# Development Workflow

Each iteration begins with exactly one artistic question.

Examples

Iteration 1

How does the portrait appear?

Iteration 2

How does the portrait disappear?

Iteration 3 (planned)

Which parts awaken first?

Questions intentionally precede implementation.

---

# Design Philosophy

One of the strongest discoveries so far:

We are not building visual effects.

We are building vocabulary.

Each iteration teaches the artwork one new concept.

Appearance.

Memory.

Recognition.

Identity.

Visual behavior emerges naturally from those concepts.

---

# Long-Term Direction

The project increasingly resembles a semantic runtime rather than a TouchDesigner project.

Current semantic chain

```
energy

↓

luminosity

↓

memory
```

Future semantic features may include

```
presence

recognition

fragility

anticipation

stillness

identity

attention
```

Each should become

- observable
- logged
- published
- composable

rather than hidden inside implementation.

---

# Final Thought

The most important realization so far:

We are not trying to formalize TouchDesigner.

We are attempting to formalize a language for computational art.

TouchDesigner is simply the first medium through which that language is being discovered.

Heroes therefore serves two purposes simultaneously:

1. Create expressive computational portraits.

2. Discover a reusable semantic architecture that could eventually extend beyond TouchDesigner to systems such as Houdini, Unreal Engine Blueprints, Max/MSP, modular synthesis, or other graph-based creative environments.

That broader language—not any individual artwork—is becoming the true research project.