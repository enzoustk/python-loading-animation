import time
from loading_animation import loading_animation

def run_demo():
    print("--- Starting loading-animation Demo ---\n")

    # Scenario 1: Simple Usage
    print("1. Scenario: Simple Loading")
    with loading_animation("Processing data"):
        time.sleep(2)
    print("Done!\n")

    # Scenario 2: Dynamic Status Updates
    print("2. Scenario: Dynamic Status Updates")
    with loading_animation("Connecting to server...") as status:
        time.sleep(1.5)
        
        status['message'] = "Downloading configuration files"
        time.sleep(2)
        
        status['message'] = "Applying security patches"
        time.sleep(1.5)
        
        status['message'] = "Finalizing"
        time.sleep(1)
    print("System updated successfully!\n")

    # Scenario 3: Batch Processing Loop
    print("3. Scenario: Batch Processing Loop")
    items = ["Image_01.png", "Image_02.png", "Image_03.png"]
    with loading_animation() as status: # Uses the default "Loading..."
        for i, item in enumerate(items, 1):
            status['message'] = f"Processing item {i} of {len(items)} ({item})"
            time.sleep(1.2)
    
    print("All items processed successfully.")
    print("\n--- End of Demo ---")

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")