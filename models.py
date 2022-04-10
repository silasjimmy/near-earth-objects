"""Classes to instantiate Near Earth Objects and Close Approaches."""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A Near-Earth object (NEO)."""

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self.designation = info.get('designation')
        self.diameter = info.get('diameter')
        self.name = info.get('name')
        self.hazardous = info.get('hazardous')
        self.approaches = []

    def serialize(self):
        """Serialize the NEO's data to a neat way.

        Returns: 
            (dict) Serialized NEO data.
        """
        return {
            'designation': self.designation,
            'name': self.name,
            'diameter_km': self.diameter,
            'potentially_hazardous': self.hazardous
        }

    @property
    def fullname(self):
        """NEO fullname.

        return: a representation of the full name of this NEO.
        """
        return f"{self.designation} ({self.name})" if self.name else f"{self.designation}"

    def __str__(self):
        """Construct a string rpresentation of NEO.

        return: a string representation of the NEO.
        """
        hazard_status = 'is' if self.hazardous else 'is not'
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and {hazard_status} potentially hazardous."

    def __repr__(self):
        """return: a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO."""

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = info.get('designation')
        self.time = cd_to_datetime(info.get('time'))
        self.distance = info.get('distance')
        self.velocity = info.get('velocity')
        self.neo = None

    def serialize(self):
        """Serialize the Close approaches' data to a neat way.

        Returns: 
            (dict) Serialized close approach data.
        """
        return {
            'datetime_utc': datetime_to_str(self.time),
            'distance_au': self.distance,
            'velocity_km_s': self.velocity
        }

    @property
    def time_str(self):
        """return: a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """return: a human-readable string representation."""
        return f"At {self.time_str}, {self.neo.fullname} approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """return: a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
