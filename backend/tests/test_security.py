from app.core.security import hash_password, verify_password

def test_password_hash_roundtrip():
    password = "super-secret"
    encoded = hash_password(password)
    assert encoded != password
    assert verify_password(password, encoded)
    assert not verify_password("wrong", encoded)
