---
title: Image Captioning with Qwen2.5-VL
description: Parameter-efficient fine-tuning for detailed image captioning under memory constraints.
short_description: Fine-tuned Qwen2.5-VL-7B with LoRA and 4-bit quantization. Placed second among 280 participants in the OBSS AI Image Captioning Challenge.
category: Machine learning / Vision-language
filter: ml
period: Competition project
order: 4
role: Participant & model developer
tools: Python · PyTorch · Qwen2.5-VL-7B · LoRA
repository: https://github.com/xNgardy/OBSS_AI_Image_Captioning_Challenge
visual: captioning-visual
visual_label: Image → Text
visual_subtitle: Vision-language models
---

## Detailed captions within a memory budget

For the **OBSS AI Image Captioning Challenge on Kaggle**, I fine-tuned a **Qwen2.5-VL-7B** multimodal transformer to generate detailed image descriptions while working within memory constraints.

I used **LoRA** for parameter-efficient adaptation and **4-bit quantization**, and iterated on training and inference strategies. My submission placed **2nd among 280 participants**.

## What I worked on

- Adapting a pretrained vision-language model to the captioning task.
- Training with parameter-efficient fine-tuning.
- Managing model memory requirements through quantization.
- Evaluating and refining inference strategies for the competition.

The [public notebook and project documentation](https://github.com/xNgardy/OBSS_AI_Image_Captioning_Challenge) provide the implementation context.
