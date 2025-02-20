import os
from dotenv import load_dotenv
load_dotenv()

from SEOContentCrew.crew import SEOContentCrew

def run():
    inputs = {
        
    }
    SEOContentCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()