# ARTIFEX - AI Image Generator

A modern web application that generates AI images from text descriptions using the Pollinations.ai API.

![ARTIFEX Screenshot](https://image.pollinations.ai/prompt/ARTIFEX%20AI%20Image%20Generator%20logo%20purple%20gradient%20modern?width=800&height=400&nologo=true)

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [How to Run](#how-to-run)
6. [How It Works](#how-it-works)
7. [API Endpoints](#api-endpoints)
8. [Frontend Explanation](#frontend-explanation)
9. [Code Walkthrough](#code-walkthrough)
10. [Team Members](#team-members)

---

## 🎯 Project Overview

**ARTIFEX** is an AI-powered image generation web application. Users enter a text description (called a "prompt"), and the application uses artificial intelligence to create a unique image based on that description.

### Example:
- **Input Prompt:** "A majestic dragon flying over a crystal castle at sunset"
- **Output:** An AI-generated image matching that description

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Text-to-Image Generation** | Convert text descriptions into images |
| **Multiple AI Models** | Choose from Flux, Flux Realism, Flux Anime, Turbo |
| **Size Options** | Square, Landscape, Portrait, Social Media sizes |
| **HD Quality Toggle** | Automatically enhances prompts for better quality |
| **Random Prompts** | Get creative inspiration with pre-written prompts |
| **Prompt Enhancement** | Add artistic keywords to improve results |
| **Negative Prompts** | Specify what to avoid in the image |
| **Favorites System** | Save and reuse your best prompts |
| **Image History** | View your last 12 generated images |
| **Download Images** | Save generated images to your device |
| **Fullscreen View** | View images in full resolution |

---

## 🛠️ Technology Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Programming language |
| **Flask** | Web framework for handling HTTP requests |
| **Pollinations.ai API** | Free AI image generation service |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Page structure |
| **CSS3** | Styling and animations |
| **JavaScript** | Interactive functionality |
| **LocalStorage** | Storing favorites and history |

---

## 📁 Project Structure

```
munavarImageGen/
│
├── app.py                 # Backend - Flask server (MAIN FILE)
├── requirements.txt       # Python dependencies
├── README.md              # This documentation file
│
├── templates/
│   └── index.html         # Frontend - User interface
│
└── static/
    └── style.css          # Styling - Visual design
```

### File Descriptions:

| File | Description |
|------|-------------|
| `app.py` | The Python backend server. Handles API requests and communicates with Pollinations.ai |
| `index.html` | The HTML page users see. Contains the form, buttons, and JavaScript logic |
| `style.css` | CSS styles for the colorful, modern UI design |
| `requirements.txt` | Lists Python packages needed (Flask) |

---

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher installed
- pip (Python package manager)

### Step-by-Step:

```bash
# 1. Navigate to project folder
cd munavarImageGen

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py

# 4. Open browser and go to:
# http://localhost:5000
```

---

## 🔄 How It Works

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER'S BROWSER                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   index.html + style.css                 │   │
│  │  • Text input for prompt                                 │   │
│  │  • Model/Size/Style dropdowns                            │   │
│  │  • Generate button                                       │   │
│  │  • Image display area                                    │   │
│  └─────────────────────┬───────────────────────────────────┘   │
└────────────────────────│────────────────────────────────────────┘
                         │
                         │ HTTP Request (POST /generate)
                         │ {prompt, model, size, negative}
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FLASK SERVER (app.py)                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1. Receive prompt from frontend                        │   │
│  │  2. Validate input                                       │   │
│  │  3. URL-encode the prompt                                │   │
│  │  4. Construct Pollinations.ai URL                        │   │
│  │  5. Return image URL to frontend                         │   │
│  └─────────────────────┬───────────────────────────────────┘   │
└────────────────────────│────────────────────────────────────────┘
                         │
                         │ Returns: {image_url: "https://..."}
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     POLLINATIONS.AI API                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  • Receives the prompt via URL                           │   │
│  │  • Uses AI (Flux model) to generate image                │   │
│  │  • Returns the generated image                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Flow:

1. **User enters prompt** → Types "A dragon flying over mountains"
2. **Clicks Generate** → JavaScript sends POST request to Flask server
3. **Flask processes** → Encodes prompt, adds parameters, creates API URL
4. **Returns URL** → Flask sends back the Pollinations.ai image URL
5. **Image loads** → Browser loads image from Pollinations.ai
6. **Display** → Image appears on the page

---

## 🔌 API Endpoints

Our Flask server provides these endpoints:

### 1. GET `/` - Home Page
```
Purpose: Serves the main HTML page
Returns: index.html
```

### 2. POST `/generate` - Generate Image
```
Purpose: Generate an AI image from a prompt
Input (JSON):
  {
    "prompt": "A dragon flying",
    "negative": "blurry",
    "width": 1024,
    "height": 1024,
    "model": "flux"
  }
Output (JSON):
  {
    "success": true,
    "image_url": "https://image.pollinations.ai/prompt/...",
    "prompt": "A dragon flying",
    "model": "flux"
  }
```

### 3. GET `/random-prompt` - Get Random Prompt
```
Purpose: Returns a random creative prompt
Output (JSON):
  {
    "prompt": "A mystical forest with glowing mushrooms..."
  }
```

### 4. POST `/enhance` - Enhance Prompt
```
Purpose: Adds quality keywords to a prompt
Input (JSON):
  {
    "prompt": "A cat"
  }
Output (JSON):
  {
    "success": true,
    "enhanced_prompt": "A cat, highly detailed, cinematic lighting, 8K"
  }
```

---

## 🎨 Frontend Explanation

### HTML Structure (index.html)

```
┌────────────────────────────────────────┐
│             HEADER                      │
│  • ARTIFEX logo                         │
│  • Tagline                              │
├────────────────────────────────────────┤
│           GENERATOR CARD                │
│  ┌─────────────────────────────────┐   │
│  │ Prompt Input                    │   │
│  │ [Save] [Favorites] [Random]     │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │ Negative Prompt (optional)      │   │
│  └─────────────────────────────────┘   │
│  ┌──────────┬──────────┬──────────┐   │
│  │  Model   │   Size   │  Style   │   │
│  └──────────┴──────────┴──────────┘   │
│  [HD Quality Toggle]                    │
│  [====== GENERATE IMAGE ======]        │
├────────────────────────────────────────┤
│           RESULT SECTION                │
│  ┌─────────────────────────────────┐   │
│  │     Generated Image              │   │
│  │     [View] [Download] [New]      │   │
│  └─────────────────────────────────┘   │
├────────────────────────────────────────┤
│           HISTORY SECTION               │
│  [img] [img] [img] [img] [img]         │
└────────────────────────────────────────┘
```

### JavaScript Functions:

| Function | Purpose |
|----------|---------|
| `generateImage()` | Sends prompt to backend, displays result |
| `getRandomPrompt()` | Fetches a random prompt idea |
| `enhancePrompt()` | Adds quality keywords to prompt |
| `savePromptToFavorites()` | Saves current prompt to localStorage |
| `loadFavorites()` | Displays saved prompts |
| `saveToHistory()` | Saves generated images to history |
| `loadHistory()` | Displays generation history |
| `downloadImage()` | Downloads the generated image |
| `openFullscreen()` | Opens image in fullscreen modal |

---

## 📖 Code Walkthrough

### Key Concepts Explained:

#### 1. Flask Routes
```python
@app.route('/generate', methods=['POST'])
def generate_image():
    # This decorator tells Flask:
    # "When someone sends a POST request to /generate, run this function"
```

#### 2. JSON Communication
```python
# Frontend sends JSON data
data = request.get_json()  # Python receives it

# Backend sends JSON response
return jsonify({'image_url': url})  # Frontend receives it
```

#### 3. URL Encoding
```python
# Spaces and special characters must be encoded for URLs
# "A cat & dog" → "A%20cat%20%26%20dog"
encoded = urllib.parse.quote("A cat & dog")
```

#### 4. Pollinations.ai API
```python
# The API URL structure:
# https://image.pollinations.ai/prompt/{YOUR_PROMPT}?width=1024&height=1024&model=flux
```

#### 5. LocalStorage (Frontend)
```javascript
// Save data to browser
localStorage.setItem('favorites', JSON.stringify(data));

// Retrieve data from browser
const data = JSON.parse(localStorage.getItem('favorites'));
```

---

## 👥 Team Members

| Name | Role |
|------|------|
| [Member 1 Name] | [Role - e.g., Backend Developer] |
| [Member 2 Name] | [Role - e.g., Frontend Developer] |
| [Member 3 Name] | [Role - e.g., UI Designer] |
| [Member 4 Name] | [Role - e.g., Documentation] |

---

## 📚 Presentation Tips

### Key Points to Highlight:

1. **Problem Statement**: Creating images manually requires artistic skills
2. **Solution**: AI can generate images from text descriptions
3. **Technology**: Flask + Pollinations.ai API + HTML/CSS/JS
4. **Demo**: Show live generation of an image
5. **Future Scope**: Add more models, user accounts, image editing

### Questions You Might Be Asked:

1. **Q: How does the AI generate images?**
   - A: We use Pollinations.ai which runs FLUX AI model, trained on millions of images

2. **Q: Why Flask?**
   - A: Flask is lightweight, easy to learn, and perfect for small web applications

3. **Q: Is this free?**
   - A: Yes, Pollinations.ai provides free API access

4. **Q: What are negative prompts?**
   - A: They tell the AI what to AVOID in the image (blurry, distorted, etc.)

---

## 📄 License

This project is created for educational purposes.

---

*Created with ❤️ for ARTIFEX AI Image Generator*
