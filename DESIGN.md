# Design

Heroes is built around one principle:

Separate implementation from artistic intention.

The project is intentionally layered.

--- 

## Design Law 1

Information should become progressively more meaningful as it travels through the system.

It should never become less observable.

Every transformation should remain inspectable.

State is not hidden.

State is surfaced.

# Layer 1

## Signals

TouchDesigner operators manipulate signals.

Examples

waveform

RMS

spectrum

centroid

transients

---

# Layer 2

## Semantic Features

Signals are interpreted into perceptual qualities.

Examples

energy

brightness

density

fragility

motion

memory

silence

---

# Layer 3

## Idioms

Semantic features create recurring visual behaviors.

Examples

breathing

sparkle

erosion

emergence

dissolution

pulse

---

# Layer 4

## Composition

Each iteration answers exactly one artistic question.

Iteration 1

How does the portrait appear?

Iteration 2

How does it disappear?

Iteration 3

Which parts awaken first?

...

---

# Components expose contracts.

AUDIO exports energy.

REACTION consumes energy.

REACTION exports luminosity.

RENDER consumes luminosity.

Components communicate through semantic interfaces rather than implementation details.

---

# Configuration

Configuration is declarative.

The configuration layer describes artistic choices.

The implementation layer interprets those choices.

---

# Version Control Philosophy

The .toe is the executable artifact.

Python, YAML, Markdown and TOX files are the architectural artifacts.

Git commits answer artistic questions rather than implementation milestones.