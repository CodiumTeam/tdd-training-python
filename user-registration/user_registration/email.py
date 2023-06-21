from dataclasses import dataclass


@dataclass
class Email:
    from_email: str
    to_email: str
    subject: str
