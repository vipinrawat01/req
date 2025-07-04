from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Newapp():
    """Newapp crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def vision_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['vision_agent'],
            verbose=True
        )

    @agent
    def audience_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['audience_agent'],
            verbose=True
        )
    
    @agent
    def feature_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['feature_agent'],
            verbose=True
        )
    
    @agent
    def chat_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chat_agent'],
            verbose=True
        )

    @task
    def vision_task(self) -> Task:
        return Task(
            config=self.tasks_config['vision_task'],
        )

    @task
    def audience_task(self) -> Task:
        return Task(
            config=self.tasks_config['audience_task'],
        )
    
    @task
    def feature_task(self) -> Task:
        return Task(
            config=self.tasks_config['feature_task'],
        )
    
    @task
    def chat_task(self) -> Task:
        return Task(
            config=self.tasks_config['chat_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Newapp crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
