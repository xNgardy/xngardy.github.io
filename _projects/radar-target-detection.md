---
title: Radar Target Detection
description: An Unreal Engine C++ simulation for detecting, classifying, and tracking moving targets.
short_description: A directional radar sweep with moving targets, classification, threat evaluation, tracking states, and visual detection feedback.
category: Real-time simulation
filter: graphics
period: Personal project
order: 3
role: Developer
tools: Unreal Engine 5 · C++
repository: https://github.com/xNgardy/Radar_Target_Detection_UE5
diagram: /assets/images/radar.svg
image_alt: Schematic of a directional radar sweep, with friendly, hostile, and unknown targets around the radar origin.
image_width: 1280
image_height: 720
caption: Directional detection schematic illustrating the project’s logic; this is a diagram, not a screenshot of the application.
---

## The radar sweep

I built a radar-style scanner in Unreal Engine using C++. A directional sweep detects moving actors and displays their classification and tracking state.

## Features

- Moving target actors and directional sweep detection.
- Target classification and tracking states.
- Threat evaluation based on target type and distance.
- Hostile warning audio, detection messages, and debug visualization.

The code is available in the [repository](https://github.com/xNgardy/Radar_Target_Detection_UE5).
