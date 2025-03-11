from ...L04_Infrastructure import IDocumentRepository
from .DocumentStrategy import IDocumentStrategy

class DocumentStrategy(IDocumentStrategy):
    def GetYamlPath(self) -> str:
        return self.repository.GetYamlPath()

    def SetYamlPath(self,value:str):
        self.repository.SetYamlPath(value)

    def GetYamlDataDict(self) -> dict:
        return self.repository.GetYamlDataDict()

    def SetYamlDataDict(self,value:dict):
        self.repository.SetYamlDataDict(value)

    def GetMarkdownPath(self) -> str:
        return self.repository.GetMarkdownPath()

    def SetMarkdownPath(self,value:str):
        self.repository.SetMarkdownPath(value)

    def GetMarkdownDataStr(self) -> str:
        return self.repository.GetMarkdownDataStr()

    def SetMarkdownDataStr(self,value:str):
        self.repository.SetMarkdownDataStr(value)

    def ReadYaml(self) -> dict:
        return self.repository.ReadYaml()

    def WriteYaml(self):
        self.repository.WriteYaml()

    def ReadMarkdown(self) -> str:
        return self.repository.ReadMarkdown()

    def WriteMarkdown(self):
        self.repository.WriteMarkdown()

    def __init__(self,repository:IDocumentRepository):
        self.repository = repository