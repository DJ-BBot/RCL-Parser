class rcl:
    """RCL is Roger's Configuration Language. This class is the pythonic parser sdk."""
    
    __tokens:list[str] = [
        "#", "=>", "->", ":", 
        "\\", "\\\\", "\\\\\\", 
        "{", "}", ".", ";"
    ]

    @classmethod
    def __GetRCLTokens(cls):
        return cls.__tokens

if __name__ == "__main__":
    print(rcl)