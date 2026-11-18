---
layout: experience
title: Fdn SOFT
description: Bullet Run, a Wild West-themed mobile runner with alternating tumbleweed and bullet controls, built in Unity and C#.
period: July–August 2024 · Ankara, Türkiye
role: Game Developer Intern
tools: Unity · C# · Rider · Bitbucket · SourceTree
links:
  - label: Fdn SOFT website
    url: https://www.fdnsoft.com
permalink: /experience/fdn-soft/
---

## Bullet Run

During my internship at Fdn SOFT, I developed *Bullet Run* for the company's Hamak Games label. It was a Wild West-themed mobile game inspired by *Geometry Dash*, intended to bring players to the company's main game, *Wild West Outlaws Redemption*.

The player avoids obstacles as a rolling tumbleweed, then passes through a portal and becomes a bullet. Portals appear every 30 seconds, alternating between the two forms and their different controls. I built the gameplay in Unity and C#, working with an assigned mentor and discussing progress in daily meetings.

## Movement and collision

I first prototyped both square and circular player shapes. The square performed a full flip when jumping, but rotating its collider caused problems when landing on raised platforms. I separated the visual object from the physics object so the artwork could rotate while the collider stayed aligned. The circular version used continuous rotation to make it look like a rolling tumbleweed.

Bullet mode used tap-to-rise controls: tapping the screen pushed the bullet upward, while releasing it let the bullet fall. I added a spinning visual effect and made ground contact end the run.

## Scrolling world and background

The player stayed in place horizontally while the platforms moved underneath it. I arranged repeating platform segments and reset them at an off-screen trigger, creating a continuous path without extending the level indefinitely.

I also made the cloud, desert, and sky backgrounds and gave them different scrolling speeds for a parallax effect. Like the ground, the background layers reset off-screen to keep the scene moving throughout the run.

## Obstacles and mode changes

I designed seven obstacle prefabs for tumbleweed mode using platforms and spikes. A spawner selected one every three seconds, with a check to prevent the same obstacle from appearing twice in a row. Touching a spike or hitting the side of a platform ended the game. An off-screen cleanup trigger removed obstacles after they had passed the player.

Each mode had its own obstacle set. When a portal was due, the obstacle spawner briefly paused to make room for it. Passing through the portal changed the player's form and switched the spawner to the matching obstacles. The two modes repeated for as long as the player survived.

## Interface and development workflow

I added a Play button and a survival-based score that started at zero and increased once per second after the run began.

I wrote the scripts in Rider on macOS and used Bitbucket and SourceTree for version control. Daily Scrum meetings and feedback from my mentor helped me track progress and resolve implementation questions. The game was developed for a planned Google Play release; this page describes the version I worked on during the internship.
