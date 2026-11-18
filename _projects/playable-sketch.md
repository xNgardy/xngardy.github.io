---
title: PlayableSketch
description: A sketch-to-level authoring tool that turns hand-drawn floor plans into editable layouts and exports them for Unreal Engine.
short_description: Detects walls and doors in a hand-drawn plan, lets you correct the layout in the browser, and exports it to Unreal Engine.
category: Creative tools / Computer vision
filter: graphics
period: Ongoing
order: 1
role: Independent developer
tools: Python · PyTorch · U-Net · YOLO11n · Unreal Engine / C++
repository: https://github.com/xNgardy/PlayableSketch
image: /assets/images/playable-sketch.webp
image_alt: PlayableSketch plan editor showing detected rooms and editable geometry from a hand-drawn plan.
image_width: 1400
image_height: 840
caption: Input sketch (left) and detected room geometry from the browser workspace (right). Composite of actual project outputs from an L-shaped example.
---

## Overview

PlayableSketch is a local prototype for turning a floor-plan drawing into an editable level layout. It proposes rooms and doors, lets you correct them in a browser, and exports the reviewed design for Unreal Engine. I am developing it independently, with work ongoing on both the application and its evaluation.

A sketch is a quick way to describe a space. Turning it into a level means deciding where the walls end, which openings are doors, and how the rooms connect. I built PlayableSketch around an initial automatic interpretation followed by user correction, so the drawing does not have to be interpreted perfectly before it becomes useful.

I developed the dataset and annotations, trained and compared models, implemented room reconstruction and the browser editor, and connected the export to Unreal Engine. Alongside Python, PyTorch, and C++, I use OpenCV for image processing and Shapely for geometry operations.

## From image to editable layout

### Walls and doors

The current perception pipeline uses **U-Net for wall segmentation** and **YOLO11n for door detection**. Separating them lets me examine how each kind of error affects the reconstructed rooms.

Images are prepared at a 1024-pixel working resolution. Door detection runs on the full image and overlapping crops, then merges duplicate boxes with non-maximum suppression. The crops help retain small door marks that can lose detail when the entire drawing is resized.

### Rooms and connections

An open doorway can make two rooms look like one connected region. The pipeline temporarily closes detected door openings in the wall mask, finds the enclosed interiors, and converts them into proposed room boundaries. It then uses the door detections to connect neighboring rooms.

An L-shaped or U-shaped space stays one room if no wall or door divides it. The current representation has no separate corridor class.

The geometry stage preserves indentations and aligns neighboring boundaries where a detected door supports a connection. This needs its own checks: a roughly correct wall mask can still produce the wrong room shape or attach a door to the wrong boundary.

<figure>
  <a href="{{ '/assets/images/playable-sketch-perception.webp' | relative_url }}"><img src="{{ '/assets/images/playable-sketch-perception.webp' | relative_url }}" alt="Four stages of sketch interpretation: input drawing, predicted wall mask, room contours and door detections, and reconstructed polygons." loading="lazy" width="1800" height="400"></a>
  <figcaption>One drawing, from wall detection to proposed room boundaries.</figcaption>
</figure>

## Dataset creation and annotation

I made a core collection of **140 floor plans**: 70 drawn by hand and 70 synthetic plans created with AI assistance. I drew and annotated the hand-drawn plans myself, recording walls, openings, and room layouts.

I added 700 augmented images, split equally between the hand-drawn and synthetic sources. These simulate rotation, perspective, lighting changes, blur, noise, and capture artifacts. For geometric transformations, I transformed the annotations alongside the images and kept metadata linking each variant to its source.

The resulting 840 images come from 140 original plans. They add variation in appearance, rather than independent layouts or drawings by new people. Later experiments also used procedurally generated plans, including connected L-, U-, and S-shaped layouts; those training and evaluation sets are documented separately.

<figure>
  <a href="{{ '/assets/images/playable-sketch-dataset.webp' | relative_url }}"><img src="{{ '/assets/images/playable-sketch-dataset.webp' | relative_url }}" alt="A hand-drawn floor plan, its colored reference annotations, and perspective, rotation, lighting, and capture variants of the same drawing." loading="lazy" width="1800" height="900"></a>
  <figcaption>One drawing, its reference annotations, and four augmented views.</figcaption>
