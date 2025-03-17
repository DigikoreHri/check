import json

def response(flow):
    """Intercept API responses and save relevant JSON responses."""
    # Check if the request is to the desired API endpoint
    if "https://wb.riffusion.com/v2/users" in flow.request.url:
        print(f"Intercepted: {flow.request.url}")
        try:
            # Parse JSON response
            response_data = json.loads(flow.response.text)

            # Append to a file
            with open("test1.json", "a", encoding="utf-8") as f:
                json.dump({
                    "url": flow.request.url,
                    "response": response_data
                }, f, ensure_ascii=False, indent=4)
                f.write(",\n")
            print("Saved response.")
        except Exception as e:
            print(f"Error processing response: {e}")

#mitmdump -s capture_response.py

