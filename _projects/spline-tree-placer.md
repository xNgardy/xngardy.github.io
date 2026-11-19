---
title: Spline Tree Placer
description: A Unity Editor tool with spline-following, uniform, and natural tree placement, adjustable distribution settings, and placement previews.
short_description: I built a Unity Editor tool with three tree placement strategies, adjustable distribution settings, and placement previews.
category: Procedural generation / Editor tools
filter: graphics
period: Personal project
order: 2.5
role: Tool & demo developer
tools: Unity · C# · Unity Splines · Editor scripting
repository: https://github.com/xNgardy/Spline_tree_Placer
image: /assets/images/windridge-landscape.png
image_alt: Windridge Meadow landscape with rolling green terrain and scattered stylized cedar trees.
image_width: 1733
image_height: 974
caption: Windridge Meadow, the generated demo landscape for Spline Tree Placer.
---

I built a Unity Editor tool for placing trees along splines, with controls for both structured rows and more irregular groups.

The idea was to use a spline to guide the overall layout, then adjust the distribution through placement settings. This makes it possible to shape a line of trees or a wooded area without positioning every tree individually.

I developed the tool in C# using Unity’s Splines package, with three placement modes available through a custom editor window.

## Placement Modes

The tool offers three placement strategies. These six examples show two configurations of each strategy in the Windridge Meadow demo, using the same planting guide and WindridgeCedar prefab. Select any image to inspect the scene and its settings at full size.

### Spline Placement

Follows the spline with adjustable lateral offsets and spacing variation. A larger side offset spreads the trees farther from the guide, while spacing variation breaks up a regular row.

<div class="image-pair">
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-spline-1.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-spline-1.webp' | relative_url }}" alt="Spline Placement output with 33 trees, side offset 5.1, and spacing variation 0.461, showing a loose row around the guide." loading="lazy" width="1770" height="1316"></a>
    <figcaption><strong>33 trees.</strong> Side offset: 5.1; spacing variation: 0.461. A looser row with a wider lateral spread.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-spline-2.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-spline-2.webp' | relative_url }}" alt="Spline Placement output with 100 trees, side offset 2, and spacing variation 0.3, showing a denser row close to the guide." loading="lazy" width="1828" height="1296"></a>
    <figcaption><strong>100 trees.</strong> Side offset: 2; spacing variation: 0.3. A denser row that stays closer to the spline.</figcaption>
  </figure>
</div>

### Uniform Placement

Distributes trees at regular intervals in the spline’s parameter space. Trees follow the curve’s direction with slight rotation variation. Changing the tree count changes the density along the same guide, making this mode useful for structured planting along paths or boundaries.

<div class="image-pair">
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-uniform-1.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-uniform-1.webp' | relative_url }}" alt="Uniform Placement output with 100 trees forming a dense, regular row along the spline." loading="lazy" width="1708" height="1316"></a>
    <figcaption><strong>100 trees.</strong> A dense row following the planting guide.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-uniform-2.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-uniform-2.webp' | relative_url }}" alt="Uniform Placement output with 42 trees forming a more widely spaced row along the same spline." loading="lazy" width="1810" height="1298"></a>
    <figcaption><strong>42 trees.</strong> Fewer trees leave wider gaps along the same guide.</figcaption>
  </figure>
</div>

### Natural Placement

Scatters trees around the spline using Perlin noise and clustering. Placement radius controls the spread around the guide, while minimum tree distance limits how closely trees can gather. Scale, tilt, and rotation variation help break up repetition.

<div class="image-pair">
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-natural-1.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-natural-1.webp' | relative_url }}" alt="Natural Placement output with a maximum of 100 trees, radius 15, and minimum distance 3, showing clusters around the spline; 100 trees were placed." loading="lazy" width="1800" height="1324"></a>
    <figcaption><strong>100 trees placed.</strong> Maximum: 100; radius: 15; minimum distance: 3. Clusters occupy a narrower corridor around the spline.</figcaption>
  </figure>
  <figure>
    <a href="{{ '/assets/images/spline-tree-placer-natural-2.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-natural-2.webp' | relative_url }}" alt="Natural Placement output with a maximum of 311 trees, radius 37.1, and minimum distance 4.13, showing a broader scattered distribution; 214 trees were placed." loading="lazy" width="1772" height="1322"></a>
    <figcaption><strong>214 trees placed.</strong> Maximum: 311; radius: 37.1; minimum distance: 4.13. A broader distribution with more space between trees.</figcaption>
  </figure>
</div>

Both natural-placement examples use a 70% cluster chance. The requested maximum is an upper limit: spacing checks and the placement attempt limit can result in fewer accepted trees, as shown by the second example.

## Spline and Terrain Handling

Placement starts with positions sampled from the spline. I transform these from the spline container’s local coordinates into world space so the tool works with a guide that has been moved or rotated in the scene.

The tool then casts downward to find the ground beneath each candidate position. This lets trees follow uneven terrain rather than remain at the spline’s height.

For spline-following placement, I use the curve’s tangent and up vector to calculate orientation and lateral offsets. Natural placement checks candidate positions against the spline and previously placed trees before accepting them.

<figure>
  <a href="{{ '/assets/images/windridge-spline-guide.png' | relative_url }}"><img src="{{ '/assets/images/windridge-spline-guide.png' | relative_url }}" alt="Unity Scene view of Windridge Meadow, showing a blue spline guide winding across the terrain among stylized cedar trees." loading="lazy" width="1733" height="999"></a>
  <figcaption>The planting guide in Windridge Meadow. Select the image to view it at full size.</figcaption>
</figure>

## Editor Workflow

I built a dedicated **Spline Tree Placer** window that responds to the current scene selection. It identifies the selected spline, exposes the settings for each placement mode, and accepts a tree prefab.

The window checks that a spline and prefab are available before enabling placement. Each strategy displays its own controls, a short behavior explanation, and a preview of the placement settings. **Place Trees** generates the distribution, **Clear Trees** removes it, and a status line reports how many trees were placed in the last run.

I kept the placement algorithms separate from their editor controls through a shared strategy interface. This gives each mode its own settings while keeping selection handling and placement actions in one window.

<figure class="photo-portrait">
  <a href="{{ '/assets/images/spline-tree-placer-editor.webp' | relative_url }}"><img src="{{ '/assets/images/spline-tree-placer-editor.webp' | relative_url }}" alt="Current Spline Tree Placer editor window with Meadow Planting Guide selected, Spline Placement settings for 33 trees, side offset 5.1, spacing variation 0.461, a settings preview, WindridgeCedar prefab, and Place Trees and Clear Trees buttons." loading="lazy" width="632" height="1268"></a>
  <figcaption>The current editor window with a selected spline, strategy-specific settings, placement preview, and prefab controls. Select the image to view it at full size.</figcaption>
</figure>

## Windridge Meadow Demo

The project includes **Windridge Meadow**, a fictional landscape for trying the tool. It contains rolling terrain, meadow and limestone surfaces, stylized cedar trees, and a winding planting guide.

The landscape is generated locally from deterministic code. Its terrain heights use layered noise, its surface textures are generated in code, and the cedar shapes are assembled from Unity primitives.

An editor command bakes the generated landscape into saved assets, including terrain data, textures, materials, and a reusable cedar prefab.

The demo provides a simple setting for comparing placement modes: following a curve closely, building a regular row, or spreading trees into looser groups.
