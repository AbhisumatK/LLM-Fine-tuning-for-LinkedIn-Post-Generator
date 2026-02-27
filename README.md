# LinkedIn Post Generator (Few-Shot + LLM)

This project is an AI-powered LinkedIn post generation tool built using Few-Shot Learning and Large Language Models. It uses **Example-driven RAG** to create content in my own style of writing. 

The system learns writing patterns from my real [LinkedIn](https://www.linkedin.com/in/abhisumat-kundu/) posts and uses them as contextual examples to produce new content that matches my tone, structure, and intent.

Deployed App - https://linkedin-llm-abhisumat.streamlit.app/

My LinkedIn - https://www.linkedin.com/in/abhisumat-kundu/

---

## Overview

The application works in three major stages:

1. Data Preprocessing
   Raw LinkedIn posts are enriched using an LLM to extract:

   * Line count
   * Topic tags

   These are then standardized using tag unification to improve consistency for training and retrieval.

2. Few-Shot Learning Engine
   The system retrieves previously written posts matching:

   * Topic
   * Length category (Short / Medium / Long)

   These examples are injected into the prompt to guide generation.

3. Post Generation
   The LLM generates a new LinkedIn post using:

   * Selected topic
   * Desired length
   * Writing style inferred from examples

---

## Features

* Topic-based post generation
* Length control (Short / Medium / Long)
* Style transfer using Few-Shot prompting
* Automatic metadata extraction from raw posts
* Tag normalization for better semantic grouping
* Streamlit UI for interactive use

---

## Project Structure

```
├── main.py                 # Streamlit frontend
├── post_gen.py             # Prompt construction + post generation
├── few_shot_learning.py    # Example retrieval engine
├── preprocess.py           # Metadata extraction + tag unification
├── llm_helper.py           # LLM initialization
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
├── .streamlit/
│   └── secrets.toml        # API key storage
```

---

## How It Works

### Step 1: Preprocess Dataset

Run:

```
python preprocess.py
```

This will:

* Extract tags and line counts using an LLM
* Merge similar tags into unified categories
* Create `processed_posts.json`

---

### Step 2: Launch App

Run:

```
streamlit run main.py
```

Select:

* Topic
* Post Length

Click **Generate** to create a new LinkedIn-style post.

---

## Authentication Setup

Create:

```
.streamlit/secrets.toml
```

Add:

```
GROQ_API_KEY = "your_api_key_here"
```

This is required for LLM access.

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq LLM API
* Few-Shot Prompting
* JSON-based dataset

---

## Example Use Case

Input:

* Topic: Robotics
* Length: Medium

Output:

A concise, professional LinkedIn post aligned with robotics trends and tone, modeled after real-world examples.

---

## Future Improvements

* Fine-tuned domain models
* Tone control (Formal / Storytelling / Thought Leadership)
* Scheduled posting support
* Multi-platform content generation

---

## Goal

The long-term goal is to build intelligent content systems that reduce writing friction while preserving authenticity and personal voice in professional communication.

---
