from agno.agent import Agent
from agno.models.ollama import Ollama
from openocr import OpenOCR
import os
import json


ocr_engine = OpenOCR()

agent = Agent(
    model=Ollama(id="gemma3:4b"),
    description="You are a really good teacher. Please answer based on the questions and keep it concise and clear. Provide examples, 25 model questions with answers,10 True or False questions with answers, equations and units if applicable. Also recommend what to study next after understanding the current topic",
    markdown=True
)

def extract_text_from_ocr_results(result_file):
    """Extract text from OCR results file"""
    try:
        with open(result_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # If the file contains the image filename followed by tab and JSON data
        if '\t' in content:
            content = content.split('\t', 1)[1]
        
        try:
            # Parse the JSON
            data = json.loads(content)
            
            if isinstance(data, list):
                if all(isinstance(item, dict) and "transcription" in item for item in data):
                    # Sort by vertical position if points are available
                    if all("points" in item for item in data):
                        try:
                            sorted_data = sorted(data, key=lambda x: min(point[1] for point in x["points"]))
                        except (TypeError, IndexError):
                            # If sorting fails, use original order
                            sorted_data = data
                    else:
                        sorted_data = data
                    
                    # Extract only the transcription text
                    extracted_text = []
                    for item in sorted_data:
                        extracted_text.append(item["transcription"])
                    
                    # Join all the text with newlines
                    text_only = '\n'.join(extracted_text)
                    return text_only
                else:
                    # Different structure, try to extract text directly
                    return str(data)
            else:
                return str(data)
            
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            # If can't parse as JSON, return raw content
            return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def process_input():
    """Function to handle user input and determine mode"""
    input_type = input("Choose input type (text/image): ").lower()
    
    if input_type == "text":
        question = input("Ask your question: ")
        return question
    
    elif input_type == "image":
        img_path = input("Enter the full path to your image: ")
        
        try:
            # Run OCR on the image
            print(f"Processing image: {img_path}")
            
            # Check if the file exists
            if not os.path.exists(img_path):
                print(f"Error: File not found: {img_path}")
                return process_input()
            
            try:
                # First try direct OCR
                extracted_text, elapsed_time = ocr_engine(img_path)
                print(f"Text extracted in {elapsed_time:.2f} seconds")
                
            except Exception as ocr_error:
                print(f"Direct OCR failed: {ocr_error}")
                print("Trying to read from results file...")
                
                # Try to read from the results file that OpenOCR might have created
                results_file = "e2e_results/system_results.txt"
                if os.path.exists(results_file):
                    extracted_text = extract_text_from_ocr_results(results_file)
                    if not extracted_text:
                        print("Could not extract text from results file")
                        return process_input()
                else:
                    print(f"Results file not found: {results_file}")
                    return process_input()
            
            #print("-" * 40)
            #print("Extracted text:")
            #print(extracted_text)
            print("-" * 40)
            
            # Option to edit the extracted text
            #edit_option = input("Would you like to edit the extracted text? (yes/no): ").lower()
            #if edit_option == "yes":
                #extracted_text = input("Enter your edited text: ")
                
            return extracted_text
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return process_input()  
    
    else:
        print("Invalid option. Please choose 'text' or 'image'.")
        return process_input()  

def main():
    print("=" * 50)
    print("Chalkboard")
    print("=" * 50)
    
    while True:
        # Get input from user
        query = process_input()
        
        if not query:
            print("No valid text to process. Please try again.")
            continue
            
        print("\nGenerating response...\n")
        agent.print_response(query)
        
        # Ask if user wants to continue
        continue_option = input("\nWould you like to ask another question? (yes/no): ").lower()
        if continue_option != "yes":
            print("Thank you!")
            break

if __name__ == "__main__":
    main()