# rough sketch, will fill out later and join it all up once it's actually needed



import json
from datetime import datetime

def save_analysis(analysis: Dict[str, Any], filename: str) -> None:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open(f"{filename}_{timestamp}.json", 'w') as f:
        json.dump(analysis, f, indent=4)
