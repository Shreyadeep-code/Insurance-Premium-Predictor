from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Annotated,Literal
from config.city_tier import tier_1_cities,tier_2_cities



class UserInput(BaseModel):
    age:Annotated[int,Field(...,gt=0,description='Age of the person')]
    weight:Annotated[float,Field(...,gt=0,description='weight of the person')]
    height:Annotated[float,Field(...,gt=0,description='height of the person')]
    income_lpa:Annotated[float,Field(...,gt=0,description='income of the person in LPA')]
    smoker:Annotated[bool,Field(...,description='is the person a smoker ?')]
    city:Annotated[str,Field(...,description='city address of the person')]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description='occupation of the person')]
    
    @field_validator('city')
    @classmethod
    def normalize_city(cls,v:str) ->str:
        v=v.strip().title()
        return v




    @computed_field
    @property
    def bmi(self)->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker or self.bmi>27:
            return 'medium'
        return 'low'
    
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
    
    @computed_field
    @property
    def Age_group(self)->str:

        if self.age<25:
            return 'Young'
        elif self.age<45:
            return 'Adult'
        elif self.age<60:
            return 'Middle_aged'
        return 'Senior'