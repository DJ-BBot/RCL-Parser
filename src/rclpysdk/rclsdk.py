import os

class rclParser:
    """RCL is Roger's Configuration Language. This class is the pythonic parser sdk."""
    
    __tokens:list[str] = [
        "#", "=>", "->", ":", 
        "\\", "\\\\", "\\\\\\", 
        "{", "}", ".", ";"
    ]

    __keywords:list[str] = [
        "title", "rclAuthor", "rclVersion"
    ]

    @classmethod
    def __GetRCLTokens(cls) -> list[str]:
        return cls.__tokens
    
    @classmethod
    def __GetRCLKeywords(cls) -> list[str]:
        return cls.__keywords
    
    def __init__(self):
        # initialize some values
        self.sourceFile:os.DirEntry = None
        self.className:str = ""
        self.classLanguage:str = ""
        self.rclAsJson:str = ""
        self.rclAsString:str = ""
        self.rclAsDict:dict[str,str] = {}
        self.rclLines = []
        self.genTargetClass:bool = False
        self.genTargetAsJSON:bool = False
        self.genTargetAsStr:bool = False
        self.genTargetAsDict:bool = False

if __name__ == "__main__":
    print(rclParser)