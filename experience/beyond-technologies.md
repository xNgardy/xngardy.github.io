---
layout: experience
title: Beyond Technologies
description: A new Unreal Engine 5.5 pipeline for satellite-derived landscapes, PCG vegetation, roads, and editor tooling.
period: July–September 2026 · Ankara, Türkiye
role: Unreal Engine Developer
tools: Unreal Engine 5.5 · PCG · Python · C++ · Rasterio · NumPy · GeoReferencing
links:
  - label: Beyond Technologies website
    url: https://beyondtech.com.tr
permalink: /experience/beyond-technologies/
---

## BeyondTerrain

During this three-month internship, I developed **BeyondTerrain**, a new Unreal Engine 5.5 project and editor pipeline for preparing large-scale aerial-simulation environments from DEM, NDVI, and true-color GeoTIFF data.

I built the raster processing, editor tools, vegetation setup, roads, and materials described below. A separate building component was handled outside my work.

## Satellite data and landscape preparation

I built the raster-preparation and editor tooling with Python, Rasterio, NumPy, and Pillow. The pipeline validates coordinate reference systems, bounds, bands, and elevation data; corrects rotated raster exports; and keeps the DEM, NDVI, and true-color inputs aligned.

It produces continuous and tiled 16-bit heightmaps with shared border vertices, an Unreal-compatible 63-quad component grid, Grass/Soil/Rock weightmaps, NDVI tree-density maps, and the transforms needed to place the data correctly in Unreal. The editor menu runs the processing steps and generates area-specific import settings and guides.

Unreal's embedded Python does not include Rasterio, so I separated the editor interface from external worker scripts that run through a configured Python environment.

## PCG vegetation

I developed and debugged PCG grass and tree setups driven by Landscape data, elevation, slope, and NDVI. Road-mask sampling removes vegetation from road surfaces, while spatial noise and density filters break up uniform placement.

For large World Partition maps, I used per-proxy PCG volumes, partitioned generation, and on-demand processing rather than generating the entire map at once. The vegetation setup uses Hierarchical Instanced Static Mesh components, distance culling, disabled grass collision, and reduced shadow and lighting work. I also worked through proxy-boundary alignment, texture transforms, point density, and generation-cost checks.

## Road implementation

I implemented a road pipeline that downloads OpenStreetMap data through Overpass, clips it to the corrected raster footprint, converts it into Unreal-local coordinates, and samples terrain heights for the road graph. The processing retains road class, surface, width, and other OSM metadata for later generation steps.

The project supports several road outputs:

- **Proxy-aligned masks and decals**, with paved, unpaved, shoulder, and vegetation-exclusion channels.
- **Native Landscape Splines**, using the C++ plugin and GeoReferencing checks to paint road layers, optionally grade terrain, and paint a separate vegetation-exclusion layer.
- **Optimized proxy road meshes**, clipped to World Partition proxies with three source LODs, tessellated junctions, separate collision meshes, and Nanite disabled.

I also added validation for coordinate transforms, loaded proxy counts, road placement, and Landscape height alignment to catch shifted roads, stale actors, and discontinuities at proxy boundaries.

## Materials and graphics

I worked on Landscape materials that combine satellite color with surface weightmaps and near-camera detail. Distance blending transitions toward satellite color, while the material also supports Runtime Virtual Texture output and road-based vegetation exclusion.

This work included area-specific material instances, world-aligned texture mapping, Landscape layer setup, and diagnostic tooling for inspecting material expressions and texture parameters.
