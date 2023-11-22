from typing import List

class PassportData:
    data: List["EncryptedPassportElement"]
    credentials: "EncryptedCredentials"

class PassportFile:
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int

class EncryptedPassportElement:
    type: str
    data: str
    phone_number: str
    email: str
    files: List["PassportFile"]
    front_side: "PassportFile"
    reverse_side: "PassportFile"
    selfie: "PassportFile"
    translation: List["PassportFile"]
    hash: str

class EncryptedCredentials:
    data: str
    hash: str
    secret: str