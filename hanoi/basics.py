import warnings


def number_of_positions(number_of_disks: int) -> int:
    number_of_positions = pow(3, number_of_disks)

    return number_of_positions


def number_of_steps_of_solution(number_of_disks: int) -> int:
    number_of_steps_of_solutions = pow(2, number_of_disks) - 1

    return number_of_steps_of_solutions


class Position:
    def __init__(self, representation: str):
        self.representation = representation
        self._warn_ambitious_players()

    def _warn_ambitious_players(self) -> None:
        if len(self.representation) > 100:
            warnings.warn("Are you sure you want to get involved with such a challenge?")

    def __str__(self) -> str:
        return self.representation

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return self.representation == other.representation
        return False
