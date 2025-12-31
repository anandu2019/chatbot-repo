from pydantic import BaseModel
from typing import List, Optional

class ResumeResponse(BaseModel):
    Name: Optional[str] = None
    Email: Optional[str] = None
    Phone_Number: Optional[str] = None
    Skills: List[str] = []
    Years_of_Experience: Optional[str] = None
    Education: Optional[str] = None
    Current_Last_Job: Optional[str] = None
    Companies_Worked_At: List[str] = []
    LinkedIn: Optional[str] = None
    Certifications: List[str] = []
    Location: Optional[str] = None