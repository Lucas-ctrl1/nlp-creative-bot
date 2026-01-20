import streamlit as st
from creative_bot import CreativeChatbot
from PIL import Image
import os

# --- SETUP ---
st.set_page_config(page_title="Creative Bot", layout="wide")

# Initialize the Class in Session State (preserves memory)
if "bot" not in st.session_state:
    with st.spinner("Waking up the AI (Loading Whisper & Ollama)..."):
        st.session_state.bot = CreativeChatbot()
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

bot = st.session_state.bot

# --- UI LAYOUT ---
st.title(f"🤖 {bot.name}: The Idea Generator")
st.markdown("Upload images, text, or **voice recordings** to generate **Stories, Music, and Visual Prompts**.")

# 1. INPUTS
col1, col2 = st.columns(2)

with col1:
    st.header("Input")
    
    # A. Text Input
    user_text = st.text_area("Enter Keywords:", placeholder="e.g. Castle, Jazz, Rain")
    
    # B. Image Input
    uploaded_file = st.file_uploader("Upload Image Context", type=['jpg', 'png'])
    user_image = None
    if uploaded_file:
        user_image = Image.open(uploaded_file)
        st.image(user_image, caption="Visual Input", width=200)

    # C. Audio Input (CRITICAL FOR TUTOR REQUIREMENT)
    uploaded_audio = st.file_uploader("Upload Voice Idea", type=['mp3', 'wav', 'm4a'])
    audio_path = None
    
    # Save audio temporarily so Whisper can read it
    if uploaded_audio:
        audio_path = f"temp_{uploaded_audio.name}"
        with open(audio_path, "wb") as f:
            f.write(uploaded_audio.getbuffer())
        st.audio(uploaded_audio)

    if st.button("Generate Creative Output"):
        if not (user_text or user_image or audio_path):
            st.error("Please provide at least one input!")
        else:
            with st.spinner("Analyzing multi-modal inputs..."):
                # A. Prepare Input Dictionary (Now includes 'audio')
                raw_input = {'text': user_text, 'image': user_image, 'audio': audio_path}
                
                # B. Call Class Methods (Inherited logic)
                processed_data = bot.process_input(raw_input)
                
                # Show the "Thinking" (Categorization)
                with st.expander("See AI Analysis"):
                    st.write(f"**Visuals:** {processed_data['visual_tags']}")
                    st.write(f"**Audio:** {processed_data['audio_context']}")
                
                # C. Generate Final Response
                response = bot.generate_response(processed_data)
                st.session_state.last_response = response
            
            # Cleanup temp audio file
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)

# 2. OUTPUTS
with col2:
    st.header("Creative Output")
    if st.session_state.last_response:
        st.markdown(st.session_state.last_response)
        
        st.divider()
        
        # Download Button (Quality of Life)
        st.download_button(
            label="💾 Save Creative Brief",
            data=st.session_state.last_response,
            file_name="creative_idea.md",
            mime="text/markdown"
        )
        
        # Challenge Mode (Interactive Requirement)
        if st.button("🔥 Challenge Me"):
            with st.spinner("Inventing a challenge..."):
                challenge = bot.challenge_user(st.session_state.last_response)
                st.warning(f"**Creative Challenge:** {challenge}")

# Footer
if not st.session_state.last_response:
    st.caption(f"System Ready. Model: {bot.text_model} | Audio: Whisper Tiny")