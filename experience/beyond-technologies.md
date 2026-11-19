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

## Satellite-Based Environment Pipeline

During my three-month experience at Beyond Technologies, I worked with Alper Keskin on an Unreal Engine 5.5 project for building large-scale environments from satellite data.

My work covered raster processing, editor tools, PCG vegetation, roads, and Landscape materials. Alper developed the building component.

A large part of my work involved keeping everything aligned: terrain elevation, satellite imagery, vegetation masks, and road coordinates all needed to describe the same area once imported into Unreal.

## Satellite Data and Landscape Preparation

I built a Python processing pipeline using Rasterio, NumPy, and Pillow to prepare three source datasets: a digital elevation model (DEM), a vegetation index (NDVI), and true-color satellite imagery.

The pipeline checks coordinate reference systems, geographic bounds, raster bands, and elevation values before processing. For rotated exports with black corner padding, it detects the footprint correction and applies the same rotation and crop to all three inputs.

It generates:

- Continuous and tiled 16-bit heightmaps, with shared border vertices between tiles.
- A valid Unreal Landscape grid using 63-quad components, selected close to the DEM’s native resolution.
- Grass, Soil, and Rock weightmaps.
- NDVI-based tree-density maps and satellite reference textures.
- Dataset-specific Landscape scales, placement transforms, and import instructions.

I connected these steps to a BeyondTerrain editor menu so processing could be launched from Unreal. Since Unreal’s embedded Python does not include Rasterio, the menu runs external worker scripts through a configured Python environment.

The tool prepares the data and settings; Landscape import, material assignment, and PCG setup remain explicit editor steps.

## PCG Vegetation

I developed and debugged grass and tree setups driven by Landscape data, elevation, slope, and NDVI. Road masks exclude vegetation from road surfaces, while spatial noise, clustering, and density filters help break up uniform placement.

For large World Partition maps, I used per-proxy PCG volumes with partitioned, on-demand generation. Each volume uses the matching road-mask slice and world-space transform to keep vegetation exclusion aligned across proxy boundaries.

The setup uses Hierarchical Instanced Static Mesh components, distance culling, disabled grass collision, and reduced shadow and lighting work. I also checked candidate-point counts, final instance counts, and generation cost while adjusting density and placement.

## Road Implementation

I implemented a road pipeline that downloads OpenStreetMap data through Overpass, clips it to the corrected raster footprint, and converts it into Unreal-local coordinates. Cached downloads can be reprocessed without repeating the network request.

One of the trickier parts was matching geographic coordinates to the Landscape actually placed in Unreal. This required handling the corrected raster frame, Unreal’s Y-axis mapping, and the Landscape’s world dimensions. Road heights are sampled from the processed heightmap so they follow the imported terrain.

The shared road graph handles connected junctions and retains OSM information such as road class, surface, width, lanes, and bridge or tunnel tags.

I implemented three output options:

- **Proxy-aligned masks and decals:** RGBA masks containing paved roads, unpaved roads, shoulders, and vegetation exclusion.
- **Native Landscape Splines:** A C++ editor path for painting road layers, optionally grading terrain, and painting a separate vegetation-exclusion layer, with GeoReferencing validation.
- **Optimized proxy road meshes:** Road ribbons and tessellated junctions clipped to World Partition proxy bounds, with three source LODs, separate collision meshes, and Nanite disabled.

Bridge and tunnel records are kept separate from terrain-snapped roads because they need their own vertical profiles.

I also added checks for incorrect transforms, unloaded proxies, stale generated actors, and differences between road heights and Landscape collision.

## Materials and Graphics

I worked on Landscape materials that combine satellite color with Grass, Soil, and Rock weightmaps and near-camera surface detail. Distance blending shifts the appearance toward satellite imagery farther from the camera.

This included world-aligned texture mapping, Runtime Virtual Texture output, Landscape layer setup, and road-mask sampling for vegetation exclusion. I also added area-specific material instances and diagnostic tools for inspecting material expressions and texture parameters.

The resulting workflow brought raster preparation, road processing, and validation into the editor, with generated settings and guides for each area.
