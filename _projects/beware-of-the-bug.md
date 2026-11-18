---
title: Beware of the Bug
description: A nature-themed Minesweeper game developed from scratch in Unity.
short_description: Minesweeper with a nature theme and art I made for the game. Built in Unity with Tilemaps.
category: Game development / Puzzle
filter: games
period: Solo project
minor: true
order: 6
role: Game developer & artist
tools: Unity · C# · Tilemaps
repository: https://github.com/xNgardy/Beware-of-the-Bug
---

## The game

I built this version of Minesweeper in Unity and made the visual assets myself.

The default board uses a 16 × 16 grid with 32 mines. It includes a main menu, sound effects, restart controls, and separate win and game-over scenes.

## Implementation

- Random mine placement: Mines are distributed across the grid, with occupied cells skipped until the requested mine count is reached.
- Number generation: Each safe cell counts the mines in its eight neighboring cells.
- Flagging: Right-clicking toggles a flag on an unrevealed cell, preventing it from being opened accidentally.
- Flood fill: Opening an empty cell recursively reveals adjacent safe cells and the numbered cells at the edge of the empty region.
- Win and loss handling: Revealing a mine ends the game; revealing every non-mine cell triggers the win state and marks the remaining mines with flags.

The board is rendered with Unity Tilemaps, with separate tiles for unknown, revealed, numbered, flagged, mined, and exploded cells.
