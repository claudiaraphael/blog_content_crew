from crewai import Agent, Crew, Process, Task # 4 main pillars of crewai project
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGrok


@CrewBase
class seo_content_crew():
    """SEOContentCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGrok(temperature = 0, model_name='mixtral-8x7b-32768')


@agent 
def [agent name](self) -> Agent:
return Agent(
    config = self.agents_config['agent name']
)

