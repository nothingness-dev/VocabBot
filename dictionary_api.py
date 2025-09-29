import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word):
    """
    Get all definitions of a word from the Dictionary API.
    
    Args:
        word (str): The word to look up.
        
    Returns:
        dict: A dictionary containing:
            - word: The word that was looked up
            - phonetics: Pronunciation guide (if available)
            - meanings: List of definitions with part of speech & examples
            - error: Error message if something went wrong
    """
    try:
        response = requests.get(API_URL + word.lower().strip())
        if response.status_code != 200:
            return {"error": "Word not found"}

        data = response.json()[0]
        word_text = data.get("word", "")
        
        # Get phonetics if available
        phonetics = ""
        for phonetic in data.get("phonetics", []):
            if "text" in phonetic and phonetic["text"]:
                phonetics = phonetic["text"]
                break

        meanings = data.get("meanings", [])
        if not meanings:
            return {"error": "No definition found"}

        results = []
        for meaning in meanings:
            part_of_speech = meaning.get("partOfSpeech", "")
            for definition in meaning.get("definitions", []):
                results.append({
                    "part_of_speech": part_of_speech,
                    "definition": definition.get("definition", ""),
                    "example": definition.get("example", "")
                })

        return {
            "word": word_text,
            "phonetics": phonetics,
            "meanings": results
        }

    except Exception as e:
        return {"error": f"Error looking up word: {str(e)}"}
