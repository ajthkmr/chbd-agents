import json

# Function to extract only the transcriptions from the OCR JSON data
def extract_text_from_file(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # If the file contains the image filename followed by tab and JSON data
    if '\t' in content:
        content = content.split('\t', 1)[1]
    
    try:
        # Parse the JSON
        data = json.loads(content)
        
        # Sort by vertical position (y-coordinate) to maintain reading order
        sorted_data = sorted(data, key=lambda x: min(point[1] for point in x["points"]))
        
        # Extract only the transcription text
        extracted_text = []
        for item in sorted_data:
            extracted_text.append(item["transcription"])
        
        # Join all the text with newlines
        text_only = '\n'.join(extracted_text)
        
        # Save to a new file
        with open('extracted_text_only.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(text_only)
        
        print(f"Extracted text has been saved to extracted_text_only.txt")
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        
# Call the function with your file
extract_text_from_file('C:\\Users\\Ajithkumar K\\Desktop\\agent base\\e2e_results\\system_results.txt')