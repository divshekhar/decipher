from dictionary.diagram import DIAGRAMS
from dictionary.trigram import TRIGRAMS
from dictionary.quadrigram import QUADRIGRAMS


def generateScore(text: str) -> float:
    score: float = 0.0
    j: int = 0
    for i in range(len(text) - 2):
        j = i+2
        diagram: str = text[i:j]
        diagram = diagram.upper()

        # check & add score
        if diagram in DIAGRAMS:
            score += DIAGRAMS[diagram]

    for i in range(len(text) - 3):
        j = i+3
        trigram: str = text[i:j]
        trigram = trigram.upper()

        # check & add score
        if trigram in TRIGRAMS:
            score += TRIGRAMS[trigram]
    
    for i in range(len(text) - 4):
        j = i+4
        quadrigram: str = text[i:j]
        quadrigram = quadrigram.lower()

        # check & add score
        if quadrigram in QUADRIGRAMS:
            score += QUADRIGRAMS[quadrigram]

    return score