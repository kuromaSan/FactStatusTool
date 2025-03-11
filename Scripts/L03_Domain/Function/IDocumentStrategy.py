from typing import Protocol

class IDocumentStrategy(Protocol):
    def GetYamlPath(self) -> str:
        pass
    def SetYamlPath(self,value:str):
        pass
    def GetYamlDataDict(self) -> dict:
        pass
    def SetYamlDataDict(self,value:dict):
        pass
    def GetMarkdownPath(self) -> str:
        pass
    def SetMarkdownPath(self,value:str):
        pass
    def GetMarkdownDataStr(self) -> str:
        pass
    def SetMarkdownDataStr(self,value:str):
        pass
    def ReadYaml(self) -> dict:
        pass
    def WriteYaml(self):
        pass
    def ReadMarkdown(self) -> str:
        pass
    def WriteMarkdown(self):
        pass