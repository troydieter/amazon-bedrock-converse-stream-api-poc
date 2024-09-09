import streamlit as st
from invoke_model_converse_stream_api import stream_conversation
import time

# Function to simulate sound effect
def play_sound(effect: str):
    st.audio(f"./sounds/{effect}.mp3", format="audio/mp3", autoplay=True)  # Assuming you have audio files for sound effects

# Title and Theme Setup
st.title("💰 Who Wants to Be an AI Millionaire? 💰")
st.subheader("🎉 Welcome to the Game Show Powered by Amazon Bedrock! 🎉")
st.write("Phone a Friend, Ask the AI, and see if you can get the right answer!")

# Show special effect balloons for a game show feel
st.balloons()

# Session state for messages (user questions & AI responses)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display each message in the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Main Game Show UI with question input
question = st.chat_input("What will your question be, contestant?")
if question:
    # Simulate Game Show lights and sound
    st.markdown("🎶 *Tension music plays...* 🎶")
    play_sound("tension_music")  # Play a background sound like in the show
    
    # Display the user's question
    with st.chat_message("user"):
        st.markdown(f"💬 **Contestant:** {question}")
    
    # Add user's question to session state
    st.session_state.messages.append({"role": "user", "content": question})
    
    # Simulate AI "Phone a Friend" delay with dramatic pause
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        st.markdown("📞 **AI is thinking...**")
        time.sleep(2)  # Pause to simulate the tension before answer
    
        # Stream the AI's response as the "Phone a Friend" answer
        answer = st.write_stream(stream_conversation(question))
        
        # Reveal the AI's final answer
        message_placeholder.markdown(f"🤖 **AI Friend:** {answer}")
        
        # Play sound effect for correct/incorrect answer
        play_sound("correct_answer" if answer else "wrong_answer")  # Placeholder for actual logic
    
    # Add assistant's answer to session state
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Add some finishing visual elements to heighten the game show theme
st.markdown("🎉 Ready for another round? Ask the AI and see if you can win the virtual millionaire title!")
