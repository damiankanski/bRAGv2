from enum import StrEnum

# on local we need only one user so we add 1
DEFAULT_NUMBER_OF_WORKERS_ON_LOCAL = 1

class Environments(StrEnum):
    LOCAL = "local"
    PRODUCTION = "production"
