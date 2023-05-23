import requests

def analyze_emotion(text):
    api_key = 'YOUR_API_KEY'  
    url = f'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_INSTANCE_ID/v1/analyze?version=2021-08-01&features=sentiment,emotion&language=en'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        'text': text,
        'features': {
            'sentiment': {},
            'emotion': {}
        }
    }
    
    response = requests.post(url, json=data, headers=headers)
    result = response.json()
    
    emotion = result['emotion']['document']['emotion']
    sentiment = result['sentiment']['document']['score']
    
    return emotion, sentiment

def recommend_songs(emotion):
    recommended_songs = ['Song 1', 'Song 2', 'Song 3']
    return recommended_songs

def chatbot_interaction():
    print("Chatbot: Hello! How are you feeling today?")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        emotion, sentiment = analyze_emotion(user_input)
        print(f"Chatbot: You seem to be feeling {emotion}.")
        
        if sentiment >= 0.5:
            print("Chatbot: That sounds great!")
        elif sentiment <= -0.5:
            print("Chatbot: I'm sorry to hear that.")
        
        songs = recommend_songs(emotion)
        
        if songs:
            print("Chatbot: Here are some songs you might like:")
            for song in songs:
                print(song)
        else:
            print("Chatbot: Sorry, I couldn't find any songs to recommend.")
        print()

chatbot_interaction()

