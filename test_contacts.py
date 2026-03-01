from contacts_manager import validate_phone, validate_email

def test_validation():
    print("Testing phone validation...")
    assert validate_phone("123-456-7890")[0] == True
    assert validate_phone("123")[0] == False
    
    print("Testing email validation...")
    assert validate_email("test@example.com") == True
    assert validate_email("invalid-email") == False
    print("All tests passed!")

if __name__ == "__main__":
    test_validation()
