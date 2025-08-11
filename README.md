# 🌌 The A Dream  

**The A Dream** is an immersive 3D narrative-driven game built with **Unity** and powered by an AI-driven dialogue system. The player follows **Acool**, the main character, through a dynamic open-world village where every NPC responds with context-aware, lifelike conversations.  

This project integrates **transformer-based NLP models** (trained in the backend) with real-time Unity gameplay to deliver **adaptive NPC behavior** and enhance player immersion.  

---

## 🎮 Features  
- **AI-Powered NPCs** - NPCs respond contextually using a fine-tuned transformer model.  
- **Dynamic World State** - Player actions influence NPC attitudes and rumor spread.  
- **Unity 3D Environment** - Custom-built environment for an open-world village feel.  
- **Seamless Backend Integration** - Python backend with Hugging Face Transformers for real-time dialogue generation.  
- **Custom Data** - Trained on bespoke dialogue datasets matching the game’s tone and lore.  

---

## 🛠 Tech Stack  

### Frontend (Game)  
- **Unity 2022+**  
- **C# Scripting** for NPC interactions and UI  
- **Cinemachine** for camera control  

### Backend (AI & API)  
- **Python 3.10+**  
- **Hugging Face Transformers** for NLP  
- **PEFT / LoRA** (optional for model optimization)  
- **FastAPI** for serving AI responses  
- **Custom Dataset** for NPC dialogues  

---

## 📂 Project Structure  
The-A-Dream/
│
├── Backend/ # AI model training and API server
│ ├── data/ # Training & validation datasets
│ ├── saved_models/ # Trained model checkpoints
│ ├── app.py # FastAPI server
│ └── requirements.txt # Backend dependencies
│
├── UnityProject/ # Unity 3D game files
│ ├── Assets/ # Game assets
│ ├── Scripts/ # C# scripts for gameplay & AI calls
│ └── Scenes/ # Unity scenes
│
└── README.md

### Backend Setup  

cd Backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

### Unity Setup
Open Unity Hub and add the UnityProject folder.
Press Play in Unity Editor to test NPC conversations.

📊 AI Model Metrics
Evaluation Loss: 0.2944

Perplexity: 1.34

ROUGE-1 (Test): 0.1956

BLEU (Test): 0.0926

Repetition Rate: 3.97%

(Full metrics & visualizations are in the Appendix.)
