from .DocumentModel import DocumnetModel
from .Function.IDocumentPolicy import IDocumentPolicy
from .Variable.DocumentConfig import DocumentConfig

class DocumentCrafter():
    def __init__(self,documentPolicy:IDocumentPolicy,documentConfig:DocumentConfig):
        self.__documentPolicy = documentPolicy
        self.__documentConfig = documentConfig

    def Crafter(self):
        return DocumnetModel(self.__documentPolicy,self.__documentConfig)