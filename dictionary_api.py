import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word):
    """
    Get the definition of a word from the Dictionary API.
    
    Args:
        word (str): The word to look up
        
    Returns:
        dict: A dictionary containing:
            - word: The word that was looked up
            - phonetics: Pronunciation guide (if available)
            - definition: Primary definition of the word
            - example: Example usage of the word (if available)
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
        phonetics_list = data.get("phonetics", [])
        for phonetic in phonetics_list:
            if "text" in phonetic and phonetic["text"]:
                phonetics = phonetic["text"]
                break
                
        meanings = data.get("meanings", [])

        if not meanings:
            return {"error": "No definition found"}

        # Get the first definition and example
        definition = meanings[0]["definitions"][0].get("definition", "")
        example = meanings[0]["definitions"][0].get("example", "")

        # Format the response
        response_data = {
            "word": word_text,
            "phonetics": phonetics,
            "definition": definition,
            "example": example
        }

        # Add part of speech if available
        if "partOfSpeech" in meanings[0]:
            response_data["part_of_speech"] = meanings[0]["partOfSpeech"]

        return response_data

    except Exception as e:
        return {"error": f"Error looking up word: {str(e)}"}


if __name__ == "__main__":
    while True:
        word = input("\nEnter a word to get its definition (or 'quit' to exit): ").strip()
        if word.lower() == 'quit':
            break
            
        result = get_definition(word)
        if "error" in result:
            print(f"\nError: {result['error']}")
        else:
            print(f"\nWord: {result['word']}")
            if result['phonetics']:
                print(f"Phonetics: {result['phonetics']}")
            print(f"Definition: {result['definition']}")
            if result['example']:
                print(f"Example: {result['example']}")