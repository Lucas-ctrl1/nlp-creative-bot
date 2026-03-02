from chatbot_base import ChatbotBase
import ollama
import io
from faster_whisper import WhisperModel

class CreativeChatbot(ChatbotBase):
    def __init__(self):
        super().__init__(name="CreativeMuse")
        self.text_model = "mistral"
        self.vision_model = "llava"
        
        # --- NEW: Load Audio Model (Required for Tutor's "Audio Input" mark) ---
        print("Loading Audio Model...")
        # 'tiny' is fast and works well on local CPU
        self.audio_model = WhisperModel("tiny", device="cpu", compute_type="int8")

    def process_input(self, user_input):
        """
        Overrides the base method.
        Accepts a dictionary of inputs (Text, Image, Audio) and categorizes them.
        """
        text = user_input.get('text', '')
        image = user_input.get('image', None)
        audio_path = user_input.get('audio', None) # Get the audio file path
        
        visual_context = "None"
        audio_context = "None"
        
        # 1. VISUAL: Handle Image (Vision)
        if image:
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            img_bytes = img_byte_arr.getvalue()
            
            try:
                response = ollama.generate(
                    model=self.vision_model,
                    prompt="Describe the artistic style and mood of this image in keywords.",
                    images=[img_bytes]
                )
                visual_context = response['response']
            except Exception as e:
                visual_context = "(Image processing failed)"

        # 2. AUDIO: Handle Voice (Whisper) - CRITICAL FOR TUTOR REQ
        if audio_path:
            try:
                # Transcribe the audio file
                segments, info = self.audio_model.transcribe(audio_path)
                audio_context = " ".join([segment.text for segment in segments])
            except Exception as e:
                audio_context = f"(Audio Error: {str(e)})"

        # 3. Return processed data dictionary
        # We include audio_context here so the Brain knows what you said
        return {
            "raw_text": text,
            "visual_tags": visual_context,
            "audio_context": audio_context,
            "combined_context": f"Keywords: {text}\nVisuals: {visual_context}\nVoice Idea: {audio_context}"
        }

    def generate_response(self, processed_input):
        """
        Overrides the base method.
        Generates the Creative Output using the Avant-Garde personality.
        """
        context = processed_input['combined_context']
        
        # This is your upgraded 'Provocative' prompt
        prompt = f"""
You are an avant-garde creative muse. Your goal is to break creative blocks by offering wild, unexpected, and provocative ideas.
Input Data: {context}

Task:
1. **The Concept**: Write a plot summary (max 50 words) that creates a twist on the input. Avoid clichés.
2. **Visual Prompt**: A highly detailed, artistic prompt for Midjourney/DALL-E (mention lighting, lens type, and texture).
3. **Audio Cue**: A specific, atmospheric soundscape description.

Do not be boring. Be bold.
"""
        
        try:
            response = ollama.generate(model=self.text_model, prompt=prompt)
            return response['response']
        except Exception:
            return "Error: Could not connect to local Ollama."

    def challenge_user(self, previous_idea):
        """
        Extending functionality for 'Interactive' marks.
        """
        prompt = f"Based on: {previous_idea}, give a difficult creative constraint to rewrite this."
        response = ollama.generate(model=self.text_model, prompt=prompt)
        return response['response']
