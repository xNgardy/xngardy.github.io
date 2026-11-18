---
layout: experience
title: TaleWorlds Entertainment
description: "A multi-stage treasure-hunt quest mod for Bannerlord, followed by debugging and optimization on an unannounced Unity project."
period: August–September 2025 · Ankara, Türkiye
role: Software Developer Intern
tools: C# · Bannerlord Editor · Unity · Plastic SCM · dnSpy
links:
  - label: TaleWorlds website
    url: https://www.taleworlds.com
  - label: "Mount & Blade II: Bannerlord on Steam"
    url: https://store.steampowered.com/app/261550/Mount_Blade_II_Bannerlord/
image: /assets/images/bannerlord.jpg
image_alt: "Mount & Blade II: Bannerlord promotional artwork."
image_url: https://store.steampowered.com/app/261550/Mount_Blade_II_Bannerlord/
image_width: 616
image_height: 353
caption: "Mount & Blade II: Bannerlord artwork from its Steam page."
permalink: /experience/taleworlds-entertainment/
---

## Treasure hunts in Bannerlord

I worked with the Design and Mission teams on a treasure-hunt quest mod for *Mount & Blade II: Bannerlord*. Another intern and I implemented the mod in C#, using TaleWorlds' proprietary engine and existing campaign and quest systems, with guidance from senior developers.

Each hunt had three stages: Early, Middle, and Final. The player followed a sequence of clues between settlements to reach the treasure. The challenge was to generate different routes while keeping the clues, quest state, and settlement tracking consistent.

## Clue generation and quest progression

I created a pool of clue templates organized by theme and stage. Each clue carried a description, difficulty points, and any required items. When a quest was generated, the system selected clues within the allowed themes and difficulty range and assigned them to settlements.

Clue difficulty determined a minimum and maximum distance from the player's position. The system picked a settlement within that range and excluded locations already used by active quests. Each selected clue was copied from its template so that assigning it a location would not change the source data.

The quest manager prevented duplicate quests, assembled the three stages, and calculated the overall difficulty. As the player entered a target settlement, the quest advanced to the next clue and updated the tracked location. Completing the final stage awarded gold scaled to the quest's difficulty.

## Disguises and campaign events

I also implemented a regional disguise mechanic. Some clues required the player to equip culturally appropriate items before progressing at a settlement. If the equipment check failed, the quest stayed on the current stage and notified the player of the missing disguise.

The mod responded to campaign events such as settlement entry, level-ups, and battles to start or advance quests. I handled event-listener cleanup when a quest ended and tested generation, clue progression, disguise checks, and event handling in the Bannerlord Editor.

To find ways to connect these features to the existing game, I read the design team's requirements and examined community mods with dnSpy. We used Plastic SCM for source control and discussed the work in code reviews, pair-programming sessions, and weekly meetings.

## Debugging an unannounced Unity project

In the latter part of the internship, I moved to an unannounced Unity project, where I fixed dozens of C# bugs and worked on performance issues. I worked with QA and developers to reproduce reported problems, trace their causes across interacting scripts, and check the fixes for regressions.

I used breakpoints, stack traces, console logging, and Unity's Profiler to investigate behavior and runtime costs. My work included state-machine-based timed sequences and fixed-timestep timing without coroutines, as well as changes to performance-critical code.

The project is covered by an NDA, so I keep its gameplay, feature details, and code out of this portfolio.

<figure class="photo-portrait">
  <img src="{{ '/assets/images/taleworlds-last-day.jpg' | relative_url }}" alt="Pelinsu Kaleli standing in front of the TaleWorlds logo" width="1235" height="1600" loading="lazy">
  <figcaption>My last day at TaleWorlds, September 2025.</figcaption>
</figure>
