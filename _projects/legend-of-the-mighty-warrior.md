---
title: The Legend of the Mighty Warrior
description: A branching text adventure recreated in Unity from an earlier C project.
short_description: A text adventure I first wrote in C, then rebuilt in Unity. Items and dice rolls change the routes and endings.
status: Playable HTML5 prototype.
category: Game development / Interactive fiction
filter: games
period: Prototype
minor: true
order: 7
role: Game developer
tools: Unity · C# · ScriptableObjects · TextMeshPro
repository: https://github.com/xNgardy/LOTMW_Unity
external_url: https://ngardy.itch.io/the-legend-of-the-mighty-warrior
external_label: Play on itch.io
---

## From C to Unity

I originally developed *The Legend of the Mighty Warrior* as a text-based game in C during my first year of university. I later recreated it in Unity and published a playable HTML5 prototype on itch.io.

The six-chapter fantasy story follows a would-be royal knight on a journey to defeat the Elden Dragon. Player choices lead through different events, encounters, and endings.

## Story system

I implemented the story as connected ScriptableObject story blocks. Each block contains its text, player options, links to subsequent blocks, and optional rules for items or final scenes.

The game tracks collected items and uses item requirements to control particular routes. At the final stage, the item count and a random dice roll determine which ending the player reaches, with multiple good and bad outcomes.

I used TextMeshPro for the story text and two-choice interface, and added audio feedback as the player moves through the story.
