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
---

## Detailed captions within a memory budget

For the **OBSS AI Image Captioning Challenge on Kaggle**, I fine-tuned a **Qwen2.5-VL-7B** multimodal transformer to generate detailed image descriptions while working within memory constraints.

I used LoRA to fine-tune the model and 4-bit quantization to reduce memory use, then iterated on training and inference strategies. My submission placed **2nd among 280 participants**.

The [public notebook](https://github.com/xNgardy/OBSS_AI_Image_Captioning_Challenge) contains the training and inference code.
