from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(m.rank in [Rank.commander, Rank.captain]
                         for m in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least one Commander or"
                             "Captain")

        if self.duration_days > 365:
            exp_crew = [m for m in self.crew if m.years_experience >= 5]
            if len(exp_crew) < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced crew"
                                 "(5+ years)")

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("--- Space Mission Crew Validation ---")
    """Testing with valid mission"""
    try:
        crew = [
            CrewMember(member_id="C01", name="Sarah",
                       rank=Rank.commander, age=45,
                       specialization="Mission Command", years_experience=20),
            CrewMember(member_id="C02", name="John",
                       rank=Rank.lieutenant, age=30,
                       specialization="Navigation", years_experience=6),
            CrewMember(member_id="C03", name="Alice",
                       rank=Rank.officer, age=28,
                       specialization="Engineering", years_experience=5)
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print("Destination: ", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"BUdget: ${mission.budget_millions}")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for memb in crew:
            print(f"- {memb.name} ({memb.rank})")

    except Exception as e:
        print(f"Unexpected Error: {e}")

    """Expected validation error:"""
    try:
        print("\nTesting invalid mission (No Captain/Commander)")
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Invalid Mission",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=[CrewMember(member_id="C99", name="Ayman", rank=Rank.cadet,
                             age=20, specialization="Cleaning",
                             years_experience=0)],
            budget_millions=50.0
        )
    except Exception as e:
        print(f"Expected validation error: {e}")


if __name__ == "__main__":
    main()
