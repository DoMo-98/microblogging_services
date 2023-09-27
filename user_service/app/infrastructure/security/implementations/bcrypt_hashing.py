"""

"""

import bcrypt

from app.infrastructure.security.interfaces.hashing_strategy import HashingStrategy


class BcryptHashing(HashingStrategy):
    """
    BcryptHashing class
    """

    def hash(self, input_data: str) -> str:
        """
        Hash input data
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(input_data.encode("utf-8"), salt)
        return hashed.decode("utf-8")
