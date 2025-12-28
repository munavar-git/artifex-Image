from flask import Flask, render_template, request, jsonify
import urllib.parse
import random

app = Flask(__name__)

# Random prompt ideas for inspiration
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

# Enhancement keywords to improve prompts
ENHANCEMENT_KEYWORDS = [
    "highly detailed", "intricate details", "professional photography",
    "cinematic lighting", "volumetric lighting", "ray tracing",
    "8K resolution", "masterpiece", "award-winning", "stunning",
    "atmospheric", "moody", "dramatic lighting", "photorealistic",
    "hyperrealistic", "octane render", "unreal engine 5", "artstation",
    "trending on artstation", "concept art", "matte painting"
]

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    """Generate image using Pollinations.ai API"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        negative = data.get('negative', '')
        width = data.get('width', 1024)
        height = data.get('height', 1024)
        model = data.get('model', 'flux')
        
        if not prompt:
            return jsonify({'error': 'Please enter a prompt'}), 400
        
        # URL encode the prompt
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Build URL with quality parameters
        # enhance=true improves prompt for better quality
        # negative_prompt helps avoid low quality outputs
        # seed for reproducibility (random seed each time)
        import random
        seed = random.randint(1, 999999)
        
        # Default negative prompt if none provided
        neg_prompt = negative if negative else "blurry, low quality, distorted, ugly, bad anatomy"
        encoded_negative = urllib.parse.quote(neg_prompt)
        
        # Construct Pollinations.ai URL with all quality parameters
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&model={model}&enhance=true&negative_prompt={encoded_negative}&seed={seed}&nologo=true"
        
        return jsonify({
            'success': True,
            'image_url': image_url,
            'prompt': prompt,
            'model': model
        })
        

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/random-prompt', methods=['GET'])
def random_prompt():
    """Get a random creative prompt for inspiration"""
    prompt = random.choice(RANDOM_PROMPTS)
    return jsonify({'prompt': prompt})

@app.route('/enhance', methods=['POST'])
def enhance_prompt():
    """Enhance a prompt with artistic keywords"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        if not prompt:
            return jsonify({'error': 'Please enter a prompt to enhance'}), 400
        
        # Select 3-4 random enhancement keywords
        enhancements = random.sample(ENHANCEMENT_KEYWORDS, random.randint(3, 4))
        enhanced_prompt = f"{prompt}, {', '.join(enhancements)}"
        
        return jsonify({
            'success': True,
            'enhanced_prompt': enhanced_prompt
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Image Generator running at http://localhost:5000")
    app.run(debug=True, port=5000)
