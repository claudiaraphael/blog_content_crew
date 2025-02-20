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
def brand_voice_researcher(self) -> Agent:
  return Agent(
  config = self.agents_config['brand voice researcher'],
  llm = self.groq_llm
    )

@agent 
def product_specifics_researcher(self) -> Agent:
  return Agent(
  config = self.agents_config['brand voice researcher'],
  llm = self.groq_llm
    )


# Understand the products unique features & benefits
@task:
def research_product_specifics(self) -> Agent:
   return Task(
      config = self.tasks_config['research_product_specifics']
      agent = self.product_specifics_researcher()
   )
   research_product_specifics

# Ensure consistency with the brands messaging
@Task
def research_brand_voice(self) -> Agent:
  return Task(
     config = self.tasks_config['research_brand_voice'],
     agent = self.brand_voice_researcher()
  ) 

@Crew
def crew(Self) -> Crew:
   """Creates the SEOContentCrew crew"""
   return Crew(
      agents = self.agents,
      tasks = self.tasks,
      process = Process.sequential,
      verbose = 2
   )