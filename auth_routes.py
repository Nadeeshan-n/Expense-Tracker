from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

from models_db import (
    get_db,
    UserDB
)

from models import (
    UserCreate,
    UserLogin
)

from auth import hash_password
from auth import verify_password

router = APIRouter()

@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(UserDB).filter(
        (UserDB.username == user.username) |
        (UserDB.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username or email already exists"
        )

    hashed_pw = hash_password(user.password)

    new_user = UserDB(
        username=user.username,
        email=user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)

    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    }


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    if not existing_user or not verify_password(
        user.password,
        existing_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={
            "sub": existing_user.username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
