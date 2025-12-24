import sys    
import time
import threading
from contextlib import contextmanager

@contextmanager
def loading_animation(
    initial_message: str = "Loading..."
    ):
    """
    Context Manager to display animated text;
    Yields the status dict to allow messages to be updated
    """
    status_data = {'message': initial_message}
    stop_event = threading.Event()
    
    animation_thread = threading.Thread(
        target=_animate_loading,
        args=(stop_event, status_data)
    )
    animation_thread.start()
    
    try:
        yield status_data
    
    finally:
        # Garante que a thread pare
        stop_event.set()
        animation_thread.join()


def _animate_loading(stop_event: threading.Event, status_data: dict):
    chars = ["   ", ".  ", ".. ", "..."]
    idx = 0
    last_line_len = 0

    while not stop_event.is_set():
        message = status_data.get('message', 'Loading')
        dots = chars[idx % len(chars)]
        
        line = f"\r{message}{dots}"
        current_line_len = len(line)

        padding = " " * max(0, last_line_len - current_line_len)
        
        sys.stdout.write(line + padding)
        sys.stdout.flush()
        
        last_line_len = current_line_len
        idx += 1
        time.sleep(0.3)
    
    sys.stdout.write("\r" + " " * last_line_len + "\r")
    sys.stdout.flush()
