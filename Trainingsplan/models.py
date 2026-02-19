from dataclasses import dataclass
from typing import List
@dataclass
class Exercise:
    name: str
    description: str
    duration: int
    categories: List[str]
    difficulty: int


all_categories = ["Beinarbeit", "Vorhand", "Rückhand", "Eröffnung", "Unregelmäßig", "Anfänger", "Fortgeschritten", "Spielsituation"]


exercises = [
    Exercise("Mühle", "Ein Spieler spielt immer diagonal, ein Spieler spielt immer gerade.", 5, ["Beinarbeit"], 3),
    Exercise("RH-Eröffnung gegen Unterschnitt", "Unterschnitt Aufschlag aus Rückhandseite. Schupf in Rückhand. Rückhand Topspin in Rückhand Seite danach frei.", 5, ["Eröffnung", "Rückhand"], 2),
    Exercise("RH-Eröffnung nach kurzem Ball", "Partner spielt kurzen Aufschlag in Vorhand. Spieler schupft kurz in Rückhand zurück. Partner schupft lang in Rückhand. Spieler spielt Rückhand Topspin aus Rückhand.", 5, ["Beinarbeit", "Rückhand", "Eröffnung" ], 4),
    Exercise("Mitte-Außen", "Partner spielt einen Ball in die Mitte. Spieler spielt Vorhand in Rückhand. Partner spielt nun entweder in Vorhand oder Rückhand. Spieler spielt Vorhand oder Rückhand in Rückhand. Partner spielt nun wieder in Mitte. Weiter im Wechsel bis zum Fehler.", 5, ["Unregelmäßig", "Beinarbeit"], 4),
    Exercise("Zwei-Zwei", "Spieler spielt jeweils zwei Bälle aus Rückhand und zwei Bälle aus Mitte im Wechsel bis zum Fehler.", 5, ["Vorhand", "Rückhand", "Anfänger"], 2),
    Exercise("Vorhand Zwei-Drittel", "Spieler spielt Vorhand aus 2/3 Vorhandseite in Vorhandseite. Partner platziert Blocks auf 2/3 der Platte.", 5, ["Vorhand", "Anfänger"], 2),
    Exercise("Eröffnung frei", "Spieler macht Unterschnitt Aufschlag. Partner spielt langen Schupf frei auf Platte. Spieler eröffnet mit Topspin. Danach freies Spiel.", 5, ["Eröffnung","Unregelmäßig", "Fortgeschritten"], 5),
    Exercise("Freies platzieren", "Spieler macht Aufschlag. Partner spielt auf gewünschte Stelle zurück. Spieler spielt Topspin auf Rückhand. Partner platziert Blocks frei auf gesamter Platte. Spieler zieht aus allen Positionen auf Rückhand bis zum Fehler", 5, ["Unregelmäßig", "Beinarbeit", "Fortgeschritten"], 5),
    Exercise("Rückhand parallel", "Spieler spielt Rückhand parallel in Vorhand des Partners bis zum Fehler.", 5, ["Rückhand", "Anfänger"], 2),
    Exercise("Vorhand parallel", "Spieler spielt Vorhand parallel in Rückhand des Partners bis zum Fehler.", 5, ["Vorhand", "Anfänger"], 2),
    Exercise("Vorhand Eröffnung", "Spieler macht Unterschnitt Aufschlag. Partner spielt langen Schupf auf Mitte. Spieler eröffnet mit Vorhand Topspin auf Rückhand. Danach frei", 5, ["Eröffnung", "Vorhand", "Anfänger"], 2),
    Exercise("Kurz-Kurz", "Kurzer Aufschlag. Danach kurz-kurz schupfen bis Ball zu lang oder hoch kommt. Dann Angriff und anschließend freies Spiel", 1, ["Anfänger"], 3),
    Exercise("Klein-Groß", "Spieler spielt Rückhand aus Rückhandseite. Anschließend aus Mitte mit Vorhand. Danach Rückhand aus Rückhandseite. Zuletzt Vorhand aus Vorhandseite. Danach wieder von vorne bis zum Fehler. Alle Bälle werden in die Rückhand des Partners gespielt.", 5, ["Beinarbeit", "Fortgeschritten"], 4),
    Exercise("Vorhand Gegentopspin am Tisch", "Spieler spielt Unterschnitt Aufschlag lang. Partner eröffnet mit Topspin in Vorhandseite des Spielers. Spieler zieht Gegentopspin am Tisch in Vorhandseite. Danach frei", 5, ["Vorhand", "Fortgeschritten"], 4),
    Exercise("11 Aufschläge","Spieler hat 11 Aufschläge und versucht so viele Punkte wie möglich zu machen", 5, ["Spielsituation", "Anfänger"], 1),
    Exercise("9:9 Eigener Aufschlag", "Spieler startet mit 9:9 Punktestand bei eigenem Aufschlag. Spieler versucht 3/4 der Sätze zu gewinnen", 5, ["Spielsituation"], 1),
    Exercise("7:9 Eigener Aufschlag", " Spieler startet mit 7:9 Punktestand bei eigenem Aufschlag. Spieler versucht die Sätze zu gewinnen", 5, ["Spielsituation"], 3),
    Exercise("1-2-3 Vorhand", "Spieler startet aus Vorhand mit Vorhandtopspin, danach Vorhand aus Mitte, danach Vorhand aus Rückhand. Alle Bälle werden in Rückhandseite des Partners gespielt. Danach wieder von vorne bis zum Fehler", 5, ["Vorhand", "Beinarbeit", "Fortgeschritten"], 5),
    Exercise("1-2-3 Vorhand mit Zwischenschritt", "Spieler startet aus Vorhand mit Vorhandtopspin, danach Vorhand aus Mitte, danach Vorhand aus Rückhand. Dann Vorhand aus Mitte. Anschließend wieder von vorne bis zum Fehler. Alle Bälle werden in Rückhand des Partners gespielt", 5, ["Vorhand", "Beinarbeit"], 3),
    Exercise("VH-VH-RH", "Spieler startet mit Vorhandtopspin aus Vorhand, danach Vorhandtopspin aus Mitte und anschließend Rückhand aus Rückhandseite. Dann wieder von vorne aus Vorhand den gleichen Ablauf bis zum Fehler spielen. Alle Bälle werden in Vorhand des Partners gespielt", 5, ["Beinarbeit", "Anfänger"], 3),
    Exercise("Vorhand Duell", "Es wird ein Satz gespielt. Es darf nur Diagonal aus den Vorhandfeldern gespielt werden. Es darf nur ohne Rotation lang aufgeschlagen werden", 5, ["Spielsituation", "Anfänger"], 1),
    Exercise("Rückhand Duell", "Es wird ein Satz gespielt. Es darf nur Diagonal aus den Rückhandfeldern gespielt werden. Es darf nur ohne Rotation lang aufgeschlagen werden", 5, ["Spielsituation", "Anfänger"], 1),
    Exercise("Rückhand Flip", "Spieler macht kurzen Aufschlag mit Unterschnitt. Partner schupft kurz in Rückhandseite. Spieler eröffnet mit Rückhand Flip in Rückhand. Danach freies Spiel",5, ["Rückhand"], 3),
    Exercise("Vorhand Flip", "Spieler macht kurzen Aufschlag mit Unterschnitt. Partner schupft kurz in Vorhandseite. Spieler eröffnet mit Vorhand Flip in Vorhand. Danach freies Spiel", 5, ["Vorhand", "Fortgeschritten"], 3),
    Exercise("Rückhand Gegentopspin am Tisch", "Spieler spielt Unterschnitt Aufschlag lang. Partner eröffnet mit Topspin in Rückhandseite des Spielers. Spieler zieht Gegentopspin am Tisch mit Rückhand in Rückhandseite. Danach frei", 5, ["Rückhand", "Fortgeschritten"], 5),
]

