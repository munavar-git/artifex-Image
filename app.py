"""
================================================================================
ARTIFEX - AI Image Generator
================================================================================
A Flask-based web application that generates AI images using the Pollinations.ai API.

HOW IT WORKS:
1. User enters a text prompt describing the image they want
2. Our Flask backend receives the prompt and constructs an API URL
3. The Pollinations.ai API generates the image based on the prompt
4. The generated image URL is sent back to the frontend for display

TECHNOLOGIES USED:
- Flask: Python web framework for creating the backend server
- Pollinations.ai: Free AI image generation API
- HTML/CSS/JavaScript: Frontend for user interface

TEAM MEMBERS: [Add your team member names here]
================================================================================
"""

# ============================================================================
# IMPORTS - External libraries we need for the application
# ============================================================================
from flask import Flask, render_template, request, jsonify
# Flask: The main web framework - handles HTTP requests and responses
# render_template: Renders HTML templates (our index.html page)
# request: Access data sent from the frontend (like the prompt text)
# jsonify: Converts Python dictionaries to JSON for API responses

import urllib.parse
# urllib.parse: Encodes text for use in URLs (handles special characters)

import random
# random: Used to generate random numbers and select random items from lists

# ============================================================================
# FLASK APP INITIALIZATION
# ============================================================================
app = Flask(__name__)
# Creates the Flask application instance
# __name__ tells Flask where to find templates and static files

# ============================================================================
# DATA: RANDOM PROMPTS FOR INSPIRATION
# ============================================================================
# These are pre-written creative prompts that users can use for inspiration
# When user clicks "Random" button, one of these prompts is selected
RANDOM_PROMPTS = [
    "A mystical forest with glowing mushrooms and fireflies at twilight",
    "An astronaut riding a horse on Mars with Earth in the background",
    "A steampunk airship floating above Victorian London at sunset",
    "A majestic phoenix rising from golden flames in a dark cave",
    "An underwater city with bioluminescent architecture and mermaids",
    "A cyberpunk street market in Tokyo with neon signs and rain",
    "A dragon made of clouds soaring through a sunset sky",
    "A magical library with floating books and spiral staircases",
    "A samurai standing in a field of cherry blossoms during a storm",
    "A crystal palace on top of a frozen mountain under northern lights",
    "A cozy coffee shop interior on a rainy evening with warm lighting",
    "A giant robot standing in a field of sunflowers at golden hour",
    "An ancient temple hidden in a misty jungle with vines and waterfalls",
    "A witch's cottage in an enchanted forest with glowing windows",
    "A futuristic spaceship interior with holographic displays",
    "A medieval castle on a cliff overlooking a stormy sea",
    "A serene Japanese garden with a koi pond and autumn leaves",
    "A post-apocalyptic city being reclaimed by nature and wildlife",
    "A cosmic whale swimming through a galaxy of stars and nebulas",
    "A fairy village inside a hollow tree with tiny lanterns",
    "A Viking longship sailing through icy waters under aurora borealis",
    "A desert oasis at night with a caravan and starry sky",
    "A massive tree city with bridges connecting giant branches",
    "A retro diner in space with aliens as customers",
    "A magical portal opening in an ancient stone circle",
    "A bioluminescent beach with glowing waves at midnight",
    "A clockwork city with gears and brass machinery everywhere",
    "A phoenix feather falling into a still pond creating ripples of fire",
    "A wizard's tower on a floating island above the clouds",
    "A neon-lit arcade from the 1980s with vintage games",
]

# ============================================================================
# DATA: ENHANCEMENT KEYWORDS
# ============================================================================
# These keywords are added to prompts to improve image quality
# When user clicks "Enhance" button, some of these are randomly added
ENHANCEMENT_KEYWORDS = [
    "highly detailed",           # Adds more detail to the image
    "intricate details",         # Complex, intricate elements
    "professional photography",  # Photo-realistic quality
    "cinematic lighting",        # Movie-like lighting effects
    "volumetric lighting",       # 3D light rays effect
    "ray tracing",              # Realistic light reflections
    "8K resolution",            # Very high quality
    "masterpiece",              # High artistic quality
    "award-winning",            # Professional quality
    "stunning",                 # Visually impressive
    "atmospheric",              # Mood and atmosphere
    "moody",                    # Emotional lighting
    "dramatic lighting",        # Strong light contrasts
    "photorealistic",           # Looks like a real photo
    "hyperrealistic",           # Extremely realistic
    "octane render",            # 3D rendering style
    "unreal engine 5",          # Game engine quality
    "artstation",               # Professional art style
    "trending on artstation",   # Popular art style
    "concept art",              # Professional concept art style
    "matte painting"            # Cinematic background art
]


# ============================================================================
# ROUTE 1: HOME PAGE
# ============================================================================
@app.route('/')
def index():
    """
    FUNCTION: Serve the main page
    
    This is the home route - when users visit http://localhost:5000/
    Flask renders and returns the index.html template
    
    DECORATORS EXPLAINED:
    - @app.route('/') means this function handles requests to the root URL
    
    RETURNS:
    - The rendered HTML page (index.html) that contains our UI
    """
    return render_template('index.html')


