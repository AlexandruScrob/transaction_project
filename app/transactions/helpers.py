from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from core.settings import get_settings

settings = get_settings()
security = HTTPBasic()


def check_headers(credentials: Annotated[HTTPBasicCredentials, Depends(security)]) -> None:
    if (
        credentials.username != settings.auth_username
        or credentials.password != settings.auth_password.get_secret_value()
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return None