</figure>

## Model development and evaluation

I compared classical image-processing methods with U-Net, YOLO detectors, Faster R-CNN, and a Mask2Former pilot to see how wall and door errors carried through to room reconstruction. I then continued training the U-Net and YOLO11n combination with real drawings and generated layouts, selecting checkpoints and inference thresholds on validation data.

On the existing human-drawing test subset, the perception pipeline produced these results before any interactive correction:

| Measure | Result |
| --- | --- |
| Door detection F1 | 89.7% |
| Room polygon F1 | 82.4% |
| Exact room count | 7 of 12 drawings |

Door evaluation covered 14 drawings with 16 labeled doors. Room evaluation covered the 12 drawings with room references. Doors and room polygons were matched to references at an intersection-over-union threshold of 0.5.

This is a small development subset whose drawings had been examined in earlier experiments, not an unseen-writer benchmark. The scores measure perception, not success across the whole application. Getting the room count right also does not mean the boundaries or connections are correct.

Training setup and per-experiment results are documented in the project repository's `Docs` directory.

## Interactive review and authoring

The browser workspace shows the sketch beside the proposed layout. Users can move or resize rooms, add missing rooms and doors, remove incorrect suggestions, and adjust connections.

<figure>
  <a href="{{ '/assets/images/playable-sketch-editor.webp' | relative_url }}"><img src="{{ '/assets/images/playable-sketch-editor.webp' | relative_url }}" alt="PlayableSketch browser editor showing a photographed four-room floor plan beside editable room geometry and door connections." loading="lazy" width="1265" height="853"></a>
  <figcaption>The current Compare view, captured on 19 November 2026. Rooms, doors, connections, and suggested dimensions can be edited before export.</figcaption>
</figure>

Written dimensions are optional. Suggested sizes are editable design estimates, rather than measurements read from the drawing.

Export requires confirmation of a specific layout revision. Changing geometry, dimensions, or relevant settings requires confirmation again. Exported bundles keep provenance and file hashes so the accepted design can be traced through the workflow.

## Unreal Engine integration

The reviewed layout is exported as validated JSON for the Unreal Engine C++ importer. There are two export modes:

- **Geometry only** exports the reviewed rooms and doors.
- **Playable level** also requires distinct start and goal rooms and checks passage clearance for the configured player.

<figure>
  <a href="{{ '/assets/images/playable-sketch-architecture.webp' | relative_url }}"><img src="{{ '/assets/images/playable-sketch-architecture.webp' | relative_url }}" alt="Workflow from sketch detection through room geometry and user review to Unreal Engine import." loading="lazy" width="1600" height="230"></a>
  <figcaption>From sketch to Unreal Engine.</figcaption>
</figure>

The Unreal runtime supports movement through the generated environment and a route-following option. Collision and traversal checks in the engine are separate from the Python clearance checks: passing geometric preflight does not by itself establish that the player can move through the level.

<figure>
  <img src="{{ '/assets/images/playable-runtime.webp' | relative_url }}" alt="Earlier PlayableSketch Unreal runtime showing generated connected rooms, a player cube, and import and route controls." loading="lazy" width="1440" height="932">
  <figcaption>An earlier Unreal development runtime with generated rooms and route playback. It shows a previous interface and a different example from the current editor images, not gameplay validation of the latest hybrid model.</figcaption>
</figure>

I checked the current hybrid model through editing, sizing, and geometry export on L-shaped and U-shaped examples. These produced the expected four-room/three-door and two-room/one-door layouts. They are integration examples; the latest hybrid update has not been separately verified through Unreal gameplay.

## Current limits and next steps

The prototype handles single-floor, top-down drawings with explicit wall and door marks. Faint or broken walls, small missed doors, and boundary reconstruction can still cause failures.

The work has made me treat recognition, spatial structure, and playability as separate problems to test. A detected door can be attached to the wrong room, and a connected layout can still contain a passage the player cannot traverse.

Next, I want to test fresh drawings from multiple people, measure how much correction users need to make, and improve checks for room connectivity and boundary preservation.

Setup instructions, code, and evaluation notes are in the [project repository](https://github.com/xNgardy/PlayableSketch).
