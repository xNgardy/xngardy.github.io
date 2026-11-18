---
title: PlayableSketch
description: A sketch-to-level authoring tool that turns hand-drawn floor plans into editable layouts and exports them for Unreal Engine.
short_description: From hand-drawn floor plans to editable layouts and playable Unreal Engine spaces. A hybrid vision pipeline keeps the creator in the loop.
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

## Drawing as a level-authoring interface

PlayableSketch explores a simple question: **can a hand-drawn plan become a useful starting point for an interactive level?**

The current system detects rooms and doors, turns the result into editable geometry, and lets the user review and adjust the layout in the browser before exporting it for Unreal Engine. It is an ongoing personal project at the intersection of computer vision, geometry processing, and game-development tools.

## How it works

- **U-Net** predicts a pixel-level wall mask.
- **YOLO11n** detects door markers.
- Image processing temporarily closes detected doors and identifies connected interior regions as rooms.
- A geometry stage converts those regions into editable room boundaries.
- The browser workspace supports moving and resizing rooms, editing doors and connections, and correcting dimensions.
- The reviewed layout is exported for Unreal Engine as geometry or as a playable level with a start and goal.

Written dimensions are optional, and suggested sizes are editable estimates rather than measurements read from the drawing. Detection can fail on faint or broken lines, so user review is part of the workflow.

## From an inferred plan to a playable space

The playable export checks passages for player clearance. In the Unreal runtime, the accepted layout can be explored using movement controls or a route-following option. The packaged application is built separately from the repository.

<figure>
  <img src="{{ '/assets/images/playable-runtime.webp' | relative_url }}" alt="PlayableSketch Unreal Engine runtime showing generated connected rooms and controls for importing and playing the accepted layout." loading="lazy" width="1440" height="932">
  <figcaption>Unreal runtime from a development example. This screenshot documents an earlier runtime interface; the project continues to evolve.</figcaption>
</figure>

## Current scope

The current pipeline handles a single floor drawn from above, with explicit wall and door marks. It does not infer an unrestricted architectural model or guarantee a correct result for every drawing. L-shaped and U-shaped examples have been used to check plan editing and geometry export; those example checks are not a dataset-wide accuracy estimate.

The latest setup instructions and implementation details are maintained in the [project repository](https://github.com/xNgardy/PlayableSketch).
