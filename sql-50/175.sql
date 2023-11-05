Select
    firstName,
    lastName,
    city,
    state
from
    Person P
    left Join Address A ON P.personId = A.personId