# ============================================================================
# ROUTE 2: GENERATE IMAGE (Main Feature)
# ============================================================================
@app.route('/generate', methods=['POST'])
def generate_image():
    """
    FUNCTION: Generate image using Pollinations.ai API
    
    This is the CORE function of our application. It:
    1. Receives the user's prompt from the frontend
    2. Constructs the Pollinations.ai API URL with all parameters
    3. Returns the image URL to the frontend
    
    DECORATORS EXPLAINED:
    - @app.route('/generate', methods=['POST']) 
      This handles POST requests to /generate endpoint
    
    API PARAMETERS:
    - prompt: The text description of the image to generate
    - negative: Things to avoid in the image
    - width: Image width in pixels
    - height: Image height in pixels  
    - model: AI model to use (flux, turbo, etc.)
    
    RETURNS:
    - JSON with image_url on success
    - JSON with error message on failure
    """
    try:
        # ========== STEP 1: Get data from frontend ==========
        # request.get_json() parses the JSON data sent from JavaScript
        data = request.get_json()
        
        # Extract individual parameters with default values
        prompt = data.get('prompt', '')           # The main image description
        negative = data.get('negative', '')       # Things to avoid
        width = data.get('width', 1024)          # Image width (default 1024px)
        height = data.get('height', 1024)        # Image height (default 1024px)
        model = data.get('model', 'flux')        # AI model (default is 'flux')
        
        # ========== STEP 2: Validate input ==========
        # Check if user entered a prompt
        if not prompt:
            return jsonify({'error': 'Please enter a prompt'}), 400
        
        # ========== STEP 3: Prepare the prompt for URL ==========
        # URL encoding converts special characters to URL-safe format
        # Example: "a cat & dog" becomes "a%20cat%20%26%20dog"
        encoded_prompt = urllib.parse.quote(prompt)
        
        # ========== STEP 4: Generate random seed ==========
        # Seed ensures we get different images each time
        # Same seed + same prompt = same image (reproducibility)
        seed = random.randint(1, 999999)
        
        # ========== STEP 5: Set up negative prompt ==========
        # Negative prompt tells the AI what to AVOID in the image
        # Default avoids common quality issues
        neg_prompt = negative if negative else "blurry, low quality, distorted, ugly, bad anatomy"
        encoded_negative = urllib.parse.quote(neg_prompt)
        
        # ========== STEP 6: Construct Pollinations.ai API URL ==========
        # This URL will return an AI-generated image when accessed
        # 
        # URL STRUCTURE:
        # https://image.pollinations.ai/prompt/{ENCODED_PROMPT}?
        #   width={WIDTH}           - Image width
        #   height={HEIGHT}         - Image height
        #   model={MODEL}           - AI model to use
        #   enhance=true            - AI improves the prompt automatically
        #   negative_prompt={NEG}   - What to avoid
        #   seed={SEED}             - Random seed for variation
        #   nologo=true             - Removes Pollinations watermark
        #
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model={model}&enhance=true&negative_prompt={encoded_negative}&seed={seed}&nologo=true"
        
        # ========== STEP 7: Return success response ==========
        return jsonify({
            'success': True,
            'image_url': image_url,    # URL where the generated image is
            'prompt': prompt,          # Original prompt for display
            'model': model             # Model used for generation
        })
        
    except Exception as e:
        # If anything goes wrong, return an error message
        return jsonify({'error': str(e)}), 500


# ============================================================================
# ROUTE 3: RANDOM PROMPT
# ============================================================================
@app.route('/random-prompt', methods=['GET'])
def random_prompt():
    """
    FUNCTION: Get a random creative prompt for inspiration
    
    When user clicks the "Random" button, this function is called.
    It selects a random prompt from our RANDOM_PROMPTS list.
    
    DECORATORS EXPLAINED:
    - @app.route('/random-prompt', methods=['GET'])
      Handles GET requests to /random-prompt
    
    RETURNS:
    - JSON with a random prompt string
    """
    # random.choice() picks one random item from the list
    prompt = random.choice(RANDOM_PROMPTS)
    return jsonify({'prompt': prompt})


# ============================================================================
# ROUTE 4: ENHANCE PROMPT
# ============================================================================
@app.route('/enhance', methods=['POST'])
def enhance_prompt():
    """
    FUNCTION: Enhance a prompt with artistic keywords
    
    When user clicks the "Enhance" button, this function:
    1. Takes their current prompt
    2. Adds 3-4 random quality-boosting keywords
    3. Returns the enhanced prompt
    
    EXAMPLE:
    Input:  "A cat sitting on a couch"
    Output: "A cat sitting on a couch, highly detailed, cinematic lighting, 8K resolution"
    
    RETURNS:
    - JSON with enhanced_prompt on success
    - JSON with error message on failure
    """
    try:
        # Get the prompt from the request
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        # Validate that a prompt was provided
        if not prompt:
            return jsonify({'error': 'Please enter a prompt to enhance'}), 400
        
        # random.sample() picks 3-4 random keywords WITHOUT repetition
        # random.randint(3, 4) randomly chooses between 3 or 4
        enhancements = random.sample(ENHANCEMENT_KEYWORDS, random.randint(3, 4))
        
        # Combine original prompt with enhancement keywords
        # ', '.join() converts list to comma-separated string
        enhanced_prompt = f"{prompt}, {', '.join(enhancements)}"
        
        return jsonify({
            'success': True,
            'enhanced_prompt': enhanced_prompt
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================
if __name__ == '__main__':
    """
    This block runs when you execute: python app.py
    
    app.run() starts the Flask development server:
    - debug=True: Auto-reloads when you change code, shows detailed errors
    - port=5000: The server runs on http://localhost:5000
    
    NOTE: In production, you would use a proper server like Gunicorn
    """
    print("=" * 60)
    print("ARTIFEX - AI Image Generator")
    print("=" * 60)
    print("Server running at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    app.run(debug=True, port=5000)
