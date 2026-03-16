from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print("--- Space Station Data Validation ---")
    """Test with valid instance"""
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-03-09T12:00:00"
        )
        print(f"Valid station created: {station.name}")
    except Exception as e:
        print(f"Error: {e}")
    """Test with invalid instance"""
    try:
        invalid_station = SpaceStation(
            station_id="FAIL01",
            name="Too Crowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now()
        )
        print(f"Inalid station created: {invalid_station.name}")
    except Exception as e:
        print(f"\nExpected validation error: {e}")


if __name__ == "__main__":
    main()
