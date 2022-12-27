from diffpy.diffmath.homogeneous import homogeneous

def test_homogeneous():
    assert homogeneous(1, -2, 1)[0] == "C₁e^(1.0x) + C₂e^(1.0x) * x"

    assert homogeneous(1, 1, 1)[0] == "e^(-0.5x) * (C₁cos(0.8660254037844386x) + C₂sin(0.8660254037844386x))"
    
    assert homogeneous(1, 1, -2)[0] == "C₁e^(-2.0x) + C₂e^(1.0x)"
    
    print('"test_homogeneous" is passed')